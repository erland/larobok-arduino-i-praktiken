# 8. Avbrott, watchdog och robust körning

## Robust körning i praktiken
Det här kapitlet handlar om hur ett Arduino-program kan reagera på händelser utan att bli skört. Använd det när ett projekt missar snabba signaler, fastnar i väntan, behöver säkra standardlägen eller måste kunna återhämta sig efter låsningar.

I praktiken hjälper kapitlet dig att:

- avgöra när vanlig polling räcker och när avbrott är motiverade
- skriva korta och säkra interrupt-funktioner
- använda timeouts i stället för att vänta för alltid
- förstå watchdog som sista skyddsnivå, inte som lösning på dålig kod
- felsöka märkliga reset-problem som ofta beror på matning, brus eller laster

## Förutsättningar

Du bör vara bekväm med `loop()`, digitala ingångar och enkla variabler. Kapitel 5 ger grunden för digital I/O, kapitel 7 för timing och PWM, och kapitel 34 blir viktigt när robusthetsproblem egentligen beror på strömförsörjning.

## Polling först

Polling betyder att programmet själv kontrollerar ett tillstånd om och om igen. När du skriver `digitalRead(buttonPin)` i `loop()` pollar du knappen. För många Arduino-projekt är det den bästa lösningen.

Ett enkelt pollingmönster kan se ut så här:

```cpp
const int buttonPin = 2;
const int ledPin = 13;

bool lastButtonState = HIGH;
unsigned long lastReadMs = 0;
const unsigned long readIntervalMs = 5;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long now = millis();

  if (now - lastReadMs >= readIntervalMs) {
    lastReadMs = now;

    bool buttonState = digitalRead(buttonPin);

    if (lastButtonState == HIGH && buttonState == LOW) {
      digitalWrite(ledPin, !digitalRead(ledPin));
    }

    lastButtonState = buttonState;
  }
}
```

Det här är ofta bättre än ett avbrott för en knapp. Knappen är långsam jämfört med mikrokontrollern, och kontaktstuds gör ändå att du behöver filtrera signalen. Polling gör dessutom koden lättare att testa och felsöka.

Polling passar särskilt bra när:

- signalen ändras långsamt
- det inte gör något om programmet reagerar några millisekunder senare
- signalen behöver debouncing eller filtrering
- logiken är lätt att beskriva som återkommande tillståndskontroll
- du vill undvika asynkron kod

Polling passar sämre när:

- pulserna är korta
- pulserna kan komma snabbt
- programmet behöver sova mellan händelser
- händelsen måste fångas även när huvudprogrammet gör något annat
- extern hårdvara förväntar sig snabb respons

En bra grundregel är: använd polling tills du har ett konkret skäl att använda avbrott.

## Vad ett avbrott är

Ett avbrott är en mekanism där mikrokontrollern tillfälligt stoppar den kod den håller på med, kör en särskild funktion och sedan fortsätter där den var. Den särskilda funktionen kallas ofta interrupt service routine, ISR.

I Arduino-kod används externa avbrott ofta med `attachInterrupt()`:

```cpp
attachInterrupt(digitalPinToInterrupt(pin), functionName, mode);
```

De tre delarna betyder:

- `digitalPinToInterrupt(pin)` översätter en digital pinne till rätt interruptnummer för kortet.
- `functionName` är funktionen som ska köras när avbrottet sker.
- `mode` anger vilken signaländring som ska trigga avbrottet.

Vanliga lägen är:

- `RISING`: signalen går från LOW till HIGH
- `FALLING`: signalen går från HIGH till LOW
- `CHANGE`: signalen ändras i någon riktning
- `LOW`: signalen är låg, på kort där detta stöds på relevant sätt

Vilka pinnar som stöder externa avbrott varierar mellan kortfamiljer. På moderna kort kan många GPIO-pinnar ofta användas. På klassiska AVR-baserade kort är stödet mer begränsat. Därför ska du nästan alltid använda `digitalPinToInterrupt(pin)` i stället för att hårdkoda interruptnummer.

## Ett första interrupt-exempel

Anta att du har en digital pulssignal på pinne 2. Det kan vara en sensor, en knapp för referensmönster eller en signal från en annan modul. Vi vill räkna hur många stigande flanker som inträffar.

```cpp
const int pulsePin = 2;

volatile unsigned long pulseCount = 0;

void onPulse() {
  pulseCount++;
}

void setup() {
  Serial.begin(115200);

  pinMode(pulsePin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pulsePin), onPulse, FALLING);
}

void loop() {
  static unsigned long lastReportMs = 0;
  unsigned long now = millis();

  if (now - lastReportMs >= 1000) {
    lastReportMs = now;

    noInterrupts();
    unsigned long countSnapshot = pulseCount;
    interrupts();

    Serial.print("Pulses: ");
    Serial.println(countSnapshot);
  }
}
```

Det finns flera viktiga detaljer här.

Variabeln `pulseCount` är deklarerad som `volatile`. Det talar om för kompilatorn att variabeln kan ändras utanför den vanliga programordningen. Utan `volatile` kan kompilatorn optimera kod på ett sätt som gör att huvudprogrammet inte alltid läser det senaste värdet.

När huvudprogrammet kopierar `pulseCount` används `noInterrupts()` och `interrupts()`. Det skapar en kort kritisk sektion. På vissa mikrokontrollers kan läsning av ett större heltal ta flera maskininstruktioner. Om ett avbrott sker mitt under läsningen kan huvudprogrammet få ett halvuppdaterat värde. Genom att stänga av avbrott mycket kort medan värdet kopieras undviker vi det.

Lägg märke till att ISR-funktionen `onPulse()` är extremt kort. Den räknar upp en variabel och gör inget mer.

## Vad som inte ska göras i en ISR

En ISR ska vara så kort och förutsägbar som möjligt. Den ska helst bara notera att något har hänt, spara ett minimalt värde eller öka en räknare.

Undvik i en ISR:

- `delay()`
- långvariga beräkningar
- dynamisk minneshantering
- seriell utskrift
- I2C- eller SPI-kommunikation
- displayuppdateringar
- filskrivning
- kod som väntar på något annat
- kod som själv är beroende av andra avbrott

Det är frestande att skriva hela reaktionen direkt i ISR-funktionen:

```cpp
void onButtonPress() {
  Serial.println("Button pressed");
  updateDisplay();
  readSensor();
}
```

Det är ett dåligt mönster. Det kan fungera i ett litet test men skapa låsningar, tappade händelser eller märkliga timingproblem när projektet växer.

Skriv hellre så här:

```cpp
volatile bool buttonEvent = false;

void onButtonPress() {
  buttonEvent = true;
}

void loop() {
  if (buttonEvent) {
    noInterrupts();
    buttonEvent = false;
    interrupts();

    handleButtonPress();
  }
}
```

ISR markerar bara att något har hänt. Huvudprogrammet gör det riktiga arbetet i normal programkontext.

## Volatile är nödvändigt men inte tillräckligt

`volatile` löser ett specifikt problem: kompilatorn får inte anta att värdet är oförändrat bara för att den vanliga koden inte ändrat det. Men `volatile` gör inte operationer atomära, och det gör inte delad data automatiskt säker.

Det här är viktigt:

```cpp
volatile unsigned long pulseCount = 0;
```

Men det här är inte automatiskt säkert i huvudprogrammet:

```cpp
unsigned long copy = pulseCount;
```

På vissa plattformar kan läsningen vara atomär, på andra inte. För portabel Arduino-kod är det ofta klokt att kopiera delade räknare i en kort kritisk sektion:

```cpp
noInterrupts();
unsigned long copy = pulseCount;
interrupts();
```

Kritiska sektioner ska vara så korta som möjligt. Stäng inte av avbrott medan du skriver till seriell monitor, uppdaterar display eller gör beräkningar. Kopiera bara data och slå på avbrott igen.

## Händelseflagga eller räknare?

Det finns två vanliga mönster för avbrott:

- flagga: något har hänt
- räknare: något har hänt ett antal gånger

En flagga passar när du bara behöver veta att en händelse inträffat sedan sist:

```cpp
volatile bool motionDetected = false;

void onMotion() {
  motionDetected = true;
}
```

En räknare passar när flera händelser kan inträffa innan huvudprogrammet hinner bearbeta dem:

```cpp
volatile unsigned long pulseCount = 0;

void onPulse() {
  pulseCount++;
}
```

För snabba pulser är räknare ofta bättre. Om du använder en boolesk flagga kan tio pulser mellan två varv i `loop()` fortfarande bara se ut som “en händelse har inträffat”.

För mer komplexa data kan du använda en liten ringbuffer, men det ökar komplexiteten. I den här boken håller vi oss till flaggor, räknare och korta snapshots tills det finns ett tydligt skäl att göra mer.

## Kontaktstuds och avbrott

Knappar och mekaniska brytare studsar. När kontakten sluts kan signalen växla flera gånger under några millisekunder innan den stabiliseras. Om du kopplar en knapp direkt till ett avbrott kan ett knapptryck därför bli flera avbrott.

Det här är en vanlig fälla. Avbrottet gör inte knappen mer exakt. Det gör bara att du upptäcker varje elektrisk flank snabbare, inklusive de oönskade flankerna.

För knappar är polling med debouncing ofta enklare. Om du ändå behöver avbrott, till exempel för att väcka ett sovande kort, kan ISR bara markera att något hänt. Sedan kan huvudprogrammet kontrollera signalen efter en kort stabiliseringstid.

Ett enkelt mönster:

```cpp
const int buttonPin = 2;

volatile bool wakeEvent = false;
unsigned long lastAcceptedMs = 0;
const unsigned long debounceMs = 30;

void onButtonEdge() {
  wakeEvent = true;
}

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(buttonPin), onButtonEdge, FALLING);
}

void loop() {
  if (wakeEvent) {
    noInterrupts();
    wakeEvent = false;
    interrupts();

    unsigned long now = millis();

    if (now - lastAcceptedMs >= debounceMs && digitalRead(buttonPin) == LOW) {
      lastAcceptedMs = now;
      handleConfirmedPress();
    }
  }
}

void handleConfirmedPress() {
  // Gör det riktiga arbetet här.
}
```

Detta är fortfarande inte perfekt för alla situationer, men det visar principen: ISR fångar kanten, huvudprogrammet bekräftar händelsen.

## Avbrott och olika kortfamiljer

Arduino-kompatibla kort skiljer sig åt mer än man först tror. Det gäller särskilt interruptstöd.

Några praktiska skillnader att förvänta sig:

- Alla pinnar har inte nödvändigtvis stöd för externa avbrott.
- Vissa pinnar används vid boot eller är kopplade till inbyggda funktioner.
- Timerresurser delas med PWM, servo, ljud eller andra bibliotek.
- Wi-Fi- och Bluetooth-kort kan ha bakgrundsprocesser som påverkar timing.
- Deep sleep och wake-up fungerar olika mellan kortfamiljer.
- Spänningsnivåer påverkar vilka externa signaler som kan kopplas direkt.

Därför bör ett kapitel eller referensmönster aldrig säga “använd pinne 2” utan att också säga vilket kort som avses. I bokens referensmönster använder vi i stället ett återkommande arbetssätt:

- välj en pinne som dokumentationen anger som interrupt-kapabel
- kontrollera att pinnen inte påverkar boot
- kontrollera logiknivå och ingångsskydd
- börja med låg frekvens och seriell rapportering
- öka komplexiteten först när mätningen är stabil

När vi senare går igenom UNO, Mega, ESP8266, ESP32 och RP2040/Pico kommer interrupt- och timerdetaljer att återkomma som kortspecifika valfrågor.

## När interrupt är rätt val

Avbrott passar bra när händelsen är kort, snabb eller behöver fångas oberoende av huvudprogrammets tempo.

Typiska exempel:

- räkna pulser från en flödesmätare
- läsa en hjulencoder
- fånga en tachometersignal
- väcka kortet från sömn med knapp eller sensor
- mäta tid mellan flanker
- reagera på en extern felindikering
- hålla koll på en signal medan huvudprogrammet gör långsammare arbete

Avbrott är mindre lämpliga när:

- signalen är långsam
- signalen behöver mycket filtrering
- händelsen kan kontrolleras enkelt i `loop()`
- kodens enkelhet är viktigare än mikrosekundrespons
- biblioteket du använder redan hanterar timing internt
- du inte har ett tydligt problem som avbrott löser

En praktisk fråga är: vad händer om programmet upptäcker händelsen 5 eller 20 millisekunder senare? Om svaret är “ingenting viktigt” behöver du ofta inte ett avbrott.

## Timeouts som robusthetsverktyg

Robust körning handlar inte bara om avbrott. Många Arduino-projekt blir opålitliga för att koden väntar för länge på något som aldrig händer.

Exempel:

- en sensor svarar inte på I2C
- en seriell modul skickar aldrig komplett meddelande
- Wi-Fi ansluter inte
- ett bibliotek väntar på hårdvara som saknas
- en knappsekvens blir halvfärdig
- en motorstyrning väntar på ett gränsläge som aldrig nås

Ett robust program bör ha timeouts. I stället för att vänta för alltid ska koden ge upp, markera fel, återgå till säkert läge eller försöka igen senare.

Ett enkelt timeoutmönster:

```cpp
bool waitForPinState(int pin, int expectedState, unsigned long timeoutMs) {
  unsigned long startMs = millis();

  while (millis() - startMs < timeoutMs) {
    if (digitalRead(pin) == expectedState) {
      return true;
    }
  }

  return false;
}
```

Detta exempel blockerar fortfarande under väntan, men det blockerar inte för alltid. I mer avancerad kod skriver du samma idé som en tillståndsmaskin utan `while`-väntan. Det viktiga är principen: alla väntelägen bör ha en plan för misslyckande.

## Säkra standardlägen

När något går fel ska systemet hamna i ett läge som är begripligt och så säkert som möjligt. Vad som är säkert beror på projektet.

Exempel:

- en motor ska stoppas
- en värmare ska stängas av
- ett relä ska gå till avstängt läge
- en LED ska visa felkod
- en loggrad ska sparas
- nätverkskommunikation ska återstartas
- systemet ska fortsätta mäta men markera data som osäker

Skriv gärna en separat funktion för säkert läge:

```cpp
const int motorEnablePin = 6;
const int statusLedPin = 13;

void enterSafeMode() {
  analogWrite(motorEnablePin, 0);
  digitalWrite(statusLedPin, HIGH);
}
```

I kommande kapitel om motorer, reläer och strömförsörjning blir detta ännu viktigare. En felhanteringsstrategi som räcker för en LED räcker inte automatiskt för en motor eller en last med separat matning.

## Watchdog: sista skyddsnivån

En watchdog timer är en timer som förväntar sig att programmet regelbundet talar om att det fortfarande lever. Om programmet inte gör det i tid antar watchdog-funktionen att systemet har fastnat och återställer mikrokontrollern eller triggar en särskild felhantering.

Begreppet brukar kallas att “mata watchdoggen”, från engelska “feed the watchdog” eller “kick the watchdog”.

Watchdog passar när:

- systemet ska kunna återhämta sig utan manuell reset
- projektet kör obevakat
- miljön kan ge störningar eller spänningsdippar
- nätverk eller externa moduler ibland låser sig
- en kontrollerad omstart är bättre än ett låst system

Watchdog passar inte som ursäkt för dålig felhantering. Om programmet återstartar hela tiden utan att du vet varför har du inte ett robust system, bara ett system som döljer ett fel.

Watchdog-stöd varierar mellan kortfamiljer. AVR, ESP8266, ESP32, RP2040 och moderna Arduino-kort har olika API:er, olika standardbeteenden och olika begränsningar. Därför använder vi inte ett enda universellt watchdog-exempel här. I stället använder vi en generell designprincip:

- aktivera watchdog först när grundprogrammet är stabilt
- välj timeout som är längre än normal längsta arbetscykel
- mata watchdog bara från huvudloopen eller en kontrollerad systempunkt
- mata den inte från kod som kan fortsätta köras trots att resten av systemet är låst
- logga eller indikera om möjligt att en omstart berodde på watchdog
- testa avsiktligt att watchdog faktiskt löser ut

Ett förenklat pseudomönster:

```cpp
void setup() {
  initializeHardware();
  initializeWatchdog();
}

void loop() {
  bool ok = runSystemStep();

  if (ok) {
    feedWatchdog();
  } else {
    enterSafeMode();
  }
}
```

Poängen är att watchdog ska bekräfta att systemet som helhet går framåt, inte bara att CPU:n fortfarande kör någon kod.

## Referensmönster: timeout och säkert standardläge

Det här referensmönstret visar ett robusthetsmönster som fungerar före, och ofta viktigare än, plattformsspecifik watchdog-kod: vänta inte obegränsat på en sensor, modul eller kommunikation. Sätt systemet i ett säkert standardläge när ett svar uteblir.

### Vad mönstret visar

Mönstret hjälper dig att:

- skilja normal väntan från fel,
- undvika att `loop()` fastnar i en evig väntan,
- sätta utgångar i ett säkert läge vid uteblivet svar,
- logga eller indikera felet,
- använda watchdog som sista skyddsnivå snarare än första felsökningsmetod.

### Kod

```cpp
const int statusLedPin = LED_BUILTIN;
const int outputPin = 9;

const unsigned long sensorTimeoutMs = 1500;
const unsigned long retryIntervalMs = 2000;

unsigned long lastGoodSensorMs = 0;
unsigned long lastRetryMs = 0;

bool safeMode = true;

bool readSensor(float &value) {
  // Ersätt detta med verklig sensorläsning.
  // Returnera false om sensorn inte svarar eller ger orimligt värde.
  value = 23.5;
  return true;
}

void enterSafeMode(const char *reason) {
  safeMode = true;
  digitalWrite(outputPin, LOW);
  digitalWrite(statusLedPin, HIGH);

  Serial.print("SAFE MODE: ");
  Serial.println(reason);
}

void leaveSafeMode() {
  if (safeMode) {
    Serial.println("Leaving safe mode");
  }

  safeMode = false;
  digitalWrite(statusLedPin, LOW);
}

void setup() {
  Serial.begin(115200);
  pinMode(statusLedPin, OUTPUT);
  pinMode(outputPin, OUTPUT);

  enterSafeMode("startup");
}

void loop() {
  unsigned long now = millis();

  if (now - lastRetryMs >= retryIntervalMs) {
    lastRetryMs = now;

    float sensorValue = 0.0;

    if (readSensor(sensorValue)) {
      lastGoodSensorMs = now;
      leaveSafeMode();

      Serial.print("sensor=");
      Serial.println(sensorValue);
    } else {
      Serial.println("Sensor read failed");
    }
  }

  if (now - lastGoodSensorMs > sensorTimeoutMs) {
    enterSafeMode("sensor timeout");
  }

  if (!safeMode) {
    digitalWrite(outputPin, HIGH);
  }

  // Watchdog kan matas här i ett verkligt projekt,
  // men bara om systemsteget ovan faktiskt fungerar.
}
```

### Kontrollera detta

- Timeout-tiden ska vara längre än normal sensortid men kort nog för att skydda systemet.
- Säkert standardläge ska stänga av eller minska riskfyllda utgångar.
- Fel ska synas i seriell monitor, LED-status, display eller logg.
- Watchdog ska inte mata sig själv från kod som kan fortsätta trots att resten av systemet är låst.
- Testa avsiktligt uteblivet sensorsvar innan projektet körs obevakat.

## Brownout, reset och konstiga fel

Alla “mjukvarufel” är inte mjukvarufel. Många robusthetsproblem i Arduino-projekt beror på strömförsörjning, jord, brus eller laster som påverkar kortet.

Symtom kan vara:

- kortet startar om när en motor startar
- seriell monitor visar skräp
- I2C-enheter försvinner ibland
- Wi-Fi-kort tappar anslutning vid hög last
- programmet verkar hoppa till början
- sensordata får extrema spikar

Brownout betyder att matningsspänningen sjunker så lågt att mikrokontrollern inte längre kan köras stabilt. Vissa kort har brownout detection som återställer systemet när spänningen blir för låg. Andra kan bete sig mer oförutsägbart.

Innan du lägger in mer komplex felhantering bör du kontrollera:

- att matningen klarar strömtoppar
- att motorer, LED-strippar och reläer inte matas från en pinne
- att GND är gemensam där signaler delas
- att induktiva laster har skydd
- att långa kablar inte plockar upp brus
- att avkopplingskondensatorer finns där de behövs
- att USB-porten inte är den svaga länken i mönstret

Watchdog kan återställa ett system efter vissa fel, men den löser inte en undermålig strömförsörjning.

## Referensmönster: pulser med polling och interrupt

Det här referensmönstret jämför polling och avbrott för samma signal. Poängen är inte exakt mätutrustning, utan att visa när polling räcker och när avbrott ger ett tydligare resultat.

### Vad mönstret visar

Mönstret hjälper dig att:

- koppla en enkel pulssignal till en digital ingång
- räkna händelser med polling
- räkna händelser med interrupt
- kopiera interrupt-data på ett säkert sätt
- jämföra resultat och resonera om felkällor

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- en knapp eller pulsgivare
- en LED med seriemotstånd, valfritt
- kopplingskablar
- breadboard
- seriell monitor

För bästa jämförelse kan du använda en signal som ger snabbare pulser än en vanlig knapp, till exempel en enkel encoder, en pulsgivare eller en signal från ett annat kort. Börja gärna med knapp för att förstå koden, men kom ihåg att kontaktstuds påverkar resultatet.

### Koppling

Använd en digital pinne som stöder externa avbrott på ditt kort. I exemplen kallas den `pulsePin`.

Koppla signalen så här för knappvarianten:

- ena sidan av knappen till `pulsePin`
- andra sidan av knappen till GND
- `pulsePin` konfigureras som `INPUT_PULLUP`

Det gör att viloläget är HIGH och knapptryck ger LOW. Avbrottet kan då triggas på `FALLING`.

### Pollingräknare

```cpp
const int pulsePin = 2;

bool lastState = HIGH;
unsigned long polledCount = 0;

void setup() {
  Serial.begin(115200);
  pinMode(pulsePin, INPUT_PULLUP);
}

void loop() {
  bool currentState = digitalRead(pulsePin);

  if (lastState == HIGH && currentState == LOW) {
    polledCount++;
  }

  lastState = currentState;

  static unsigned long lastReportMs = 0;
  unsigned long now = millis();

  if (now - lastReportMs >= 1000) {
    lastReportMs = now;

    Serial.print("Polling count: ");
    Serial.println(polledCount);
  }
}
```

Testa först långsamma tryck. Du kommer troligen att se att räknaren ibland ökar mer än en gång per tryck på grund av kontaktstuds. Det är förväntat.

### Interrupträknare

```cpp
const int pulsePin = 2;

volatile unsigned long interruptCount = 0;

void onPulse() {
  interruptCount++;
}

void setup() {
  Serial.begin(115200);
  pinMode(pulsePin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(pulsePin), onPulse, FALLING);
}

void loop() {
  static unsigned long lastReportMs = 0;
  unsigned long now = millis();

  if (now - lastReportMs >= 1000) {
    lastReportMs = now;

    noInterrupts();
    unsigned long countSnapshot = interruptCount;
    interrupts();

    Serial.print("Interrupt count: ");
    Serial.println(countSnapshot);
  }
}
```

Med knapp kan även interruptversionen räkna flera pulser per tryck. Det visar att avbrott inte ersätter debouncing. Med en renare pulssignal bör interruptversionen däremot fånga händelser även när `loop()` gör annat.

### Jämför när loop blir upptagen

Lägg till en avsiktlig period där huvudprogrammet gör något långsamt. Detta är inte ett rekommenderat mönster i färdig kod, men det visar skillnaden.

```cpp
if (now % 5000 < 1000) {
  delay(200);
}
```

I pollingversionen kan pulser missas under fördröjningen. I interruptversionen kan pulser fortfarande räknas, så länge ISR är kort och signalen inte är snabbare än systemet klarar.

### Förväntat resultat

Du bör se att:

- polling är enkel och fungerar bra för långsamma signaler
- polling kan missa pulser när loopen blockeras
- interrupt kan fånga pulser även när huvudprogrammet är upptaget
- både polling och interrupt påverkas av kontaktstuds
- interrupt kräver mer noggrann hantering av delad data

### Anpassningar

Prova att:

- byta från `FALLING` till `CHANGE`
- lägga till enkel debounce i huvudprogrammet
- rapportera pulser per sekund i stället för totalt antal
- testa på två olika kortfamiljer
- jämföra med en rotary encoder eller flödesmätare
- mäta hur många pulser som tappas när huvudprogrammet blockeras

## Vanliga misstag

- **Misstag: Att använda avbrott för allt.**
  - Varför det händer: Avbrott känns mer avancerade och snabbare än polling.
  - Hur man undviker det: Börja med polling och byt till avbrott först när du har en konkret händelse som annars missas.

- **Misstag: Att skriva för mycket kod i ISR-funktionen.**
  - Varför det händer: Det känns naturligt att hantera händelsen där den upptäcks.
  - Hur man undviker det: Låt ISR bara sätta en flagga, öka en räknare eller spara ett minimalt tidsvärde.

- **Misstag: Att använda `Serial.print()` i en ISR.**
  - Varför det händer: Seriell utskrift är ett vanligt felsökningsverktyg.
  - Hur man undviker det: Spara en flagga i ISR och skriv ut från `loop()`.

- **Misstag: Att tro att `volatile` gör all delad data säker.**
  - Varför det händer: `volatile` nämns ofta tillsammans med interrupt.
  - Hur man undviker det: Använd `volatile` för delade variabler, men kopiera större värden i korta kritiska sektioner.

- **Misstag: Att ignorera kontaktstuds.**
  - Varför det händer: Avbrott reagerar snabbt och kan därför misstas för att vara mer “exakta”.
  - Hur man undviker det: Debounca mekaniska signaler även när de triggar avbrott.

- **Misstag: Att mata watchdog från fel plats.**
  - Varför det händer: Man vill undvika oönskade resets och matar watchdog så ofta som möjligt.
  - Hur man undviker det: Mata watchdog bara när huvudsystemet faktiskt har genomfört en rimlig arbetscykel.

- **Misstag: Att felsöka resets som kodfel utan att kontrollera matningen.**
  - Varför det händer: Symptomen syns i programmet.
  - Hur man undviker det: Mät spänning, kontrollera GND, separera laster och leta efter brownout innan du bygger mer mjukvarulogik.

## Snabbreferens

| Teknik | Passar för | Undvik när | Viktig kontroll |
|---|---|---|---|
| Polling | Långsamma signaler, knappar, enkel logik | Pulser kan vara korta eller snabba | Loopen får inte blockeras för länge |
| Externt avbrott | Pulser, flankdetektion, wake-up | Signalen är brusig eller mekaniskt studsande utan filtrering | Pinnen måste stödja interrupt |
| Flagga i ISR | Enstaka händelse sedan sist | Flera händelser kan hinna inträffa | Nollställ flaggan säkert i huvudprogrammet |
| Räknare i ISR | Pulser och upprepade händelser | Räknaren kan flöda över utan hantering | Använd `volatile` och snapshot |
| Kritisk sektion | Kopiera delad data säkert | Lång kod, utskrift eller I/O | Håll `noInterrupts()` så kort som möjligt |
| Watchdog | Återhämtning från låsning | Grundfelet är okänt och ignoreras | Mata bara när systemet är friskt |
| Timeout | Väntan på sensor, modul eller tillstånd | Händelsen måste hanteras helt asynkront | Bestäm säkert läge vid timeout |

## Relaterat


- Använd kapitel 5 när avbrottet kommer från en knapp, brytare, pulssignal eller digital sensormodul.
- Använd kapitel 7 när problemet kan lösas med icke-blockerande tid i stället för avbrott.
- Använd kapitel 35 när reset, watchdog, brownout eller sporadiska låsningar behöver felsökas systematiskt.


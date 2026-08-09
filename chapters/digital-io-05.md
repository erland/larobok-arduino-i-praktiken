# 5. Digital I/O, knappar och logiska signaler

## Grundfunktion i praktiken
Digital I/O är den mest grundläggande formen av kontakt mellan ett Arduino-kompatibelt kort och omvärlden. En digital pinne kan ofta läsa om en signal är LOW eller HIGH, eller själv driva en signal LOW eller HIGH. Det låter enkelt, men många hårdvaruproblem börjar just här: en knapp som ibland triggar två gånger, en ingång som slumpmässigt växlar, en modul som ger fel logiknivå, en lång kabel som plockar upp störningar eller en utgång som belastas mer än mikrokontrollern klarar.

Som erfaren programmerare kan du tänka på digital I/O som ett mycket enkelt API med hårda fysiska kontrakt. Funktionen `digitalRead()` returnerar bara ett logiskt värde, men värdet beror på spänning, jord, ingångsimpedans, pull-up, kabeldragning, brus, timing och ibland kortets uppstartslogik. Funktionen `digitalWrite()` sätter en utgång, men pinnen kan bara leverera eller sänka en begränsad ström och den kan inte ersätta en drivkrets.

Det här kapitlet ger dig ett robust arbetssätt för digitala signaler. Vi börjar med enkla in- och utgångar, går vidare till knappar och debouncing, tittar på open drain-liknande kopplingar och avslutar med ett referensmönster för en liten knappmodul som beter sig pålitligt utan att använda `delay()`.

Kapitlet är särskilt användbart när du vill förstå skillnaden mellan digital ingång, digital utgång och högimpedant läge, undvika flytande ingångar, använda intern pull-up för enkla knappar, läsa knappar utan blockerande kod och avgöra när en GPIO behöver extern drivning eller skydd.

## Förutsättningar

Du behöver ha med dig några begrepp från tidigare kapitel:

- **Logiknivå:** vilken spänning som representerar LOW och HIGH för kortet.
- **Gemensam jord:** signaler fungerar bara som tänkt om kretsarna har samma referensnivå.
- **Pull-up och pull-down:** motstånd eller interna funktioner som ger en ingång ett definierat viloläge.
- **Flytande ingång:** en ingång utan definierad nivå, som därför kan läsa slumpmässigt.
- **Strömbudget:** varje pinne, modul och last måste hålla sig inom säkra gränser.

I detta kapitel håller vi oss till säkra lågspänningskopplingar. Koppla inte nätspänning, större motorer, reläspolar eller andra laster direkt till en GPIO. De behandlas senare i kapitel om motorer, reläer, MOSFET:ar och drivkretsar.

## Digital I/O som kontrakt

En digital pinne har normalt flera möjliga roller. På ett Arduino-kompatibelt kort anger du rollen med `pinMode()`.

```cpp
pinMode(2, INPUT);
pinMode(3, INPUT_PULLUP);
pinMode(13, OUTPUT);
```

Det ser ut som tre enkla mjukvarulägen, men varje läge motsvarar ett elektriskt beteende.

| Läge | Typisk användning | Elektrisk idé |
|---|---|---|
| `INPUT` | Läsa signal från extern krets | Pinnen är högimpedant och påverkar kretsen mycket lite |
| `INPUT_PULLUP` | Läsa knapp eller brytare mot GND | Intern pull-up håller pinnen HIGH när knappen inte är tryckt |
| `OUTPUT` | Driva enkel logisk signal eller liten indikator | Pinnen driver aktivt LOW eller HIGH |

Högimpedant betyder att pinnen har mycket hög resistans mot resten av kretsen. Det är bra när du vill mäta eller läsa en signal utan att belasta den. Men det betyder också att en lös ingång lätt påverkas av elektriskt brus, statisk laddning eller närliggande ledningar.

En digital ingång behöver därför nästan alltid ett definierat viloläge. Antingen får den det från en annan krets som aktivt driver signalen, eller från en pull-up/pull-down.

## LOW och HIGH är inte abstrakta värden

I kod ser det ut som att en digital signal bara har två värden.

```cpp
int state = digitalRead(buttonPin);

if (state == HIGH) {
  // Signal is active
}
```

Elektriskt är det mer nyanserat. LOW och HIGH motsvarar spänningsområden, inte exakta värden. Ett 5 V-kort tolkar normalt en viss låg spänning som LOW och en tillräckligt hög spänning som HIGH. Ett 3,3 V-kort gör samma sak, men med andra nivåer. Mellan områdena finns ett osäkert område där signalen kan tolkas fel eller variera.

Det här får praktiska konsekvenser:

- En 5 V-signal kan skada eller överbelasta en 3,3 V-ingång om kortet inte är 5 V-tolerant.
- En 3,3 V-signal kan ibland läsas som HIGH av ett 5 V-kort, men det ska kontrolleras i datablad eller kortdokumentation.
- Långa kablar kan göra signalflanker långsamma och mer störkänsliga.
- Digitala moduler kan ha egna pullups, lysdioder eller nivåskiftare som påverkar signalen.

Utgå därför inte från att “digitalt är digitalt”. Kontrollera alltid logiknivå, matning och signalriktning.

## Digital utgång: att driva signal, inte last

När en pinne är `OUTPUT` kan den normalt driva en logisk signal. Det betyder inte att den kan driva vad som helst. En GPIO är avsedd för signaler och mycket små laster, inte motorer, reläer, solenoider eller LED-strippar.

En enkel LED med seriemotstånd är ofta en rimlig testlast. En buzzer, relämodul eller transistorstyrning kan också styras från en utgång om modulen är avsedd för det och strömkraven är rimliga. Men pinnen ska inte användas som strömförsörjning för en last.

En bra tumregel i experiment är:

- Låt GPIO styra.
- Låt separat matning och drivkrets leverera ström.
- Koppla gemensam jord när signalen behöver gemensam referens.
- Kontrollera om modulen är aktiv HIGH eller aktiv LOW.
- Dokumentera om signalen är styrsignal eller matning.

Det är särskilt viktigt med tredjepartsmoduler eftersom vissa har inbyggda transistorer, optokopplare eller nivåskiftare medan andra i praktiken bara exponerar komponentens pinne.

## Digital ingång: läs alltid ett definierat tillstånd

En digital ingång bör aldrig lämnas flytande. En vanlig nybörjarkoppling är att ansluta en knapp mellan 5 V och en ingång, men glömma motståndet som definierar LOW när knappen inte är tryckt. Då kan pinnen läsa nästan vad som helst i viloläge.

Det finns tre vanliga lösningar:

| Lösning | Viloläge | Aktivt läge | Kommentar |
|---|---|---|---|
| Extern pull-down | LOW | HIGH | Pedagogiskt tydlig men kräver extra motstånd |
| Extern pull-up | HIGH | LOW | Vanlig i elektronik och bussar |
| Intern pull-up | HIGH | LOW | Enkelt för knappar och brytare |

I Arduino-projekt är intern pull-up ofta det bästa förstavalet för enkla knappar. Du kopplar knappen mellan pinnen och GND och använder `INPUT_PULLUP`.

```cpp
const byte buttonPin = 2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  int rawState = digitalRead(buttonPin);

  if (rawState == LOW) {
    Serial.println("Button pressed");
  } else {
    Serial.println("Button released");
  }

  delay(250);
}
```

Observera att logiken blir inverterad: tryckt knapp ger LOW. Det är inte ett fel, utan en konsekvens av att pull-up håller signalen HIGH när knappen är öppen.

## Aktiv HIGH och aktiv LOW

Många digitala signaler är antingen aktiv HIGH eller aktiv LOW.

| Signaltyp | Viloläge | Aktivt läge | Exempel |
|---|---|---|---|
| Aktiv HIGH | LOW | HIGH | Vissa sensormoduler, statusutgångar |
| Aktiv LOW | HIGH | LOW | Knappar med pull-up, många modulingångar, chip select på SPI |

Aktiv LOW är mycket vanligt i elektronik. En signal kan heta `RESET`, `CS`, `ENABLE` eller `INT`, men dokumentationen kan markera att den är aktiv låg med ett streck ovanför namnet, ett suffix som `_N` eller formuleringar som “active low”.

I kod bör du göra detta tydligt. Undvik att sprida råa jämförelser överallt.

```cpp
const byte buttonPin = 2;

bool isButtonPressed() {
  return digitalRead(buttonPin) == LOW;
}
```

Det gör resten av programmet lättare att läsa.

```cpp
if (isButtonPressed()) {
  // Do the thing
}
```

Samma princip fungerar för moduler som har aktiv LOW-ingångar.

```cpp
const byte relayPin = 8;
const byte relayOn = LOW;
const byte relayOff = HIGH;

void setRelay(bool enabled) {
  digitalWrite(relayPin, enabled ? relayOn : relayOff);
}
```

Även om reläer behandlas mer senare är kodmönstret viktigt redan nu: dölj elektrisk polaritet bakom ett tydligt funktionsnamn.

## Knappar studsar

En mekanisk knapp växlar inte perfekt från öppen till sluten. När kontakterna möts kan signalen studsa mellan HIGH och LOW under några millisekunder. Detta kallas kontaktstuds eller debouncing-problem.

Om du läser knappen direkt kan ett enda tryck se ut som flera tryck.

```cpp
if (digitalRead(buttonPin) == LOW) {
  counter++;
}
```

Den koden kan öka räknaren många gånger under ett tryck, både för att knappen studsar och för att `loop()` körs snabbt. Det är två olika problem:

- **Kontaktstuds:** signalen växlar fysiskt flera gånger vid övergången.
- **Upprepad läsning:** programmet hinner läsa samma nedtryckning många gånger.

En robust knapphantering bör därför både filtrera studsen och identifiera en händelse, till exempel “knappen blev just tryckt”.

## Enkel men dålig lösning: delay-baserad debounce

En vanlig lösning är att vänta en kort stund efter att en knapptryckning upptäckts.

```cpp
if (digitalRead(buttonPin) == LOW) {
  delay(50);
  if (digitalRead(buttonPin) == LOW) {
    Serial.println("Pressed");
  }
}
```

Det kan fungera i små tester, men det blockerar programmet. Under `delay(50)` kan du inte läsa andra sensorer, uppdatera display, hantera kommunikation eller reagera på andra händelser. I en större bok som denna vill vi tidigt etablera ett bättre mönster: icke-blockerande kod med `millis()`.

## Icke-blockerande debounce med händelse

Följande kod läser en knapp med intern pull-up, filtrerar studs och genererar en händelse när knappen blir tryckt.

```cpp
const byte buttonPin = 2;
const unsigned long debounceMs = 30;

bool stableState = HIGH;
bool lastRawState = HIGH;
bool lastStableState = HIGH;
unsigned long lastChangeMs = 0;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  bool rawState = digitalRead(buttonPin);
  unsigned long now = millis();

  if (rawState != lastRawState) {
    lastRawState = rawState;
    lastChangeMs = now;
  }

  if ((now - lastChangeMs) >= debounceMs && stableState != rawState) {
    lastStableState = stableState;
    stableState = rawState;

    if (lastStableState == HIGH && stableState == LOW) {
      Serial.println("Button pressed event");
    }

    if (lastStableState == LOW && stableState == HIGH) {
      Serial.println("Button released event");
    }
  }
}
```

Koden gör tre saker:

- Den märker när råsignalen ändras.
- Den väntar tills signalen har varit stabil en kort tid.
- Den rapporterar bara övergången, inte varje varv i `loop()`.

Det här mönstret är användbart i många senare kapitel. Du kan använda samma idé för brytare, reed switches, enklare digitala sensorer och vissa modulers interrupt-signaler.

## Att paketera knapphantering som en liten modul

När du börjar använda flera knappar blir det snabbt rörigt om varje knapp har egna globala variabler. Ett bättre experimentmönster är att skapa en liten struktur eller klass. Här är en kompakt variant som fortfarande är begriplig i Arduino-miljö.

```cpp
struct DebouncedButton {
  byte pin;
  bool stableState = HIGH;
  bool lastRawState = HIGH;
  bool previousStableState = HIGH;
  unsigned long lastChangeMs = 0;
  unsigned long debounceMs = 30;

  void begin() {
    pinMode(pin, INPUT_PULLUP);
    stableState = digitalRead(pin);
    lastRawState = stableState;
    previousStableState = stableState;
  }

  void update(unsigned long now) {
    bool rawState = digitalRead(pin);

    if (rawState != lastRawState) {
      lastRawState = rawState;
      lastChangeMs = now;
    }

    if ((now - lastChangeMs) >= debounceMs && stableState != rawState) {
      previousStableState = stableState;
      stableState = rawState;
    }
  }

  bool wasPressed() const {
    return previousStableState == HIGH && stableState == LOW;
  }

  bool wasReleased() const {
    return previousStableState == LOW && stableState == HIGH;
  }

  bool isPressed() const {
    return stableState == LOW;
  }

  void consumeEvent() {
    previousStableState = stableState;
  }
};

DebouncedButton modeButton{2};

void setup() {
  Serial.begin(115200);
  modeButton.begin();
}

void loop() {
  unsigned long now = millis();
  modeButton.update(now);

  if (modeButton.wasPressed()) {
    Serial.println("Mode button pressed");
    modeButton.consumeEvent();
  }
}
```

Detta är inte tänkt som ett färdigt bibliotek. Det är ett sätt att visa hur hårdvarubeteende kan kapslas så att resten av programmet får ett renare gränssnitt. I senare kapitel kan samma princip användas för sensorer, displayer och aktuatorer.

## Digitala sensormoduler

Många enkla sensormoduler har en digital utgång. Det kan vara en PIR-sensor, ljuströskelmodul, ljudtrigger, vibrationssensor, reed switch, regnsensor eller närhetssensor. Ofta finns en liten komparator på modulen och en potentiometer som ställer tröskeln.

Det gör modulen enkel att använda:

```cpp
const byte sensorPin = 4;

void setup() {
  pinMode(sensorPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(sensorPin) == HIGH) {
    Serial.println("Sensor active");
  }
}
```

Men enkelheten har ett pris. En digital tröskelutgång säger ofta bara “över eller under gräns”. Du får inte veta hur nära gränsen signalen är, hur brusig den är eller om modulen är dåligt kalibrerad.

En digital sensormodul passar bra när:

- du bara behöver en ja/nej-signal
- tröskeln kan justeras på modulen
- långsiktig noggrannhet inte är kritisk
- signalen kan testas enkelt med seriell monitor eller LED

En analog eller digital bussbaserad sensor passar bättre när:

- du behöver mätvärde, inte bara tröskel
- du vill kalibrera i kod
- du behöver logga värden över tid
- du vill kunna analysera marginaler, brus och trend

## Interrupt-signaler från moduler

Vissa sensorer och IC-kretsar har en digital pinne för att signalera att något har hänt. Den kan heta `INT`, `IRQ`, `DRDY`, `ALERT` eller liknande. Sådana signaler används ofta för att slippa fråga enheten hela tiden.

Exempel:

- en rörelsesensor signalerar att data är redo
- en I/O-expander signalerar att en knapp har ändrats
- en strömsensor signalerar att ett tröskelvärde har passerats
- en RTC signalerar alarm eller sekundpuls

Du behöver inte alltid använda avbrott i mikrokontrollern bara för att pinnen heter `INT`. I många fall kan du läsa pinnen vanligt i `loop()`, särskilt om händelsen är långsam. Riktiga avbrott behandlas mer i kapitel 8. I detta kapitel räcker principen: en digital signal från en modul ska ha definierad vilonivå, rätt logiknivå och tydligt aktivt läge.

## Open drain och delade signaler

Vissa utgångar driver inte både HIGH och LOW. En open drain- eller open collector-utgång kan aktivt dra signalen LOW men släpper den annars fri. För att signalen ska bli HIGH behövs en pull-up.

Det här används ofta för:

- I2C-bussar
- interrupt-linjer som delas av flera komponenter
- nivåanpassning mellan vissa kretsar
- signaler där flera enheter ska kunna dra samma linje LOW

Arduino-kod kan ibland efterlikna open drain-beteende genom att växla mellan `OUTPUT LOW` och `INPUT` i stället för att driva HIGH. Det ska göras med försiktighet och bara när du förstår kopplingen.

```cpp
const byte sharedLinePin = 5;

void driveLineLow() {
  pinMode(sharedLinePin, OUTPUT);
  digitalWrite(sharedLinePin, LOW);
}

void releaseLine() {
  pinMode(sharedLinePin, INPUT);
}
```

I de flesta vanliga experiment är detta inte nödvändigt. Men det är viktigt att känna igen principen eftersom du kommer att möta den i I2C, vissa sensormoduler och interrupt-signaler.

## Långa kablar och störningar

En knapp på breadboard med korta ledningar är förlåtande. En knapp på en panel med en meter kabel är en annan sak. Långa ledningar kan fungera som antenner, fånga upp störningar och göra signalflanker långsammare.

Problem som kan uppstå:

- knappen triggar utan att tryckas
- flera tryck registreras trots debounce
- signalen fungerar på skrivbordet men inte i kapsling
- motorer eller LED-strippar stör ingången
- sensorn fungerar tills USB-kabeln byts eller matningen ändras

Åtgärder kan vara:

- använd pull-up eller pull-down med lägre resistans än den interna om miljön är störig
- håll signalkablar korta
- tvinna signal och GND för enkla externa knappar
- separera motor- och lastkablar från signalkablar
- lägg till enkel RC-filtrering vid behov
- använd skärmad kabel eller robustare gränssnitt för längre avstånd
- isolera eller buffra signalen i mer krävande miljöer

För bokens praktiska experiment räcker ofta intern pull-up och korta ledningar. Men när du bygger vidare mot riktiga installationer behöver du tänka på signalmiljön.

## Pin-konflikter och uppstartslägen

Alla GPIO-pinnar är inte lika fria. På vissa kort används vissa pinnar vid uppstart, programmering, USB-seriekommunikation, flashminne, inbyggd LED eller bootval. Det gäller särskilt ESP8266 och ESP32, men även andra kortfamiljer har specialpinnar.

En digital koppling som fungerar på UNO kan därför orsaka problem på ett annat kort om den använder en boot-relaterad pinne. Exempelvis kan en knapp, sensor eller modul hålla en pinne i fel läge under uppstart så att kortet inte startar normalt.

Arbetssättet från kapitel 2 gäller även här:

- kontrollera pinout för exakt kortmodell
- markera boot-relaterade pinnar i dina projektanteckningar
- undvik specialpinnar för första versionen om det finns alternativ
- testa uppstart med alla moduler inkopplade
- dokumentera om en signal är aktiv LOW och kan påverka uppstart

## När digital I/O är rätt val

Digital I/O är rätt när informationen verkligen är binär eller när en modul redan gjort tolkningen åt dig.

Typiska fall:

- knapp tryckt eller inte tryckt
- dörrkontakt öppen eller stängd
- PIR-sensor aktiv eller inaktiv
- gränslägesbrytare träffad eller inte
- relämodul på eller av
- status-LED på eller av
- chip select för SPI
- enable-signal för modul

Digital I/O är ofta fel eller otillräckligt när du behöver veta storlek, trend, marginal eller kvalitet.

Exempel:

- ljusnivå, inte bara mörkt/ljust
- temperatur, inte bara över/under tröskel
- ljudnivå, inte bara ljud/inte ljud
- motorposition, inte bara ändläge
- batterispänning, inte bara “låg”

I sådana fall ska du överväga analog läsning, I2C/SPI-sensor eller annan mätteknik.

## Referensmönster: robust knappmodul utan delay

Det här referensmönstret visar hur en knapp kan läsas stabilt utan `delay()`, med intern pull-up, debounce och tydlig händelseloggik. Mönstret passar när en knapp ska styra läge, bekräfta ett val eller fungera som användarinput i ett större projekt.

### Vad mönstret visar

Mönstret visar hur du kan:

- använder intern pull-up
- läser en knapp utan flytande ingång
- filtrerar kontaktstuds
- skapar en händelse när knappen trycks
- växlar ett läge mellan `idle`, `active` och `error`
- visar status med inbyggd LED eller extern LED
- använder `millis()` i stället för `delay()`

### Det här används i exemplet

- Ett Arduino-kompatibelt kort
- En tryckknapp
- Kopplingskablar
- Breadboard
- Eventuellt en extern LED med seriemotstånd
- USB-kabel och seriell monitor

Om du använder kortets inbyggda LED behöver du kontrollera vilket pinnamn som gäller. På många kort fungerar `LED_BUILTIN`, men inte på alla.

### Koppling

Koppla knappen mellan vald digital pinne och GND. I koden använder vi intern pull-up.

| Funktion | Arduino UNO/Nano-exempel | Kommentar |
|---|---|---|
| Knappsignal | D2 | Kopplas till ena sidan av knappen |
| Knappens andra sida | GND | Tryckt knapp ger LOW |
| Status-LED | `LED_BUILTIN` | Kan ersättas med extern LED och motstånd |
| Matning | USB | Räcker för detta referensmönster |

För ESP8266, ESP32, Pico eller andra kort: välj en GPIO som inte är bootkritisk och som fungerar som vanlig digital ingång.

### Kod

```cpp
enum SystemMode {
  MODE_IDLE,
  MODE_ACTIVE,
  MODE_ERROR
};

struct DebouncedButton {
  byte pin;
  bool stableState = HIGH;
  bool lastRawState = HIGH;
  bool previousStableState = HIGH;
  unsigned long lastChangeMs = 0;
  unsigned long debounceMs = 30;

  void begin() {
    pinMode(pin, INPUT_PULLUP);
    stableState = digitalRead(pin);
    lastRawState = stableState;
    previousStableState = stableState;
  }

  void update(unsigned long now) {
    bool rawState = digitalRead(pin);

    if (rawState != lastRawState) {
      lastRawState = rawState;
      lastChangeMs = now;
    }

    if ((now - lastChangeMs) >= debounceMs && stableState != rawState) {
      previousStableState = stableState;
      stableState = rawState;
    }
  }

  bool wasPressed() const {
    return previousStableState == HIGH && stableState == LOW;
  }

  bool isPressed() const {
    return stableState == LOW;
  }

  void consumeEvent() {
    previousStableState = stableState;
  }
};

const byte buttonPin = 2;
const byte statusLedPin = LED_BUILTIN;

DebouncedButton modeButton{buttonPin};
SystemMode mode = MODE_IDLE;

unsigned long lastStatusMs = 0;
const unsigned long statusIntervalMs = 500;

void setup() {
  pinMode(statusLedPin, OUTPUT);
  Serial.begin(115200);

  modeButton.begin();

  Serial.println("Digital I/O pattern started");
  printMode();
}

void loop() {
  unsigned long now = millis();

  modeButton.update(now);

  if (modeButton.wasPressed()) {
    nextMode();
    printMode();
    modeButton.consumeEvent();
  }

  updateStatusLed(now);
}

void nextMode() {
  if (mode == MODE_IDLE) {
    mode = MODE_ACTIVE;
  } else if (mode == MODE_ACTIVE) {
    mode = MODE_ERROR;
  } else {
    mode = MODE_IDLE;
  }
}

void updateStatusLed(unsigned long now) {
  if (mode == MODE_IDLE) {
    digitalWrite(statusLedPin, LOW);
    return;
  }

  if (mode == MODE_ACTIVE) {
    digitalWrite(statusLedPin, HIGH);
    return;
  }

  if (mode == MODE_ERROR && (now - lastStatusMs) >= statusIntervalMs) {
    lastStatusMs = now;
    digitalWrite(statusLedPin, !digitalRead(statusLedPin));
  }
}

void printMode() {
  Serial.print("Mode: ");

  if (mode == MODE_IDLE) {
    Serial.println("idle");
  } else if (mode == MODE_ACTIVE) {
    Serial.println("active");
  } else {
    Serial.println("error");
  }
}
```

### Förväntat resultat

När programmet startar skriver det ut aktuellt läge. Varje tydlig knapptryckning växlar till nästa läge. Status-LED visar läget:

| Läge | LED-beteende |
|---|---|
| `idle` | Släckt |
| `active` | Tänd |
| `error` | Blinkar |

Knappen ska inte hoppa flera lägen vid ett normalt tryck. Om den gör det behöver du felsöka koppling, debounce-tid eller kortets pinnval.

### Kontrollpunkter när samma knappkod flyttas mellan kort

När samma knappmönster flyttas till ett annat kort är det oftast inte debounce-koden som ändras först, utan pinnval och elektriska antaganden.

Kontrollera detta:

- Välj en digital ingång som inte är bootkritisk.
- Kontrollera om `LED_BUILTIN` finns och om den är aktiv HIGH eller aktiv LOW.
- Kontrollera om kortet är 5 V eller 3,3 V.
- Kontrollera att intern pull-up fungerar på vald pinne.
- Byt debounce-tid bara om beteendet faktiskt kräver det.
- Spara fungerande pinnval tillsammans med projektets konfiguration.

Då blir samma knappmodul lättare att återanvända i senare projekt.

## Praktiska varianter

### Variation 1: Långt knapptryck

Lägg till logik som skiljer mellan kort tryck och långt tryck. Ett kort tryck kan byta läge, medan ett långt tryck återställer systemet till `idle`.

Grundidé:

- spara tiden när knappen blir tryckt
- jämför med tiden när knappen släpps
- tolka skillnaden som kort eller långt tryck

### Variation 2: Två knappar

Lägg till en andra knapp med samma `DebouncedButton`-struktur. Låt den ena knappen byta läge och den andra bekräfta eller återställa.

Det visar ett viktigt mönster: när du kapslar hårdvarulogik kan du lägga till fler ingångar utan att duplicera all kod.

### Variation 3: Digital sensormodul

Byt ut knappen mot en digital sensormodul, till exempel PIR, reed switch eller vibrationssensor. Kontrollera om modulen är aktiv HIGH eller aktiv LOW och ändra hjälpmetoden så att koden fortfarande uttrycker `isActive()` i stället för rå elektrisk polaritet.

## Vanliga misstag

- **Misstag: Att läsa en knapp med `INPUT` utan pull-up eller pull-down.**
  - **Varför det händer:** Kopplingen ser komplett ut när knappen är tryckt, men ingången saknar definierat viloläge.
  - **Hur man undviker det:** Använd `INPUT_PULLUP` eller ett externt pull-motstånd.

- **Misstag: Att tolka LOW som fel när intern pull-up används.**
  - **Varför det händer:** Det känns intuitivt att tryckt knapp borde vara HIGH.
  - **Hur man undviker det:** Dokumentera att knappen är aktiv LOW och kapsla logiken i en funktion som `isButtonPressed()`.

- **Misstag: Att lösa debounce med långa `delay()` i ett växande projekt.**
  - **Varför det händer:** Det fungerar i första testet.
  - **Hur man undviker det:** Använd `millis()` och händelsebaserad knapphantering redan från början.

- **Misstag: Att driva last direkt från GPIO.**
  - **Varför det händer:** En pinne kan tända en LED, och då verkar det som att den kan driva andra saker också.
  - **Hur man undviker det:** Låt GPIO vara styrsignal och använd transistor, MOSFET, relämodul eller drivkrets för laster.

- **Misstag: Att anta att samma pinne fungerar på alla kort.**
  - **Varför det händer:** Arduino-API:t gör kod portabel, men hårdvaran är inte identisk.
  - **Hur man undviker det:** Kontrollera pinout, boot-pinnar, inbyggda funktioner och logiknivå för varje kort.

- **Misstag: Att ignorera långa kablar.**
  - **Varför det händer:** Kopplingen fungerar på breadboard.
  - **Hur man undviker det:** Testa med verklig kabellängd, använd tydliga pullups och separera signalledningar från störande laster.

## Snabbreferens

| Situation | Rekommenderat förstaval | Kommentar |
|---|---|---|
| Enkel knapp | `INPUT_PULLUP`, knapp mot GND | Tryckt knapp blir LOW |
| Panelknapp med längre kabel | Extern pull-up eller pull-down, kort test med multimeter | Intern pull-up kan vara för svag i störig miljö |
| Digital sensormodul | Läs modulens aktivt läge och logiknivå | Kontrollera om utgången är aktiv HIGH eller LOW |
| Enkel status-LED | GPIO plus seriemotstånd eller `LED_BUILTIN` | Kontrollera om inbyggd LED är inverterad på kortet |
| Större last | GPIO som styr drivkrets | Driv inte last direkt från pinnen |
| Delad signallinje | Pull-up och open drain-princip | Vanligt i I2C och vissa interrupt-linjer |
| Portering mellan kort | Dokumenterad pinout och logiknivå | Testa uppstart med kopplingar anslutna |


## Begreppsförklaring: pull-up, pull-down och open drain

En digital ingång som inte är tydligt ansluten till HIGH eller LOW kan flyta och ge slumpmässiga värden. Därför används ofta:

- **Pull-up:** en resistor som drar signalen mot HIGH när inget annat aktivt driver den.
- **Pull-down:** en resistor som drar signalen mot LOW när inget annat aktivt driver den.
- **Open drain/open collector:** ett signalmönster där en enhet aktivt kan dra linjen låg, men låter en pull-up dra den hög.

Det här blir särskilt viktigt för knappar, I2C-bussar och moduler där flera enheter delar samma signalledning.

## Relaterat


- Använd kapitel 8 när en digital signal behöver fångas som snabb puls, händelse eller timeout.
- Använd kapitel 9 när modulen inte bara har en digital signal utan använder I2C, SPI, UART eller 1-Wire.
- Använd kapitel 21 innan en digital pin används för att styra reläer, motorer, lampor eller andra laster.


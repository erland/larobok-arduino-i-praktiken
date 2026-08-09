# 15. Raspberry Pi Pico, RP2040 och RP2350 i Arduino-miljö

## Kortprofil i korthet
Raspberry Pi Pico är ett intressant sidospår i Arduino-världen. Det är inte ett Arduino-kort i klassisk mening, men det kan användas på ett Arduino-liknande sätt genom en Arduino core. Resultatet är en plattform som ofta känns bekant för en Arduino-användare, men som har en annan personlighet än både klassiska ATmega-kort och ESP-baserade kort.

Pico-korten är särskilt intressanta när du vill ha många GPIO, bra pris/prestanda, stabil timing, USB-möjligheter och en mikrokontroller som är byggd för experiment snarare än för att vara ett färdigt IoT-kort. RP2040, som sitter i den ursprungliga Raspberry Pi Pico, blev snabbt populär eftersom den kombinerar två kärnor, gott om GPIO, bra dokumentation och ett unikt I/O-system som kallas PIO. RP2350, som används i Pico 2-familjen och liknande kort, bygger vidare på idén med mer minne, modernare kärnor och fler möjligheter.

Det här kapitlet finns för att hjälpa dig placera Pico i rätt sammanhang:

- När är Pico ett bättre val än klassisk Arduino?
- När är Pico ett bättre val än ESP8266 eller ESP32?
- När är det bättre att välja ett kort med inbyggt Wi-Fi?
- Vad betyder RP2040, RP2350, Pico, Pico W, Pico 2 och Pico 2 W i praktiken?
- Vad innebär PIO för en Arduino-programmerare?
- Vilka begränsningar behöver du känna till kring spänning, analog mätning, strömförsörjning och bibliotek?

Målet är inte att göra dig till Pico-specialist. Målet är att ge dig en praktisk karta så att du vet när Pico är rätt val, när det är fel val och hur du kan använda Pico som en kraftfull Arduino-kompatibel testplattform.

## Bedöm kortet med detta i åtanke

Raspberry Pi Pico och andra RP2040/RP2350-kort passar ofta när du vill ha snabb och billig I/O, många GPIO eller deterministisk styrning utan inbyggd Wi-Fi som standard. Kontrollera särskilt 3,3 V-logik, ADC-begränsningar, pinout, bibliotek, eventuell trådlös variant och vilken Arduino-core projektet bygger på.

## Plattformen i praktiken

Raspberry Pi Pico programmeras ofta med MicroPython, C/C++ via Raspberry Pi Pico SDK eller CircuitPython. I den här boken intresserar vi oss för Arduino-miljön, eftersom vi vill kunna jämföra Pico med andra Arduino-kompatibla kort.

Det centrala är att Pico behöver en Arduino core. En sådan core översätter Arduino-programmeringsmodellen till RP2040/RP2350-plattformen. Du kan då skriva kod som liknar andra Arduino-sketcher:

```cpp
const int ledPin = 25;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(250);
  digitalWrite(ledPin, LOW);
  delay(250);
}
```

Det ser enkelt ut, men under ytan skiljer sig Pico från klassiska Arduino-kort. Den har annan processor, annan minnesmodell, annan USB-lösning, annan pinout, annan ADC och andra möjligheter för tidskritisk I/O.

Det betyder att du bör se Pico som en Arduino-kompatibel plattform, inte som “en snabbare UNO”. Många grundläggande Arduino-mönster fungerar, men vissa detaljer behöver kontrolleras.

## RP2040, RP2350 och Pico-familjen

### RP2040

RP2040 är mikrokontrollern i den ursprungliga Raspberry Pi Pico. Den är känd för:

- två processorkärnor
- många GPIO
- flera UART-, I2C- och SPI-gränssnitt
- PWM på många pinnar
- analoga ingångar
- USB-stöd
- PIO, alltså programmerbara I/O-state machines

Det praktiska värdet är att RP2040 passar väldigt bra för experiment där du vill koppla många signaler, skapa egen timing eller bygga ett projekt som inte behöver inbyggt Wi-Fi.

RP2040 är däremot inte automatiskt det bästa valet för batteridriven IoT, färdiga molnexempel eller Wi-Fi-projekt. Där är ESP32 eller Pico W ofta mer naturliga.

### RP2350

RP2350 är en nyare mikrokontrollerfamilj som används i Pico 2-kort och kompatibla RP2350-kort. Den har mer modern arkitektur och mer resurser än RP2040. På praktisk nivå betyder det att Pico 2 ofta är ett bättre val när du vill ha mer marginal, men ändå vill vara kvar i Pico-ekosystemet.

För den här boken räcker det att tänka så här:

| Behov | RP2040/Pico | RP2350/Pico 2 |
|---|---|---|
| Billiga experiment | Mycket bra | Bra, men kan vara dyrare |
| Många GPIO | Mycket bra | Mycket bra |
| Mer modern plattform | Bra | Bättre |
| Mer minne och säkerhetsfunktioner | Begränsat jämfört med nyare kort | Bättre |
| Kompatibilitet med äldre Pico-exempel | Mycket bra | Ofta bra, men kontrollera core och bibliotek |
| Nya projekt där priset inte är enda faktorn | Bra | Ofta bättre |

RP2350 är inte en anledning att kasta bort RP2040. Snarare är det ett tecken på att Pico-familjen har blivit bredare.

### Pico, Pico W, Pico 2 och Pico 2 W

En praktisk jämförelse:

| Kort | Typisk roll | Styrka | Begränsning |
|---|---|---|---|
| Pico | Grundkort med RP2040 | Billigt, enkelt, många GPIO | Ingen inbyggd trådlös kommunikation |
| Pico W | RP2040 med trådlöst stöd | Wi-Fi/Bluetooth-hårdvara i Pico-format | Trådlöst stöd beror på mjukvarustack och core |
| Pico 2 | Nyare RP2350-baserat kort | Mer modern mikrokontroller | Inte lika etablerat i äldre exempel |
| Pico 2 W | RP2350 med trådlöst stöd | Nyare Pico med nätverksmöjlighet | Kontrollera alltid aktuellt biblioteksläge |

När du väljer mellan dessa bör du börja med projektets krav. Behöver projektet inte nätverk är ett vanligt Pico- eller Pico 2-kort ofta enklare. Behöver projektet skicka data trådlöst är W-varianterna mer relevanta, men du bör kontrollera att den Arduino core och de bibliotek du tänker använda stöder just din kombination av kort och funktion.

## När Pico är ett bra val

Pico är ofta ett bra val när projektet är I/O-tungt eller timingnära.

Typiska situationer:

- du behöver många digitala pinnar
- du vill läsa flera knappar, encoders eller digitala signaler
- du vill styra flera PWM-utgångar
- du vill experimentera med protokoll, signaler eller specialtiming
- du vill ha ett billigt men kraftfullt kort utan Wi-Fi-komplexitet
- du vill använda USB på ett mer flexibelt sätt än på enklare Arduino-kort
- du vill bygga en stabil lokal styrenhet snarare än ett molnkopplat IoT-projekt

Ett typiskt Pico-projekt kan vara:

- en knapp- och LED-matris
- en motorstyrd mekanisk panel
- en sensorstation med lokal display
- en datalogger utan nätverk
- ett testinstrument
- en signalgenerator på hobby- eller undervisningsnivå
- en gateway mellan flera enkla signaler och USB

Pico är också trevlig som testkort eftersom den inte försöker göra allt. Den har inte samma inbyggda nätverksfokus som ESP32. Det kan vara en fördel: färre radio- och strömsparlager, färre boot-pinnar att råka störa och ofta ett tydligare fokus på ren I/O.

## När du bör välja något annat

Pico är inte alltid rätt val.

Välj hellre ESP8266 eller ESP32 när:

- Wi-Fi är centralt från början
- projektet ska använda MQTT, webserver, BLE eller moderna IoT-protokoll
- du vill ha många färdiga nätverksexempel
- trådlös kommunikation är viktigare än ren I/O

Välj hellre klassisk Arduino UNO/Nano när:

- du behöver 5 V-logik utan nivåskiftning
- du arbetar med äldre shields och exempel
- målgruppen för projektet är nybörjare
- maximal enkelhet är viktigare än prestanda

Välj hellre ett modernt officiellt Arduino-kort när:

- du vill ha tydligare officiell Arduino-dokumentation
- du vill ha bättre koppling till Arduino Cloud eller officiella exempel
- du prioriterar långsiktig undervisningsbarhet framför låg kostnad

Välj hellre Teensy, Portenta eller annan mer avancerad plattform när:

- projektet kräver mycket hög prestanda
- ljudbehandling, avancerad grafik eller realtidskrav dominerar
- du behöver mer minne, fler specialgränssnitt eller professionell formfaktor

Pico är starkt, men det är inte ett universalval. Det är bäst när du behöver en prisvärd, kraftfull och I/O-vänlig mikrokontrollerplattform.

## Pinout och pinnamn

Pico använder ofta GPIO-namn som GP0, GP1, GP2 och så vidare. I Arduino-kod används pin-nummer enligt den core du installerat. Ofta sammanfaller Arduino-pin-numret med GPIO-numret, men du bör inte anta det utan att kontrollera dokumentationen för den board-definition du valt.

Skriv därför inte bara:

```cpp
const int buttonPin = 2;
```

Skriv hellre:

```cpp
const int buttonPin = 2;  // GP2 on this board definition
```

Eller ännu tydligare i referensmönstrets dokumentation:

```text
buttonPin = 2
Fysisk signal: GP2
Kortets fysiska pinne: kontrollera Pico-pinout
Koppling: knapp mellan GP2 och GND, intern pull-up används
```

Det här är samma princip som i tidigare kapitel: skilj mellan fysisk pinne, GPIO-funktion och kodens namn. Den regeln är extra viktig på kort som finns i många varianter.

## Spänningsnivåer och matning

Pico arbetar med 3,3 V-logik. Det betyder att du bör vara försiktig med 5 V-signaler in till GPIO. Vissa moduler kan matas med 5 V men ge 3,3 V-signaler. Andra ger 5 V ut. Du behöver kontrollera modulen, inte bara rubriken i webbshoppen.

Praktiska regler:

- Mata inte en Pico-GPIO direkt med 5 V-signal.
- Använd nivåskiftning när en 5 V-modul skickar digital signal till Pico.
- Se till att Pico och modulen har gemensam jord när de ska kommunicera.
- Var försiktig med relämoduler, motorer och LED-strippar som behöver mer ström än Pico kan leverera.
- Använd extern matning för laster och låt Pico styra via transistor, MOSFET eller drivmodul.
- Dokumentera alltid om sensorn är 3,3 V-native, 5 V-tolerant eller kräver nivåskiftning.

Exempel på dokumentation:

```text
Kort: Raspberry Pi Pico
Sensor: BME280 breakout
Matning: 3,3 V från Pico
Gränssnitt: I2C
Logiknivå: 3,3 V
Nivåskiftning: inte nödvändig i denna koppling
Risk: kontrollera att breakout-kortet inte har 5 V pull-ups på I2C
```

Det sista är viktigt. En I2C-modul kan ha pull-up-motstånd till sin matningsspänning. Om modulen matas med 5 V kan I2C-linjerna hamna på 5 V. Det är inte vad du vill koppla direkt till en 3,3 V-mikrokontroller.

## Kommunikation på Pico

Pico lämpar sig väl för kommunikation med sensorer och moduler. Den kan använda vanliga Arduino-mönster för UART, I2C och SPI, men du bör kontrollera vilka pinnar som används för vald buss.

### I2C

I2C är vanligt för sensorer, OLED-displayer, I/O-expanders och realtidsklockor. På Pico är det vanligt att du kan välja mellan flera möjliga I2C-pinnar, beroende på core och konfiguration.

Ett enkelt I2C-test kan börja med en scanner:

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(10);
  }

  Wire.begin();

  Serial.println("Scanning I2C bus...");
  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Found I2C device at 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.println(address, HEX);
    }
  }
  Serial.println("Done.");
}

void loop() {
}
```

Om inget hittas bör du kontrollera:

- SDA och SCL är kopplade till rätt pinnar
- modulen får rätt spänning
- GND är gemensam
- I2C-adressen är rätt
- pull-up-motstånd finns och går till rätt spänning
- rätt board är vald i Arduino IDE

### SPI

SPI passar bra för snabba displayer, SD-kort och vissa ADC-/DAC-kretsar. Eftersom SPI använder separata chip select-signaler kan du ha flera enheter på samma buss, men varje enhet behöver egen CS.

Praktiska Pico-frågor:

- Vilken SPI-buss använder du?
- Vilka pinnar är SCK, MOSI och MISO?
- Är chip select en vanlig GPIO?
- Behöver modulen 3,3 V eller 5 V?
- Är SD-kortmodulen korrekt nivåanpassad?

### UART

UART passar för GPS, seriella sensorer, vissa kommunikationsmoduler och debug. Pico har ofta mer än en hårdvaru-UART, vilket gör den praktisk när du vill ha både debug via USB och separat seriell kommunikation till en modul.

Det är en stor skillnad mot enklare kort där en enda seriell port kan behöva delas mellan uppladdning, debug och extern modul.

## PIO: Picos särskilda superkraft

PIO står för Programmable I/O. Det är ett särskilt system i RP2040/RP2350-familjen som kan hantera tidskritiska I/O-uppgifter utan att huvudprocessorn behöver göra varje bitoperation själv.

För en erfaren programmerare kan PIO beskrivas som små specialiserade state machines nära pinnarna. De kan användas för att skapa eller läsa signaler med exakt timing.

PIO kan vara användbart för:

- egenutformade seriella protokoll
- LED-protokoll med känslig timing
- parallella signaler
- pulsmätning
- enkla signalgeneratorer
- experiment där `digitalWrite()` och interrupt inte räcker

I en Arduino-bok bör vi inte börja med PIO. Det är mer avancerat än vanlig Arduino-kod. Men det är viktigt att veta att PIO finns, eftersom det är en av de stora anledningarna att välja Pico framför många andra kort.

Ett praktiskt sätt att tänka:

| Problem | Vanlig Arduino-lösning | Pico-möjlighet |
|---|---|---|
| Blinkande LED | `digitalWrite()` och `millis()` | Samma som Arduino |
| PWM | `analogWrite()` eller timer | Samma princip, ofta många pinnar |
| Snabb specialsignal | Interrupt, timer eller bit-banging | PIO kan vara bättre |
| Många exakta pulser | Svårt på enklare kort | PIO eller dedikerad hårdvara |
| Tidskritisk LED-strip | Bibliotek med noggrann timing | Bibliotek kan använda PIO under ytan |

Du behöver inte skriva PIO-kod för att dra nytta av PIO. Vissa bibliotek använder PIO internt. Det är ofta den bästa vägen i början.

## Picos unika styrka: stabil timing och PIO

Pico är ofta mest intressant när projektet behöver stabil lokal styrning, många GPIO eller signaler med bättre timing än en vanlig `loop()` enkelt kan ge. Det betyder inte att varje Pico-projekt ska börja med PIO-kod, men det är bra att känna igen när PIO kan vara rätt verktyg.

Typiska fall där Pico kan vara starkare än ett enklare Arduino-kort:

| Situation | Varför Pico kan passa |
|---|---|
| Många lokala in- och utgångar | gott om GPIO och flera bussinstanser |
| Exakta pulser | timing kan flyttas närmare hårdvaran |
| Specialprotokoll | PIO kan skapa eller läsa signaler som saknar färdigt periferiestöd |
| Tidskritiska LED-protokoll | bibliotek kan använda PIO under ytan |
| Lokal styrnod utan radio | mindre nätverkskomplexitet än Wi-Fi-kort |

Börja ändå med vanlig Arduino-kod. Använd PIO först när timing, signalform eller antal samtidiga I/O gör den vanliga lösningen svår att lita på.

## Analog mätning på Pico

Pico har analoga ingångar, men du bör inte se den som ett precisionsinstrument. Samma principer från ADC-kapitlet gäller:

- kontrollera mätområde
- undvik att mata analog ingång med för hög spänning
- använd stabil referens om mätningen behöver vara noggrann
- filtrera brus i både hårdvara och mjukvara
- kalibrera om resultatet ska tolkas som fysisk storhet
- jämför inte råvärden mellan olika kort utan kontroll

Ett enkelt analogt test:

```cpp
const int analogPin = 26;  // Often GP26 / ADC0 on Pico-style boards

void setup() {
  Serial.begin(115200);
}

void loop() {
  int raw = analogRead(analogPin);
  float normalized = raw / 1023.0;

  Serial.print("raw=");
  Serial.print(raw);
  Serial.print(" normalized=");
  Serial.println(normalized, 3);

  delay(200);
}
```

Det här exemplet är medvetet försiktigt. Olika cores och kort kan använda olika ADC-upplösning som standard. På vissa plattformar kan du behöva ställa upplösning eller tolka `analogRead()` annorlunda. Därför är det bättre att börja med normaliserade värden och dokumentera den faktiska upplösningen i referensmönstret.

Ett bättre experimentsteg är att först skriva ut maxvärdet du förväntar dig enligt core-dokumentationen och sedan mäta mot kända spänningar.

## USB som praktisk styrka

Pico-kort har ofta en tydlig USB-närvaro. USB används för ström, uppladdning och seriell kommunikation. På vissa projekt kan USB även bli en del av själva funktionen, till exempel när Pico fungerar som en liten inmatningsenhet, seriell brygga eller testutrustning.

I den här boken bör USB behandlas praktiskt:

- USB gör seriell debug bekvämt.
- Kortet kan ibland behöva sättas i bootloader-läge vid uppladdningsproblem.
- Kabeln spelar roll. Vissa USB-kablar är endast laddkablar.
- USB-matning räcker inte för motorer, många LED eller tunga laster.
- USB-seriell port kan bete sig annorlunda än klassisk UART via USB-seriechip.

Ett vanligt felsökningsmönster:

```text
Problem: Kortet syns inte i Arduino IDE.
Kontrollera:

1. Är USB-kabeln en datakabel?
2. Är rätt board package installerat?
3. Är kortet i bootloader-läge?
4. Visas kortet som lagringsenhet eller seriell port?
5. Är rätt port vald?
6. Har operativsystemet låst porten i ett annat program?
```

## Flera kärnor och samtidighet

Både RP2040 och RP2350-familjen erbjuder mer än en processorkärna, men det betyder inte att varje Arduino-projekt bör börja med multikärnig kod. För de flesta experiment är det bättre att skriva enkel, icke-blockerande kod med `millis()` och tydlig tillståndslogik.

Flera kärnor kan bli intressant när du har:

- en uppgift som samlar data kontinuerligt
- en annan uppgift som uppdaterar display eller användargränssnitt
- timingkänslig logik som inte bör störas av långsam kod
- experiment där du medvetet vill utforska samtidighet

Men det finns en kostnad:

- delat tillstånd måste skyddas
- buggar blir svårare att reproducera
- debug blir svårare
- bibliotek är inte alltid skrivna för att användas från flera kärnor

I den här boken bör grundregeln vara:

> Använd först icke-blockerande enkärnig kod. Använd flera kärnor först när du kan beskriva exakt vilket problem det löser.

Det är samma designprincip som i andra delar av boken: välj inte den mer avancerade tekniken för att den finns, utan för att den löser ett tydligt problem.

## Referensmönster: Pico som lokal sensor- och styrnod

Det här referensmönstret visar en liten Pico-baserad nod som läser en analog signal, läser en digital knapp och styr en LED. Mönstret är enkelt, men det verifierar viktiga Pico-principer:

- kontrollera pinout
- använda 3,3 V-logik
- skilja mellan analog och digital signal
- skriva icke-blockerande kod
- använda seriell monitor för felsökning

### Det här används i exemplet

Du behöver:

- ett Raspberry Pi Pico-, Pico W-, Pico 2- eller Pico 2 W-liknande kort
- en potentiometer, exempelvis 10 kΩ
- en tryckknapp
- en LED
- ett lämpligt seriemotstånd till LED, exempelvis 220–1000 Ω
- kopplingskablar
- breadboard
- USB-datakabel

### Kopplingsidé

Använd följande principer:

| Funktion | Pico-signal | Kommentar |
|---|---|---|
| Potentiometer mittpinne | analog ingång, exempelvis GP26/ADC0 | Kontrollera pinout för ditt kort |
| Potentiometer ytterpinnar | 3,3 V och GND | Använd inte 5 V till analog ingång |
| Knapp | digital ingång, exempelvis GP2 | Använd intern pull-up |
| LED | digital/PWM-utgång, exempelvis GP15 | Använd seriemotstånd |
| Gemensam referens | GND | Alla delar delar jord |

Kontrollera exakt vilka pinnar du faktiskt använder innan du felsöker koden.

### Kod

```cpp
const int analogPin = 26;  // Check: GP26 / ADC0 on your board definition
const int buttonPin = 2;   // Check: GP2
const int ledPin = 15;     // Check: GP15

unsigned long lastSampleTime = 0;
const unsigned long sampleIntervalMs = 200;

bool lastButtonState = HIGH;

void setup() {
  Serial.begin(115200);

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);

  Serial.println("Pico sensor and output node");
  Serial.println("Check pin mapping before trusting the readings.");
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleTime >= sampleIntervalMs) {
    lastSampleTime = now;

    int raw = analogRead(analogPin);
    bool buttonPressed = digitalRead(buttonPin) == LOW;

    int ledLevel = map(raw, 0, 1023, 0, 255);
    ledLevel = constrain(ledLevel, 0, 255);

    if (buttonPressed) {
      analogWrite(ledPin, ledLevel);
    } else {
      analogWrite(ledPin, 0);
    }

    Serial.print("raw=");
    Serial.print(raw);
    Serial.print(" ledLevel=");
    Serial.print(ledLevel);
    Serial.print(" button=");
    Serial.println(buttonPressed ? "pressed" : "released");
  }
}
```

### Viktig kontroll

Det här exemplet antar att `analogRead()` ger värden i intervallet 0–1023. Om din core använder annan upplösning eller om du har ändrat ADC-upplösningen behöver du justera `map()`-raden.

Ett säkrare nästa steg är att införa en konstant:

```cpp
const int adcMax = 1023;
```

Och sedan använda:

```cpp
int ledLevel = map(raw, 0, adcMax, 0, 255);
```

Då blir det tydligt vad referensmönstret antar.

### Förväntat resultat

När knappen inte är nedtryckt ska LED vara släckt. När knappen är nedtryckt ska potentiometern styra LED-ljusstyrkan. Seriell monitor ska visa råvärde, beräknad LED-nivå och knappstatus.

### Anpassningar

När grundreferensmönstret fungerar kan du prova att:

- byta LED mot en RGB-LED
- visa värdet på en OLED-display via I2C
- logga min- och maxvärde över tid
- byta potentiometern mot en ljussensor
- använda en encoder i stället för knapp
- portera samma experiment till UNO, ESP32 och Pico och jämföra skillnader

Det sista är särskilt värdefullt. Samma experiment visar tydligt hur kortfamiljer skiljer sig i pinout, ADC, PWM och spänningsnivå.

## Valguide

### Välj Pico eller Pico 2 när

- du vill ha många GPIO
- du vill ha ett billigt men kraftfullt testkort
- projektet är lokalt och behöver inte nätverk
- du vill utforska timing, PWM, signaler och PIO
- du vill ha bra separation mellan debug via USB och externa seriella moduler
- du vill bygga ett undervisnings- eller labbprojekt där I/O står i centrum

### Välj Pico W eller Pico 2 W när

- du vill behålla Pico-formfaktorn men behöver trådlös kommunikation
- projektet behöver skicka data lokalt över nätverk
- du accepterar att nätverksstöd och bibliotek behöver kontrolleras noggrant för vald core
- du vill jämföra Pico-ekosystemet med ESP32 i ett IoT-liknande projekt

### Välj ESP32 i stället när

- Wi-Fi, BLE eller IoT är huvudfunktionen
- du vill ha mycket färdiga nätverksexempel
- du behöver ett stort ekosystem av IoT-bibliotek
- du accepterar ESP32-familjens pinout-, ADC- och strömsparnyanser

### Välj klassisk Arduino i stället när

- 5 V-logik är viktigt
- projektet bygger på äldre shields
- du vill ha maximal enkelhet
- du undervisar absoluta nybörjare

### Välj ett mer avancerat kort när

- Pico inte har nog med minne eller specialfunktioner
- projektet kräver avancerad ljudbehandling, grafik eller maskininlärning
- du behöver industriella anslutningar eller mer robust formfaktor

## Vanliga misstag

- **Misstag:** Att behandla Pico som en 5 V-Arduino.
  - **Varför det händer:** Kortet används i Arduino IDE och känns därför som ett Arduino-kort.
  - **Hur man undviker det:** Dokumentera alltid att Pico använder 3,3 V-logik och kontrollera alla ingångssignaler.

- **Misstag:** Att koppla efter en bild utan att kontrollera pinout.
  - **Varför det händer:** Pico-liknande kort kan ha olika märkning, och exempel kan använda olika pinnamn.
  - **Hur man undviker det:** Kontrollera aktuell pinout och skriv både GPIO-namn och kodens pin-nummer i projektanteckningarna.

- **Misstag:** Att anta att alla Arduino-bibliotek fungerar likadant på Pico.
  - **Varför det händer:** Arduino-API:t ser likadant ut på ytan.
  - **Hur man undviker det:** Testa varje bibliotek i en minimal sketch innan du integrerar det i större projekt.

- **Misstag:** Att välja Pico W eller Pico 2 W enbart för att “Pico plus Wi-Fi” låter bäst.
  - **Varför det händer:** Trådlös kommunikation uppfattas som en enkel tilläggsfunktion.
  - **Hur man undviker det:** Kontrollera aktuellt stöd i vald Arduino core och jämför med ESP32 om nätverk är projektets huvudfunktion.

- **Misstag:** Att använda flera kärnor för tidigt.
  - **Varför det händer:** Flera kärnor låter som en enkel prestandavinst.
  - **Hur man undviker det:** Börja med `millis()`-baserad icke-blockerande kod och använd flera kärnor först när du har ett tydligt behov.

- **Misstag:** Att glömma ADC-upplösning och referens.
  - **Varför det händer:** `analogRead()` ser likadant ut som på andra Arduino-kort.
  - **Hur man undviker det:** Dokumentera förväntat värdeintervall och kalibrera mätningen innan du tolkar den som fysisk storhet.

## Felsökning

När ett Pico-experiment inte fungerar, felsök i denna ordning:

1. **Board-val:** Är rätt Pico-, Pico W-, Pico 2- eller RP2040/RP2350-kort valt?
2. **USB-kabel:** Är kabeln en datakabel?
3. **Uppladdningsläge:** Behöver kortet sättas i bootloader-läge?
4. **Serial monitor:** Är rätt port och baud rate vald?
5. **Pinout:** Stämmer kodens pin-nummer med den fysiska kopplingen?
6. **Spänning:** Får modulen 3,3 V eller 5 V, och är det rätt?
7. **Logiknivå:** Finns någon 5 V-signal som går direkt till Pico?
8. **GND:** Delar alla moduler gemensam jord?
9. **Bibliotek:** Fungerar bibliotekets enklaste exempel på just ditt kort?
10. **Minimal sketch:** Kan du isolera felet till kort, pinne, modul eller bibliotek?

En bra Pico-felsökning börjar nästan alltid med tre minimala tester:

- blinka en LED
- skriv till seriell monitor
- läs en pinne eller I2C-enhet

Först därefter bör du kombinera flera funktioner.

## Snabbreferens

| Fråga | Kort svar |
|---|---|
| Är Pico ett officiellt Arduino-kort? | Nej, men det kan användas i Arduino-miljö via lämplig core. |
| Är Pico 5 V-kompatibelt? | Nej, räkna med 3,3 V-logik och kontrollera alla signaler. |
| När är Pico särskilt bra? | Många GPIO, timing, PWM, USB och lokala styrprojekt. |
| När är ESP32 bättre? | När Wi-Fi, BLE och IoT är huvudkrav. |
| Vad är PIO? | Programmerbara I/O-state machines för tidskritiska signaler. |
| Måste jag kunna PIO? | Nej, men det är bra att veta att det finns. |
| Är Pico bra för analoga mätningar? | Ja för många experiment, men inte utan kalibrering och brusmedvetenhet. |
| Är Pico bra för nybörjare? | Ja om labbet är väl beskrivet, men klassisk Arduino kan vara enklare i vissa undervisningslägen. |
| Är Pico bra som referenskort i den här boken? | Ja, särskilt för jämförelser av I/O, ADC, PWM, USB och kortval. |

## Sammanfattande valbild

- Pico är en Arduino-kompatibel testplattform när den används med rätt Arduino core.
- RP2040 och RP2350 är mikrokontrollerfamiljer; Pico, Pico W, Pico 2 och Pico 2 W är kort.
- Pico är starkt när projektet behöver många GPIO, bra timing, PWM, USB eller lokal styrning.
- ESP32 är ofta bättre när trådlös kommunikation är huvudfunktionen.
- Klassisk Arduino kan fortfarande vara bättre när 5 V-logik, äldre shields eller maximal enkelhet är viktigast.
- Pico använder 3,3 V-logik, så nivåskiftning och modulernas pull-ups måste kontrolleras.
- PIO är en särskild styrka, men bör introduceras först när vanliga Arduino-mönster inte räcker.
- Dokumentera alltid kortmodell, core, pinout, logiknivå och antaganden om ADC/PWM i projektanteckningarna.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | 3,3 V-logik |
| Typiskt gränssnitt | Digital I/O, I2C, SPI, UART, PWM, USB och PIO |
| Välj när | du vill ha många GPIO, bra timingkontroll och låg kostnad |
| Välj inte när | du behöver inbyggd Wi-Fi/BLE utan extra variant eller modul |
| Vanliga fel | fel kärna, pinout-miss, antaganden om AVR-register, 5 V-signaler |
| Alternativ att överväga | ESP32, Pico W, klassiska Arduino-kort |

Använd referensrutan som en snabb kontroll innan du bygger referensmönstret. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När valet står mellan Pico, Arduino-kort och ESP32, börja med kapitel 2.
- När projektet kräver många I/O-pinnar, jämför med kapitel 30 innan du byter kort.
- När 3,3 V-logik, matning eller sensormoduler påverkar konstruktionen, använd kapitel 4, 33 och 34.

# 3. Utvecklingsmiljö, bibliotek och projektstruktur

## Arbetsmiljö i korthet
Det här kapitlet handlar om arbetsmiljön runt Arduino-projektet: IDE, board packages, bibliotek, seriell felsökning och projektstruktur. Använd det när ett test behöver bli mer reproducerbart än “jag öppnade ett exempel och ändrade några rader”.

Kapitlet hjälper dig särskilt att:

- välja och dokumentera rätt kortstöd
- förstå skillnaden mellan sketch, bibliotek, board package och core
- installera bibliotek utan att blint lita på första sökträffen
- strukturera test så att pinout, konfiguration och logik är lätta att hitta
- använda seriell monitor och seriell plotter som praktiska felsökningsverktyg
- testa en sensor eller modul i liten skala innan den byggs in i ett större projekt

## Arduino IDE som arbetsmiljö

Arduino IDE är fortfarande den enklaste startpunkten för många test. Den ger dig editor, kompilering, uppladdning, board manager, library manager, seriell monitor, seriell plotter och tillgång till många exempel.

För den här bokens nivå är det viktigaste inte att memorera alla menyer. Det viktiga är att förstå vilka delar av miljön som påverkar testet.

### Board Manager

Board Manager används för att installera stöd för olika kortfamiljer. Ett klassiskt Arduino UNO-kort använder ett annat stöd än ett ESP32-kort, ett ESP8266-kort eller ett RP2040-baserat kort. Det installerade stödet innehåller bland annat kortdefinitioner, kompilatorinställningar, upload-verktyg och koppling mellan kortnamn och teknisk målplattform.

Det praktiska problemet är att två kort kan se lika enkla ut i IDE:n men kräva helt olika board packages. Om du väljer fel kort i menyn kan koden kompilera men inte laddas upp, laddas upp men inte starta, eller starta men använda fel pin-mappning.

En bra vana är att dokumentera tre saker i varje test:

- kortets faktiska modell
- valt kortnamn i utvecklingsmiljön
- eventuell teknisk målidentifierare, till exempel FQBN i Arduino CLI

FQBN står för fully qualified board name. Det är ett entydigare sätt att beskriva vilket kortstöd som används. I vardagligt arbete i Arduino IDE behöver du inte alltid skriva FQBN själv, men begreppet är användbart när du vill göra byggsteg reproducerbara.

### Library Manager

Library Manager används för att installera bibliotek. Det är bekvämt, men det betyder inte att alla bibliotek är lika lämpliga. När du söker på en sensor kan du ofta hitta flera bibliotek med liknande namn. Vissa är officiella från komponent- eller korttillverkare. Vissa är mycket använda communitybibliotek. Vissa är gamla, smala eller skrivna för en specifik modulvariant.

När du väljer bibliotek bör du kontrollera:

- om biblioteket stöder den sensor- eller kretsvariant du faktiskt har
- vilka kortfamiljer biblioteket är testat med
- om det använder I2C, SPI, UART eller analog läsning på det sätt du förväntar dig
- om exempelprojekten är tydliga och små
- om biblioteket verkar underhållas eller åtminstone stabilt
- om licensen spelar roll för ditt projekt

För test i den här boken är en enkel tumregel bra: börja med ett bibliotek som har ett litet, tydligt exempel för just den komponent du använder. Lägg inte in biblioteket i ett stort projekt innan du har kört det fristående.

### Examples

Exempelprojekten är ofta den snabbaste vägen till en fungerande första koppling. Samtidigt kan exempel vara skrivna för ett annat kort, en annan pinout eller en annan sensoradress än din modul.

Behandla därför exempel som startpunkter, inte som facit.

När du öppnar ett exempel, leta efter:

- vilka pinnar exemplet antar
- vilken buss exemplet använder
- vilken I2C-adress eller SPI-chip-select som används
- vilken baudrate som används för seriell kommunikation
- om exemplet använder `delay()` på ett sätt som senare kan bli problem
- om exemplet innehåller hårdkodade kortspecifika antaganden

Ett bra arbetssätt är att spara en egen kopia av exemplet med ett tydligt namn, till exempel `bme280_i2c_uno_test`, och sedan ändra stegvis.

### Serial Monitor

Seriell monitor är ofta det viktigaste felsökningsverktyget i början av ett projekt. Den gör det möjligt att se om programmet startar, vilken konfiguration som används, vilka mätvärden som läses och var programmet stannar.

För en erfaren programmerare är seriell monitor i praktiken en enkel loggkanal. Den bör användas med samma disciplin som annan loggning:

- skriv ut en tydlig startbanner
- skriv ut vilket kortläge eller vilken konfiguration som används
- skriv ut sensorstatus innan huvudloopen börjar
- skriv ut felmeddelanden som går att söka på
- undvik att skriva ut så mycket att timing eller läsbarhet förstörs

Ett enkelt exempel:

```cpp
void setup() {
  Serial.begin(115200);
  delay(200);

  Serial.println();
  Serial.println("=== Environment test ===");
  Serial.println("Board: Arduino-compatible");
  Serial.println("Test: BME280 I2C smoke test");
  Serial.println("Baud: 115200");
}
```

Den korta `delay(200)` är inte en generell lösning, men kan göra att seriella utskrifter syns tydligare på vissa kort när USB-seriell anslutning startar. Senare i boken kommer vi att vara försiktiga med `delay()` i faktisk programlogik.

### Serial Plotter

Seriell plotter är användbar när du vill se mätvärden över tid. Den passar särskilt bra för analog läsning, temperatur, ljusnivå, avstånd, ljudnivå eller annan kontinuerlig data.

För att plottern ska vara användbar bör utskrifterna vara enkla och konsekventa. Exempel:

```cpp
int rawValue = analogRead(A0);
Serial.println(rawValue);
```

För flera serier kan du skriva tab-separerade eller tydligt formaterade värden beroende på verktygets förväntningar:

```cpp
Serial.print("raw:");
Serial.print(rawValue);
Serial.print("\tfiltered:");
Serial.println(filteredValue);
```

Seriell plotter ersätter inte ett oscilloskop eller en logikanalysator, men den är ett snabbt sätt att upptäcka brus, trender, mättnad och uppenbart felaktiga mätvärden.

## Arduino CLI och varför det är värt att känna till

Arduino CLI är kommandoradsverktyget bakom mycket av den moderna Arduino-verktygskedjan. Du behöver inte använda det för varje test, men det är värdefullt att känna till eftersom det gör byggprocessen mer reproducerbar.

Med Arduino CLI kan du bland annat:

- installera kortstöd
- installera bibliotek
- kompilera sketches
- ladda upp till kort
- lista anslutna kort
- beskriva miljön i script eller dokumentation

Det här är särskilt användbart när du vill kunna bygga samma projekt senare, eller när du vill använda versionshantering och automatiserade kontroller.

I boken kommer Arduino IDE att vara den huvudsakliga miljön för testen, men vi kommer ibland att tänka på projektstruktur på ett sätt som även fungerar med Arduino CLI eller andra verktyg.

Ett projekt som är begripligt för både människa och verktyg har tydliga namn, separerade konstanter och dokumenterad kortkonfiguration. Det gör det också lättare att senare flytta ett test till PlatformIO eller annan mer avancerad miljö om projektet växer.

## PlatformIO och andra miljöer

PlatformIO är populärt bland många utvecklare eftersom det ger mer traditionell projektstruktur, tydlig beroendehantering, flera miljöer, editorintegration och enklare automatisering. Den här boken utgår inte från PlatformIO som standard, eftersom Arduino IDE och Arduino CLI är närmare Arduino-ekosystemets grundflöde.

Men som erfaren programmerare kan du ha nytta av att känna till skillnaden:

| Egenskap | Arduino IDE | Arduino CLI | PlatformIO |
|---|---|---|---|
| Låg tröskel | Mycket hög | Medel | Medel |
| Grafiskt arbetsflöde | Ja | Nej | Via editor |
| Reproducerbara kommandon | Begränsat | Bra | Bra |
| Flera byggmiljöer | Begränsat | Möjligt | Starkt |
| Bra för snabbtest | Mycket bra | Bra | Bra |
| Bra för större projekt | Okej | Bra med struktur | Mycket bra |

Det viktiga är inte att välja ett verktyg för alltid. Det viktiga är att projektet inte blir beroende av osynliga antaganden. Om du dokumenterar kort, bibliotek, pinnar, spänning och teststeg kan projektet överleva ett byte av editor.

## Sketchens grundstruktur

En Arduino-sketch består typiskt av en eller flera `.ino`-filer. Den mest kända formen innehåller `setup()` och `loop()`:

```cpp
void setup() {
  // Körs en gång vid start eller reset.
}

void loop() {
  // Körs om och om igen.
}
```

Det enkla upplägget är bra för små test, men det kan snabbt bli rörigt om allt hamnar på samma nivå: pin-definitioner, bibliotek, globala variabler, initiering, mätlogik, utskrifter, felhantering och testkod.

Ett bättre mönster är att dela upp sketchen i tydliga sektioner även om allt fortfarande ligger i en enda fil.

Exempel på grundstruktur:

```cpp
#include <Arduino.h>

// ------------------------------------------------------------
// Configuration
// ------------------------------------------------------------

const unsigned long SERIAL_BAUD = 115200;
const int STATUS_LED_PIN = LED_BUILTIN;
const int SENSOR_PIN = A0;
const unsigned long SAMPLE_INTERVAL_MS = 500;

// ------------------------------------------------------------
// State
// ------------------------------------------------------------

unsigned long lastSampleAt = 0;

// ------------------------------------------------------------
// Setup helpers
// ------------------------------------------------------------

void setupSerial() {
  Serial.begin(SERIAL_BAUD);
  delay(200);
  Serial.println();
  Serial.println("=== Analog sensor test ===");
}

void setupPins() {
  pinMode(STATUS_LED_PIN, OUTPUT);
}

// ------------------------------------------------------------
// Application logic
// ------------------------------------------------------------

void sampleSensor() {
  int rawValue = analogRead(SENSOR_PIN);

  Serial.print("raw=");
  Serial.println(rawValue);

  digitalWrite(STATUS_LED_PIN, !digitalRead(STATUS_LED_PIN));
}

// ------------------------------------------------------------
// Arduino entry points
// ------------------------------------------------------------

void setup() {
  setupSerial();
  setupPins();
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleAt >= SAMPLE_INTERVAL_MS) {
    lastSampleAt = now;
    sampleSensor();
  }
}
```

Det här är fortfarande en enkel Arduino-sketch, men den har flera fördelar:

- konfigurationen ligger samlad
- hårdvarupinnar är lätta att hitta
- initiering är separerad från huvudlogik
- `loop()` visar programmets rytm
- testet är lättare att ändra utan att förstöra allt annat

Det är ett mönster vi kommer att återanvända i boken.

## Pinout-kommentarer som dokumentation

Många Arduino-exempel börjar med ett par `const int`-rader. Det räcker för små test, men när du arbetar med olika kortfamiljer bör pinout dokumenteras mer explicit.

Exempel:

```cpp
// Hardware: Arduino UNO or compatible ATmega328P board
// Logic level: 5 V
//
// Connections:
// - A0  -> potentiometer wiper
// - 5V  -> potentiometer outer pin
// - GND -> potentiometer outer pin
// - D13 -> built-in LED

const int SENSOR_PIN = A0;
const int STATUS_LED_PIN = LED_BUILTIN;
```

För ett ESP32-kort kan samma typ av kommentar vara ännu viktigare:

```cpp
// Hardware: ESP32 DevKit-style board
// Logic level: 3.3 V
//
// Connections:
// - GPIO 34 -> analog sensor output
// - 3V3     -> sensor VCC if sensor supports 3.3 V
// - GND     -> sensor GND
//
// Notes:
// - GPIO 34 is input-only on many ESP32 boards.
// - Do not connect 5 V sensor output directly to GPIO 34.

const int SENSOR_PIN = 34;
const int STATUS_LED_PIN = 2;
```

Poängen är inte att alla kommentarer ska vara långa. Poängen är att information som annars bara finns i ditt huvud eller på en lös lapp ska finnas där koden finns.

## Konfiguration först, magi senare

I många exempel på nätet dyker tal upp direkt i koden:

```cpp
digitalWrite(7, HIGH);
delay(1000);
digitalWrite(7, LOW);
```

Det fungerar, men det gör projektet svårare att förstå och flytta. I bokens test bör vi hellre skriva:

```cpp
const int RELAY_PIN = 7;
const unsigned long PULSE_TIME_MS = 1000;

digitalWrite(RELAY_PIN, HIGH);
delay(PULSE_TIME_MS);
digitalWrite(RELAY_PIN, LOW);
```

Det ger tre fördelar:

- namnet förklarar avsikten
- pinnen kan ändras på ett ställe
- värdet kan dokumenteras och motiveras

Det här är extra viktigt i Arduino-världen eftersom samma fysiska pinne kan ha olika namn eller betydelse på olika kort. `D1` på ett NodeMCU-kort är inte samma sak som digital pin 1 på ett UNO-kort. Namngiven konfiguration minskar risken att du råkar flytta ett antagande mellan kort.

## Ett praktiskt projektmönster

För testen i den här boken rekommenderar vi ett enkelt mönster som fungerar även i Arduino IDE:

```text
test-name/
  test-name.ino
  README.md
  notes.md
```

För större test kan du lägga till fler filer:

```text
sensor-station/
  sensor-station.ino
  config.h
  sensor_bme280.h
  sensor_bme280.cpp
  display_oled.h
  display_oled.cpp
  README.md
  notes.md
```

Arduino IDE kan hantera flera filer i samma sketchmapp. För små test är en enda `.ino`-fil ofta enklast. För mer återanvändbar kod kan `.h`- och `.cpp`-filer göra strukturen tydligare.

Ett praktiskt riktmärke:

- en fil när du testar en komponent första gången
- flera funktioner när testet får tydliga steg
- separata filer när samma kod återanvänds i flera test
- ett riktigt bibliotek först när koden har stabiliserats

## README för ett litet testprojekt

Ett litet testprojekt blir lättare att återanvända om det har en kort README. Den behöver inte vara lång, men bör förklara vad projektet testar, vilken hårdvara som används och vilket resultat som förväntas. En bra README kan se ut så här:

```md
# BME280 I2C smoke test

## Vad testet visar

Testa att en BME280-modul fungerar över I2C innan den används i sensorstationen.

## Hårdvara

- Kort: Arduino UNO R4 WiFi
- Sensor: BME280 breakout
- Logiknivå: 3,3 V på sensormodulen
- Buss: I2C

## Koppling

| Kort | Modul | Kommentar |
|---|---|---|
| 3V3 | VCC | Kontrollera modulens märkning |
| GND | GND | Gemensam jord |
| SDA | SDA | I2C data |
| SCL | SCL | I2C clock |

## Bibliotek

- BME280-bibliotek enligt Library Manager
- Wire

## Förväntat resultat

Seriell monitor visar temperatur, luftfuktighet och tryck ungefär en gång per sekund.

## Felsökning

- Kör I2C-scanner om sensorn inte hittas.
- Kontrollera adress 0x76 eller 0x77.
- Kontrollera att modulen klarar vald matningsspänning.
```

Den här typen av README gör att ett test kan fungera som framtida referens. Det är särskilt värdefullt när du senare undrar varför du valde ett visst bibliotek eller vilken I2C-adress modulen hade.

## Minimal testsketch före integration

När du får en ny sensor, display eller IC-krets bör du inte börja med att lägga in den i ett stort projekt. Börja med en minimal testsketch.

En minimal testsketch ska svara på fyra frågor:

1. Startar programmet?
2. Hittas komponenten?
3. Kommer rimliga data eller rimligt beteende?
4. Går felet att beskriva om det inte fungerar?

Exempel på struktur:

```cpp
#include <Arduino.h>
#include <Wire.h>

const unsigned long SERIAL_BAUD = 115200;

void setup() {
  Serial.begin(SERIAL_BAUD);
  delay(200);

  Serial.println();
  Serial.println("=== I2C device smoke test ===");

  Wire.begin();

  Serial.println("I2C initialized.");
  Serial.println("Next step: add sensor-specific begin() call.");
}

void loop() {
  Serial.println("Program is alive.");
  delay(1000);
}
```

Det här exemplet gör nästan ingenting, men det är poängen. Om det inte startar vet du att problemet inte ligger i sensorns avancerade logik. Om det startar kan du lägga till en sak i taget.

## Ett enkelt I2C-scanner-mönster

I2C-scanner är ett klassiskt Arduino-verktyg. Det visar vilka adresser som svarar på I2C-bussen. Det säger inte vilken komponent som sitter där, men det kan snabbt visa om bussen är levande.

Ett förenklat scanner-mönster:

```cpp
#include <Arduino.h>
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  delay(200);

  Serial.println();
  Serial.println("=== I2C scanner ===");

  Wire.begin();
}

void loop() {
  byte deviceCount = 0;

  Serial.println("Scanning...");

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Found I2C device at 0x");

      if (address < 16) {
        Serial.print("0");
      }

      Serial.println(address, HEX);
      deviceCount++;
    }
  }

  Serial.print("Devices found: ");
  Serial.println(deviceCount);
  Serial.println();

  delay(5000);
}
```

När du använder scanner ska du komma ihåg begränsningarna:

- vissa enheter kan påverkas av scanning om de har speciellt protokollbeteende
- scanner visar inte om rätt bibliotek används
- scanner visar inte om sensorn ger rimliga mätvärden
- scanner löser inte spänningsproblem eller dåliga pullups automatiskt

Men den är utmärkt som första kontroll. Samma mönster återkommer senare när du felsöker displayer, miljösensorer, I/O-expansion och andra I2C-moduler. Spara gärna scannern som ett eget litet testprojekt, så att du kan använda den innan ett större projekt börjar felsökas.

## Bibliotek som beroenden

Arduino-bibliotek känns ofta enklare än beroenden i större mjukvaruprojekt, men de är fortfarande beroenden. De kan ha versioner, buggar, API-förändringar och kortspecifika antaganden.

När ett test fungerar bör du dokumentera biblioteket. För en snabb anteckning räcker det ofta med:

```md
Bibliotek:

- Adafruit BME280 Library, installerat via Library Manager
- Adafruit Unified Sensor, installerat som beroende
```

För mer reproducerbara projekt kan du även dokumentera versioner:

```md
Bibliotek:

- Adafruit BME280 Library 2.x
- Adafruit Unified Sensor 1.x
```

Var försiktig med att skriva alltför snäva versioner i boken om det inte behövs. Bibliotek uppdateras. Det viktiga i en handbok är att förklara vilket biblioteksmönster som används och vilka antaganden som gäller.

## När ett bibliotek döljer för mycket

Bibliotek är praktiska, men de kan också dölja detaljer som du behöver förstå. Ett sensorbibliotek kan till exempel:

- välja standardadress automatiskt
- initiera I2C med standardpinnar
- använda blockande väntan
- filtrera eller skala värden utan att du märker det
- förutsätta en viss upplösning, frekvens eller mätcykel
- returnera ett “rimligt” värde även när sensorn inte är korrekt initierad

I praktiska test är detta oftast acceptabelt. Men när något beter sig konstigt är det bra att gå en nivå djupare:

- läs exempelens initieringskod
- kontrollera om `begin()` returnerar felstatus
- skriv ut sensoradress eller identifieringsregister om biblioteket stöder det
- kontrollera bibliotekets dokumentation för standardpinnar och standardinställningar
- jämför med ett enklare exempel eller annan biblioteksversion

Målet är inte att skriva alla drivrutiner själv. Målet är att inte bli hjälplös när biblioteket inte gör exakt det du trodde.

## Kodstil

Det brukar löna sig att använda en konsekvent, enkel kodstil. Den behöver inte vara perfekt för alla organisationer, men den ska vara läsbar, flyttbar och praktisk.

Föreslagen stil:

- engelska namn i kod
- tydliga konstanter i början
- `const` för pinnar och fasta värden
- `unsigned long` för tidsvärden från `millis()`
- inga magiska tal i huvudlogiken
- små funktioner med tydligt ansvar
- seriell loggning med begripliga meddelanden
- undvik `delay()` i huvudlogik om tidsbeteendet spelar roll
- kommentera hårdvaruantaganden mer än självklar C++-syntax

Exempel:

```cpp
const int BUTTON_PIN = 4;
const int STATUS_LED_PIN = LED_BUILTIN;
const unsigned long DEBOUNCE_TIME_MS = 30;

bool lastButtonState = HIGH;
unsigned long lastChangeAt = 0;
```

Det här är tydligare än att sprida `4`, `13` och `30` genom koden.

## Konfigurationsblock för flera kort

Ett enkelt sätt är att samla kortspecifika val i ett konfigurationsblock.

```cpp
// Select one hardware profile.
#define PROFILE_UNO
// #define PROFILE_ESP32_DEVKIT
// #define PROFILE_PICO

#if defined(PROFILE_UNO)
const char* BOARD_PROFILE = "Arduino UNO-compatible";
const int STATUS_LED_PIN = LED_BUILTIN;
const int ANALOG_SENSOR_PIN = A0;
const float LOGIC_LEVEL_V = 5.0;

#elif defined(PROFILE_ESP32_DEVKIT)
const char* BOARD_PROFILE = "ESP32 DevKit-style";
const int STATUS_LED_PIN = 2;
const int ANALOG_SENSOR_PIN = 34;
const float LOGIC_LEVEL_V = 3.3;

#elif defined(PROFILE_PICO)
const char* BOARD_PROFILE = "Raspberry Pi Pico-style";
const int STATUS_LED_PIN = LED_BUILTIN;
const int ANALOG_SENSOR_PIN = A0;
const float LOGIC_LEVEL_V = 3.3;

#else
#error "Select a hardware profile."
#endif
```

Det här är inte alltid den snyggaste lösningen för produktionskod, men det är pedagogiskt. Det gör skillnader mellan kort synliga. Det hjälper också läsaren att förstå att samma test kan kräva olika pinnar och spänningsantaganden.

## Att skilja exempel, test och projekt

I boken använder vi tre nivåer:

| Nivå | Vad nivån används till | Typisk storlek |
|---|---|---|
| Exempel | Visa ett kodmönster eller en princip | Några rader till en liten sketch |
| Test | Kontrollera en komponent eller teknik praktiskt | En komplett sketch med koppling och felsökning |
| Projekt | Kombinera flera delar till ett system | Flera moduler, flera filer eller flera kapitel |

Det är viktigt att inte blanda ihop nivåerna. Ett exempel behöver inte vara komplett. Ett test ska kunna köras och ge ett tydligt resultat. Ett projekt behöver struktur, dokumentation och tydliga val.

När du använder boken som referens kan du ofta hoppa direkt till testet eller referensmönstret i ett kapitel. Läs valguiden och felsökningsdelarna när du behöver förstå varför mönstret är byggt som det är.

## Referensmönster: skapa ett återanvändbart testprojekt

Det här referensmönstret visar en enkel projektstruktur som kan återanvändas när du testar en sensor, modul eller kortprofil innan den byggs in i ett större projekt. Mönstret använder en analog sensorpinne. Du kan koppla en potentiometer, en enkel ljussensor med spänningsdelare eller tillfälligt låta pinnen vara kopplad till en stabil testspänning inom kortets tillåtna område.

### Vad mönstret visar

Mönstret ger ett litet testprojekt som:

- har tydlig pinout-dokumentation
- skriver ut startinformation
- läser ett analogt värde
- filtrerar värdet enkelt
- använder `millis()` i stället för `delay()` för huvudloopen
- kan anpassas mellan olika kortprofiler

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- USB-kabel
- potentiometer eller annan enkel analog signalkälla
- eventuellt kopplingsdäck och kablar
- seriell monitor eller seriell plotter

Använd bara spänningar som är säkra för kortets analoga ingång. Ett 3,3 V-kort ska inte få 5 V på en GPIO eller analog ingång.

### Koppling

För en potentiometer:

| Kort | Potentiometer | Kommentar |
|---|---|---|
| 3V3 eller 5V | Ytterpinne | Välj spänning som är säker för kortet |
| GND | Ytterpinne | Gemensam jord |
| Analog ingång | Mittpinne | Signalen som mäts |

Om du använder ett 3,3 V-kort, använd 3,3 V som potentiometerns matning.

### Kod

```cpp
#include <Arduino.h>

// ------------------------------------------------------------
// Hardware profile
// ------------------------------------------------------------

// Select one profile.
// #define PROFILE_UNO
#define PROFILE_GENERIC_3V3

#if defined(PROFILE_UNO)
const char* BOARD_PROFILE = "UNO-compatible 5 V";
const int STATUS_LED_PIN = LED_BUILTIN;
const int SENSOR_PIN = A0;
const float INPUT_MAX_VOLTAGE = 5.0;

#elif defined(PROFILE_GENERIC_3V3)
const char* BOARD_PROFILE = "Generic 3.3 V Arduino-compatible";
const int STATUS_LED_PIN = LED_BUILTIN;
const int SENSOR_PIN = A0;
const float INPUT_MAX_VOLTAGE = 3.3;

#else
#error "Select a hardware profile."
#endif

// ------------------------------------------------------------
// Test configuration
// ------------------------------------------------------------

const unsigned long SERIAL_BAUD = 115200;
const unsigned long SAMPLE_INTERVAL_MS = 250;
const float FILTER_ALPHA = 0.15;

// ------------------------------------------------------------
// State
// ------------------------------------------------------------

unsigned long lastSampleAt = 0;
float filteredValue = 0.0;
bool hasFilteredValue = false;

// ------------------------------------------------------------
// Setup helpers
// ------------------------------------------------------------

void printStartupInfo() {
  Serial.println();
  Serial.println("=== Reusable analog test ===");
  Serial.print("Board profile: ");
  Serial.println(BOARD_PROFILE);
  Serial.print("Sensor pin: ");
  Serial.println(SENSOR_PIN);
  Serial.print("Expected max input voltage: ");
  Serial.print(INPUT_MAX_VOLTAGE, 1);
  Serial.println(" V");
  Serial.println("Columns: raw filtered");
}

void setupSerial() {
  Serial.begin(SERIAL_BAUD);
  delay(200);
  printStartupInfo();
}

void setupPins() {
  pinMode(STATUS_LED_PIN, OUTPUT);
}

// ------------------------------------------------------------
// Application logic
// ------------------------------------------------------------

void updateSensor() {
  int rawValue = analogRead(SENSOR_PIN);

  if (!hasFilteredValue) {
    filteredValue = rawValue;
    hasFilteredValue = true;
  } else {
    filteredValue = FILTER_ALPHA * rawValue + (1.0 - FILTER_ALPHA) * filteredValue;
  }

  Serial.print(rawValue);
  Serial.print('\t');
  Serial.println(filteredValue, 2);

  digitalWrite(STATUS_LED_PIN, !digitalRead(STATUS_LED_PIN));
}

// ------------------------------------------------------------
// Arduino entry points
// ------------------------------------------------------------

void setup() {
  setupSerial();
  setupPins();
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleAt >= SAMPLE_INTERVAL_MS) {
    lastSampleAt = now;
    updateSensor();
  }
}
```

### Förväntat resultat

Seriell monitor ska visa en startbanner och därefter två kolumner: råvärde och filtrerat värde. Om du öppnar seriell plotter bör du se hur värdet förändras mjukare i den filtrerade serien än i råvärdet.

### Anpassningar

Testa att ändra:

- `SAMPLE_INTERVAL_MS`
- `FILTER_ALPHA`
- kortprofil
- analog källa
- seriell utskriftsformatering

Fundera på vilka ändringar som hör hemma i konfigurationen och vilka som hör hemma i själva programlogiken.

## Vanliga misstag

- **Misstag: Att välja fel kort i Board-menyn.**
  - **Varför det händer:** Många kort har liknande namn och samma USB-port kan användas för flera kort.
  - **Hur man undviker det:** Dokumentera exakt board-val och kontrollera uppladdningsmeddelandet när du byter kort.

- **Misstag: Att installera första bästa bibliotek.**
  - **Varför det händer:** Library Manager kan visa flera bibliotek med liknande namn.
  - **Hur man undviker det:** Börja med bibliotekets enklaste exempel, kontrollera sensorvariant och läs initieringskoden.

- **Misstag: Att ändra ett stort projekt innan komponenten är testad separat.**
  - **Varför det händer:** Det känns snabbare att lägga in allt direkt där det ska användas.
  - **Hur man undviker det:** Skapa en minimal testsketch först. Integrera först när komponenten fungerar ensam.

- **Misstag: Att glömma vilken pinout testet byggdes för.**
  - **Varför det händer:** Kodens pin-nummer känns självklara när du skriver den, men inte tre veckor senare.
  - **Hur man undviker det:** Skriv kopplingstabell eller pinout-kommentar i projektet.

- **Misstag: Att tro att seriell utskrift är gratis.**
  - **Varför det händer:** `Serial.print()` känns enkel och ofarlig.
  - **Hur man undviker det:** Använd seriell loggning med måtta, särskilt i snabb loop, interruptnära kod eller tidskänsliga test.

- **Misstag: Att använda `delay()` i kod som senare ska bli reaktiv.**
  - **Varför det händer:** Många exempel använder `delay()` för enkelhet.
  - **Hur man undviker det:** Använd `millis()` för återkommande uppgifter när projektet ska läsa sensorer, styra utenheter eller reagera på inmatning samtidigt.

## Snabbreferens

| Fråga | Rekommendation |
|---|---|
| Snabbaste start | Arduino IDE med kortets enklaste exempel |
| Mest reproducerbart Arduino-flöde | Arduino CLI eller tydlig dokumentation av board och bibliotek |
| Bästa första test av ny komponent | Minimal sketch som bara testar den komponenten |
| Viktigaste dokumentationen | Kortmodell, board-val, pinout, spänning, bibliotek och förväntat resultat |
| Första felsökningsverktyg | Seriell monitor |
| Första verktyg för mätvärdestrend | Seriell plotter |
| När projektet växer | Dela upp konfiguration, hårdvarulager och applikationslogik |



## Relaterat

- När felet verkar komma från fel kortprofil, USB-chip eller bootloader, jämför med kapitel 10 och 11.
- När biblioteksexemplet fungerar ensamt men inte i projektet, använd felsökningsordningen i kapitel 35.
- När projektet ska delas upp i återanvändbara delar, gå vidare till modulmallen i kapitel 36.

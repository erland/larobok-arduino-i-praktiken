# 36. Från breadboard till återanvändbar modul

## Arbetsmönster i korthet
Breadboard är perfekt när du vill prova en idé snabbt. Du kan flytta en ledning, byta en resistor, testa en sensor och ladda upp ny kod utan att bygga om allt från början. Men samma egenskaper som gör breadboard smidigt gör också att det snabbt blir skört: lösa kablar, otydlig pinout, okänd strömväg, komponenter utan mekaniskt stöd och kod som är hårt kopplad till just dagens experiment.

När ett projekt har fungerat en gång på breadboard uppstår nästa fråga: hur gör du lösningen återanvändbar? Inte nödvändigtvis som en färdig produkt, utan som en modul du kan koppla in igen, förstå om tre månader och använda i ett annat projekt utan att börja om från noll.

Det här kapitlet handlar om övergången från testkoppling till modul. Du kommer att arbeta med både hårdvara och kod: pinout-dokumentation, kopplingsbeskrivning, konfigurationsfiler, enkla wrapper-klasser, testsketcher och versionsanteckningar. Målet är inte att göra professionell elektronikproduktion, utan att bygga ett arbetssätt där dina Arduino-projekt blir robusta byggblock.

## Förutsättningar

Du bör känna igen GPIO, pull-up, nivåskiftning, I2C, SPI, UART, PWM, extern matning, gemensam jord och grundläggande felsökning. Kapitlet bygger också på arbetssättet från kapitel 35: isolera problem, testa en sak i taget och dokumentera det som faktiskt fungerade.

## Från testkoppling till modul

Ett breadboardtest börjar ofta som en fråga: fungerar den här sensorn, kan jag styra den här lasten, går det att visa mätvärdet på en display? När svaret är ja är testkopplingen värdefull, men fortfarande inte särskilt återanvändbar.

En modul börjar med en annan fråga: hur kan jag göra det här till en tydlig del av ett större system?

Skillnaden syns i hur du tänker om gränser.

Ett första test har ofta kod som direkt använder pinnummer, bibliotek och logik på samma ställe:

```cpp
#include <Wire.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme;

void setup() {
  Serial.begin(115200);
  bme.begin(0x76);
}

void loop() {
  float temperature = bme.readTemperature();
  Serial.println(temperature);
  delay(1000);
}
```

Det är bra som första test. Men om sensorn senare ska ingå i ett större projekt behöver du veta mer:

- Vilken I2C-adress används?
- Vilken spänning kräver modulen?
- Vilka bibliotek krävs?
- Vad händer om sensorn saknas?
- Hur ofta ska den läsas?
- Hur rapporteras fel?
- Var i koden byter du sensor, adress eller läsintervall?

En återanvändbar modul gör dessa beslut synliga. Den behöver inte vara komplicerad. Ofta räcker det med tre delar:

- en dokumenterad koppling
- en liten konfiguration
- ett kodlager med tydligt ansvar

## När är det dags att lämna breadboard?

Alla testkopplingar behöver inte bli moduler. Ibland är poängen bara att förstå en komponent. Men det finns tydliga signaler på att du bör ta nästa steg.

Det är dags att gå vidare när:

- samma koppling används i flera projekt
- du börjar bygga vidare ovanpå testkopplingen
- fel uppstår för att kablar lossnar eller hamnar fel
- du behöver transportera projektet
- strömmen är högre än vad breadboard känns lämplig för
- flera personer ska kunna förstå eller återskapa kopplingen
- du vill kunna felsöka modulen separat från resten av systemet
- du börjar kopiera samma kod mellan projekt

Breadboard är ofta sämst just när projektet börjar bli intressant. När du har flera sensorer, en display, en motor, extern matning och nätverk blir varje lös kabel en potentiell felkälla. Då är det bättre att göra moduler av delarna innan hela systemet växer ihop till ett enda stort felsökningsproblem.

## Modulchecklista före nästa steg

Använd den här checklistan när en fungerande koppling ska bli mer återanvändbar.

| Kontrollpunkt | Fråga | Praktiskt beslut |
|---|---|---|
| Syfte | Vad ska modulen göra i ett större projekt? | Skriv en mening som beskriver ansvar och gräns |
| Pinout | Vilka pinnar, adresser och signalnivåer används? | Gör en liten tabell innan kopplingen flyttas |
| Matning | Varifrån kommer strömmen och hur delas jord? | Markera matning, jord och eventuell extern last |
| Gränssnitt | Är det GPIO, analogt, I2C, SPI, UART eller PWM? | Dokumentera buss, adress och bibliotek |
| Test | Hur vet du att modulen fungerar ensam? | Behåll en diagnostisk testsketch |
| Mekanik | Kan kablar, kontakter och modul riktas fel? | Märk kontakter och avlasta lösa ledningar |
| Flyttbarhet | Vad behöver ändras för annat kort? | Lägg pinout och adresser i konfigurationsfil |

## Tre nivåer av återanvändbarhet

Du behöver inte hoppa direkt från breadboard till designat kretskort. Det finns flera mellanlägen.

| Nivå | Hårdvara | Kod | När den passar |
|---|---|---|---|
| Första test | Breadboard och lösa kablar | En enkel sketch | När du vill förstå en komponent snabbt |
| Stabil prototyp | Prototypkort, kontakter, dokumenterad pinout | Konfiguration och testsketch | När kopplingen ska återanvändas |
| Modul | Tydligt gränssnitt, mekanisk stabilitet, egen testmetod | Wrapper-klass eller modulfil | När delen ska ingå i flera projekt |
| Produktnära lösning | Eget kretskort eller färdig kapslad modul | Versionshanterad kod och tester | När lösningen ska användas långsiktigt |

För bokens praktiska mönster räcker nivån “stabil prototyp” ofta långt. Du kan exempelvis löda en BME280-modul, en kontakt och eventuella pull-up-val på ett litet prototypkort. Sedan skriver du en testsketch som verifierar att modulen svarar och ger rimliga mätvärden. När det fungerar kan samma modul användas i flera projekt.

## Modulens gränssnitt

En modul bör kunna beskrivas med fyra frågor:

1. Vad behöver modulen?
2. Vad ger modulen tillbaka?
3. Hur styrs eller konfigureras den?
4. Hur vet jag att den fungerar?

För en sensor kan svaret vara:

- behöver 3,3 V, GND, SDA och SCL
- ger temperatur, luftfuktighet och tryck
- konfigureras med I2C-adress och läsintervall
- testas med en sketch som läser ID och skriver ut mätvärden

För en motorstyrningsmodul kan svaret vara:

- behöver extern motormatning, GND, PWM och riktning
- styr motorhastighet och riktning
- konfigureras med PWM-pin, direction-pin och max duty cycle
- testas med ett säkert rampmönster utan mekanisk last först

När du kan svara på dessa frågor har du börjat tänka modulärt.

## Före och efter: från lös sketch till modul

Modulering blir mest användbar när den gör huvudprogrammet enklare, inte när den bara flyttar kod till fler filer.

En lös sketch kan börja så här:

```cpp
digitalWrite(FAN_PIN, temperature > 28.0 ? HIGH : LOW);
```

Det fungerar i ett litet test, men pinne, gränsvärde, felhantering och styrlogik hamnar direkt i huvudloopen.

I en återanvändbar modul kan samma beslut uttryckas tydligare:

```cpp
fan.update(temperature);
```

Efter-formen gör att huvudloopen beskriver vad systemet gör, medan modulen tar hand om hur fläkten styrs. Pinout, aktiv nivå, säker standardstatus och diagnostik kan då ligga på ett enda ställe.

Det här är inte överarkitektur. Det är en praktisk gränsdragning: huvudprogrammet ska läsa, uppdatera och presentera; modulen ska känna till sina egna pinnar, gränser och felstatus.

## Spara pinout medan kopplingen fungerar

Pinout-dokumentation är en av de enklaste sakerna att göra och en av de mest värdefulla. Den bör skrivas medan kopplingen fortfarande ligger framför dig. En bra pinout är inte bara en lista över pinnar. Den beskriver också riktning, spänning, gränssnitt och särskilda regler.

Exempel för en liten miljösensormodul:

| Modulstift | Kopplas till | Typ | Kommentar |
|---|---|---|---|
| VCC | 3V3 | Matning | Använd inte 5 V om breakout-kortet saknar regulator |
| GND | GND | Matning | Gemensam jord med mikrokontrollern |
| SDA | SDA | I2C data | Kräver fungerande pull-up på bussen |
| SCL | SCL | I2C clock | Kort kabel vid standardhastighet |
| ADDR | GND eller VCC | Konfiguration | Väljer I2C-adress om modulen stöder det |

För en MOSFET-baserad lastmodul kan dokumentationen se ut så här:

| Modulstift | Kopplas till | Typ | Kommentar |
|---|---|---|---|
| VIN+ | Extern lastmatning | Matning | Dimensioneras efter lasten |
| VIN- | Extern GND | Matning | Ska kopplas till Arduino-GND om styrsignalen inte är isolerad |
| LOAD+ | Lastens plus | Last | Vanligt vid low-side switching |
| LOAD- | Lastens minus | Last | Går via MOSFET till GND |
| SIG | Arduino PWM/GPIO | Styrsignal | Kontrollera logiknivå och gate-tröskel |

Det viktiga är att dokumentationen gör felkoppling svårare. Skriv hellre tydligt än elegant.

## Kopplingsbeskrivning som text

Du behöver inte alltid skapa ett grafiskt schema direkt. En bra textbaserad kopplingsbeskrivning räcker ofta i tidiga projekt, särskilt när du vill kunna återskapa kopplingen senare.

Exempel:

```text
BME280-modul till Arduino Nano ESP32:

- VCC till 3V3
- GND till GND
- SDA till SDA
- SCL till SCL
- I2C-adress: 0x76
- Bibliotek: Adafruit BME280 Library
- Testsketch: examples/bme280_diagnostic
```

För en servo:

```text
Standardservo till Arduino UNO:

- Servo röd kabel till extern 5 V
- Servo brun/svart kabel till extern GND
- Arduino GND till extern GND
- Servo orange/gul kabel till D9
- Lägg gärna 470 uF eller större kondensator nära servomatningen
- Testa utan mekanisk last först
```

Den här typen av beskrivning är snabb att skriva och enkel att kontrollera. Den kan senare översättas till schema om projektet växer.

## Skapa en modulfil för hårdvarukonfiguration

Ett vanligt problem i Arduino-projekt är att pinnummer och adresser sprids över hela koden. Det gör projektet svårt att flytta mellan kort eller bygga om.

Ett första steg är att samla hårdvarukonfigurationen på ett ställe:

```cpp
#pragma once

const int STATUS_LED_PIN = 13;
const int BUTTON_PIN = 2;
const int MOTOR_PWM_PIN = 5;
const int MOTOR_DIR_PIN = 4;

const uint8_t ENV_SENSOR_ADDRESS = 0x76;
const unsigned long SENSOR_INTERVAL_MS = 2000;
```

I små Arduino-projekt kan detta ligga i en flik som heter `HardwareConfig.h`. Poängen är inte att skapa en avancerad arkitektur, utan att göra hårdvarubeslut synliga.

När du byter från UNO till ESP32 eller Pico kan du börja med konfigurationsfilen i stället för att leta efter pinnummer i hela projektet.

## Separera vad modulen gör från hur den är kopplad

En återanvändbar kodmodul bör inte behöva veta allt om huvudprogrammet. Den ska ha ett tydligt ansvar.

Tänk på en enkel status-LED. I första testkoden kan den styras direkt:

```cpp
digitalWrite(STATUS_LED_PIN, HIGH);
delay(100);
digitalWrite(STATUS_LED_PIN, LOW);
```

Det fungerar, men när statuslogiken växer blir koden snabbt utspridd. En enkel modul kan kapsla beteendet:

```cpp
class StatusLed {
public:
  explicit StatusLed(int pin) : pin_(pin) {}

  void begin() {
    pinMode(pin_, OUTPUT);
    off();
  }

  void on() {
    digitalWrite(pin_, HIGH);
  }

  void off() {
    digitalWrite(pin_, LOW);
  }

  void set(bool active) {
    digitalWrite(pin_, active ? HIGH : LOW);
  }

private:
  int pin_;
};
```

Huvudprogrammet blir då tydligare:

```cpp
#include "HardwareConfig.h"
#include "StatusLed.h"

StatusLed statusLed(STATUS_LED_PIN);

void setup() {
  statusLed.begin();
}

void loop() {
  statusLed.set(true);
}
```

För en enkel LED kan detta kännas överdrivet, men mönstret blir användbart för sensorer, displayer och motorstyrning. Målet är att huvudprogrammet ska uttrycka vad systemet gör, medan modulerna hanterar detaljerna.

## Wrapper-klass runt en sensor

En wrapper-klass är ett tunt lager runt ett bibliotek eller en komponent. Den gör inte biblioteket onödigt, men den ger ditt projekt ett stabilt gränssnitt. Om du byter sensor senare kan resten av projektet påverkas mindre.

Exempel med en tänkt miljösensor:

```cpp
#pragma once

#include <Adafruit_BME280.h>

struct EnvironmentReading {
  float temperatureC;
  float humidityPercent;
  float pressureHpa;
  bool valid;
};

class EnvironmentSensor {
public:
  explicit EnvironmentSensor(uint8_t address) : address_(address) {}

  bool begin() {
    return bme_.begin(address_);
  }

  EnvironmentReading read() {
    EnvironmentReading reading;
    reading.temperatureC = bme_.readTemperature();
    reading.humidityPercent = bme_.readHumidity();
    reading.pressureHpa = bme_.readPressure() / 100.0F;
    reading.valid = true;
    return reading;
  }

private:
  uint8_t address_;
  Adafruit_BME280 bme_;
};
```

I huvudprogrammet kan du nu arbeta med `EnvironmentReading` i stället för att direkt sprida biblioteksanrop överallt:

```cpp
#include "HardwareConfig.h"
#include "EnvironmentSensor.h"

EnvironmentSensor environment(ENV_SENSOR_ADDRESS);

void setup() {
  Serial.begin(115200);

  if (!environment.begin()) {
    Serial.println("Environment sensor not found");
    while (true) {
      delay(100);
    }
  }
}

void loop() {
  EnvironmentReading reading = environment.read();

  if (reading.valid) {
    Serial.print("Temperature C: ");
    Serial.println(reading.temperatureC);
  }

  delay(SENSOR_INTERVAL_MS);
}
```

I en mer robust version skulle `read()` kunna kontrollera orimliga värden, hantera felstatus och spara senaste giltiga mätning. Men redan den enkla wrappern ger bättre struktur.

## Felhantering som del av modulens gränssnitt

En modul bör inte bara fungera när allt är rätt. Den bör också kunna berätta när något är fel.

För en sensor kan det innebära:

- `begin()` returnerar `false` om sensorn inte hittas
- `read()` returnerar en struktur med `valid`
- senaste felkod kan läsas med en metod
- huvudprogrammet kan välja om felet ska vara kritiskt eller bara loggas

Exempel:

```cpp
enum class ModuleStatus {
  ok,
  notFound,
  readError
};
```

Det kan verka formellt, men det gör större projekt lättare att förstå. I stället för att varje del av koden gör egna antaganden om fel får modulen ett gemensamt språk.

En enkel modul behöver inte ha avancerade exceptions, dynamisk minneshantering eller komplex objektmodell. I Arduino-miljö är tydliga returvärden ofta tillräckligt.

## Testsketch som modulens kontrakt

Varje återanvändbar modul bör ha en testsketch. Testsketchen är inte bara ett exempel. Den är ett kontrakt: om den här sketchen fungerar är modulen troligen korrekt kopplad och grundfunktionen verifierad.

En bra testsketch gör följande:

- startar seriell kommunikation
- skriver ut modulnamn och förväntad koppling
- initierar bibliotek och hårdvara
- rapporterar tydligt om initiering misslyckas
- visar råa eller enkla mätvärden
- undviker onödig logik
- är kort nog att förstå snabbt

Exempelstruktur:

```cpp
#include <Wire.h>
#include "HardwareConfig.h"
#include "EnvironmentSensor.h"

EnvironmentSensor environment(ENV_SENSOR_ADDRESS);

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("Environment module diagnostic");
  Serial.println("Expected wiring: 3V3, GND, SDA, SCL");

  if (!environment.begin()) {
    Serial.println("ERROR: sensor not found");
    while (true) {
      delay(500);
    }
  }

  Serial.println("Sensor found");
}

void loop() {
  EnvironmentReading reading = environment.read();

  Serial.print("Temperature C: ");
  Serial.print(reading.temperatureC);
  Serial.print(" Humidity %: ");
  Serial.print(reading.humidityPercent);
  Serial.print(" Pressure hPa: ");
  Serial.println(reading.pressureHpa);

  delay(2000);
}
```

När ett större projekt slutar fungera kan du gå tillbaka till modulens testsketch. Om testsketchen fungerar ligger felet troligen i integrationen. Om testsketchen inte fungerar ligger felet troligen i koppling, ström, adress, bibliotek eller själva modulen.

## Exempel: enkel modul-README

För återanvändbara moduler kan du skapa en enkel struktur:

```text
examples/
  environment-module/
    README.md
    EnvironmentSensor.h
    EnvironmentSensor.cpp
    HardwareConfig.h
    environment-module-diagnostic.ino
```

I bokens projektstruktur finns `examples/` för scenarier, figurer, data eller icke-kodexempel och `code/` för körbar kod. För en faktisk bokexport kan större kodexempel ligga separat så att kapitlet inte blir för tungt. I kapitlet kan du visa utdrag och hänvisa till den kompletta versionen.

En enkel modul-README kan innehålla:

```md
# Environment module

## Vad modulen gör

Läser temperatur, luftfuktighet och lufttryck via I2C.

## Koppling

| Modul | Arduino |
|---|---|
| VCC | 3V3 |
| GND | GND |
| SDA | SDA |
| SCL | SCL |

## Konfiguration

- I2C-adress: 0x76
- Läsintervall: 2000 ms

## Test

Ladda upp `environment-module-diagnostic.ino` och kontrollera att rimliga mätvärden visas i seriell monitor.
```

Den dokumentationen tar några minuter att skriva men sparar mycket tid senare.

## Mekanisk stabilitet

Många Arduino-problem ser ut som kodfel men är egentligen mekaniska. En Dupont-kabel som nästan sitter fast kan ge intermittenta fel. En sensor som hänger i fyra stela ledningar kan fungera på bordet men sluta fungera när projektet flyttas. En motorledning kan dra loss jord när motorn startar.

När du gör en modul bör du tänka på mekanisk stabilitet:

- använd kontakter som inte lossnar för lätt
- avlasta kablar som rör sig
- undvik att tunga moduler bara hålls av stiftlister
- märk kontakter med riktning och spänning
- använd färgkonventioner konsekvent
- separera kraftledningar från känsliga sensorsignaler där det går
- montera komponenter så att de inte kortsluts mot underlag

För temporära projekt kan skruvplintar, JST-kontakter, Dupont-hus med flera poler eller färdiga Grove/Qwiic/Stemma QT-liknande kontakter vara praktiska. Det viktigaste är att kontakten motsvarar användningen. En lös enpolig Dupont-kabel kan vara okej i ett kort test men dålig i en modul som flyttas ofta.

## Färgkodning och märkning

En enkel färgkonvention minskar risken för fel:

| Färg | Rekommenderad användning |
|---|---|
| Röd | Positiv matning |
| Svart eller brun | GND |
| Gul | Digital styrsignal eller PWM |
| Grön | I2C SDA |
| Blå | I2C SCL |
| Vit | UART TX/RX eller övrig signal |

Detta är ingen universell standard. Det viktiga är att du är konsekvent inom projektet och dokumenterar om något avviker. Förväxling mellan 5 V och 3,3 V är ett av de fel som kan skada komponenter, så märk matningsledningar extra tydligt.

## Från breadboard till lödbart prototypkort

När kopplingen är stabil kan du flytta den till ett lödbart prototypkort. Då bör du inte bara kopiera breadboard-layouten rakt av. Breadboard-layout är optimerad för snabb ändring, inte för tydlighet, strömväg eller mekanisk hållbarhet.

Arbeta i stället stegvis:

1. Rita eller skriv kopplingen som nät: vilka punkter ska sitta ihop?
2. Bestäm var kontakter ska sitta.
3. Placera komponenter så att signalflödet blir begripligt.
4. Håll matning och jord tydliga.
5. Lägg avkopplingskondensatorer nära komponenter som behöver dem.
6. Märk stift och kontakter innan modulen används.
7. Testa varje del innan hela modulen kopplas in i systemet.

För små moduler är målet inte att skapa perfekt layout. Målet är att minska risken för lösa kontakter och felkoppling.

## Modulär kod utan överarkitektur

Erfarna programmerare kan ibland göra Arduino-projekt onödigt abstrakta. Det är frestande att skapa generella interface, inheritance-hierarkier och konfigurationssystem redan från början. I små mikrokontrollerprojekt kan det bli mer problem än hjälp.

En bra tumregel är: kapsla det som ändras eller upprepas, men abstrahera inte det du ännu inte förstår.

Bra kandidater för modulär kod:

- sensorläsning med initiering och felhantering
- displayuppdatering
- motorstyrning med säkerhetsgränser
- LED-statusmönster
- datalogging
- kommunikation mot en extern modul

Sämre kandidater tidigt i projektet:

- generella plugin-system
- dynamisk allokering utan tydlig anledning
- djupa arvsträd
- komplexa konfigurationsformat
- “framtidssäkra” lager som bara används av en enda rad kod

Arduino-kod tjänar ofta på att vara enkel, tydlig och statiskt konfigurerad.

## Ett praktiskt moduleringsmönster

Ett bra mönster för många Arduino-moduler är:

- `begin()` initierar hårdvara
- `update()` kör periodiskt utan att blockera
- `read()` eller `get...()` returnerar senaste data
- `set...()` ändrar styrning
- `status()` rapporterar om modulen fungerar

Exempel för en temperaturstyrd fläktmodul:

```cpp
class FanController {
public:
  FanController(int pwmPin, int enablePin)
      : pwmPin_(pwmPin), enablePin_(enablePin) {}

  void begin() {
    pinMode(pwmPin_, OUTPUT);
    pinMode(enablePin_, OUTPUT);
    stop();
  }

  void setSpeed(uint8_t speed) {
    currentSpeed_ = speed;
    digitalWrite(enablePin_, speed > 0 ? HIGH : LOW);
    analogWrite(pwmPin_, speed);
  }

  void stop() {
    currentSpeed_ = 0;
    analogWrite(pwmPin_, 0);
    digitalWrite(enablePin_, LOW);
  }

  uint8_t currentSpeed() const {
    return currentSpeed_;
  }

private:
  int pwmPin_;
  int enablePin_;
  uint8_t currentSpeed_ = 0;
};
```

Det här är inte ett komplett motorstyrningssystem, men det visar principen: huvudprogrammet behöver inte veta exakt hur fläkten aktiveras. Det använder `setSpeed()` och `stop()`.

## Konfiguration per kortfamilj

När boken arbetar med flera Arduino-kompatibla kort blir hårdvarukonfiguration extra viktig. Samma modul kan behöva olika pinnar på UNO, ESP32 och Pico.

Ett enkelt sätt är att använda separata konfigurationsblock:

```cpp
#pragma once

#if defined(ARDUINO_AVR_UNO)
const int STATUS_LED_PIN = 13;
const int BUTTON_PIN = 2;
const int FAN_PWM_PIN = 5;
#elif defined(ARDUINO_ARCH_ESP32)
const int STATUS_LED_PIN = 2;
const int BUTTON_PIN = 18;
const int FAN_PWM_PIN = 25;
#elif defined(ARDUINO_ARCH_RP2040)
const int STATUS_LED_PIN = 25;
const int BUTTON_PIN = 14;
const int FAN_PWM_PIN = 15;
#else
#error "Unsupported board. Add pin mapping in HardwareConfig.h"
#endif
```

Det här gör två saker. För det första blir det tydligt att projektet inte automatiskt stöder alla kort. För det andra får du ett kontrollerat fel vid kompilering i stället för en märklig koppling på fel pinne.

I större projekt kan du dela upp konfigurationen i flera filer, men börja enkelt.

## Versioner och beroenden

En modul är inte fullständigt dokumenterad om du inte vet vilka bibliotek och antaganden den bygger på. Skriv åtminstone:

- vilket bibliotek som används
- ungefär vilken version som testats
- vilket kort eller vilka kort som testats
- vilken spänning modulen körts på
- kända begränsningar
- datum för senaste fungerande test

Exempel:

```md
## Testad miljö

- Kort: Arduino UNO R4 WiFi och ESP32 DevKit
- Spänning: 3,3 V logik för sensorn
- Bibliotek: Adafruit BME280 Library
- Buss: I2C, adress 0x76
- Senast testad: 2026-06-30
- Begränsning: ej testad med lång I2C-kabel
```

Detta är särskilt viktigt när du använder tredjepartskort, kloner eller bibliotek som utvecklas snabbt. En modul som fungerade med en äldre biblioteksversion kan bete sig annorlunda senare.

## Vanliga misstag

- **Misstag: Att flytta ett fungerande breadboard-projekt utan att först dokumentera kopplingen.**
  - Varför det händer: Kopplingen känns självklar när den ligger framför dig.
  - Hur du undviker det: Skriv pinout, spänning, buss och bibliotek innan du plockar isär något.

- **Misstag: Att sprida pinnummer över hela koden.**
  - Varför det händer: Det går snabbt i ett första test.
  - Hur du undviker det: Samla pinnar, adresser och intervall i en konfigurationsfil.

- **Misstag: Att kalla något modulärt bara för att det ligger i en egen fil.**
  - Varför det händer: Filindelning förväxlas med tydligt ansvar.
  - Hur du undviker det: Se till att modulen har ett tydligt gränssnitt, initiering, felrapportering och testsketch.

- **Misstag: Att göra en för generell lösning för tidigt.**
  - Varför det händer: Programmerare vill ofta bygga återanvändbara ramverk.
  - Hur du undviker det: Kapsla konkreta återkommande behov först. Generalisera när du har två eller tre verkliga användningar.

- **Misstag: Att glömma mekaniken.**
  - Varför det händer: Kod och schema får mer uppmärksamhet än kablar, kontakter och montering.
  - Hur du undviker det: Välj kontakter, avlastning och märkning som passar hur modulen faktiskt ska hanteras.

- **Misstag: Att integrera en modul utan separat test.**
  - Varför det händer: Modulen fungerade en gång i ett tidigare projekt.
  - Hur du undviker det: Kör modulens diagnostiska sketch innan den kopplas in i ett större system.

## Snabbreferens

- Breadboard är bäst för snabba tester, men blir skört när projektet växer.
- En återanvändbar modul behöver tydlig pinout, spänningsnivå, gränssnitt, testmetod och dokumentation.
- Samla pinnummer, adresser och intervall i en konfigurationsfil.
- Wrapper-klasser kan göra sensorer, displayer och aktuatorer lättare att använda i större projekt.
- Varje modul bör ha en diagnostisk testsketch som kan köras separat.
- Mekanisk stabilitet, kontakter och märkning är lika viktiga som kodstruktur när testkopplingar ska återanvändas.
- Gör lösningen så modulär som den behöver vara, men undvik överarkitektur.

## Slutkontroll för modulen
Använd checklistan när kopplingen fungerar och du vill göra den återanvändbar utan att tappa kontroll över pinnar, matning och testbarhet.

- Beskriv modulens praktiska ansvar i en mening.
- Samla pinnummer, I2C-adresser och tidsintervall i en konfigurationsfil.
- Skriv modulens ansvar: vad den initierar, läser, styr eller rapporterar.
- Skapa en diagnostisk testsketch som kan köras utan huvudprojektet.
- Spara matning, jord, logiknivå och eventuella externa laster tillsammans med pinout.
- Kontrollera mekanisk stabilitet, kontaktorientering och märkning.
- Skriv vilka delar som måste ändras vid flytt mellan UNO, ESP32 och Pico.
- Håll modulen enkel tills du har flera verkliga användningar för mer generell kod.

## Relaterat

- När modulen ska ingå i ett större projekt, gå vidare till integrationsordningen i kapitel 37.
- När modulen behöver egen matning, skydd eller batteridrift, använd kapitel 34.
- När dokumentationen ska bli snabb att återanvända, jämför med referensmallarna i kapitel 38.

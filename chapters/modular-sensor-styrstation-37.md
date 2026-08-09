# 37. Sammanhängande projekt: modulär sensor- och styrstation

## Projektöversikt
Hittills har boken arbetat med en teknik i taget: kortval, digitala signaler, analog mätning, bussar, kortfamiljer, sensorer, aktuatorer, drivkretsar, strömförsörjning, felsökning och återanvändbara moduler. Det är ett bra sätt att lära sig, men verkliga Arduino-projekt består sällan av en enda komponent.

Ett typiskt projekt kan behöva läsa en miljösensor, visa status på en display, ge ljus- eller ljudsignal, logga data, styra en fläkt och kanske skicka mätvärden över Wi-Fi. Då räcker det inte att varje del fungerar för sig. Delarna behöver också fungera tillsammans utan att koden blir svår att förstå, strömförsörjningen blir instabil eller felsökningen fastnar i gissningar.

Det här kapitlet knyter ihop bokens tidigare delar i ett sammanhängande projekt: en modulär sensor- och styrstation. Projektet är inte tänkt som ett enda färdigt facit. Det är en projektmall som du kan anpassa. Du kan bygga den som miljöstation, verkstadsmonitor, växthusvakt, batteridriven datalogger, enkel IoT-nod eller interaktiv statuspanel.

Målet är att visa hur du tänker när flera Arduino-kompatibla tekniker ska kombineras på ett robust och inspirerande sätt.

## Förutsättningar

Det här projektkapitlet bygger på flera tidigare delar: kortval, digital I/O, analog mätning, kommunikationsbussar, sensorer, displayer, aktuatorer, strömförsörjning och felsökning. Du behöver inte minnas alla detaljer, men bör kunna slå upp dem när projektet kräver det.

## Projektidén

Vi bygger en sensor- och styrstation som kan mäta miljödata, visa status och reagera på mätvärden. Grundvarianten består av:

- ett Arduino-kompatibelt kort
- en miljösensor via I2C
- en status-LED eller RGB-LED
- en buzzer för enkla varningssignaler
- en liten OLED-display via I2C
- en knapp för att byta visningsläge
- en styrutgång för exempelvis fläkt, relämodul eller MOSFET-styrd last
- valfri datalogging eller nätverksrapportering

Exempel på användning:

- En verkstadsmonitor som varnar vid hög temperatur.
- En växthusstation som visar temperatur, luftfuktighet och styr en fläkt.
- En enkel datalogger som visar mätvärden lokalt och sparar dem.
- En IoT-nod som skickar miljödata via Wi-Fi.
- En undervisningsstation där samma sensorer testas på flera kortfamiljer.

Stationen är medvetet bred. Den är inte optimerad för en enda produkt. Den är ett sammanhållet referensprojekt som gör det lätt att jämföra kort, sensorer, displayer, aktuatorer och kodstruktur.

## Systemöversikt

En bra systemöversikt visar inte bara komponenterna, utan även hur information och energi rör sig genom systemet.

I det här projektet har vi fyra huvudflöden:

- **Mätflöde:** sensorer läses med jämna intervall.
- **Beslutsflöde:** mätvärden tolkas och omvandlas till status.
- **Utflöde:** status visas, signaleras eller används för styrning.
- **Diagnostikflöde:** fel, saknade sensorer och orimliga värden rapporteras.

En enkel textbaserad arkitektur kan se ut så här:

```text
Sensorer -> Mätlager -> Systemstatus -> Utgångar
                     -> Display
                     -> Loggning
                     -> Seriell diagnostik
```

Hårdvaran kan beskrivas på samma sätt:

```text
Kort
+-- I2C-buss
|   +-- Miljösensor
|   `-- OLED-display
+-- Digital ingång
|   `-- Knapp
+-- Digital/PWM-utgång
|   +-- Status-LED eller RGB-LED
|   `-- Buzzer
`-- Styrutgång
    `-- MOSFET, relämodul eller motor-/fläktdriver
```

Poängen är att varje del har en tydlig roll. Sensorn ska inte veta hur displayen fungerar. Displaykoden ska inte bestämma fläktlogik. Knappen ska inte innehålla hela projektets tillstånd. När ansvaret delas upp blir projektet lättare att bygga, testa och ändra.

## Välj ambitionsnivå

Projektet kan byggas på flera nivåer. Välj en nivå som passar dina komponenter och din tid.

| Nivå | Funktioner | Lämpligt kort | När den passar |
|---|---|---|---|
| Grund | Sensor, LED, seriell logg | UNO, Nano, Pico, ESP32 | Första integrationstest |
| Lokal station | Sensor, OLED, knapp, buzzer | UNO R4, Nano, Pico, ESP32 | Fristående bordsprojekt |
| Styrstation | Sensor, display, MOSFET/relä, statuslogik | UNO, Mega, ESP32, Pico | När projektet ska påverka omgivningen |
| IoT-nod | Sensor, display eller LED, Wi-Fi, webbsida/MQTT | ESP8266, ESP32, Nano ESP32 | Uppkopplade experiment |
| Batterinod | Sensor, sleep, låg ström, enkel status | ESP32, SAMD, vissa Pico-varianter | När energiförbrukning styr designen |

Boken använder lokal station med styrutgång som huvudvariant. Det ger tillräckligt många delar för att öva integration, men håller projektet begripligt.

## Kortval

Börja med projektkraven, inte med kortet du råkar ha framme. För den modulära sensor- och styrstationen är de viktigaste kraven:

- Minst en I2C-buss för sensor och OLED.
- Tillräckligt många GPIO för knapp, LED, buzzer och styrutgång.
- Stabil 3,3 V eller 5 V-matning beroende på moduler.
- Tillräckligt minne för displaybibliotek och eventuellt nätverk.
- Rimlig seriell felsökning.
- Möjlighet till extern matning om en last ska styras.

Ett klassiskt UNO- eller Nano-kort fungerar bra om projektet hålls lokalt och minneskraven är små. En OLED och ett större displaybibliotek kan däremot äta mycket minne på äldre AVR-kort. Ett ESP32-baserat kort passar bättre om du vill lägga till Wi-Fi, mer minne eller fler samtidiga funktioner. En Pico eller ett RP2040/RP2350-kort passar bra om du vill ha många pinnar och god prestanda utan inbyggt Wi-Fi på grundkortet. Ett UNO R4-liknande kort kan vara ett bra mellanting om du vill ha Arduino-känsla men modernare hårdvara.

En enkel kortvalsprofil kan se ut så här:

| Krav | Grundvariant | IoT-variant | Batterivariant |
|---|---|---|---|
| Sensorbuss | I2C | I2C | I2C |
| Display | OLED via I2C | OLED eller webbgränssnitt | Ingen eller liten status-LED |
| Nätverk | Nej | Wi-Fi | Eventuellt, men sällan alltid aktivt |
| Aktuator | LED, buzzer, MOSFET | LED, buzzer, MOSFET | Mycket låg ström eller ingen |
| Rekommenderat kort | UNO R4, Nano, Pico, ESP32 | ESP32 eller ESP8266 | ESP32 med deep sleep eller annat lågströmskort |

Välj inte automatiskt det mest avancerade kortet. Ett enklare kort kan ge färre plattformsproblem och tydligare felsökning. Välj däremot inte ett för begränsat kort om projektet redan från början behöver display, nätverk och flera bibliotek.

## Komponentförslag

Här är en möjlig komponentlista för huvudvarianten:

| Funktion | Exempelkomponent | Gränssnitt | Kommentar |
|---|---|---|---|
| Kort | UNO R4, ESP32 DevKit, Nano ESP32, Pico | USB/GPIO | Välj efter variant |
| Miljösensor | BME280, SHT31 eller liknande | I2C | Temperatur, fukt och ibland tryck |
| Display | 0,96 tum OLED SSD1306 | I2C | Vanlig och lätt att integrera |
| Statusljus | RGB-LED eller enkel LED | GPIO/PWM | Visar normal, varning och fel |
| Ljudsignal | Passiv eller aktiv buzzer | GPIO/PWM | Enkel lokal varning |
| Knapp | Momentan tryckknapp | Digital ingång | Byter vy eller kvitterar varning |
| Styrutgång | MOSFET-modul, relämodul eller driver | GPIO/PWM | Styr fläkt, LED-strip eller annan lågspänningslast |
| Matning | USB och separat lastmatning | 5 V/extern | Lasten bör ofta ha separat matning |

Välj gärna komponenter du redan har. Projektet blir mer lärorikt om du dokumenterar skillnaderna.

## Kopplingsprincip

En möjlig koppling för en 3,3 V-baserad ESP32-variant:

| Funktion | Kortpinne | Kommentar |
|---|---|---|
| I2C SDA | GPIO 21 | Vanlig ESP32-standard, kontrollera ditt kort |
| I2C SCL | GPIO 22 | Vanlig ESP32-standard, kontrollera ditt kort |
| Knapp | GPIO 27 | Kopplas mot GND med `INPUT_PULLUP` |
| Status-LED | GPIO 25 | Via seriemotstånd om enkel LED används |
| Buzzer | GPIO 26 | Via modul eller transistor vid högre ström |
| Styrutgång | GPIO 14 | Till MOSFET-/relämodul, inte direkt till stor last |

För UNO-liknande kort kan I2C i stället ligga på A4/A5 eller dedikerade SDA/SCL-pinnar beroende på modell. För Pico och andra kort väljer du de pinnar som stöds av den Arduino-kärna du använder. Dokumentera alltid både kortets fysiska märkning och kodens pinnummer.

Kom ihåg tre regler från tidigare kapitel:

- Sensorer och display på samma I2C-buss behöver kompatibla adresser.
- All styrning mellan kort och moduler behöver gemensam jord, om den inte är galvaniskt isolerad på rätt sätt.
- Laster som motorer, fläktar, solenoider och LED-strippar ska normalt inte matas från mikrokontrollerns GPIO eller svaga 3,3 V-regulator.

## Programarkitektur

Ett större Arduino-program behöver inte bli objektorienterat på avancerad nivå, men det behöver ha struktur. För det här projektet räcker det med fem delar:

- konfiguration
- mätning
- tillståndsbedömning
- utgångar
- diagnostik

I kod kan vi tänka så här:

```cpp
struct SensorData {
  float temperatureC;
  float humidityPercent;
  bool valid;
};

enum class SystemState {
  Starting,
  Normal,
  Warning,
  Alarm,
  SensorError
};
```

`SensorData` beskriver vad vi vet om mätningen. `SystemState` beskriver vad systemet tycker att mätningen betyder.

Den uppdelningen är viktig. Ett temperaturvärde på 31,2 grader är data. Att det är en varning är ett beslut. Att displayen ska visa gul status eller att buzzern ska pipa är presentation och utgång.

När dessa saker blandas ihop blir koden snabbt svår att ändra. Om displaykoden själv jämför temperaturgränser och buzzern gör samma sak på ett annat ställe får du två versioner av sanningen. Lägg därför gränser och statuslogik på ett ställe.

## Konfiguration

Börja med en tydlig konfigurationssektion. Anpassa pinnarna efter ditt kort.

```cpp
#include <Wire.h>

const uint8_t PIN_BUTTON = 27;
const uint8_t PIN_STATUS_LED = 25;
const uint8_t PIN_BUZZER = 26;
const uint8_t PIN_CONTROL_OUT = 14;

const uint32_t SENSOR_INTERVAL_MS = 2000;
const uint32_t DISPLAY_INTERVAL_MS = 500;
const uint32_t HEARTBEAT_INTERVAL_MS = 1000;

const float WARNING_TEMP_C = 28.0;
const float ALARM_TEMP_C = 32.0;
```

För ett UNO-liknande kort byter du pinnarna till exempelvis 2, 5, 6 och 9. Det viktiga är att konfigurationen ligger samlad. Då kan du portera projektet till ett annat kort utan att leta efter hårdkodade pinnummer i hela programmet.

## Grundläggande datastrukturer

Nästa steg är att definiera enkla strukturer för systemets data och status.

```cpp
struct SensorData {
  float temperatureC = 0.0;
  float humidityPercent = 0.0;
  bool valid = false;
};

enum class SystemState {
  Starting,
  Normal,
  Warning,
  Alarm,
  SensorError
};

SensorData currentData;
SystemState currentState = SystemState::Starting;
```

Det här är avsiktligt enkelt. Målet är inte att skapa ett stort ramverk, utan att undvika att alla funktioner skickar runt lösa globala variabler utan tydlig betydelse.

## Icke-blockerande loop

Stationen ska göra flera saker samtidigt ur användarens perspektiv:

- läsa sensor regelbundet
- uppdatera display
- blinka status
- reagera på knapp
- styra utgång
- skriva diagnostik

Det betyder inte att du behöver ett realtidsoperativsystem. Däremot bör du undvika långa `delay()`-pauser i huvudloopen.

En förenklad loop kan se ut så här:

```cpp
uint32_t lastSensorRead = 0;
uint32_t lastDisplayUpdate = 0;
uint32_t lastHeartbeat = 0;

void loop() {
  uint32_t now = millis();

  handleButton(now);

  if (now - lastSensorRead >= SENSOR_INTERVAL_MS) {
    lastSensorRead = now;
    currentData = readSensors();
    currentState = evaluateState(currentData);
    applyControlOutput(currentState);
    printDiagnostics(currentData, currentState);
  }

  if (now - lastDisplayUpdate >= DISPLAY_INTERVAL_MS) {
    lastDisplayUpdate = now;
    updateDisplay(currentData, currentState);
  }

  if (now - lastHeartbeat >= HEARTBEAT_INTERVAL_MS) {
    lastHeartbeat = now;
    updateStatusLed(currentState);
  }

  updateBuzzer(now, currentState);
}
```

Varje funktion har ett tydligt ansvar. Loopen är inte tom, men den är läsbar. Den beskriver projektets rytm.

## Sensorläsning

I ett riktigt projekt använder du ett bibliotek för din valda sensor. Här visar vi formen med pseudonära Arduino-kod. Byt ut innehållet mot ditt faktiska sensorbibliotek.

```cpp
SensorData readSensors() {
  SensorData data;

  float temperature = readTemperatureFromSensor();
  float humidity = readHumidityFromSensor();

  bool temperatureOk = !isnan(temperature);
  bool humidityOk = !isnan(humidity);

  if (temperatureOk && humidityOk) {
    data.temperatureC = temperature;
    data.humidityPercent = humidity;
    data.valid = true;
  }

  return data;
}
```

Poängen är att sensorkoden inte bara returnerar ett tal. Den returnerar också om värdet är giltigt. Det gör resten av systemet mer robust. Displayen kan visa “sensorfel” i stället för ett gammalt värde, och styrlogiken kan välja ett säkert läge.

## Tillståndsbedömning

Nu översätter vi data till systemstatus.

```cpp
SystemState evaluateState(const SensorData& data) {
  if (!data.valid) {
    return SystemState::SensorError;
  }

  if (data.temperatureC >= ALARM_TEMP_C) {
    return SystemState::Alarm;
  }

  if (data.temperatureC >= WARNING_TEMP_C) {
    return SystemState::Warning;
  }

  return SystemState::Normal;
}
```

Det här är projektets centrala beslutslogik. I en växthusvariant kan den också väga in luftfuktighet och ljusnivå. I en verkstadsmonitor kan den titta på temperatur, ljudnivå eller partikelsensor. I en batterinod kan låg batterispänning vara viktigare än temperatur.

Lägg beslutslogiken på ett ställe. Då kan du ändra gränser, lägga till hysteresis eller införa fler lägen utan att skriva om display, buzzer och styrutgång var för sig.

## Styrutgång

En styrutgång kan betyda olika saker:

- slå på en fläkt med MOSFET
- aktivera ett relä
- dimma en LED-strip
- starta en pump
- öppna en ventil via driver

I kapitlets exempel håller vi oss till en enkel digital styrutgång.

```cpp
void applyControlOutput(SystemState state) {
  bool outputOn = false;

  if (state == SystemState::Alarm) {
    outputOn = true;
  }

  digitalWrite(PIN_CONTROL_OUT, outputOn ? HIGH : LOW);
}
```

Det här är medvetet konservativt: styrutgången aktiveras först vid alarm. I en verklig temperaturreglering vill du ofta använda hysteresis så att fläkten inte slår av och på hela tiden kring gränsvärdet.

En enkel hysteresis-variant kan se ut så här:

```cpp
bool fanOn = false;

void updateFanWithHysteresis(float temperatureC, bool sensorValid) {
  if (!sensorValid) {
    fanOn = false;
  } else if (!fanOn && temperatureC >= 32.0) {
    fanOn = true;
  } else if (fanOn && temperatureC <= 29.0) {
    fanOn = false;
  }

  digitalWrite(PIN_CONTROL_OUT, fanOn ? HIGH : LOW);
}
```

Hysteresis är särskilt viktigt när styrningen påverkar det som mäts. En fläkt sänker temperaturen. Om gränsen är exakt samma för på och av kan systemet börja pendla.

## Status-LED

Status-LED är både användargränssnitt och felsökningsverktyg. Den bör fungera även om displayen saknas eller sensorn krånglar.

En enkel variant är:

| Systemstatus | LED-beteende |
|---|---|
| Starting | Snabb blinkning |
| Normal | Långsam blinkning |
| Warning | Dubbelblink |
| Alarm | Fast på eller snabb blinkning |
| SensorError | Tre korta blinkningar |

I kod kan du börja mycket enklare:

```cpp
void updateStatusLed(SystemState state) {
  static bool ledOn = false;
  ledOn = !ledOn;

  if (state == SystemState::Normal) {
    digitalWrite(PIN_STATUS_LED, ledOn ? HIGH : LOW);
  } else if (state == SystemState::Warning) {
    digitalWrite(PIN_STATUS_LED, HIGH);
  } else if (state == SystemState::Alarm || state == SystemState::SensorError) {
    digitalWrite(PIN_STATUS_LED, ledOn ? HIGH : LOW);
  } else {
    digitalWrite(PIN_STATUS_LED, LOW);
  }
}
```

Det här är inte den mest eleganta blinklogiken, men det är lätt att förstå. För ett mer avancerat projekt kan du skapa en liten statusmodul som hanterar olika blinkmönster utan att blockera huvudloopen.

## Buzzer utan att låsa programmet

En buzzer ska inte göra att resten av systemet stannar. Undvik därför långa ljudsekvenser med `delay()`. En enkel start är att bara ge ljud vid alarm.

```cpp
void updateBuzzer(uint32_t now, SystemState state) {
  static uint32_t lastToggle = 0;
  static bool buzzerOn = false;

  if (state != SystemState::Alarm) {
    noTone(PIN_BUZZER);
    buzzerOn = false;
    return;
  }

  if (now - lastToggle >= 250) {
    lastToggle = now;
    buzzerOn = !buzzerOn;

    if (buzzerOn) {
      tone(PIN_BUZZER, 2000);
    } else {
      noTone(PIN_BUZZER);
    }
  }
}
```

På vissa kort kan `tone()` påverka timers eller sakna exakt samma beteende som på klassiska Arduino-kort. Om ljudet är viktigt bör du testa buzzerfunktionen separat på valt kort innan den integreras i stationen.

## Knapp och visningsläge

Knappen kan användas för att byta vy, kvittera larm eller starta diagnostik. Håll första versionen enkel: ett kort tryck byter vy.

```cpp
uint8_t displayMode = 0;

void handleButton(uint32_t now) {
  static bool lastStable = HIGH;
  static bool lastReading = HIGH;
  static uint32_t lastChange = 0;

  bool reading = digitalRead(PIN_BUTTON);

  if (reading != lastReading) {
    lastReading = reading;
    lastChange = now;
  }

  if (now - lastChange > 30 && reading != lastStable) {
    lastStable = reading;

    if (lastStable == LOW) {
      displayMode = (displayMode + 1) % 3;
    }
  }
}
```

Koden använder aktiv LOW-logik med `INPUT_PULLUP`, vilket passar en knapp mellan pinne och GND. Den är enkel men tillräcklig för många experiment.

## Display som presentation, inte beslutslogik

Displayen ska visa systemets tillstånd, inte äga systemets tillstånd. En displayfunktion bör alltså få data och status som indata.

```cpp
void updateDisplay(const SensorData& data, SystemState state) {
  // Anpassa denna funktion till ditt displaybibliotek.
  // Exempel:
  // display.clearDisplay();
  // display.setCursor(0, 0);
  // display.print("Temp: ");
  // display.println(data.temperatureC);
  // display.display();

  (void)data;
  (void)state;
}
```

När du sedan använder ett riktigt OLED-bibliotek kan funktionen visa olika vyer:

- vy 0: temperatur och luftfuktighet
- vy 1: systemstatus och styrutgång
- vy 2: diagnostik, I2C-adress, uptime eller felräknare

En bra display i ett experimentprojekt visar inte bara fina mätvärden. Den hjälper dig också felsöka.

## Seriell diagnostik

Seriell logg är projektets enklaste svarta låda. Skriv inte ut så mycket att loggen blir oläslig, men skriv tillräckligt för att förstå vad systemet gör.

```cpp
const char* stateName(SystemState state) {
  switch (state) {
    case SystemState::Starting: return "Starting";
    case SystemState::Normal: return "Normal";
    case SystemState::Warning: return "Warning";
    case SystemState::Alarm: return "Alarm";
    case SystemState::SensorError: return "SensorError";
    default: return "Unknown";
  }
}

void printDiagnostics(const SensorData& data, SystemState state) {
  Serial.print("state=");
  Serial.print(stateName(state));
  Serial.print(" valid=");
  Serial.print(data.valid ? "yes" : "no");
  Serial.print(" tempC=");
  Serial.print(data.temperatureC);
  Serial.print(" humidity=");
  Serial.println(data.humidityPercent);
}
```

Loggen bör särskilt visa:

- startinformation
- valt kort eller konfiguration om du har flera varianter
- sensorns initieringsresultat
- mätvärden
- systemstatus
- felräknare
- när styrutgången ändras

När projektet växer är seriell diagnostik ofta snabbare än att gissa utifrån LED-beteende.

## Setup

I `setup()` initierar du hårdvara i en ordning som underlättar felsökning.

```cpp
void setup() {
  pinMode(PIN_BUTTON, INPUT_PULLUP);
  pinMode(PIN_STATUS_LED, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);
  pinMode(PIN_CONTROL_OUT, OUTPUT);

  digitalWrite(PIN_STATUS_LED, LOW);
  digitalWrite(PIN_CONTROL_OUT, LOW);
  noTone(PIN_BUZZER);

  Serial.begin(115200);
  delay(200);

  Serial.println();
  Serial.println("Modular sensor and control station starting");

  Wire.begin();

  bool sensorOk = initSensor();
  bool displayOk = initDisplay();

  if (!sensorOk) {
    Serial.println("Sensor init failed");
    currentState = SystemState::SensorError;
  }

  if (!displayOk) {
    Serial.println("Display init failed");
  }

  if (sensorOk) {
    currentState = SystemState::Normal;
  }
}
```

`initSensor()` och `initDisplay()` är platshållare för dina faktiska bibliotek. I ett bra experiment skriver de tydligt i seriell monitor om de lyckas eller misslyckas.

## Initieringsfunktioner

Du kan börja med stubbar om du vill bygga systemet stegvis innan alla komponenter är inkopplade.

```cpp
bool initSensor() {
  // Byt ut mot sensorbibliotekets begin-funktion.
  // Exempel: return bme.begin(0x76);
  return true;
}

bool initDisplay() {
  // Byt ut mot displaybibliotekets begin-funktion.
  return true;
}

float readTemperatureFromSensor() {
  // Byt ut mot verklig sensorläsning.
  return 24.5;
}

float readHumidityFromSensor() {
  // Byt ut mot verklig sensorläsning.
  return 45.0;
}
```

Stubbar kan kännas konstgjorda, men de är mycket användbara. De låter dig testa knapp, LED, buzzer, displayflöde och styrlogik innan sensorn fungerar. Sedan ersätter du stubbarna med verklig sensorläsning.

Det är samma princip som i mjukvaruutveckling: isolera beroenden så att du kan testa systemlogiken.

## Integrationsplan

Bygg inte allt på en gång. Ett större Arduino-projekt bör integreras i små steg.

| Steg | Test | Förväntat resultat |
|---|---|---|
| 1 | Kort och seriell monitor | Startmeddelande visas |
| 2 | LED | LED blinkar enligt status |
| 3 | Knapp | Visningsläge ändras i loggen |
| 4 | Buzzer | Ljud hörs vid simulerat alarm |
| 5 | Styrutgång | Utgång ändras vid alarm |
| 6 | I2C-scanner | Sensor och display hittas |
| 7 | Sensor | Rimliga mätvärden visas i logg |
| 8 | Display | Mätvärden visas lokalt |
| 9 | Full integration | Sensorvärde styr status, display och utgång |
| 10 | Feltest | Systemet visar sensorfel när sensorn kopplas bort |

Den sista raden är viktig. Testa inte bara normalfallet. Koppla bort sensorn, använd fel I2C-adress, stäng av extern lastmatning och se vad systemet gör. Robusthet byggs genom att testa felvägar.

## Så hänger projektet ihop med tidigare mönster

Slutprojektet är inte ett fristående specialfall. Det är en sammansättning av flera mindre mönster som redan har använts tidigare i boken.

| Del i projektet | Bygger på |
|---|---|
| I2C-sensor | I2C-scanner, miljösensorläsning och rimlighetskontroll |
| OLED-display | liten mätpanel med display och knapp |
| Status-LED | statusljus med flera lägen |
| Buzzer | ljudsignaler för systemstatus |
| Styrutgång | MOSFET, relä och riskkontroll för laster |
| Seriell diagnostik | felsökningskapitlets logg- och minimisketchmönster |
| Strömförsörjning | strömbudget, svag matning och längre driftkontroll |

När något krånglar bör du felsöka delen som ett eget mönster först. Integrera den igen först när den fungerar stabilt på egen hand.

## Felsökning i projektet

När flera komponenter ingår kan fel se ut som om de kommer från fel del. En display som flimrar kan bero på I2C-problem, för svag matning, fel adress, för långa kablar eller att koden blockerar uppdateringen. En sensor som visar konstiga värden kan bero på självuppvärmning, dålig jord, fel bibliotek eller att den sitter för nära en värmekälla.

Arbeta systematiskt:

- Testa kortet ensamt med seriell monitor.
- Testa I2C-bussen med scanner.
- Testa sensor och display separat.
- Testa knapp, LED och buzzer utan sensor.
- Testa styrutgång med en liten ofarlig last innan riktig last.
- Mät matningsspänning när lasten slår på.
- Logga systemstatus och mätvärden samtidigt.
- Återgå till senaste fungerande steg när något går fel.

Ett bra större projekt har alltid en väg tillbaka till ett minimalt test.

## Valguide för projektvarianter

Projektet kan anpassas i flera riktningar.

| Projektvariant | Lägg till | Ta bort eller förenkla | Kort som ofta passar |
|---|---|---|---|
| Växthusvakt | Fukt, ljus, fläkt eller pump | Buzzer om ljud inte behövs | ESP32, UNO R4, Mega |
| Verkstadsmonitor | Temperatur, partiklar, ljudnivå | Display om logg räcker | ESP32, Pico, UNO R4 |
| Batterilogger | Batterimätning, sleep, SD/FRAM | Display och buzzer | ESP32, SAMD, lågströmskort |
| Interaktiv panel | RGB/NeoPixel, rotary encoder, display | Nätverk | Pico, ESP32, Teensy |
| IoT-nod | Wi-Fi, MQTT/webb, konfigurationsläge | Relä om bara mätning krävs | ESP8266, ESP32, Nano ESP32 |

Varje variant bör fortfarande följa samma arkitektur: mätning, status, utgångar, diagnostik och dokumentation.

## När du bör välja en annan lösning

En Arduino-kompatibel sensor- och styrstation är ett utmärkt experiment, men inte alltid rätt lösning.

Välj något annat när:

- projektet kräver certifierad elsäkerhet eller hanterar nätspänning utan färdig säker modul
- uppgiften kräver långsiktig industriell drift utan omkonstruktion
- mycket data ska behandlas lokalt med avancerad analys
- realtidskraven är hårda och Arduino-miljön gör timing svår att garantera
- användargränssnittet behöver vara grafiskt avancerat
- batteritiden mäts i år och varje mikroampere är kritisk
- du behöver robust fjärruppdatering och säkerhetsmodell från start

Det betyder inte att Arduino är fel som prototypplattform. Tvärtom kan det vara rätt plats att lära sig systemet. Men när kraven blir professionella måste även arkitektur, kapsling, strömförsörjning, säkerhet och testning bli professionella.

## Spara projektets viktiga beslut

När projektet fungerar är det värt att spara de beslut som gör det möjligt att felsöka, bygga om eller vidareutveckla systemet senare.

Spara framför allt:

- kortmodell och board-val i IDE
- matningsspänning och extern matning
- pinout-tabell
- I2C-adresser
- bibliotek och versioner om det är viktigt
- vilka sensorer och moduler som används
- vilka gränsvärden som styr varning och alarm
- hur fel visas
- hur projektet testades
- kända begränsningar
- idéer för nästa version

En enkel pinout-tabell är ofta mer värd än ett långt stycke text när något ska felsökas senare.

| Funktion | Pinne | Riktning | Aktiv nivå | Kommentar |
|---|---|---|---|---|
| Knapp | GPIO 27 | Ingång | LOW | `INPUT_PULLUP` |
| Status-LED | GPIO 25 | Utgång | HIGH | Seriemotstånd krävs |
| Buzzer | GPIO 26 | Utgång | Varierar | `tone()` eller modul |
| Styrutgång | GPIO 14 | Utgång | HIGH | Till MOSFET-/relämodul |
| I2C SDA | GPIO 21 | Buss | - | Sensor och display |
| I2C SCL | GPIO 22 | Buss | - | Sensor och display |

## Utbyggnadsidéer

När grundstationen fungerar kan du göra projektet mer avancerat.

Möjliga utbyggnader:

- Lägg till ljussensor och skapa dag-/nattlogik.
- Lägg till batterimätning och visa energistatus.
- Lägg till SD-kort eller FRAM för datalogging.
- Lägg till Wi-Fi och enkel webbsida på ESP32.
- Lägg till MQTT och skicka mätvärden till en server.
- Lägg till rotary encoder för menyval.
- Lägg till NeoPixel-ring som visuell statusindikator.
- Lägg till hysteresis och minsta av/på-tid för fläktstyrning.
- Lägg till felräknare för sensoravbrott.
- Gör två varianter av samma projekt på olika kort och jämför.

Ett bra experimentprojekt fortsätter att vara lärorikt även när det fungerar. Varje utbyggnad bör dock ske stegvis. Lägg inte till Wi-Fi, SD-kort, ny display och ny sensor samtidigt. Då vet du inte vad som orsakade nästa fel.

## Vanliga misstag

- **Misstag: Att bygga allt på en gång.**
  - **Varför det händer:** Projektet känns tydligt i huvudet och komponenterna ligger redan på bordet.
  - **Hur man undviker det:** Integrera i små steg och spara testsketcher för varje modul.

- **Misstag: Att låta displaykoden styra systemlogiken.**
  - **Varför det händer:** Displayen är synlig och blir ofta den plats där man först tänker på status.
  - **Hur man undviker det:** Låt systemstatus beräknas separat och låt displayen bara presentera den.

- **Misstag: Att sakna felstatus.**
  - **Varför det händer:** Normalfallet fungerar under första testet.
  - **Hur man undviker det:** Låt sensorläsning returnera både värde och giltighet, och testa vad som händer när sensorn saknas.

- **Misstag: Att mata laster från kortets regulator utan strömbudget.**
  - **Varför det händer:** Modulerna har 5 V- eller 3,3 V-pinnar och det ser praktiskt ut.
  - **Hur man undviker det:** Beräkna och mät ström, använd separat matning för laster och koppla gemensam jord där det behövs.

- **Misstag: Att använda `delay()` för ljud, blink och uppdateringar.**
  - **Varför det händer:** Det fungerar i små exempel.
  - **Hur man undviker det:** Använd `millis()`-baserad tidsstyrning så att flera delar kan arbeta samtidigt.

- **Misstag: Att inte dokumentera vilken pinne som betyder vad.**
  - **Varför det händer:** Kopplingen känns självklar när du bygger den.
  - **Hur man undviker det:** Skriv pinout-tabell innan projektet blir stort.

- **Misstag: Att glömma att samma I2C-buss delas av flera enheter.**
  - **Varför det händer:** Varje modul fungerar separat.
  - **Hur man undviker det:** Kör I2C-scanner, kontrollera adresser och håll kablar korta i första versionen.

## Integrationsordning

### Steg 1: Bygg grundstationen med stubbar

Skapa en första version där sensorvärdena simuleras i kod. Koppla LED, buzzer och knapp. Låt knappen byta visningsläge eller skriva valt läge i seriell monitor.

Det testar systemlogiken innan sensorn integreras.

### Steg 2: Lägg till verklig miljösensor

Ersätt stubbarna med en verklig I2C-sensor. Skriv ut temperatur, luftfuktighet och giltighetsstatus i seriell monitor. Koppla bort sensorn och kontrollera att systemet går till `SensorError`.

### Steg 3: Lägg till display

Visa mätvärde, systemstatus och valt displayläge på en OLED eller annan display. Kontrollera att systemet fortfarande fungerar om displayen saknas men sensorn finns.

### Steg 4: Lägg till styrutgång

Koppla en ofarlig last, till exempel en LED via MOSFET-modul eller en liten fläkt med separat matning. Låt styrutgången aktiveras vid alarm. Mät matningsspänningen när lasten slår på.

När grundsystemet fungerar kan uppkoppling läggas till som en separat version. Behåll samma grundarkitektur: mätning, status, utgångar och diagnostik.

## Kontroll före nästa version

Använd punkterna när grundstationen fungerar och nästa version ska byggas utan att tappa kontrollen över helheten.

- Skilj mellan rått sensorvärde, giltigt mätvärde och systemstatus.
- Kontrollera att kortvalet matchar pinnar, minne, nätverk, logiknivå och strömkrav.
- Låt displayen presentera status, inte äga projektets beslutslogik.
- Mata fläktar, reläer och andra laster från lämplig extern matning med gemensam jord.
- Kör I2C-scanner innan sensor och display integreras i samma program.
- Använd hysteresis och minsta av/på-tid vid styrning av fläkt, relä eller annan last.
- Testa stubbar, statuslogik och utgångar innan verklig sensorläsning läggs till.
- Skriv separat plan för batteridrift om projektet ska lämna USB-matning.
- Visa fel som användaren kan agera på: saknad sensor, fel adress, svag matning eller frånkopplad last.
- Spara pinout, bibliotek, gränsvärden, testordning och kända begränsningar innan nästa version.

## Snabbreferens

- Ett större Arduino-projekt bör delas upp i mätning, status, utgångar, presentation och diagnostik.
- Välj kort utifrån krav: I/O, minne, nätverk, spänningsnivå, ström och bibliotek.
- Bygg inte allt på en gång. Integrera en komponent eller funktion i taget.
- Låt sensorläsning rapportera om värdet är giltigt, inte bara vilket värde som lästes.
- Lägg beslutslogik på ett ställe så att display, buzzer och styrutgång inte får egna motstridiga regler.
- Använd `millis()`-baserad tidsstyrning för blink, ljud, mätning och uppdatering.
- Dokumentera pinout, I2C-adresser, matning, bibliotek, gränsvärden och felbeteende.
- Testa även felvägar: saknad sensor, fel adress, svag matning och frånkopplad last.

## Relaterat

- När projektkraven ändras, gå tillbaka till kortvalet i kapitel 2 innan du bygger vidare.
- När flera sensorer, displayer eller minnesmoduler delar buss, använd kapitel 9, 30 och 32 som kontrollpunkter.
- När stationen får omstarter, brus eller svårförklarliga fel, börja med kapitel 34 och felsök sedan enligt kapitel 35.
- När projektet ska dokumenteras som återanvändbart mönster, använd modulmallen i kapitel 36 och referensmallarna i kapitel 38.

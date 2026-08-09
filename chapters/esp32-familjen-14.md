# 14. ESP32-familjen i Arduino-världen

## Kortprofil i korthet
ESP32 är inte ett enda kort. Det är en hel familj av mikrokontroller, moduler och utvecklingskort som ofta används tillsammans med Arduino-miljön. För många projekt är ESP32 ett naturligt steg efter klassisk Arduino och ESP8266: mer minne, fler funktioner, bättre nätverksmöjligheter, fler gränssnitt och ett mycket stort ekosystem.

Men ESP32 är också en källa till förvirring. Två kort kan båda kallas “ESP32” men ha olika chip, olika antal pinnar, olika USB-lösning, olika trådlös teknik, olika ADC-beteende, olika flashstorlek och olika pinout. En sketch som fungerar på ett ESP32 DevKit-kort fungerar inte automatiskt på ett ESP32-C3-, ESP32-S3- eller ESP32-C6-kort utan kontroll.

Det här kapitlet finns för att ge dig en praktisk karta. Målet är inte att memorera varje ESP32-variant, utan att kunna resonera om familjen:

- När är ESP32 ett bättre val än ESP8266?
- När är ESP32 ett bättre val än ett klassiskt Arduino-kort?
- Vilken ESP32-variant passar bäst för Wi-Fi, BLE, USB, många GPIO, låg strömförbrukning eller moderna IoT-protokoll?
- Vilka pinnar bör du undvika i första versionen av ett experiment?
- Varför kräver analog mätning, batteridrift och nätverkskod mer eftertanke på ESP32 än man först tror?

ESP32-familjen är kraftfull, billig och inspirerande. Den är också mer plattformsberoende än den klassiska Arduino-världen. Det är just därför den förtjänar ett eget kapitel.

## Bedöm kortet med detta i åtanke

ESP32-familjen passar när du behöver mer kraft, fler funktioner eller trådlös kommunikation. Bedöm alltid kortet utifrån variant, pinout, 3,3 V-logik, boot-pinnar, strömbehov, analog noggrannhet och bibliotekens stöd för just den modul du använder.

## Plattformen i praktiken

När någon säger “ESP32” kan det betyda minst tre olika saker.

Det kan betyda **ESP32-chipet**, alltså själva mikrokontrollern från Espressif.

Det kan betyda **en ESP32-modul**, till exempel en metallkapslad modul med chip, flashminne, antenn och några stödkomponenter.

Det kan också betyda **ett ESP32-utvecklingskort**, där modulen sitter på ett större kort med USB, regulator, resetknapp, bootknapp och stift för breadboard.

Det är viktigt att skilja på dessa nivåer. När du programmerar i Arduino IDE väljer du normalt ett board entry som motsvarar utvecklingskortet eller åtminstone chipfamiljen. När du kopplar elektronik måste du däremot förstå utvecklingskortets faktiska pinout och elmatning. När du läser mer avancerad dokumentation kan den ibland handla om chipet snarare än ditt specifika kort.

Ett praktiskt sätt att tänka är:

| Nivå | Exempel | Varför det spelar roll |
|---|---|---|
| Chip | ESP32, ESP32-S3, ESP32-C3 | Avgör CPU, radio, periferienheter och grundläggande begränsningar. |
| Modul | WROOM, WROVER, MINI, NORA-liknande modul | Avgör antenn, flash, PSRAM och fysisk kapsling. |
| Utvecklingskort | ESP32 DevKit, NodeMCU-32S, ESP32-S3 DevKit, Nano ESP32 | Avgör USB, regulator, pinout, knappar och hur du kopplar i praktiken. |

I praktiska Arduino-projekt är utvecklingskortet ofta den viktigaste nivån. Det är där pinout-fällor, regulatorbegränsningar och silkscreen-namn uppstår.

## Vanliga ESP32-varianter i praktiken

ESP32-familjen har vuxit mycket. I hobby- och utbildningsprojekt är det vanligt att stöta på original-ESP32, ESP32-S2, ESP32-S3, ESP32-C3, ESP32-C6 och ibland ESP32-H2 eller nyare varianter.

Du behöver inte kunna alla detaljer från början. Det räcker ofta att känna igen den praktiska profilen.

| Variant | Praktisk profil | Typiska skäl att välja |
|---|---|---|
| ESP32 | Klassisk ESP32 med Wi-Fi och Bluetooth/BLE. Vanlig i många DevKit-kort. | Bra allroundval, många exempel, stor community. |
| ESP32-S2 | Wi-Fi, ofta native USB, men inte klassisk Bluetooth. | USB-projekt, Wi-Fi-projekt, enklare modern plattform. |
| ESP32-S3 | Wi-Fi, BLE, ofta native USB och mer avancerade funktioner. | Modern IoT, USB, mer minne, vissa AI-/signalprojekt. |
| ESP32-C3 | RISC-V-baserad, Wi-Fi och BLE, ofta billig och kompakt. | Små moderna IoT-noder och ersättare för enklare ESP8266-projekt. |
| ESP32-C6 | Wi-Fi 6, BLE och ofta IEEE 802.15.4-stöd beroende på modul och mjukvarustöd. | Mer framtidsinriktade IoT-projekt och experiment med nyare nätverksteknik. |
| ESP32-H2 | BLE och IEEE 802.15.4, men normalt inte Wi-Fi. | Experiment där lågströmsradio eller mesh-protokoll är viktigare än Wi-Fi. |

Det viktigaste är att inte anta att alla ESP32-varianter har samma funktioner. Vissa har Bluetooth Classic, andra bara BLE. Vissa har Wi-Fi men inte Bluetooth. Vissa har native USB. Vissa har färre pinnar. Vissa har andra ADC-, PWM- eller pinout-detaljer.

I ett Arduino-projekt bör du därför dokumentera exakt kort och vald board-profil, inte bara skriva “ESP32”.

## När ESP32 är rätt val

ESP32 är ofta rätt val när projektet behöver en kombination av mikrokontroller och nätverk.

Typiska situationer:

- En sensor ska skicka data via Wi-Fi.
- Ett projekt ska styras via webbsida, HTTP, MQTT eller lokal server.
- Bluetooth Low Energy behövs för konfiguration, närvaro eller mobilinteraktion.
- Flera sensorer, display och styrning ska rymmas i samma kort.
- Projektet behöver mer RAM och flash än klassiska AVR-baserade kort.
- Du vill bygga batteridrivna IoT-noder med deep sleep.
- Du vill ha ett billigt kort som ändå klarar relativt avancerade experiment.

ESP32 är också bra när du vill inspireras. Det är lätt att börja med en temperaturmätning och sedan lägga till webbserver, MQTT, BLE, datalogging, LED-status och sleep-lägen.

Det är just den vägen som gör ESP32 rolig. Samma väg kan också göra projekt röriga. Om du lägger till allt samtidigt blir felsökningen snabbt svår.

## När du bör välja något annat

ESP32 är inte alltid rätt val.

Välj ett klassiskt Arduino-kort, till exempel UNO eller Nano, när:

- du vill ha maximal enkelhet
- 5 V-logik är praktiskt
- projektet inte behöver nätverk
- utbildningsmaterial eller shields är byggda för klassisk Arduino
- du vill minska antalet plattformsspecifika detaljer

Välj ESP8266 när:

- du behöver billig Wi-Fi
- projektet är litet
- du redan har ESP8266-kort
- du inte behöver BLE, mycket I/O eller modernare periferienheter

Välj ett modernare officiellt Arduino-kort när:

- dokumentation och reproducerbarhet är viktigare än lägsta pris
- du vill ha tydligare support i Arduino-ekosystemet
- boken, kursen eller arbetsgruppen ska kunna följa samma hårdvara

Välj Raspberry Pi Pico/RP2040-liknande kort när:

- du behöver många GPIO
- du vill ha bra timingnära I/O utan Wi-Fi
- PIO-liknande funktioner är mer relevanta än trådlös kommunikation

ESP32 är alltså inte “det bästa Arduino-kortet”. Det är en mycket bra plattform när projektets krav matchar dess styrkor.

## Chip, modul och utvecklingskort

Många ESP32-kort har namn som liknar varandra men beter sig olika. Det beror ofta på att utvecklingskortet och modulen blandas ihop i beskrivningen.

Ett utvecklingskort kan till exempel bygga på en ESP32-WROOM-modul. Modulen kan i sin tur innehålla ett ESP32-chip, flashminne och antenn. Utvecklingskortet lägger till USB-serieadapter, regulator, knappar, stift och ibland extra LED eller batteriladdning.

För snabba tester är utvecklingskortet bekvämt. För produktliknande konstruktion behöver du däremot förstå modulen.

Titta efter följande när du identifierar ett ESP32-kort:

- Vilket chip eller vilken modul sitter på kortet?
- Har kortet USB-C, micro-USB eller separat USB-seriechip?
- Vilka pinnar är markerade på silkscreen?
- Vilka pinnar är säkra som vanlig I/O?
- Vilka pinnar påverkar boot?
- Vilken regulator används och hur mycket ström kan den ge?
- Finns det inbyggd LED, knapp, batteriladdning, display eller kamera?
- Har kortet PSRAM?
- Vilken board-profil används i Arduino IDE?

Skriv gärna denna information i en kortprofil innan du bygger ett större experiment.

## 3,3 V-logik är grundregeln

ESP32 är en 3,3 V-plattform. Det betyder att GPIO-pinnar normalt inte ska matas med 5 V-signaler.

Detta är en av de vanligaste skillnaderna mot klassiska Arduino-kort. Många UNO- och Nano-projekt bygger på 5 V-logik. Många ESP32-projekt bygger på 3,3 V-logik. Om du flyttar sensorer, relämoduler eller LED-drivare mellan dessa världar måste du kontrollera nivåerna.

Tre saker är särskilt viktiga:

- En ESP32-pinne ska normalt inte få 5 V på ingång.
- En 3,3 V HIGH-signal från ESP32 räcker inte alltid för att säkert styra 5 V-logikmoduler.
- Vissa moduler har regulator och nivåskiftning, andra har det inte.

I praktiken betyder det att samma modul kan vara säker i ett UNO-projekt men olämplig direktkopplad i ett ESP32-projekt.

En bra vana är att skriva på varje testkort:

```cpp
// Board: ESP32 DevKit, 3.3 V logic
// Sensor power: 3.3 V
// I2C pullups: to 3.3 V
```

Det ser enkelt ut, men det hindrar många fel.

## Pinout på ESP32

ESP32-kort har ofta många pinnar, men alla är inte lika användbara. Vissa påverkar uppstarten. Vissa används till flashminne. Vissa saknas på vissa kort. Vissa är bara ingångar. Vissa har specialfunktioner. Vissa har inbyggda pullups eller pulldowns som påverkar beteendet.

På klassiska ESP32-kort är det vanligt att se GPIO-nummer som 0, 2, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 32, 33, 34, 35, 36 och 39. Men den listan är inte en garanti. Ditt kort kan exponera andra pinnar, och en ESP32-S3 eller ESP32-C3 har annan pinout.

En försiktig strategi för första versionen av ett experiment är:

- Använd pinnar som kortets dokumentation uttryckligen rekommenderar för generell I/O.
- Undvik boot-relaterade pinnar tills du vet hur de fungerar.
- Undvik pinnar kopplade till flash eller inbyggda funktioner.
- Kontrollera om en pinne är input-only.
- Dokumentera både GPIO-nummer och fysisk märkning på kortet.

Exempel på dokumentation i kod:

```cpp
const int statusLedPin = 2;      // GPIO2, built-in LED on this board variant
const int buttonPin = 27;        // GPIO27, external button to GND
const int sensorSdaPin = 21;     // GPIO21, I2C SDA on this board
const int sensorSclPin = 22;     // GPIO22, I2C SCL on this board
```

Kommentarerna är inte överflödiga. De gör kopplingen och kortprofilen lättare att återskapa.

## Boot-relaterade pinnar

ESP32 har pinnar som kan påverka bootläge, flashspänning eller uppstartsbeteende. Exakta detaljer varierar mellan varianter, men principen är densamma: vissa GPIO läses vid reset för att avgöra hur chipet ska starta.

Det kan skapa märkliga fel. Projektet fungerar på skrivbordet, men när du ansluter en sensor, knapp eller modul på “fel” pinne startar kortet inte längre. Ibland hamnar kortet i bootloader-läge. Ibland ser du bara konstig seriell output. Ibland fungerar det när USB är inkopplat men inte när extern matning används.

Det säkraste är att behandla boot-relaterade pinnar som en riskkategori.

Skriv i kortprofilen:

| Pinne | Användning | Risk |
|---|---|---|
| GPIO0 | Boot/flash på många kort | Undvik som första val för extern knapp eller modul. |
| GPIO2 | Inbyggd LED eller boot-relaterad på vissa kort | Kontrollera kortdokumentation. |
| GPIO12 | Kan påverka flashspänningsval på vissa klassiska ESP32-kort | Undvik utan dokumentation. |
| GPIO15 | Boot-relaterad på vissa varianter | Kontrollera dokumentation. |

Detta är inte en komplett tabell för alla ESP32-varianter. Det är en påminnelse om arbetssättet: behandla pinout som kortspecifik information.

## ADC på ESP32

ESP32 har analog-digital omvandling, men den ska inte behandlas som identisk med `analogRead()` på klassisk Arduino.

I praktiska projekt bör du känna till fyra saker:

- ADC-värden kan vara mindre linjära än du väntar dig.
- Mätområde och upplösning beror på konfiguration och plattform.
- Vissa ADC-resurser kan påverkas av Wi-Fi på vissa ESP32-varianter.
- Brus, matning och layout påverkar mätningen tydligt.

Det betyder inte att ADC på ESP32 är oanvändbar. Den är utmärkt för potentiometrar, ungefärliga batterimätningar, enkla analoga sensorer och relativa mätningar. Men om du behöver hög noggrannhet kan en extern ADC över I2C eller SPI vara bättre.

Ett bra ESP32-mönster är att normalisera mätvärdet i egen funktion:

```cpp
float readBatteryVoltage() {
  const int raw = analogRead(batterySensePin);
  const float adcMax = 4095.0;
  const float referenceVoltage = 3.3;
  const float dividerRatio = 2.0;

  return (raw / adcMax) * referenceVoltage * dividerRatio;
}
```

I ett riktigt projekt ska värdena kalibreras. Funktionen visar ändå principen: göm inte antaganden om ADC-upplösning, referens och spänningsdelare i resten av programmet.

## PWM och LEDC

På ESP32 används ofta LEDC-periferienheten för PWM i Arduino-miljön. I enklare kod kan du ibland använda Arduino-liknande funktioner, men på ESP32 blir det snabbt viktigt att förstå att PWM är mer konfigurerbar än på klassisk Arduino.

Du behöver tänka på:

- frekvens
- upplösning
- kanal eller pinne beroende på core-version och API
- konflikt med andra funktioner
- skillnader mellan ESP32-varianter

För LED-dimning är detta oftast enkelt. För motorstyrning, servosignaler eller ljudliknande signaler bör du kontrollera bibliotek och exempel för just din core-version.

Ett generellt råd är att börja med ett minimalt PWM-test innan du kopplar in motorer eller externa drivare.

## Wi-Fi i Arduino-miljö

Wi-Fi är ett av de vanligaste skälen att välja ESP32. Men nätverk förändrar hur du bör skriva kod.

Ett blink-exempel kan anta att allt fungerar direkt. Ett Wi-Fi-projekt bör anta att nätverket ibland saknas.

Använd därför timeout, statusindikator och lokalt reservläge. Undvik kod som fastnar för alltid i väntan på Wi-Fi.

Ett enkelt mönster:

```cpp
#include <WiFi.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

bool connectToWiFi(unsigned long timeoutMs) {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  const unsigned long start = millis();

  while (WiFi.status() != WL_CONNECTED && millis() - start < timeoutMs) {
    delay(100);
  }

  return WiFi.status() == WL_CONNECTED;
}

void setup() {
  Serial.begin(115200);
  delay(500);

  if (connectToWiFi(10000)) {
    Serial.print("Connected. IP address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("Wi-Fi unavailable. Continuing in local mode.");
  }
}

void loop() {
  // Läs sensorer och låt projektet fungera även utan nätverk.
}
```

Koden använder `delay()` i anslutningsloopen eftersom setup-fasen är avgränsad. I ett mer avancerat projekt kan även Wi-Fi-anslutningen göras helt icke-blockerande.

## BLE och Bluetooth

ESP32-familjen är också vanlig för Bluetooth Low Energy. Här måste du vara extra noga med variant. Alla ESP32-liknande chip har inte samma Bluetooth-stöd. Klassisk ESP32 har både Bluetooth Classic och BLE, medan flera nyare varianter fokuserar på BLE och andra radiotekniker.

BLE passar bra när:

- en mobiltelefon ska konfigurera en nod
- små mängder data ska skickas lokalt
- enheten ska annonsera närvaro eller status
- Wi-Fi är onödigt eller för energikrävande

Wi-Fi passar bättre när:

- enheten ska prata med webbtjänster
- data ska skickas till MQTT-broker eller HTTP-server
- högre datamängder eller befintligt lokalt nätverk behövs

För den här boken räcker det att du kan göra valet. Djup BLE-programmering kan bli en egen bok, men grundprincipen är användbar: välj inte Wi-Fi av gammal vana om projektet egentligen bara behöver lokal konfiguration eller korta meddelanden.

## Deep sleep och batteridrift

ESP32 är populär i batteridrivna projekt, men utvecklingskort kan lura dig. Chipet kan ha mycket låga strömlägen, men hela utvecklingskortet kan fortfarande dra mer ström än väntat på grund av regulator, USB-seriechip, power-LED eller andra stödkomponenter.

Det betyder att “ESP32 stöder deep sleep” inte automatiskt betyder “mitt ESP32 DevKit-kort är perfekt för batteridrift”.

Vid batteriprojekt bör du kontrollera:

- chipets sleep-läge
- utvecklingskortets verkliga viloström
- regulatorns egenförbrukning
- om power-LED kan kopplas bort
- hur sensorer och externa moduler stängs av
- hur ofta enheten vaknar
- hur länge Wi-Fi är aktivt
- om data kan buffras och skickas mer sällan

Ett enkelt batterimönster är:

1. Vakna.
2. Slå på sensor.
3. Vänta kort på stabilisering.
4. Läs värde.
5. Anslut till nätverk om det behövs.
6. Skicka eller lagra data.
7. Stäng av kringkretsar.
8. Gå tillbaka till sleep.

Detta arbetssätt återkommer senare i kapitlen om strömmätning och strömförsörjning.

## I2C, SPI och UART på ESP32

ESP32 är flexibel med många periferienheter, men flexibilitet kan också skapa otydlighet.

På klassisk Arduino finns ofta en förväntad plats för I2C. På ESP32 kan I2C ofta mappas till olika pinnar, men exempel och bibliotek antar ibland vanliga standardpinnar.

Ett robust mönster är att initiera bussen tydligt:

```cpp
#include <Wire.h>

const int i2cSdaPin = 21;
const int i2cSclPin = 22;

void setup() {
  Serial.begin(115200);
  Wire.begin(i2cSdaPin, i2cSclPin);

  Serial.println("I2C bus started.");
}

void loop() {
}
```

Det gör experimentet tydligare när du byter kort.

För SPI gäller samma princip: dokumentera MOSI, MISO, SCK och CS. För UART: dokumentera RX, TX och spänningsnivå. Gissa inte utifrån ett annat korts pinout.

## ESP32 och Arduino-kodstil

ESP32 kan köras i Arduino-miljö, men det finns ofta fler lager under ytan. Arduino-ESP32 bygger ovanpå Espressifs ekosystem och använder underliggande funktioner som inte alltid beter sig exakt som på AVR-baserad Arduino.

Det betyder att god kodstil blir viktigare:

- Samla pin-konfiguration i början av filen.
- Skriv kortprofil i kommentarer.
- Använd namngivna konstanter.
- Separera sensorläsning, nätverk och presentation.
- Lägg timeout på nätverksoperationer.
- Logga tydligt till seriell monitor.
- Testa varje buss och sensor separat.
- Dokumentera core-version när något är plattformsberoende.

Ett enkelt skelett:

```cpp
#include <WiFi.h>
#include <Wire.h>

const int i2cSdaPin = 21;
const int i2cSclPin = 22;
const int statusLedPin = 2;

const unsigned long sampleIntervalMs = 2000;
unsigned long lastSampleMs = 0;

void setupBoard() {
  pinMode(statusLedPin, OUTPUT);
  Wire.begin(i2cSdaPin, i2cSclPin);
}

void readSensors() {
  Serial.println("Read sensors here.");
}

void updateStatusLed() {
  digitalWrite(statusLedPin, !digitalRead(statusLedPin));
}

void setup() {
  Serial.begin(115200);
  delay(500);

  setupBoard();

  Serial.println("ESP32 experiment started.");
}

void loop() {
  const unsigned long now = millis();

  if (now - lastSampleMs >= sampleIntervalMs) {
    lastSampleMs = now;
    readSensors();
    updateStatusLed();
  }
}
```

Poängen är inte att detta är ett komplett projekt. Poängen är strukturen: kortspecifik setup, återkommande loop utan blockering och tydliga funktioner som kan bytas ut.

## Valguide

Använd ESP32 när du behöver nätverk, BLE, mer resurser eller modernare IoT-funktioner.

Använd inte ESP32 bara för att det är billigt och kraftfullt. Fråga vad projektet faktiskt kräver.

| Projektkrav | ESP32 passar? | Kommentar |
|---|---|---|
| Enkel knapp och LED | Ofta överdrivet | UNO/Nano räcker och är enklare. |
| Wi-Fi-baserad sensor | Ja | Ett av ESP32:s starkaste användningsområden. |
| Batteridriven sensor | Ja, men mät ström | Utvecklingskortets viloström kan dominera. |
| Många 5 V-moduler | Med försiktighet | Nivåskiftning kan behövas. |
| BLE-konfiguration | Ja, på rätt variant | Kontrollera stöd för vald ESP32-variant. |
| Hög noggrannhet i analog mätning | Inte utan kontroll | Extern ADC kan vara bättre. |
| Många enkla GPIO | Ofta ja | Kontrollera vilka pinnar som faktiskt är användbara. |
| Undervisning med nybörjare | Beror på | Kraftfullt men mer plattformsdetaljer än klassisk Arduino. |

## Referensmönster: ESP32 som Wi-Fi-baserad sensorindikator

Det här referensmönstret visar en enkel ESP32-nod som läser ett simulerat sensorvärde, försöker ansluta till Wi-Fi och fortsätter fungera lokalt även om nätverket saknas. Du kan senare byta ut det simulerade värdet mot en riktig sensor.

### Vad mönstret verifierar

Mönstret verifierar:

- att kortmodell och board-val är kända
- att seriell monitor fungerar
- att Wi-Fi-anslutning har timeout
- att programmet har ett lokalt reservläge
- att `millis()` används för återkommande mätning
- att grunden finns för senare sensor- och IoT-projekt

### Det här används i exemplet

- Ett ESP32-baserat utvecklingskort.
- USB-kabel för data, inte bara laddning.
- Dator med Arduino IDE eller motsvarande miljö.
- Valfri LED om kortets inbyggda LED inte fungerar tydligt.
- Eventuellt en potentiometer eller enkel sensor för senare variation.

### Kortkontroll före koppling

Kontrollera kortmodell, board-val, logiknivå, inbyggd LED, I2C-pinnar och boot-relaterade pinnar innan du kopplar in externa moduler. Om någon av uppgifterna är oklar bör första testet vara seriell monitor och en säker LED-pinne, inte ett större sensorprojekt.

### Kod

Byt ut Wi-Fi-namn och lösenord innan du laddar upp koden. Dela inte riktiga lösenord i kod som publiceras.

```cpp
#include <WiFi.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

const int statusLedPin = 2;

const unsigned long wifiTimeoutMs = 10000;
const unsigned long sampleIntervalMs = 2000;

bool wifiAvailable = false;
unsigned long lastSampleMs = 0;
int simulatedSensorValue = 0;

bool connectToWiFi(unsigned long timeoutMs) {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  const unsigned long start = millis();

  while (WiFi.status() != WL_CONNECTED && millis() - start < timeoutMs) {
    delay(100);
  }

  return WiFi.status() == WL_CONNECTED;
}

int readSimulatedSensor() {
  simulatedSensorValue += 137;

  if (simulatedSensorValue > 1000) {
    simulatedSensorValue = 0;
  }

  return simulatedSensorValue;
}

void showStatus(bool online) {
  if (online) {
    digitalWrite(statusLedPin, HIGH);
  } else {
    digitalWrite(statusLedPin, !digitalRead(statusLedPin));
  }
}

void setup() {
  Serial.begin(115200);
  delay(500);

  pinMode(statusLedPin, OUTPUT);

  Serial.println();
  Serial.println("ESP32 sensor indicator starting.");

  wifiAvailable = connectToWiFi(wifiTimeoutMs);

  if (wifiAvailable) {
    Serial.print("Wi-Fi connected. IP address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("Wi-Fi unavailable. Continuing in local mode.");
  }
}

void loop() {
  const unsigned long now = millis();

  if (now - lastSampleMs >= sampleIntervalMs) {
    lastSampleMs = now;

    const int value = readSimulatedSensor();

    Serial.print("Sensor value: ");
    Serial.print(value);

    if (wifiAvailable && WiFi.status() == WL_CONNECTED) {
      Serial.println(" | network: online");
    } else {
      Serial.println(" | network: local mode");
      wifiAvailable = false;
    }

    showStatus(wifiAvailable);
  }
}
```

### Förväntat resultat

I seriell monitor ska du se att kortet startar, försöker ansluta till Wi-Fi och sedan skriver ut mätvärden varannan sekund. Om Wi-Fi fungerar visas IP-adressen. Om Wi-Fi saknas fortsätter programmet ändå i lokalt läge.

Det är detta som är mönstrets viktigaste poäng: nätverket är en funktion, inte en förutsättning för att hela programmet ska leva.

### Anpassningar

När grundmönstret fungerar kan du bygga vidare:

- Byt simulerat värde mot en potentiometer via ADC.
- Byt simulerat värde mot en I2C-sensor.
- Låt status-LED blinka snabbt vid Wi-Fi-fel och långsamt vid normal drift.
- Lägg till en enkel webbsida som visar senaste värdet.
- Lägg till MQTT senare när nätverksgrunden är stabil.
- Mät strömförbrukning med och utan Wi-Fi.

Gör bara en anpassning i taget.

## ESP32-specifik variant: deep sleep för batterinod

ESP32 passar bra när en nod ska vakna, göra ett kort arbete och sedan sova igen. Det är en annan programstruktur än ett alltid-på-projekt: varje uppvaknande bör kunna köras färdigt utan att förutsätta att tidigare RAM-tillstånd finns kvar.

Det här mönstret är avsiktligt kort. Exakt strömförbrukning, väckningspinne och beteende beror på utvecklingskort, regulator, USB-seriechip och anslutna moduler.

### Vad mönstret visar

Mönstret visar att:

- batteridrift handlar om både kod och hårdvara
- Wi-Fi är en energikostnad, inte bara en funktion
- uppvakning, mätning och sömn bör vara tydligt separerade
- seriell utskrift är användbar vid test men kan döljas i färdig nod
- deep sleep bör testas med den faktiska kortmodellen

### Kort kodmönster med timeruppvakning

```cpp
#include <WiFi.h>

const uint64_t SLEEP_TIME_US = 5ULL * 60ULL * 1000000ULL; // 5 minuter
const int STATUS_LED_PIN = 2;

int readSensorValue() {
  // Byt senare mot riktig sensorläsning.
  return analogRead(34);
}

void indicateBriefly() {
  pinMode(STATUS_LED_PIN, OUTPUT);
  digitalWrite(STATUS_LED_PIN, HIGH);
  delay(100);
  digitalWrite(STATUS_LED_PIN, LOW);
}

void setup() {
  Serial.begin(115200);
  delay(300);

  WiFi.mode(WIFI_OFF);

  const int value = readSensorValue();

  Serial.print("Wake, sensor=");
  Serial.println(value);

  indicateBriefly();

  esp_sleep_enable_timer_wakeup(SLEEP_TIME_US);
  Serial.println("Entering deep sleep.");
  Serial.flush();

  esp_deep_sleep_start();
}

void loop() {
}
```

### Kontrollera detta

Kontrollera detta innan mönstret används i ett batteriprojekt:

- om vald analog pinne fungerar på din ESP32-variant
- om inbyggd LED sitter på rätt pinne eller saknas
- om utvecklingskortets regulator och USB-seriechip drar ström även i deep sleep
- om externa sensorer behöver stängas av med lastbrytare eller enable-pinne
- om Wi-Fi verkligen behövs vid varje uppvaknande
- om uppvakningsintervallet är rimligt för batteriet

Timeruppvakning är ofta enklast att börja med. Extern väckning via pinne är mycket användbar, men den är mer beroende av exakt ESP32-variant och vilka pinnar som är RTC-kompatibla.

## Felsökning

### Kortet hittas inte av datorn

Kontrollera USB-kabeln först. Många kablar är endast laddkablar. Kontrollera sedan drivrutin om kortet använder CH340 eller CP210x. Om kortet har native USB kan reset- och bootbeteendet skilja sig från äldre ESP32 DevKit-kort.

### Uppladdning misslyckas

Håll BOOT-knappen intryckt vid uppladdning om kortet kräver det. Kontrollera också rätt board-val och port. Om något är kopplat till boot-relaterade pinnar, koppla bort det och prova igen.

### Kortet startar inte efter att en modul kopplats in

Misstänk boot-relaterade pinnar, fel matning eller 5 V-signal på 3,3 V-ingång. Koppla bort modulen och återgå till minimal sketch.

### Wi-Fi ansluter inte

Kontrollera SSID, lösenord, 2,4 GHz-nät och signalstyrka. Många ESP32-varianter använder 2,4 GHz Wi-Fi, inte 5 GHz. Lägg alltid timeout i testprogram så att projektet inte fastnar.

### Analogvärden är instabila

Mät matningen. Kontrollera spänningsdelare, jord, brus och kabellängd. Medelvärdesbilda flera mätningar. För noggranna mätningar: överväg extern ADC.

### LED-pinnen verkar fel

`GPIO2` är vanligt i exempel, men inte universellt. Vissa kort har ingen LED på den pinnen, eller LED:n är inverterad. Kontrollera kortets dokumentation och ändra `statusLedPin`.

## Vanliga misstag

- **Misstag:** Att skriva “ESP32” i dokumentationen utan exakt kortmodell.
  - **Varför det händer:** Många kort marknadsförs generiskt som ESP32.
  - **Hur man undviker det:** Dokumentera chip, modul, utvecklingskort och board-val.

- **Misstag:** Att behandla ESP32 som en 5 V-Arduino.
  - **Varför det händer:** Arduino-API:t ser bekant ut.
  - **Hur man undviker det:** Utgå från 3,3 V-logik och nivåskifta vid behov.

- **Misstag:** Att använda första bästa GPIO utan att kontrollera boot-funktion.
  - **Varför det händer:** Det finns många pinnar och de ser likvärdiga ut.
  - **Hur man undviker det:** Börja med dokumenterat säkra pinnar och uppdatera kortprofilen.

- **Misstag:** Att låta Wi-Fi-kod blockera hela programmet.
  - **Varför det händer:** Många exempel antar att nätverket alltid finns.
  - **Hur man undviker det:** Använd timeout och lokalt reservläge.

- **Misstag:** Att lita blint på ADC-värden.
  - **Varför det händer:** `analogRead()` finns och ger ett tal.
  - **Hur man undviker det:** Kalibrera, filtrera och dokumentera mätområdet.

- **Misstag:** Att välja ESP32 för alla projekt.
  - **Varför det händer:** Kortet är billigt och kraftfullt.
  - **Hur man undviker det:** Utgå från projektkrav, inte från maximal specifikation.

## Snabbreferens

- ESP32 är en familj, inte ett enda kort.
- Skilj mellan chip, modul och utvecklingskort.
- ESP32 är ofta starkt för Wi-Fi, BLE, IoT, mer minne och mer avancerade experiment.
- Alla ESP32-varianter har inte samma radio, USB, pinout eller periferienheter.
- ESP32 använder 3,3 V-logik; behandla inte GPIO som 5 V-toleranta.
- Pinout måste kontrolleras kortspecifikt, särskilt boot-relaterade pinnar.
- ADC fungerar för många praktiska mätningar men kräver kalibrering och försiktighet vid precision.
- Nätverkskod ska ha timeout och reservläge.
- Batteridrift kräver mätning av hela utvecklingskortet, inte bara läsning av chipets sleep-specifikation.
- En tydlig ESP32-kortprofil gör projekt mer reproducerbara.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | 3,3 V-logik |
| Typiskt gränssnitt | Wi-Fi, BLE, digital I/O, I2C, SPI, UART, ADC och PWM |
| Välj när | du behöver uppkoppling, prestanda och flexibel I/O |
| Välj inte när | du vill ha helt förutsägbar AVR-kompatibilitet eller 5 V-logik |
| Vanliga fel | strapping pins, ADC-antaganden, deep sleep-läckage, biblioteksversioner |
| Alternativ att överväga | ESP8266, Nano ESP32, RP2040/Pico |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När ESP32 känns för kraftfullt eller komplext, jämför med kapitel 2, 12 och 15.
- När många funktioner delar pinnar, bussar eller timers, använd kapitel 7, 9 och 30.
- När trådlös drift, batteri eller omstarter påverkar projektet, gå vidare till kapitel 34 och 35.

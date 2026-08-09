# 13. ESP8266 och NodeMCU

## Kortprofil i korthet
Det här kapitlet är en praktisk guide till ESP8266 och NodeMCU-liknande kort. Använd det när du vill bygga ett billigt Wi-Fi-projekt, läsa en sensor över nätverket, visa data på en enkel webbsida eller förstå varför ett ESP8266-kort beter sig annorlunda än en UNO.

Kapitlet hjälper dig framför allt att:

- se skillnaden mellan ESP8266-chip, ESP-modul och utvecklingskort
- välja ESP8266 när billig Wi-Fi är rätt prioritet
- välja bort ESP8266 när ESP32, klassisk Arduino eller ett modernare kort passar bättre
- undvika vanliga pinout-, boot- och 3,3 V-fällor
- bygga Wi-Fi-kod med timeout och tydliga felmeddelanden

## Bedöm kortet med detta i åtanke

ESP8266 är framför allt relevant när projektet behöver enkel Wi-Fi-anslutning och begränsat antal I/O räcker. Var särskilt uppmärksam på 3,3 V-logik, boot-pinnar, strömspikar och bibliotekens nätverksbeteende.

## ESP8266 som Arduino-kompatibel plattform

ESP8266 är i grunden en Wi-Fi-mikrokontroller. Den kan köra användarens program direkt, vilket betyder att den inte behöver sitta bredvid en separat Arduino som en ren Wi-Fi-modul. När du använder Arduino-kärnan för ESP8266 skriver du en vanlig sketch med `setup()` och `loop()`, men koden kompileras för ESP8266 och körs direkt på chipet.

Det gör ESP8266 annorlunda än en del äldre Wi-Fi-moduler som bara styrdes via AT-kommandon från en annan mikrokontroller. I ett Arduino-kompatibelt ESP8266-projekt är ESP8266 vanligtvis både huvudprocessor, Wi-Fi-enhet och I/O-styrenhet.

Det är en stor styrka. Du kan bygga ett uppkopplat sensorprojekt med ett enda litet kort, en sensor och en strömförsörjning. Samtidigt gör det att nätverksfunktionen och användarkoden delar samma resurser. Om din kod blockerar för länge, använder fel pinnar eller gör antaganden från klassisk Arduino kan systemet bli instabilt.

En bra mental modell är därför:

- ESP8266 är inte en UNO med Wi-Fi.
- ESP8266 är en liten uppkopplad mikrokontroller med Arduino-lik programmeringsmodell.
- NodeMCU och D1 mini är utvecklingskort som gör ESP8266 enklare att använda.
- Pinout, boot-pinnar och 3,3 V-logik är en del av plattformen, inte specialfall.

## Vanliga ESP8266-varianter

ESP8266 förekommer både som chip, modul och utvecklingskort. I praktiska Arduino-projekt är det oftast utvecklingskortet du håller i handen som avgör hur enkelt projektet blir.

| Variant | Typisk användning | Styrka | Begränsning |
|---|---|---|---|
| ESP-01 | Liten modul, ibland som Wi-Fi-tillägg eller minimalistiskt projekt | Mycket liten och billig | Få tillgängliga pinnar och kräver mer kringkoppling |
| ESP-12E/ESP-12F | Modul på många utvecklingskort | Fler GPIO och vanlig modulbas | Inte lika breadboard-vänlig utan bärarkort |
| NodeMCU | Utvecklingskort med USB, regulator och märkta D-pinnar | Enkel att programmera och testera med | Kan vara bred på breadboard och har pinout-fällor |
| Wemos/Lolin D1 mini | Kompakt utvecklingskort | Liten, populär och många shields/moduler | Mindre fysisk yta och varierande klonkvalitet |
| ESP8266 Dev Board-varianter | Diverse tredjepartskort | Ofta billiga och lättillgängliga | Dokumentation och märkning varierar |

NodeMCU och D1 mini är särskilt viktiga i den här boken eftersom de ofta dyker upp i startkit, sensorkit och hemautomationsprojekt. De är dessutom tillräckligt användarvänliga för att vara bra testkort.

## När ESP8266 är ett bra val

ESP8266 är ett bra val när projektets centrum är enkel Wi-Fi-kommunikation och när antalet anslutna komponenter är måttligt. Det passar särskilt bra för små sensornoder, webbaserade statuspaneler, MQTT-noder, enkla styrningar och test där låg kostnad gör det möjligt att bygga flera enheter.

Typiska projekt där ESP8266 passar bra:

- temperatur- eller fuktmätare som skickar data över Wi-Fi
- enkel webbsida som visar sensorvärden
- MQTT-baserad nod för hemautomation
- Wi-Fi-styrd LED-indikator
- batteritest där deep sleep används noggrant
- liten datainsamlare som publicerar mätvärden periodiskt
- lokal konfigurationssida för ett enkelt projekt

ESP8266 är också bra när du vill lära dig nätverksnära mikrokontrollerprogrammering utan att ta steget direkt till ESP32. Många begrepp återkommer senare: Wi-Fi-anslutning, IP-adress, webserver, klientanrop, MQTT, OTA, flashfilssystem och strömsparläge.

## När du bör välja något annat

ESP8266 är inte alltid rätt val. Den är äldre och mer begränsad än ESP32, och den är inte lika enkel elektriskt som en klassisk UNO.

Välj hellre ESP32 när projektet behöver:

- Bluetooth eller BLE
- fler GPIO-pinnar
- bättre prestanda
- fler moderna varianter
- mer minne
- mer avancerade timers eller periferi
- bättre marginal för nätverkskod och samtidig sensorkod

Välj hellre klassisk UNO, Nano eller Mega när projektet behöver:

- 5 V-logik utan nivåskiftning
- maximal enkelhet
- enklare felsökning utan nätverk
- många klassiska shields
- stabilt beteende med äldre exempel och bibliotek
- undervisning där nätverksdelen bara skulle störa

Välj hellre ett modernt officiellt Arduino-kort när projektet behöver:

- bättre dokumenterad produktplattform
- tydligare officiell support
- modernare USB-funktioner
- Arduino-formfaktor och Arduino-dokumentation
- långsiktigare undervisnings- eller kursmaterial

Välj hellre RP2040/RP2350-baserade kort när projektet behöver:

- många GPIO
- bra timingnära I/O
- hög testkapacitet utan Wi-Fi som huvudkrav
- låg kostnad men mer generell mikrokontrollerkaraktär

ESP8266 är alltså bäst när Wi-Fi är huvudpoängen och projektet kan leva med 3,3 V, begränsat antal säkra pinnar och plattformens specialfall.

## Elektriska egenskaper att känna till

Den viktigaste elektriska regeln är enkel:

ESP8266 är en 3,3 V-plattform.

Det betyder att GPIO-pinnarna normalt inte ska matas med 5 V-signaler. Många NodeMCU- och D1 mini-kort kan däremot matas via USB eller via en 5 V-/VIN-pin eftersom utvecklingskortet har regulator. Det betyder inte att GPIO-pinnarna blir 5 V-tåliga.

Skilj därför alltid mellan:

- matningsspänning till utvecklingskortet
- regulatorns utspänning
- mikrokontrollerns logiknivå
- sensorsignalens nivå
- modulens märkning

En del breakout-moduler har inbyggd nivåskiftning eller regulator. Andra har det inte. En sensor som marknadsförs som “Arduino compatible” kan vara avsedd för 5 V, 3,3 V eller båda. Läs märkningen och databladet innan du kopplar.

### Matning

NodeMCU- och D1 mini-liknande kort har vanligtvis USB och en lokal 3,3 V-regulator. För enkla test räcker USB från datorn ofta. För Wi-Fi-projekt med sensorer och LED kan strömtoppar bli mer tydliga än på ett klassiskt blink-exempel.

Praktiska regler:

- Mata kortet via USB under tidig utveckling.
- Använd stabil matning när Wi-Fi används.
- Undvik att driva större laster från kortets 3,3 V-pin.
- Dokumentera om moduler matas från 3,3 V, 5 V eller extern källa.
- Koppla gemensam jord mellan ESP8266 och externa moduler.
- Var försiktig med motorer, reläer och LED-strippar; de behöver normalt separat drivning.

### ADC och analog ingång

ESP8266 har begränsad analog funktion jämfört med många andra kort. Många utvecklingskort exponerar en analog ingång märkt `A0`, men spänningsområdet kan bero på kortets inbyggda spänningsdelare.

Det här är en klassisk fälla. På vissa ESP8266-moduler är den underliggande ADC-ingången avsedd för ett lägre spänningsområde, medan utvecklingskortet kan ha en spänningsdelare som gör `A0` mer testvänlig. Kontrollera alltid dokumentationen för just ditt kort.

För en erfaren programmerare är den bästa regeln att aldrig anta ADC-området. Mät och dokumentera.

Exempel på dokumentation i projektet:

```cpp
// Board: NodeMCU ESP8266 v1.0
// A0 range: verify for this board before connecting external voltage.
// Sensor: potentiometer module powered from 3.3 V.
// Note: do not connect 5 V directly to A0.
```

### Pinnar som påverkar uppstart

ESP8266 läser vissa pinnar vid uppstart för att avgöra bootläge. Om externa komponenter drar dessa pinnar åt fel håll kan kortet vägra starta, hamna i uppladdningsläge eller bete sig instabilt.

De vanligaste pinnar att vara försiktig med är GPIO0, GPIO2 och GPIO15. På NodeMCU-kort motsvaras de ofta av D3, D4 och D8, men kontrollera alltid pinout för ditt kort.

En praktisk första version av ett ESP8266-projekt bör därför undvika boot-relaterade pinnar för saker som kan hålla pinnen hög eller låg vid start. Använd hellre säkrare pinnar för första prototypen och flytta bara om du vet varför.

## NodeMCU-pinnar och GPIO-pinnar

På många NodeMCU-kort står det `D0`, `D1`, `D2` och så vidare på kortet. Det är inte samma sak som ESP8266-chipets GPIO-nummer. I Arduino-koden kan du ofta använda `D1`, `D2` och liknande symboler när rätt board package är valt, men det är viktigt att förstå att dessa översätts till faktiska GPIO.

Ett vanligt exempel är att `D5` på NodeMCU ofta motsvarar GPIO14. Det betyder att dokumentation, bibliotek och kodexempel kan använda olika namn för samma fysiska pinne.

Därför bör bokens test dokumentera båda namnen när ESP8266 används.

| Silkscreen | Vanlig GPIO | Typisk kommentar |
|---|---|---|
| D0 | GPIO16 | Särskild pinne, ofta kopplad till deep sleep-wake på vissa kort |
| D1 | GPIO5 | Ofta lämplig för I2C SCL i exempel |
| D2 | GPIO4 | Ofta lämplig för I2C SDA i exempel |
| D3 | GPIO0 | Boot-relaterad, använd med försiktighet |
| D4 | GPIO2 | Boot-relaterad, ofta kopplad till inbyggd LED på vissa kort |
| D5 | GPIO14 | Ofta SPI SCLK |
| D6 | GPIO12 | Ofta SPI MISO |
| D7 | GPIO13 | Ofta SPI MOSI |
| D8 | GPIO15 | Boot-relaterad, använd med försiktighet |
| RX | GPIO3 | Seriell mottagning, påverkar uppladdning/debug |
| TX | GPIO1 | Seriell sändning, påverkar uppladdning/debug |
| A0 | ADC | Analog ingång, kontrollera spänningsområde |

Tabellen ska inte ersätta pinout för ditt kort. Den ska hjälpa dig att se vilken typ av problem du letar efter.

Ett bra kodmönster är att definiera projektets pinnar i början och använda namn som beskriver funktion, inte bara fysisk pinne.

```cpp
const int STATUS_LED_PIN = D4;
const int SENSOR_SDA_PIN = D2;
const int SENSOR_SCL_PIN = D1;
```

Det gör koden lättare att flytta till ett annat ESP8266-kort. Om du senare byter från NodeMCU till D1 mini behöver du bara kontrollera konfigurationsdelen.

## Wi-Fi som del av programflödet

På en klassisk Arduino kan `loop()` ofta få vara ganska enkel. Du läser en sensor, styr en utgång och skriver något till seriell monitor. På ESP8266 måste du tänka på att Wi-Fi-stacken också behöver tid.

Det betyder att långa blockerande loopar, tung beräkning eller felaktig användning av `delay()` kan påverka nätverksstabilitet och watchdog. Det betyder inte att du aldrig får använda `delay()`, men det betyder att du bör skriva kod med rimlig hänsyn till plattformen.

Bra mönster:

- anslut till Wi-Fi i en avgränsad funktion
- ha timeout vid anslutning
- skriv tydlig status till seriell monitor
- låt `loop()` vara kort
- använd `millis()` för återkommande arbete
- undvik oändliga blockerande väntelägen
- hantera frånkopplingar eller misslyckad anslutning

Ett ESP8266-program ska inte bara fungera när nätverket är perfekt. Det ska också ge rimlig information när Wi-Fi-lösenordet är fel, routern är nere eller signalen är svag.

## Praktisk struktur för ESP8266-projekt

Ett litet ESP8266-projekt blir ofta mer robust om det delas upp i tydliga delar:

- kort- och pinnkonfiguration
- Wi-Fi-konfiguration
- sensorläsning
- statusutskrift
- nätverkspublicering
- felhantering

Undvik att blanda allt direkt i `loop()`. Det fungerar i ett blink-exempel, men blir snabbt svårt att felsöka i ett Wi-Fi-projekt.

Ett enkelt grundmönster:

```cpp
#include <ESP8266WiFi.h>

const char* WIFI_SSID = "your-ssid";
const char* WIFI_PASSWORD = "your-password";

const int STATUS_LED_PIN = LED_BUILTIN;
const unsigned long SAMPLE_INTERVAL_MS = 5000;

unsigned long lastSampleAt = 0;

void connectToWiFi() {
  Serial.print("Connecting to WiFi");

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  const unsigned long timeoutMs = 15000;
  const unsigned long startAt = millis();

  while (WiFi.status() != WL_CONNECTED && millis() - startAt < timeoutMs) {
    delay(250);
    Serial.print(".");
  }

  Serial.println();

  if (WiFi.status() == WL_CONNECTED) {
    Serial.print("Connected. IP address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("WiFi connection failed. Continuing without network.");
  }
}

int readExampleSensor() {
  return analogRead(A0);
}

void reportSample(int value) {
  Serial.print("Sensor value: ");
  Serial.println(value);
}

void setup() {
  pinMode(STATUS_LED_PIN, OUTPUT);

  Serial.begin(115200);
  delay(200);

  Serial.println();
  Serial.println("ESP8266 sensor test");

  connectToWiFi();
}

void loop() {
  const unsigned long now = millis();

  if (now - lastSampleAt >= SAMPLE_INTERVAL_MS) {
    lastSampleAt = now;

    int sensorValue = readExampleSensor();
    reportSample(sensorValue);

    digitalWrite(STATUS_LED_PIN, !digitalRead(STATUS_LED_PIN));
  }
}
```

Observera att koden är ett grundmönster, inte ett färdigt produktionsprogram. I ett riktigt projekt skulle du inte hårdkoda Wi-Fi-lösenord i versionshanterad kod. Du skulle också hantera återanslutning, konfiguration och felstatus mer tydligt.

## Enkel webbsida på ESP8266

Ett klassiskt ESP8266-test är att läsa ett sensorvärde och visa det via en liten webbsida. Det är pedagogiskt eftersom det visar att kortet inte bara skickar data ut på nätverket, utan också kan agera enkel server.

```cpp
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* WIFI_SSID = "your-ssid";
const char* WIFI_PASSWORD = "your-password";

ESP8266WebServer server(80);

int readSensorValue() {
  return analogRead(A0);
}

void handleRoot() {
  int value = readSensorValue();

  String page = "<!doctype html><html><head><meta charset='utf-8'>";
  page += "<title>ESP8266 Sensor</title></head><body>";
  page += "<h1>ESP8266 Sensor</h1>";
  page += "<p>Analog value: ";
  page += String(value);
  page += "</p>";
  page += "</body></html>";

  server.send(200, "text/html", page);
}

void connectToWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("Open http://");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);
  delay(200);

  connectToWiFi();

  server.on("/", handleRoot);
  server.begin();

  Serial.println("HTTP server started.");
}

void loop() {
  server.handleClient();
}
```

Det här exemplet är medvetet enkelt. Det visar principen, men det har ingen timeout i Wi-Fi-anslutningen. När du använder mönstret i egna test bör du lägga till samma typ av timeout som i föregående exempel.

## I2C på ESP8266

ESP8266 har inte samma fasta I2C-känsla som vissa andra plattformar. I Arduino-exempel för NodeMCU används ofta D1 som SCL och D2 som SDA, men du bör dokumentera pinnar explicit.

```cpp
#include <Wire.h>

const int I2C_SDA_PIN = D2;
const int I2C_SCL_PIN = D1;

void setup() {
  Serial.begin(115200);
  delay(200);

  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);

  Serial.println("I2C scanner");
}

void loop() {
  byte found = 0;

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Found I2C device at 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.println(address, HEX);
      found++;
    }
  }

  Serial.print("Devices found: ");
  Serial.println(found);

  delay(5000);
}
```

Det här är ett bra första test innan du lägger till ett sensorbibliotek. Om I2C-scannern inte hittar sensorn är det oftast ingen idé att felsöka bibliotekskoden först. Kontrollera i stället matning, jord, SDA/SCL, adress och pullups.

## SPI på ESP8266

ESP8266 kan använda SPI, men precis som på andra kort behöver du kontrollera vilka pinnar som är kopplade till SPI-funktionerna på ditt utvecklingskort. På NodeMCU används ofta D5, D6 och D7 för SCLK, MISO och MOSI. D8 används ofta som chip select i exempel, men D8 är också boot-relaterad på många ESP8266-kort. Det betyder att du måste tänka igenom vad den anslutna SPI-enheten gör vid uppstart.

För första testet är det ofta enklare att börja med I2C-sensorer på ESP8266. Gå vidare till SPI när du behöver högre hastighet, display, SD-kort eller en komponent som bara stöder SPI.

## Deep sleep och batteridrift

ESP8266 kan vara intressant för batteridrivna projekt, men batteridrift är inte automatiskt enkel. Själva chipet kan spara mycket ström i deep sleep, men utvecklingskortets regulator, USB-seriechip och eventuella power-LED kan dra ström även när mikrokontrollern sover.

För batteriprojekt ska du därför skilja mellan:

- vad ESP8266-chipet kan göra
- vad ditt utvecklingskort faktiskt förbrukar
- vad sensorer och moduler drar
- hur ofta enheten vaknar
- hur länge Wi-Fi-anslutningen tar
- om data måste skickas varje gång

Många ESP8266-batteriprojekt följer mönstret:

1. vakna
2. läsa sensor
3. ansluta till Wi-Fi
4. skicka data
5. somna igen

Det är ett bra mönster när mätningen är periodisk och projektet inte behöver reagera direkt på händelser. För en interaktiv knapp, display eller styrning är deep sleep ofta mindre lämpligt.

På vissa ESP8266-kort används GPIO16 för att väcka kortet från deep sleep via reset. Kontrollera kortets dokumentation innan du bygger batteriprojekt runt den funktionen.

## Säkerhets- och robusthetsgränser

ESP8266 lockar till snabba IoT-projekt. Det är roligt, men uppkoppling ändrar också projektets riskprofil. Ett lokalt blink-test kan vara ofarligt även om koden är enkel. En nätverksstyrd relämodul eller portöppnare kräver mer eftertanke.

Praktiska regler:

- Exponera inte en enkel ESP8266-webserver direkt mot internet.
- Använd lokalt nätverk för test.
- Hårdkoda inte lösenord i kod som delas publikt.
- Låt farliga laster ha fysisk säkerhet oberoende av Wi-Fi.
- Se till att projektet har säkert standardläge vid omstart.
- Anta att nätverket ibland försvinner.
- Anta att kortet ibland startar om.

Särskilt vid reläer, värme, motorer, pumpar och dörrlås måste elektroniken byggas så att ett programfel inte blir en fysisk fara. ESP8266 gör inte ett projekt säkert bara för att det är uppkopplat.

## Valguide

| Projektkrav | ESP8266 passar? | Kommentar |
|---|---|---|
| Billig Wi-Fi-sensornod | Ja | Ett av ESP8266:s bästa användningsområden |
| Många GPIO | Ibland | Kontrollera antal säkra pinnar; ESP32 eller Mega kan passa bättre |
| 5 V-sensorer utan nivåskiftning | Nej | Välj 5 V-kort eller använd nivåskiftning |
| BLE/Bluetooth | Nej | Välj ESP32 |
| Enkel lokal webbsida | Ja | Mycket praktiskt och användbart som lokalt test |
| Batteridrift | Ibland | Kräver rätt kort, deep sleep och mätning av faktisk ström |
| Snabb display via SPI | Ibland | Möjligt, men kontrollera pinnar och boot-beteende |
| Undervisning i grundläggande digital I/O | Ibland | UNO/Nano är ofta enklare pedagogiskt |
| Lågkostnads-hemautomation | Ja | Vanligt användningsområde, men tänk på säkerhet |
| Robust produkt med lång livslängd | Ibland | Välj dokumenterad hårdvara och kontrollera tillgänglighet |

## Referensmönster: Wi-Fi-baserad sensorindikator

Det här referensmönstret visar en enkel ESP8266-nod som läser ett analogt värde, skriver det till seriell monitor och visar enkel status via inbyggd LED. Om Wi-Fi fungerar visas IP-adressen. Om Wi-Fi inte fungerar fortsätter noden ändå att läsa sensorn lokalt.

Mönstret är inte tänkt som den mest avancerade webbnoden. Det visar en robust grundstruktur med pinoutkontroll, Wi-Fi-timeout och lokal fallback.

### Det här används i exemplet

- NodeMCU ESP8266 eller Wemos/Lolin D1 mini
- USB-kabel som stödjer data, inte bara laddning
- potentiometer eller analog sensormodul som är säker för kortets A0-område
- eventuellt kopplingsdäck och några kablar
- dator med Arduino IDE och ESP8266-board package installerat

### Koppling

Koppla potentiometern eller den analoga modulen enligt kortets dokumenterade A0-område. Om du är osäker, använd en färdig potentiometermodul matad från 3,3 V och mät spänningen innan du ansluter A0.

Kontrollera innan du bygger vidare:

- exakt kortmodell
- valt board i Arduino IDE
- USB-seriechip om det är relevant
- A0-spänningsområde enligt dokumentation eller mätning
- vilka pinnar som används
- Wi-Fi-nätets namn, men inte lösenord i publik dokumentation

### Kod

```cpp
#include <ESP8266WiFi.h>

const char* WIFI_SSID = "your-ssid";
const char* WIFI_PASSWORD = "your-password";

const int STATUS_LED_PIN = LED_BUILTIN;
const int SENSOR_PIN = A0;

const unsigned long SAMPLE_INTERVAL_MS = 2000;
unsigned long lastSampleAt = 0;

bool wifiConnected = false;

void setStatusLed(bool on) {
  // LED_BUILTIN is active LOW on many ESP8266 boards.
  digitalWrite(STATUS_LED_PIN, on ? LOW : HIGH);
}

void connectToWiFiWithTimeout() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.print("Connecting to WiFi");

  const unsigned long timeoutMs = 15000;
  const unsigned long startAt = millis();

  while (WiFi.status() != WL_CONNECTED && millis() - startAt < timeoutMs) {
    delay(250);
    Serial.print(".");
  }

  Serial.println();

  wifiConnected = WiFi.status() == WL_CONNECTED;

  if (wifiConnected) {
    Serial.print("Connected. IP address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("WiFi not connected. Running local sensor mode.");
  }
}

void setup() {
  pinMode(STATUS_LED_PIN, OUTPUT);
  setStatusLed(false);

  Serial.begin(115200);
  delay(200);

  Serial.println();
  Serial.println("ESP8266 WiFi sensor indicator");
  Serial.println("Verify A0 voltage range before connecting analog signals.");

  connectToWiFiWithTimeout();
}

void loop() {
  const unsigned long now = millis();

  if (now - lastSampleAt >= SAMPLE_INTERVAL_MS) {
    lastSampleAt = now;

    int rawValue = analogRead(SENSOR_PIN);

    Serial.print("A0 raw value: ");
    Serial.print(rawValue);

    Serial.print(" | WiFi: ");
    Serial.println(wifiConnected ? "connected" : "offline");

    setStatusLed(!digitalRead(STATUS_LED_PIN));
  }

  if (wifiConnected && WiFi.status() != WL_CONNECTED) {
    wifiConnected = false;
    Serial.println("WiFi connection lost.");
    setStatusLed(false);
  }
}
```

### Förväntat resultat

När kortet startar ska seriell monitor visa anslutningsförsök. Om Wi-Fi-uppgifterna är korrekta ska IP-adressen skrivas ut. Därefter ska analogvärdet visas med jämna mellanrum.

Om Wi-Fi-lösenordet är fel ska programmet inte fastna för alltid. Det ska skriva att Wi-Fi saknas och fortsätta läsa sensorn lokalt.

### Anpassningar

- Byt analogvärdet mot en I2C-sensor och använd I2C-scannern först.
- Publicera värdet via enkel webbsida.
- Publicera värdet via MQTT i ett senare test.
- Lägg till en extern LED på en säker pinne i stället för inbyggd LED.
- Mät strömförbrukningen under anslutning och vila.
- Jämför samma test på ESP32 i nästa kapitel.

## Vanliga misstag

- **Misstag:** Att koppla 5 V-signaler direkt till ESP8266-GPIO.
  - **Varför det händer:** Många Arduino-moduler marknadsförs som kompatibla utan att det är tydligt om signalerna är 3,3 V eller 5 V.
  - **Hur man undviker det:** Kontrollera logiknivå och använd nivåskiftning eller 3,3 V-kompatibla moduler.

- **Misstag:** Att använda D3, D4 eller D8 utan att tänka på uppstart.
  - **Varför det händer:** Pinnarna ser ut som vanliga digitala pinnar på silkscreen.
  - **Hur man undviker det:** Kontrollera om pinnen motsvarar GPIO0, GPIO2 eller GPIO15 och undvik dem i första versionen av projektet.

- **Misstag:** Att blanda ihop D-nummer och GPIO-nummer.
  - **Varför det händer:** NodeMCU-märkning och ESP8266-GPIO är två olika namnsystem.
  - **Hur man undviker det:** Dokumentera både silkscreen-namn och faktisk GPIO i projektanteckningarna.

- **Misstag:** Att anta att A0 tål samma spänning på alla ESP8266-kort.
  - **Varför det händer:** Utvecklingskort kan ha olika spänningsdelare och dokumentation.
  - **Hur man undviker det:** Kontrollera kortets dokumentation och mät innan extern analog signal ansluts.

- **Misstag:** Att låta Wi-Fi-anslutning blockera programmet för alltid.
  - **Varför det händer:** Många enkla exempel väntar i en loop tills anslutningen lyckas.
  - **Hur man undviker det:** Använd timeout och låt projektet ha ett lokalt reservläge.

- **Misstag:** Att felsöka sensorbibliotek innan bussen fungerar.
  - **Varför det händer:** Det är frestande att börja i den högsta kodnivån.
  - **Hur man undviker det:** Testa först kort, port, seriell monitor, I2C-scanner och minimal sensorläsning.

- **Misstag:** Att använda ett utvecklingskort för batteridrift utan att mäta viloström.
  - **Varför det händer:** Man läser om ESP8266 deep sleep men glömmer att utvecklingskortets regulator och USB-chip också drar ström.
  - **Hur man undviker det:** Mät faktisk ström på hela kortet och välj batterivänlig hårdvara om det behövs.

## Praktiska ESP8266-varianter

### I2C-scanner på NodeMCU eller D1 mini

När en I2C-sensor används på NodeMCU eller D1 mini bör du kontrollera bussens grunddata innan bibliotekskoden felsöks:

- SDA-pin
- SCL-pin
- sensoradress
- matningsspänning
- om externa pullups används
- vad som händer om SDA och SCL byts

När scannern hittar sensorn är nästa steg att kontrollera att sensorbiblioteket använder samma I2C-pinnar.

### Webbsida med sensorvärde

En enkel nästa variant är att visa ett verkligt sensorvärde på webbsidan. Det kan vara A0, en I2C-temperatursensor eller ett simulerat värde.

Lägg gärna till:

- kortets IP-adress i seriell monitor
- tidsstämpel eller räknare
- felmeddelande om sensorn inte kan läsas

### Reservläge utan Wi-Fi

Ett robust ESP8266-projekt bör ha ett lokalt reservläge när nätverket saknas:

- uppkopplat läge, där data visas via nätverk
- lokalt läge, där data bara visas via seriell monitor och LED-status

Det viktiga är att nätverket inte får stoppa hela programmet.

## Snabbreferens

- ESP8266 är en Wi-Fi-mikrokontroller som kan programmeras med Arduino-liknande API.
- NodeMCU och D1 mini är vanliga utvecklingskort som gör ESP8266 enkel att använda.
- ESP8266 passar bra för billiga Wi-Fi-sensornoder, enkla webbsidor, MQTT och hemautomationstest.
- ESP8266 är inte en UNO med Wi-Fi; 3,3 V-logik, boot-pinnar och pinout-skillnader måste hanteras.
- D-nummer på NodeMCU är inte samma sak som ESP8266-GPIO-nummer.
- GPIO0, GPIO2 och GPIO15 påverkar uppstart och bör behandlas med försiktighet.
- A0-spänningsområdet kan variera mellan utvecklingskort och ska kontrolleras.
- Wi-Fi-kod bör ha timeout och tydliga felmeddelanden.
- Batteridrift kräver mätning av hela utvecklingskortets strömförbrukning, inte bara kunskap om chipets deep sleep.
- ESP8266 är ofta rätt när Wi-Fi och låg kostnad är viktigast, men ESP32 är ofta bättre när projektet behöver mer marginal.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | 3,3 V-logik |
| Typiskt gränssnitt | Wi-Fi, digital I/O, I2C, SPI och UART |
| Välj när | billig Wi-Fi och enkla IoT-test räcker |
| Välj inte när | du behöver många pinnar, Bluetooth eller modernare periferistöd |
| Vanliga fel | boot pins, fel D/GPIO-mappning, för svag regulator, 5 V-signaler |
| Alternativ att överväga | ESP32, Nano ESP32, Pico W |

Använd referensrutan som en snabb kontroll innan du bygger testet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När Wi-Fi inte är huvudkravet, jämför med kortvalet i kapitel 2 och alternativen i kapitel 12–15.
- När 3,3 V-nivåer påverkar givare, relämoduler eller bussar, använd kapitel 4, 9 och 33.
- När projektet får omstarter vid Wi-Fi eller sändning, börja med strömförsörjningen i kapitel 34.

# 32. Displaykretsar, minne och datalagring

## Lagrings- och displayöversikt
I kapitel 22 byggde du enkla användargränssnitt med displayer, knappar och rotary encoders. Där låg fokus på vad användaren ser och gör. I det här kapitlet går vi ett steg djupare och tittar på kretsarna och modulerna bakom två vanliga behov i praktiska Arduino-system:

- att visa information på ett effektivt sätt
- att spara data så att den finns kvar efter omstart

Det här är två områden som ofta verkar enkla i början men som snabbt påverkar hela systemets design. En liten OLED-display kan kännas trivial tills minnet tar slut på ett AVR-kort. Ett SD-kort kan kännas som en vanlig filyta tills loggningen blockerar resten av programmet. Ett EEPROM kan kännas perfekt för konfiguration tills du råkar skriva till det varje sekund och sliter ut minnescellerna. En displaydrivare kan verka som en detalj tills du upptäcker att den kräver SPI, extra buffertminne eller en specifik uppdateringsmodell.

Kapitlet handlar därför inte bara om komponentnamn. Det handlar om val:

- När räcker intern EEPROM?
- När är extern EEPROM eller FRAM bättre?
- När är SD-kort rätt val?
- När bör du visa data direkt och när bör du logga den?
- När är en enkel displaymodul bättre än en rå displaypanel?
- När blir bibliotekets minneskrav viktigare än själva hårdvaran?
- Hur bygger du en logger som inte förstör data om strömmen bryts?

Målet är att du ska kunna välja en rimlig lösning för display och datalagring utan att bygga in onödig komplexitet.

Kapitlet fungerar som stöd när du behöver välja lagring, displaykoppling och loggstruktur utan att slita ut minnen, blockera programmet eller fylla RAM på små kort.

## Förutsättningar

Det här kapitlet bygger på flera tidigare kapitel:

- Från kapitel 4: spänning, ström, avkoppling, jord och nivåskiftning.
- Från kapitel 6: mätvärden, filtrering och mätosäkerhet.
- Från kapitel 9: UART, I2C, SPI och 1-Wire.
- Från kapitel 22: displayer, knappar, menyer och enkel användarinteraktion.
- Från kapitel 29: tid, tidsstämplar, nod-ID och händelseloggar.
- Från kapitel 30: I/O-expansion och hur externa kretsar kan avlasta mikrokontrollern.

En viktig princip är:

> Visa det som användaren behöver just nu. Spara det som systemet eller du behöver kunna förstå senare.

Det betyder att display och datalagring inte är samma sak. En display ger direkt återkoppling. Lagring ger spårbarhet, konfiguration, historik och möjlighet att analysera data i efterhand.

## Tre typer av data i Arduino-projekt

Innan vi väljer minnesteknik behöver vi förstå vilken sorts data som ska sparas. Ett vanligt misstag är att behandla all data som “något som ska skrivas till minne”. I praktiken finns minst tre olika kategorier.

| Datatyp | Exempel | Typisk lagring | Viktigaste krav |
|---|---|---|---|
| Konfiguration | kalibreringsvärde, nod-ID, valt läge | EEPROM, flash, FRAM | få skrivningar, överlever omstart |
| Händelser | larm, knapptryck, RFID-läsning | FRAM, SD-kort, seriell logg | tidsstämpel, ordning, robusthet |
| Mätserier | temperatur varje minut, ström över tid | SD-kort, extern flash, nätverk | volym, format, analysbarhet |

Konfiguration ändras sällan. Den kan ofta sparas i EEPROM eller flash.

Händelser är små men viktiga. De behöver ofta sparas även om strömmen försvinner. Här är FRAM ibland mycket trevligt eftersom det tål många skrivningar och beter sig mer som vanligt RAM.

Mätserier kan snabbt bli stora. Där är SD-kort ofta det mest praktiska valet om projektet ska vara fristående.

## Flyktigt och icke-flyktigt minne

Ett minne är flyktigt om det tappar sitt innehåll när strömmen försvinner. SRAM i en mikrokontroller är flyktigt. Det används för variabler medan programmet körs.

Ett minne är icke-flyktigt om det behåller sitt innehåll efter avstängning. EEPROM, flash, FRAM och SD-kort är icke-flyktiga.

Det kan låta som att icke-flyktigt minne alltid är bättre, men det finns avvägningar:

- Det är ofta långsammare att skriva.
- Det kan ha begränsat antal skrivcykler.
- Det kan behöva skrivas i block eller sidor.
- Det kan bli korrupt om strömmen bryts mitt under skrivning.
- Det kan kräva bibliotek, filsystem eller buffertar.

För en erfaren programmerare är det bra att tänka på datalagring som ett litet persistenslager. Du behöver veta vad som sparas, när det sparas, hur ofta det sparas och hur programmet återhämtar sig om skrivningen misslyckas.

## Intern EEPROM

Många klassiska AVR-baserade Arduino-kort har intern EEPROM. Den är liten men praktisk. Den passar för konfiguration som ändras sällan:

- kalibreringsvärden
- senaste valda läge
- nod-ID
- räknare som uppdateras sällan
- små flaggor

Intern EEPROM passar däremot dåligt för kontinuerlig loggning. Om du skriver ett nytt mätvärde varje sekund kan minnet slitas ut onödigt snabbt. Exakta gränser beror på mikrokontroller och datablad, men tumregeln är enkel: skriv inte till EEPROM i en snabb loop.

### När intern EEPROM är rätt val

Använd intern EEPROM när:

- datamängden är liten
- värdet ändras sällan
- du vill slippa extra komponenter
- projektet körs på ett kort som faktiskt har EEPROM
- du kan hantera standardvärden om minnet är tomt

### När intern EEPROM är fel val

Välj något annat när:

- du behöver spara många mätvärden
- du skriver ofta
- du behöver flytta data enkelt till dator
- kortet saknar riktig EEPROM
- datan är större än några få bytes eller små strukturer

### Enkel EEPROM-struktur

För konfiguration är det bättre att spara en liten struktur med versionsnummer än att sprida enskilda bytes på olika adresser utan dokumentation.

```cpp
#include <EEPROM.h>

struct DeviceConfig {
  uint16_t magic;
  uint8_t version;
  uint8_t nodeId;
  float temperatureOffset;
};

const uint16_t CONFIG_MAGIC = 0xA42B;
const uint8_t CONFIG_VERSION = 1;
const int CONFIG_ADDRESS = 0;

DeviceConfig config;

void loadDefaultConfig() {
  config.magic = CONFIG_MAGIC;
  config.version = CONFIG_VERSION;
  config.nodeId = 1;
  config.temperatureOffset = 0.0;
}

void loadConfig() {
  EEPROM.get(CONFIG_ADDRESS, config);

  if (config.magic != CONFIG_MAGIC || config.version != CONFIG_VERSION) {
    loadDefaultConfig();
    EEPROM.put(CONFIG_ADDRESS, config);
  }
}

void saveConfigIfChanged(const DeviceConfig& nextConfig) {
  if (memcmp(&config, &nextConfig, sizeof(DeviceConfig)) != 0) {
    config = nextConfig;
    EEPROM.put(CONFIG_ADDRESS, config);
  }
}

void setup() {
  Serial.begin(115200);
  loadConfig();

  Serial.print("Node ID: ");
  Serial.println(config.nodeId);
}

void loop() {
}
```

Det viktiga här är inte själva koden utan mönstret:

- använd en `magic`-markör för att se om minnet verkar initierat
- använd versionsnummer för framtida ändringar
- skriv bara när värdet faktiskt ändrats
- ha rimliga standardvärden

På vissa moderna kort emuleras EEPROM i flash. Det kan fungera bra, men det betyder att skrivningarna egentligen hanteras av flashminne och ett bibliotek. Då bör du vara extra noggrann med dokumentationen för just den plattformen.

## Extern EEPROM

Extern EEPROM är en separat minneskrets, ofta via I2C eller SPI. Den används när intern EEPROM saknas eller inte räcker.

Vanliga skäl att använda extern EEPROM:

- du behöver lite mer icke-flyktigt minne än det interna
- du vill ha samma lagringslösning oavsett Arduino-kort
- du vill spara kalibrering nära en viss modul
- du vill separera konfiguration från mikrokontrollerns interna minne

Extern EEPROM är fortfarande inte förstahandsvalet för stora loggar. Den är mer en robust konfigurations- och smådatalösning.

### Praktiska frågor vid extern EEPROM

Kontrollera alltid:

- matningsspänning
- I2C-adress eller SPI-chip select
- sidstorlek vid skrivning
- skrivfördröjning efter varje skrivning
- maximal skrivfrekvens
- bibliotekets adressmodell

Vissa EEPROM-kretsar skriver inte enskilda bytes helt fritt internt, utan arbetar med sidor. Om du skriver över en sidgräns på fel sätt kan resultatet bli oväntat beroende på bibliotek och krets.

Som huvudregel: använd ett beprövat bibliotek och skriv små, tydligt avgränsade strukturer.

## FRAM

FRAM står för ferroelectric random-access memory. För Arduino-projekt är det intressant eftersom det ofta kombinerar två trevliga egenskaper:

- det är icke-flyktigt
- det tål väldigt många skrivningar jämfört med EEPROM

FRAM används ofta via I2C eller SPI. Det beter sig mer som ett minne där du kan uppdatera data ofta utan att tänka lika mycket på slitage.

### När FRAM är rätt val

FRAM passar bra när:

- du behöver spara små eller medelstora data ofta
- du vill logga händelser robust
- du vill spara tillstånd vid varje viktig förändring
- du vill undvika EEPROM-slitage
- du inte behöver SD-kortets stora lagringsvolym

Exempel:

- räknare som uppdateras ofta
- senaste kända stabila tillstånd
- händelsekö vid opålitlig strömförsörjning
- korta mätloggar
- transaktionsliknande statusdata

### När FRAM inte är rätt val

FRAM är inte alltid bäst. Välj något annat när:

- du behöver lagra megabyte eller gigabyte
- datan ska kunna tas ut enkelt som fil
- pris per byte är viktigare än skrivtålighet
- du redan har nätverksloggning eller SD-kort

FRAM är ofta utmärkt för robusthet, men SD-kort är bättre för stora loggfiler.

## Flash och programminne

Flash är minnet där programmet normalt ligger. Många moderna mikrokontrollers har mycket flash. Vissa plattformar låter dig också använda delar av flash för filsystem eller inställningar.

På ESP8266 och ESP32 är det vanligt med flashbaserade filsystem eller partitionslösningar. På vissa andra kort finns också varianter av intern flashlagring.

Det här kan vara praktiskt, men det finns fallgropar:

- flash har begränsade skrivcykler
- skrivningar kan ske i större block än du tror
- filsystemet kan påverka hur programmet är partitionerat
- olika kortfamiljer har olika API:er
- långvarig loggning till intern flash kan vara olämplig

Använd flashbaserad lagring för inställningar, små filer, webbinnehåll, certifikat eller sällan ändrad data. Använd inte intern flash som ersättning för SD-kort vid tät mätloggning utan att först förstå plattformens rekommendationer.

## SD-kort

SD-kort är den vanligaste lösningen när Arduino-projekt ska spara större mängder data lokalt. Det är billigt, flyttbart och lätt att läsa på en dator.

Typiska användningar:

- datalogging
- CSV-filer
- händelselogg
- konfigurationsfiler
- ljudfiler eller bilder i mer avancerade projekt
- export av mätdata utan nätverk

De flesta SD-kortmoduler använder SPI. Vissa kort och shields har färdiga SD-kortplatser. Många moduler fungerar med 3,3 V-logik, men billiga moduler för Arduino-marknaden kan ha nivåanpassning och regulator för 5 V-system. Kontrollera alltid modulens specifikation.

### Fördelar med SD-kort

SD-kort är bra när:

- du behöver mycket lagring
- datan ska kunna läsas i dator
- du vill använda filformat som CSV
- loggen ska överleva omstart
- projektet inte alltid har nätverk

### Nackdelar med SD-kort

SD-kort kräver mer omsorg än många tror:

- skrivningar kan blockera programmet
- filsystem kan bli korrupt vid strömavbrott
- vissa kort drar relativt mycket ström
- billiga SD-moduler kan ha tveksam nivåanpassning
- långa kablar och breadboard-kopplingar kan ge SPI-problem
- det är lätt att skriva för ofta

För dataloggers är det ofta bättre att samla mätvärden i en liten buffert och skriva i kontrollerade intervall än att öppna, skriva och stänga filen för varje sensorvärde. Samtidigt ökar buffring risken att förlora de senaste värdena om strömmen bryts. Det är en designavvägning.

## Välja lagringsteknik

En praktisk valguide:

| Behov | Rekommenderad teknik | Kommentar |
|---|---|---|
| Spara ett nod-ID | Intern EEPROM eller flashinställning | Skriv bara när värdet ändras. |
| Spara kalibreringsvärden | EEPROM, extern EEPROM eller FRAM | Lägg till versionsnummer och standardvärden. |
| Spara ofta ändrat tillstånd | FRAM | Bra när skrivningar sker ofta. |
| Logga många mätvärden | SD-kort | Använd CSV eller annat enkelt format. |
| Spara webbfiler på ESP-kort | Flashbaserat filsystem | Passar sällan ändrade filer. |
| Exportera data till dator | SD-kort | Flyttbart och lätt att läsa. |
| Lagra mycket data långsiktigt | SD-kort eller nätverk | EEPROM/FRAM är för små datamängder. |

En tumregel:

> EEPROM för inställningar, FRAM för ofta ändrat tillstånd, SD-kort för stora loggar.

## Loggformat

Ett loggformat ska vara enkelt att skriva, enkelt att läsa och enkelt att felsöka. För många Arduino-projekt är CSV tillräckligt.

Ett bra loggformat innehåller ofta:

- tidsstämpel
- nod-ID
- mätvärden
- enhet eller tydlig kolumnrubrik
- statuskod
- eventuell felindikering

Exempel:

```text
timestamp,node_id,temperature_c,humidity_percent,status
2026-06-30T10:15:00Z,3,22.6,44.1,OK
2026-06-30T10:16:00Z,3,22.7,44.0,OK
2026-06-30T10:17:00Z,3,,43.8,TEMP_ERROR
```

Notera att ett saknat värde är bättre än ett påhittat värde. Om temperatursensorn misslyckas ska loggen visa det.

Om projektet saknar riktig klocka kan du använda `millis()` som relativ tid:

```text
uptime_ms,node_id,temperature_c,status
1000,3,22.6,OK
61000,3,22.7,OK
```

Det är sämre för analys över flera dagar, men mycket bättre än ingen tid alls.

## Enkel SD-logger

Här är ett grundexempel som loggar ett simulerat mätvärde till SD-kort. Exemplet är avsiktligt enkelt. I ett verkligt projekt bör du lägga till mer felhantering, strömsäkerhet och eventuellt RTC eller nätverkstid.

```cpp
#include <SPI.h>
#include <SD.h>

const int SD_CS_PIN = 10;
const char* LOG_FILE = "log.csv";

unsigned long lastSampleMs = 0;
const unsigned long SAMPLE_INTERVAL_MS = 5000;

float readTemperatureC() {
  int raw = analogRead(A0);
  float voltage = raw * (5.0 / 1023.0);
  return 20.0 + voltage;
}

void ensureHeader() {
  if (!SD.exists(LOG_FILE)) {
    File file = SD.open(LOG_FILE, FILE_WRITE);
    if (file) {
      file.println("uptime_ms,node_id,temperature_c,status");
      file.close();
    }
  }
}

void appendLogRow(unsigned long uptimeMs, uint8_t nodeId, float temperatureC, const char* status) {
  File file = SD.open(LOG_FILE, FILE_WRITE);

  if (!file) {
    Serial.println("Could not open log file");
    return;
  }

  file.print(uptimeMs);
  file.print(",");
  file.print(nodeId);
  file.print(",");
  file.print(temperatureC, 2);
  file.print(",");
  file.println(status);

  file.close();
}

void setup() {
  Serial.begin(115200);

  if (!SD.begin(SD_CS_PIN)) {
    Serial.println("SD card initialization failed");
    while (true) {
      delay(1000);
    }
  }

  ensureHeader();
  Serial.println("Logger ready");
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleMs >= SAMPLE_INTERVAL_MS) {
    lastSampleMs = now;

    float temperatureC = readTemperatureC();
    appendLogRow(now, 3, temperatureC, "OK");

    Serial.println("Sample written");
  }
}
```

Det här exemplet gör tre saker rätt:

- det skriver en rubrikrad första gången filen skapas
- det använder ett tydligt intervall i stället för att skriva i varje loop-varv
- det stänger filen efter varje rad, vilket minskar risken för dataförlust vid strömavbrott

Det gör också saker som kan förbättras:

- varje skrivning öppnar och stänger filen, vilket kan vara långsamt
- koden blockerar under SD-skrivning
- den använder bara relativ tid
- den hanterar inte full disk, dåligt kort eller tillfälliga skrivfel särskilt elegant

För många experiment är detta ändå en bra start.

## Robustare loggning

När dataloggern blir viktigare behöver du tänka mer som en systembyggare.

### Skriv inte för ofta

Om mätningen sker ofta kan du separera sampling och skrivning:

- Sampla sensor var 100 ms.
- Beräkna medelvärde över 10 sekunder.
- Skriv ett sammanfattat värde var 10:e sekund eller varje minut.

Det minskar datamängden och gör loggen mer användbar.

### Skriv status, inte bara värden

En logg utan status är svår att tolka. Om sensorn misslyckas bör raden säga det.

```text
uptime_ms,node_id,temperature_c,status
5000,3,22.60,OK
10000,3,,SENSOR_TIMEOUT
15000,3,22.71,OK
```

### Planera för strömavbrott

Om projektet kan tappa ström bör du välja strategi:

- stäng filen efter varje rad för enkel robusthet
- eller buffra data men acceptera att de senaste raderna kan försvinna
- eller använd FRAM som mellanlager och skriv till SD i batchar
- eller använd superkondensator/batteribackup för kontrollerad avstängning

Det finns ingen universallösning. För snabba tester är enkelhet ofta viktigast. För fältloggning blir robusthet viktigare.

## Displaykretsar och displaymoduler

En display är sällan bara “en skärm”. Den består ofta av flera lager:

- själva displaypanelen
- en displaykontroller
- en breakout board eller modul
- ett gränssnitt som I2C eller SPI
- ett bibliotek
- ibland en framebuffer i mikrokontrollerns RAM

En OLED-modul med SSD1306-kontroller över I2C är enkel att använda eftersom modulen döljer mycket av detaljerna. En rå TFT-panel kräver mer kunskap om kontroller, initieringssekvenser, färgformat och uppdateringsmetod.

För Arduino-projekt är displaymoduler oftast bättre än råa displaypaneler. De är enklare att koppla, har tydligare exempel och fungerar bättre på breadboard.

## I2C-display eller SPI-display

Många små OLED- och LCD-moduler finns i både I2C- och SPI-varianter.

| Egenskap | I2C-display | SPI-display |
|---|---|---|
| Antal pinnar | Få | Fler |
| Hastighet | Ofta långsammare | Ofta snabbare |
| Koppling | Enkel | Lite mer omfattande |
| Delad buss | Enkel med flera sensorer | Kräver chip select per enhet |
| Passar bäst för | text, små statusvyer | grafik, snabbare uppdatering |

I2C är ofta bäst när displayen bara visar status, mätvärden och enkla menyer. SPI är ofta bättre när displayen är större, färgad eller behöver uppdateras snabbt.

## Framebuffer och RAM

Många grafikbibliotek använder en framebuffer. Det betyder att hela eller delar av displaybilden byggs i RAM innan den skickas till displayen.

Det är bekvämt men kan bli dyrt på små kort.

En 128x64 monokrom display kräver:

```text
128 * 64 / 8 = 1024 byte
```

Det är hanterbart på många kort, men på ett AVR-baserat UNO-kort med begränsat SRAM är 1024 byte mycket.

En färgdisplay är betydligt tyngre. En 240x320-display med 16-bitars färg skulle kräva:

```text
240 * 320 * 2 = 153600 byte
```

Det är långt mer än vad ett klassiskt UNO-kort kan hålla i RAM. Därför använder många TFT-bibliotek radbuffertar, partiella uppdateringar eller direkt skrivning till displayen.

### Praktisk regel

- På små AVR-kort: välj små monokroma displayer och bibliotek med rimlig minnesanvändning.
- På ESP32, RP2040 och andra modernare kort: större displayer och grafik är mer realistiskt.
- För snabb grafik: välj SPI och kort med gott om RAM.
- För enkel status: I2C-OLED eller text-LCD räcker långt.

## Display som statusyta

En display i ett Arduino-system behöver ofta inte vara avancerad. Den kan vara en statusyta som visar:

- vilket läge systemet är i
- senaste sensorvärde
- om SD-kortet fungerar
- om nätverket är anslutet
- batteristatus
- felkod
- tid sedan start

Det är ofta mer användbart än snygg grafik.

Exempel på enkel statusmodell:

```cpp
struct SystemStatus {
  bool sdOk;
  bool sensorOk;
  bool networkOk;
  float temperatureC;
  unsigned long lastLogMs;
};

void printStatusToSerial(const SystemStatus& status) {
  Serial.println("System status");
  Serial.print("SD: ");
  Serial.println(status.sdOk ? "OK" : "ERROR");
  Serial.print("Sensor: ");
  Serial.println(status.sensorOk ? "OK" : "ERROR");
  Serial.print("Network: ");
  Serial.println(status.networkOk ? "OK" : "OFFLINE");
  Serial.print("Temperature: ");
  Serial.println(status.temperatureC);
  Serial.print("Last log ms: ");
  Serial.println(status.lastLogMs);
}
```

Samma modell kan senare visas på OLED, LCD eller webbsida. Det viktiga är att separera systemets status från själva displaybiblioteket.

## Displaydrivare

En displaydrivare är hårdvara eller mjukvara som gör att mikrokontrollern kan styra displayen utan att själv hantera varje elektrisk detalj.

Exempel på displayrelaterade kretsar och kontrollertyper:

| Typ | Exempel | Vanlig användning |
|---|---|---|
| OLED-kontroller | SSD1306, SH1106 | små monokroma OLED-displayer |
| LCD-backpack | PCF8574-baserad I2C-adapter | 16x2 och 20x4 text-LCD |
| TFT-kontroller | ILI9341, ST7735, ST7789 | färgdisplayer via SPI |
| LED-displaydrivare | MAX7219, HT16K33 | 7-segment, LED-matriser |
| E-paper-kontroller | varierar per modul | lågströmsdisplay med långsam uppdatering |

Som vanligt i Arduino-världen är modulen ofta viktigare än den lösa kretsen. Två moduler med “samma” display kan ha olika upplösning, annan kontroller, annan I2C-adress eller annan pinout.

Dokumentera därför alltid:

- displaytyp
- kontroller
- upplösning
- gränssnitt
- matningsspänning
- logiknivå
- bibliotek
- eventuella specialpinnar

## LED-displaydrivare

LED-matriser och 7-segmentsdisplayer kan drivas direkt, men det blir snabbt många pinnar och mycket multiplexering. Därför är drivkretsar som MAX7219 eller HT16K33 vanliga.

En LED-displaydrivare kan:

- multiplexa rader och kolumner
- styra ljusstyrka
- minska antalet pinnar
- förenkla kod
- ge jämnare visning

Välj LED-displaydrivare när du vill visa siffror, enkla symboler eller matrisgrafik utan att belasta mikrokontrollern med ständig multiplexering.

## Minne för display och minne för data

Det är lätt att blanda ihop minne för display och minne för datalagring, men de löser olika problem.

Displayminne används för att rita. Det kan vara:

- en framebuffer i mikrokontrollerns RAM
- displayens interna minne
- en liten radbuffert i biblioteket

Datalagring används för att spara information över tid. Det kan vara:

- EEPROM
- FRAM
- flash
- SD-kort

En datalogger med display behöver ofta båda. Displayen visar senaste status. Lagringen sparar historiken.

## Referensmönster: liten datalogger med statusdisplay

Det här referensmönstret visar en liten datalogger som:

- läser ett simulerat analogt mätvärde
- skriver mätvärdet till SD-kort
- håller en enkel statusmodell
- visar status via seriell monitor
- är förberedd för att senare kopplas till OLED eller LCD

Seriell monitor används som display i grundversionen för att hålla mönstret oberoende av exakt displaymodul. `showStatus()` kan senare bytas mot kod för en OLED eller LCD.

### Det här används i exemplet

- Ett Arduino-kompatibelt kort.
- En SD-kortmodul.
- Ett microSD-kort formaterat med lämpligt filsystem för ditt bibliotek.
- En potentiometer eller analog sensor.
- Kopplingskablar.
- Eventuellt en OLED- eller LCD-display för utbyggnad.


### Typisk loggrad med statusfält

En praktisk logg bör spara mer än bara råvärdet. Status och fel gör det möjligt att förstå datan efteråt, särskilt när projektet körs utan dator.

```text
uptime_ms,node_id,raw_value,voltage,status,error
12500,3,512,2.502,OK,
14500,3,0,0.000,SENSOR_ERROR,no_reading
16500,3,519,2.536,OK,
```

Använd helst en header-rad och ett format som kan öppnas i ett kalkylblad. Fält som ofta är värda att ha med är tid, nod-ID, råvärde, omräknat värde, status och senaste fel. Då blir loggen användbar även när displayen bara visar den senaste statusen.


### Kopplingsidé

- SD-kortmodulen kopplas via SPI.
- Potentiometern kopplas till analog ingång.
- Kortets 3,3 V/5 V-val måste matcha SD-modulen.
- Alla delar ska ha gemensam jord.

Använd kortets dokumentation för SPI-pinnarna. På UNO används ofta pinne 10 som chip select i exempel, men andra kort kan ha annan rekommenderad CS-pinne och andra fysiska SPI-pinnar.

### Kod

```cpp
#include <SPI.h>
#include <SD.h>

const int SD_CS_PIN = 10;
const int SENSOR_PIN = A0;
const uint8_t NODE_ID = 3;

const unsigned long SAMPLE_INTERVAL_MS = 2000;
const char* LOG_FILE = "data.csv";

struct SystemStatus {
  bool sdOk;
  bool sensorOk;
  unsigned long lastSampleMs;
  unsigned long lastWriteMs;
  int rawValue;
  float voltage;
  const char* lastError;
};

SystemStatus status = {
  false,
  false,
  0,
  0,
  0,
  0.0,
  "Not started"
};

unsigned long lastSampleTime = 0;

float rawToVoltage(int raw) {
  return raw * (5.0 / 1023.0);
}

void writeHeaderIfNeeded() {
  if (!SD.exists(LOG_FILE)) {
    File file = SD.open(LOG_FILE, FILE_WRITE);
    if (file) {
      file.println("uptime_ms,node_id,raw_value,voltage,status,error");
      file.close();
    }
  }
}

bool appendDataRow(unsigned long now, int rawValue, float voltage) {
  File file = SD.open(LOG_FILE, FILE_WRITE);

  if (!file) {
    status.lastError = "Could not open data.csv";
    return false;
  }

  file.print(now);
  file.print(",");
  file.print(NODE_ID);
  file.print(",");
  file.print(rawValue);
  file.print(",");
  file.print(voltage, 3);
  file.print(",");
  file.print("OK");
  file.print(",");
  file.println(status.lastError);

  file.close();
  return true;
}

void showStatus() {
  Serial.println();
  Serial.println("Status");
  Serial.print("SD: ");
  Serial.println(status.sdOk ? "OK" : "ERROR");
  Serial.print("Sensor: ");
  Serial.println(status.sensorOk ? "OK" : "ERROR");
  Serial.print("Raw value: ");
  Serial.println(status.rawValue);
  Serial.print("Voltage: ");
  Serial.println(status.voltage, 3);
  Serial.print("Last write ms: ");
  Serial.println(status.lastWriteMs);
  Serial.print("Last error: ");
  Serial.println(status.lastError);
}

void setup() {
  Serial.begin(115200);

  if (!SD.begin(SD_CS_PIN)) {
    status.sdOk = false;
    status.lastError = "SD init failed";
    showStatus();
    return;
  }

  status.sdOk = true;
  status.lastError = "OK";
  writeHeaderIfNeeded();
  showStatus();
}

void loop() {
  unsigned long now = millis();

  if (now - lastSampleTime >= SAMPLE_INTERVAL_MS) {
    lastSampleTime = now;

    status.rawValue = analogRead(SENSOR_PIN);
    status.voltage = rawToVoltage(status.rawValue);
    status.sensorOk = true;
    status.lastSampleMs = now;

    if (status.sdOk) {
      bool written = appendDataRow(now, status.rawValue, status.voltage);
      if (written) {
        status.lastWriteMs = now;
        status.lastError = "OK";
      } else {
        status.sdOk = false;
      }
    }

    showStatus();
  }
}
```

### Vad mönstret visar

Referensmönstret visar tre viktiga mönster:

- statusdata hålls i en struktur
- loggning sker med tydligt intervall
- displayen eller statusvisningen är separerad från mätning och lagring

I en senare version kan `showStatus()` rita till OLED i stället för att skriva till seriell monitor. Resten av programmet behöver då inte ändras lika mycket.

## Utbyggnad: OLED-status

Om du har en liten I2C-OLED kan du ersätta `showStatus()` med en displayfunktion. Exakt kod beror på bibliotek och displaykontroller, men strukturen bör vara densamma:

```cpp
void showStatusOnDisplay(const SystemStatus& status) {
  // Pseudokod:
  // clear display
  // print SD status
  // print sensor status
  // print latest value
  // print last error if any
  // update display
}
```

Poängen är att displayen visar statusmodellen. Den ska inte själv äga sensordata, SD-logik eller felhantering.

## När en display är bättre än loggning

Välj display när:

- användaren behöver omedelbar feedback
- projektet ska kunna användas utan dator
- felstatus behöver synas direkt
- kalibrering eller inställning görs på plats
- mätvärdet bara är intressant i stunden

Exempel: en batteritestare som visar aktuell spänning, en växthusmonitor som visar temperatur, eller en felsökningsenhet som visar I2C-adresser.

## När loggning är bättre än display

Välj loggning när:

- historik är viktig
- mätvärden ska analyseras senare
- projektet körs obevakat
- du vill se trender
- data ska jämföras mellan flera noder
- systemet ska felsökas efter att ett fel inträffat

Exempel: temperatur över en vecka, batteriförbrukning över ett dygn, händelser från en dörrsensor eller strömvariationer under motorstart.

## När du behöver både display och loggning

Många praktiska system behöver båda. En bra uppdelning är:

- Displayen visar senaste värde, status och fel.
- Loggen sparar tidsstämplad historik.
- Konfigurationen sparar inställningar.
- Seriell monitor används för utvecklingsdiagnostik.

Det ger fyra separata informationskanaler. De ska inte blandas ihop i onödan.

## Vanliga misstag

- **Misstag: Att använda EEPROM som datalogger.**
  - Varför det händer: EEPROM känns enkelt och kräver ingen extra modul.
  - Hur man undviker det: Använd EEPROM för sällan ändrad konfiguration. Använd SD-kort eller annan logglösning för mätserier.

- **Misstag: Att skriva till icke-flyktigt minne i varje loop-varv.**
  - Varför det händer: Programmet fungerar först, men slitage och prestandaproblem syns inte direkt.
  - Hur man undviker det: Skriv bara när värden ändras eller med tydliga intervall. Använd FRAM vid täta små skrivningar.

- **Misstag: Att välja en display utan att kontrollera RAM-krav.**
  - Varför det händer: Displayens upplösning ser liten ut, men biblioteket använder framebuffer.
  - Hur man undviker det: Kontrollera bibliotekets minnesmodell och jämför med kortets SRAM.

- **Misstag: Att blanda ihop displayfel med sensorfel.**
  - Varför det händer: Koden läser sensor, formaterar text och ritar display i samma funktion.
  - Hur man undviker det: Separera mätning, statusmodell, loggning och visning.

- **Misstag: Att anta att alla SD-kortmoduler är 5 V-tåliga.**
  - Varför det händer: Moduler marknadsförs ofta som Arduino-kompatibla utan tydlig elektrisk beskrivning.
  - Hur man undviker det: Kontrollera regulator, nivåanpassning och logiknivå innan koppling.

- **Misstag: Att använda långa breadboardkablar för SPI till SD-kort.**
  - Varför det händer: Kopplingen fungerar ibland på låg hastighet men blir instabil vid skrivning.
  - Hur man undviker det: Håll ledningar korta, använd gemensam jord, bra matning och sänk hastighet vid behov.

- **Misstag: Att skapa loggfiler utan rubrikrad eller enhet.**
  - Varför det händer: Fokus ligger på att få skrivningen att fungera.
  - Hur man undviker det: Skriv alltid kolumnnamn, enheter och statusfält där det passar.

## Felsökning

### SD-kortet initieras inte

Kontrollera:

- rätt chip select-pinne
- rätt SPI-pinnar för kortet
- matningsspänning
- gemensam jord
- om modulen kräver 3,3 V-logik
- om SD-kortet är formaterat på ett sätt biblioteket stöder
- om en annan SPI-enhet håller bussen aktiv

Testa först med bibliotekets enklaste SD-exempel innan du lägger till sensor, display och meny.

### Filen skapas men inga data syns

Kontrollera:

- att filen stängs eller flushas
- att du tittar på rätt filnamn
- att programmet faktiskt når skrivfunktionen
- att intervallet inte är mycket längre än du tror
- att SD-kortet inte är skrivskyddat eller fullt

Skriv även till seriell monitor vid varje lyckad loggrad under felsökning.

### Displayen visar inget

Kontrollera:

- I2C-adress eller SPI-pinnar
- matningsspänning
- kontrast eller initieringssekvens
- rätt displaykontroller i biblioteket
- att `display.display()` eller motsvarande uppdateringsfunktion faktiskt anropas
- att kortet har tillräckligt RAM

För I2C-displayer: kör I2C-scanner från kapitel 9.

### Displayen fungerar men SD-kortet slutar fungera

Om båda använder SPI kan problemet vara chip select eller bussdelning. Kontrollera:

- att varje SPI-enhet har egen CS-pinne
- att oanvända CS-pinnar hålls inaktiva
- att biblioteken inte ändrar SPI-inställningar på ett inkompatibelt sätt
- att kablarna är korta
- att matningen räcker

Om displayen använder I2C och SD-kortet SPI är problemet oftare minne, ström eller blockerande kod.

## Snabbreferens

| Teknik | Bäst för | Undvik när |
|---|---|---|
| Intern EEPROM | små inställningar på kort som stöder det | tät loggning eller stora datamängder |
| Extern EEPROM | portabel konfigurationslagring | hög skrivfrekvens eller stora loggar |
| FRAM | ofta ändrat tillstånd och robusta småloggar | mycket stora datamängder |
| Intern flash | inställningar, webbfiler, sällan ändrad data | tät datalogging utan plattformsanalys |
| SD-kort | stora loggar och flyttbara filer | mycket enkla system eller extremt strömsnåla projekt |
| I2C-display | enkel status och små menyer | snabb grafik eller stora färgdisplayer |
| SPI-display | snabbare grafik och större displayer | när få pinnar och enkel koppling är viktigast |
| LED-displaydrivare | 7-segment och LED-matriser | när du behöver full grafik eller text |

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V för SD och många minneskretsar |
| Typiskt gränssnitt | I2C, SPI eller SD-gränssnitt |
| Välj när | mätdata, konfiguration eller historik behöver sparas |
| Välj inte när | RAM eller seriell logg räcker |
| Vanliga fel | för många skrivningar, saknad filstängning, nivåproblem med SD |
| Alternativ att överväga | EEPROM, FRAM, SD-kort, intern flash |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När displaykrets eller minne inte svarar, börja med busskontrollen i kapitel 9.
- När många moduler delar samma buss eller adressutrymme, jämför med kapitel 30.
- När data ska visas, lagras och kopplas till tid eller identitet, gå vidare till kapitel 29.
- När problemet först syns efter lång körning, använd felsökningsmönstren i kapitel 35.

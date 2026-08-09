# 9. Kommunikation: UART, I2C, SPI och 1-Wire

## Kommunikationsval i praktiken
När ett Arduino-projekt växer räcker det sällan med enstaka digitala och analoga pinnar. Du vill läsa flera sensorer, visa information på en display, logga data på ett SD-kort, prata med en GPS-modul, styra en drivkrets eller koppla ihop två mikrokontrollers. Då blir kommunikationsbussar ett av de viktigaste verktygen.

Det här kapitlet handlar om fyra mycket vanliga sätt att låta Arduino-kompatibla kort prata med andra kretsar:

- UART
- I2C
- SPI
- 1-Wire

De löser olika problem. UART är ofta rätt när två enheter ska prata punkt till punkt, till exempel ett kort och en GPS-modul. I2C är ofta rätt när flera sensorer ska dela två ledningar på kort avstånd. SPI är ofta rätt när data ska flyttas snabbt, till exempel till en display eller ett SD-kort. 1-Wire är specialiserat men praktiskt, framför allt för DS18B20-liknande temperatursensorer där många sensorer kan sitta på samma dataledning.

Som erfaren programmerare kan du tänka på en buss ungefär som ett API mellan hårdvara. Det finns ett protokoll, timingregler, adresser eller chip select-signaler, felmoder och ibland bibliotek som döljer detaljerna. Skillnaden är att hårdvaru-API:et också påverkas av kabellängd, pull-up-motstånd, spänningsnivåer, brus, jordning och exakt vilka pinnar kortet använder.

Målet med kapitlet är inte att du ska memorera varje elektrisk detalj. Målet är att du ska kunna välja rätt buss, koppla den rimligt säkert, känna igen vanliga fel och skriva testkod som snabbt visar om problemet ligger i mjukvara, bibliotek, koppling eller komponentval.

I praktiken använder du kapitlet som stöd när du ska välja mellan UART, I2C, SPI och 1-Wire, kontrollera spänningsnivåer och pinnar, hitta en I2C-adress, resonera om pull-up-motstånd, baud rate eller chip select och felsöka kommunikationsproblem med minimal testkod innan modulen byggs in i ett större system.

## Förutsättningar

Det här kapitlet bygger vidare på tidigare kapitel:

- från kapitel 4: spänningsnivåer, common ground, pull-up-motstånd och kabellängd
- från kapitel 5: digitala signaler, HIGH, LOW och flytande ingångar
- från kapitel 7: timing, icke-blockerande kod och varför `delay()` kan störa responsivitet
- från kapitel 8: händelser, robust körning och varför korta testfall gör felsökning lättare

Du behöver inte kunna elektronik på konstruktörsnivå. Däremot bör du vara bekväm med att läsa ett datablad eller en modulbeskrivning och hitta följande information:

- matningsspänning
- logiknivå
- kommunikationsgränssnitt
- pinnar
- standardadress eller hastighet
- rekommenderat bibliotek

Om du är osäker på en modul är det bättre att börja med låg hastighet, korta kablar och en minimal testsketch än att direkt bygga in den i ett större projekt.

## Kommunikationsbussar som praktiskt designval

En kommunikationsbuss är en gemensam uppsättning regler för hur data flyttas mellan kretsar. I Arduino-världen möter du ofta bussar genom bibliotek. Du inkluderar ett bibliotek, skapar ett objekt och anropar metoder som `begin()`, `read()` eller `write()`. Det kan få kommunikationen att se enkel ut.

Men bakom biblioteket finns alltid några praktiska designfrågor:

- Hur många ledningar behövs?
- Kan flera enheter dela samma ledningar?
- Behövs adress, chip select eller separat port?
- Vilken hastighet är rimlig?
- Vilken logiknivå använder enheterna?
- Vilka pinnar på kortet stöder gränssnittet?
- Hur långa kablar fungerar i praktiken?
- Finns det bibliotek för just den kortfamilj du använder?

Ett vanligt misstag är att börja i fel ände: man hittar ett bibliotek och antar att hårdvaran därmed fungerar. Ett bättre arbetssätt är att först identifiera buss och elektriska krav, därefter testa bussen med minimal kod och först sedan bygga funktionaliteten.

## Snabb jämförelse

| Buss | Typiska ledningar | Flera enheter | Typisk användning | Styrka | Vanlig fallgrop |
|---|---:|---|---|---|---|
| UART | TX, RX, GND | Vanligen punkt-till-punkt | GPS, seriella moduler, debug | Enkel och robust | TX/RX korsas fel eller baud rate stämmer inte |
| I2C | SDA, SCL, GND | Ja, med adresser | Sensorer, RTC, små displayer, I/O-expanders | Många enheter på två signaler | Saknade pullups, adresskonflikt eller för långa kablar |
| SPI | SCK, MOSI, MISO, CS, GND | Ja, med separat CS | SD-kort, TFT, snabba ADC/DAC, radio | Hög hastighet och tydlig signalering | Fel chip select eller pinout |
| 1-Wire | DATA, GND, ofta VCC | Ja, med unika ID | DS18B20-temperatursensorer | Många sensorer på enkel kabel | Pullup, kabellängd och timingproblem |

Tabellen är en förenkling, men den är användbar som första valguide. Om du vill ansluta många små sensorer på ett kort avstånd är I2C ofta enklast. Om du vill ansluta en GPS-modul är UART naturligt. Om du ska driva en snabb display eller logga till SD-kort är SPI ofta rätt. Om du ska läsa flera DS18B20-sensorer över en enkel kabel är 1-Wire ett bra specialfall.

## Namn på roller

Äldre dokumentation använder ofta orden master och slave. Nyare dokumentation använder allt oftare controller och peripheral, eller host och device. I praktiska Arduino-sammanhang kommer du fortfarande att se båda uppsättningarna.

I den här boken använder vi främst:

- controller: enheten som initierar kommunikationen
- peripheral: enheten som svarar
- transmitter: enhet som skickar data
- receiver: enhet som tar emot data

När bibliotek eller datablad använder äldre termer behöver du kunna känna igen dem. Det viktigaste är inte terminologin utan vem som styr klocka, vem som har adress och vilken enhet som får prata när.

## UART

UART står för Universal Asynchronous Receiver/Transmitter. Det är ett seriellt gränssnitt där data skickas bit för bit utan en separat klockledning. Båda sidor måste vara överens om hastighet och format.

De vanligaste signalerna är:

- TX: transmit, skickar data
- RX: receive, tar emot data
- GND: gemensam jord

Ofta behöver du korsa TX och RX:

- kortets TX går till modulens RX
- kortets RX går till modulens TX
- GND kopplas till GND

Detta är så vanligt att det också är en av de vanligaste felkopplingarna.

### När UART passar

UART passar bra när två enheter ska prata direkt med varandra. Vanliga exempel är:

- GPS/GNSS-moduler
- Bluetooth-seriella moduler
- vissa CO2-sensorer
- vissa fingeravtrycksläsare
- seriell debug mellan två mikrokontrollers
- modem och kommunikationsmoduler
- industriella moduler med TTL-seriell port

UART är lätt att förstå, lätt att logga och kräver få ledningar. Den är ofta mer förlåtande än I2C över något längre kablar, men den saknar inbyggd adressering för många enheter på samma buss.

### När något annat passar bättre

UART är mindre smidig när du vill ansluta många sensorer till samma kort. Varje UART-länk vill i praktiken ha en egen port eller någon form av multiplexing. Många klassiska Arduino-kort har bara en hårdvaru-UART, och den används ofta även av USB-seriell kommunikation till datorn.

Välj hellre I2C när du har många små sensorer med unika adresser. Välj SPI när du behöver hög hastighet till display, minne eller snabb datainsamling.

### Baud rate

Eftersom UART saknar separat klockledning måste båda sidor använda samma baud rate. Vanliga hastigheter är:

- 9600 baud
- 19200 baud
- 38400 baud
- 57600 baud
- 115200 baud

Om baud rate är fel får du ofta skräptecken i seriell monitor eller ingen begriplig data alls.

En typisk start för seriell debug är:

```cpp
void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // Vänta på seriell port på kort där det behövs.
  }

  Serial.println("UART test started");
}

void loop() {
  Serial.println("Hello from Arduino");
  delay(1000);
}
```

På vissa kort är `while (!Serial)` praktiskt när USB-seriell port behöver tid att öppnas. På andra kort kan det blockera programmet om ingen seriell monitor ansluts. I test är det ofta bra, men i fristående projekt bör du vara försiktig.

### Hårdvaru-UART och mjukvaru-UART

En hårdvaru-UART är en periferienhet i mikrokontrollern som sköter seriell sändning och mottagning effektivt. En mjukvaru-UART emulerar samma beteende i kod.

Klassiska Arduino UNO har en hårdvaru-UART som också används av USB-seriell kommunikation. Arduino Mega har flera hårdvaru-UART:ar. ESP32-kort har normalt flera UART-möjligheter, men exakt pinout och användning beror på kort och core. På enklare AVR-kort används ofta `SoftwareSerial` när man behöver en extra seriell port, men det har begränsningar i hastighet, timing och samtidighet.

Som grundregel:

- använd hårdvaru-UART om den finns
- använd mjukvaru-UART bara när projektet är enkelt och hastigheten låg
- undvik att kombinera timingkänslig kod, många interrupts och mjukvaru-UART om du kan
- dokumentera tydligt vilka pinnar som används för seriell kommunikation

### Exempel: läsa en GPS-liknande seriell modul

Det här exemplet visar ett generellt mönster: ta emot textbaserad data från en seriell modul och skriv vidare till datorn. Exemplet använder en extra seriell port som heter `Serial1`, vilket finns på vissa kort men inte alla.

```cpp
void setup() {
  Serial.begin(115200);
  Serial1.begin(9600);

  Serial.println("Serial bridge started");
}

void loop() {
  while (Serial1.available() > 0) {
    char c = Serial1.read();
    Serial.write(c);
  }
}
```

På ett kort utan `Serial1` behöver du använda rätt hårdvaruport, ett mjukvaruseriellt bibliotek eller välja ett kort med fler UART:ar. Det är ett typiskt exempel på varför kortval spelar roll.

## I2C

I2C, ofta skrivet I²C, är en tvåtrådsbuss för kommunikation mellan en controller och en eller flera peripherals. De två signalerna är:

- SDA: data
- SCL: clock

Dessutom behövs gemensam jord, och enheterna måste ha kompatibla logiknivåer.

I Arduino-kod används ofta biblioteket `Wire`.

```cpp
#include <Wire.h>

void setup() {
  Wire.begin();
}

void loop() {
}
```

I2C är ett av de vanligaste gränssnitten för sensorer och små moduler. Du hittar det i miljösensorer, realtidsklockor, I/O-expanders, små OLED-displayer, ADC-kretsar, DAC-kretsar och många andra komponenter.

### Varför I2C är så praktiskt

I2C är populärt eftersom många enheter kan dela samma två signalledningar. Varje enhet har en adress. När controllern vill prata med en viss enhet skickar den adressen först, och bara den enheten svarar.

Det gör I2C mycket praktiskt för projekt som:

- en miljöstation med flera sensorer
- en liten display och en RTC på samma buss
- ett mätkort med I/O-expander och ADC
- en prototyp där du vill lägga till moduler utan att förbruka många pinnar

Med I2C kan ett kort med få pinnar ändå prata med många komponenter.

### Pull-up-motstånd

I2C-signaler drivs normalt inte aktivt både högt och lågt på samma sätt som en vanlig digital utgång. Enheter drar signalen låg, medan pull-up-motstånd drar signalen hög när ingen drar den låg. Därför behöver SDA och SCL pull-up-motstånd.

Många breakout boards har redan pullups monterade. Det är praktiskt, men kan också skapa problem om du kopplar många moduler parallellt och därmed får för stark sammanlagd pullup.

Typiska symptom på I2C-problem är:

- I2C-scanner hittar ingen enhet
- enheten hittas ibland men inte alltid
- kommunikationen fungerar med korta kablar men inte med längre
- bussen låser sig efter några läsningar
- värden är orimliga eller uppdateras inte

När I2C beter sig konstigt bör du kontrollera:

- att SDA och SCL inte är förväxlade
- att GND är gemensam
- att spänningsnivåerna är kompatibla
- att pullups finns
- att pullups inte är för starka när många moduler är inkopplade
- att adresserna inte krockar
- att kablarna är korta nog för vald hastighet

### I2C-adresser

Varje I2C-enhet har en adress. Många moduler har en standardadress, ibland med möjlighet att ändra en eller två adressbitar genom lödbryggor eller adresspinnar.

Adresskonflikt uppstår när två enheter på samma buss har samma adress. Då kan controllern inte skilja dem åt.

Det finns flera lösningar:

- välj moduler där adressen kan ändras
- använd en I2C-multiplexer
- placera enheterna på olika I2C-bussar om kortet stödjer det
- välj en annan sensormodell med annan adress
- använd SPI-version av komponenten om sådan finns

Adresskonflikter är en vanlig anledning att två moduler fungerar var för sig men inte tillsammans.

### I2C-scanner

En I2C-scanner är ett av de bästa första felsökningsverktygen. Den försöker kontakta adresser på bussen och skriver ut vilka som svarar.

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ;
  }

  Wire.begin();
  Serial.println("I2C scanner started");
}

void loop() {
  byte foundDevices = 0;

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Found I2C device at 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.println(address, HEX);
      foundDevices++;
    }
  }

  if (foundDevices == 0) {
    Serial.println("No I2C devices found");
  } else {
    Serial.print("Devices found: ");
    Serial.println(foundDevices);
  }

  delay(3000);
}
```

Kör gärna scannern innan du testar ett sensorspecifikt bibliotek. Om scannern inte hittar modulen är det sällan bibliotekets högre nivå som är problemet.

### I2C-hastighet

Vanliga I2C-hastigheter är 100 kHz och 400 kHz. Vissa enheter och kort stödjer högre hastigheter, men i praktiska Arduino-projekt är 100 kHz ofta en bra start, särskilt med längre kablar eller flera moduler.

I vissa miljöer kan du sätta hastigheten med:

```cpp
Wire.setClock(100000);
```

eller:

```cpp
Wire.setClock(400000);
```

Välj inte högre hastighet bara för att det går. Sensorer som uppdateras några gånger per sekund vinner sällan mycket på snabbare I2C, medan felsökningskostnaden kan öka.

### Flera I2C-bussar

Vissa kort har stöd för mer än en I2C-buss eller kan mappa I2C till olika pinnar. Detta är vanligt på mer avancerade kortfamiljer, men syntax och stöd varierar.

När du skriver kod som ska vara portabel mellan kort bör du:

- samla I2C-pinnar och businställningar i konfiguration
- undvika hårdkodade antaganden om SDA/SCL
- kommentera vilken kortfamilj exemplet är testat med
- börja med standardbussen om inget annat behövs

## SPI

SPI står för Serial Peripheral Interface. Det är en snabb synkron buss där controllern normalt styr klockan. De vanligaste signalerna är:

- SCK: serial clock
- MOSI: controller out, peripheral in
- MISO: controller in, peripheral out
- CS eller SS: chip select
- GND

SPI använder fler ledningar än I2C, men är ofta snabbare och enklare elektriskt för korta avstånd. Flera enheter kan dela SCK, MOSI och MISO, men varje enhet behöver normalt en egen chip select-signal.

### När SPI passar

SPI passar bra för komponenter som behöver flytta mer data:

- TFT-displayer
- OLED-displayer med SPI
- SD-kortmoduler
- externa flashminnen
- vissa radiomoduler
- snabba ADC- och DAC-kretsar
- Ethernet-moduler
- LED- eller displaydrivare

SPI är också vanligt när timing och datahastighet är viktigare än att spara pinnar.

### När något annat passar bättre

Välj I2C om du har många långsamma sensorer och vill spara pinnar. Välj UART om du pratar med en modul som skickar en kontinuerlig textström. Välj 1-Wire om du använder DS18B20-liknande temperatursensorer.

SPI kräver mer pinplanering. Om du kopplar många SPI-enheter behöver du tillräckligt många chip select-pinnar och tydlig dokumentation.

### Chip select

Varje SPI-enhet behöver normalt en egen chip select-pinne. När CS är inaktiv ska enheten ignorera trafiken på bussen. När CS är aktiv lyssnar just den enheten.

### Praktiskt SPI-mönster: en buss, flera chip select

Ett vanligt SPI-upplägg är att flera enheter delar `SCK`, `MOSI` och `MISO`, men har varsin CS-pinne. Det gör att en display, ett minneskort och en annan SPI-modul kan sitta på samma buss utan att prata samtidigt.

```cpp
const int CS_DISPLAY = 10;
const int CS_MEMORY = 9;

void selectDevice(int csPin) {
  digitalWrite(CS_DISPLAY, HIGH);
  digitalWrite(CS_MEMORY, HIGH);
  digitalWrite(csPin, LOW);
}

void releaseSpiBus() {
  digitalWrite(CS_DISPLAY, HIGH);
  digitalWrite(CS_MEMORY, HIGH);
}
```

Kontrollera särskilt detta när SPI beter sig konstigt:

- bara en CS-pinne ska vara aktiv åt gången
- alla CS-pinnar bör ha ett definierat viloläge
- modulerna måste tåla samma logiknivå
- bibliotek kan anta egna standardpinnar
- en lång eller slarvig koppling kan ge fel som ser ut som kodproblem

### SPI-inställningar

SPI-kommunikation har flera inställningar:

- klockhastighet
- bitordning
- SPI mode, som beskriver klockpolaritet och fas

Många bibliotek hanterar detta åt dig. När flera SPI-enheter delar buss är det viktigt att varje bibliotek ställer in bussen korrekt innan det pratar med sin enhet.

I egen kod kan du se mönster som:

```cpp
#include <SPI.h>

const int csPin = 10;

void setup() {
  pinMode(csPin, OUTPUT);
  digitalWrite(csPin, HIGH);

  SPI.begin();
}

void loop() {
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));

  digitalWrite(csPin, LOW);
  byte response = SPI.transfer(0x00);
  digitalWrite(csPin, HIGH);

  SPI.endTransaction();

  delay(1000);
}
```

Det här är inte kod för en specifik sensor. Det visar bara grundmönstret: starta transaktion, aktivera CS, överför data, avaktivera CS och avsluta transaktion.

### SPI och kortfamiljer

På klassiska Arduino-kort finns SPI ofta på fasta pinnar och på ICSP-headern. På ESP32- och RP2040-baserade kort kan det finnas flera SPI-bussar eller mer flexibel pinmappning, men bibliotekens stöd varierar.

För att minska problem:

- kontrollera kortets pinout
- använd standardpinnar när du kan
- ange egna pinnar bara när biblioteket stödjer det
- undvik att dela SPI med en display och ett SD-kort utan att förstå CS-hanteringen
- börja med en SPI-enhet i taget

## 1-Wire

1-Wire är en buss där data kan skickas över en enda dataledning plus jord. Ofta används även separat matning, även om vissa komponenter stöder parasitic power.

I Arduino-sammanhang är 1-Wire mest känt genom DS18B20-temperatursensorer. Varje sensor har ett unikt ID, vilket gör att flera sensorer kan sitta på samma dataledning.

### När 1-Wire passar

1-Wire passar särskilt bra när du vill läsa flera temperatursensorer med få pinnar. Exempel:

- temperaturmätning på flera platser i en låda
- växthus eller akvarium
- värmesystem på lågspänningssidan
- enklare övervakning av rör, kylflänsar eller batteripack

Det är inte en generell ersättning för I2C eller SPI. Det är mer ett specialiserat gränssnitt för vissa komponentfamiljer.

### Pull-up och kablar

Precis som I2C behöver 1-Wire en pull-up på dataledningen. Ett vanligt värde är 4,7 kΩ, men praktiska system kan kräva anpassning beroende på kabellängd och antal sensorer.

Vanliga problem är:

- sensorer hittas ibland men inte alltid
- bara en sensor hittas när flera är inkopplade
- mätvärden blir orimliga
- bussen fungerar på breadboard men inte med längre kabel
- parasitic power fungerar sämre än väntat

Som grundregel är separat matning ofta enklare och mer robust än parasitic power i test.

### Exempelstruktur för DS18B20

Det här är en typisk struktur med biblioteken `OneWire` och `DallasTemperature`. Exakt installation av bibliotek sker i utvecklingsmiljön.

```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

const int oneWirePin = 2;

OneWire oneWire(oneWirePin);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  sensors.begin();

  Serial.print("Devices found: ");
  Serial.println(sensors.getDeviceCount());
}

void loop() {
  sensors.requestTemperatures();

  float temperatureC = sensors.getTempCByIndex(0);

  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.println(" C");

  delay(2000);
}
```

I ett mer robust projekt bör du inte bara läsa index 0 och anta att rätt sensor sitter där. Använd sensorns unika adress när ordningen spelar roll.

## Spänningsnivåer och nivåskiftning

Kommunikation fungerar bara om enheterna tolkar HIGH och LOW på kompatibla sätt. Många klassiska Arduino-kort använder 5 V-logik. Många moderna sensorer, ESP-kort och RP2040-baserade kort använder 3,3 V-logik.

Det betyder inte automatiskt att allt går sönder, men det betyder att du måste kontrollera nivåerna.

Särskilt viktigt:

- En 3,3 V-modul kan skadas av 5 V-signaler.
- En 5 V-enhet kanske inte alltid tolkar 3,3 V som HIGH, även om det ofta fungerar i praktiken för vissa kretsar.
- I2C med pullups till 5 V kan vara farligt för 3,3 V-enheter.
- SPI-signaler från ett 5 V-kort till ett 3,3 V-SD-kort behöver ofta nivåanpassning.
- UART mellan 5 V och 3,3 V kräver samma eftertanke som annan digital kommunikation.

En nivåskiftare är inte ett tecken på överdriven försiktighet. Den är ofta det som gör skillnaden mellan en stabil prototyp och ett intermittent fel.

För I2C är en liten MOSFET-baserad logic level converter ofta det praktiska standardvalet när en 5 V-sida och en 3,3 V-sida måste dela buss. Koppla då lågspänningssidan till 3,3 V, högspänningssidan till 5 V och se till att båda sidor har gemensam jord. Kontrollera också modulernas egna pull-up-motstånd; flera moduler kan tillsammans ge för stark pull-up och göra bussen svår att felsöka.

## Kabellängd, brus och praktiska gränser

Datablad beskriver ofta idealfall. Breadboard, Dupont-kablar och långa sladdar är inte idealfall.

Som praktiska tumregler:

- Börja alltid med korta kablar när du testar en ny buss.
- Lägg GND tillsammans med signalerna.
- Håll I2C kort, särskilt vid 400 kHz.
- Sänk I2C-hastigheten vid problem.
- För SPI: håll kablar korta och undvik långa oterminerade ledningar vid hög hastighet.
- För UART: kontrollera baud rate och signalnivå innan du misstänker bibliotek.
- För 1-Wire: testa först med en sensor nära kortet innan du bygger en lång sensorsträng.
- Undvik att dra kommunikationskablar nära motorer, reläer och andra störkällor.

Om ett projekt fungerar på bordet men inte i lådan är det ofta kablage, strömförsörjning eller jordning som har ändrats, inte koden.

## När Wi-Fi och BLE inte är rätt val

Wi-Fi och BLE är praktiska när projektet behöver nätverk, mobilapp eller internetkoppling, men de är inte alltid bästa valet. I många Arduino-projekt vill du bara skicka några få värden mellan två noder, styra något på avstånd, dra kommunikation över längre kabel eller prata med ett fordonssystem. Då kan enklare radio- eller fältbussmoduler vara mer rimliga.

| Modul eller buss | Passar bäst när | Se upp med |
|---|---|---|
| nRF24L01 | Flera små noder ska skicka korta datapaket på kort till medellångt avstånd | Kräver stabil 3,3 V-matning, ofta extra kondensator nära modulen |
| 433 MHz RF | Enkel fjärrsignal eller mycket enkel envägskommunikation | Ofta begränsad återkoppling, störningar och varierande räckvidd |
| RS485 | Flera noder ska prata över längre kabel i störigare miljö | Kräver transceiver, terminering, gemensam referens och genomtänkt protokoll |
| CAN | Robust kommunikation i fordon, robotar eller system med flera noder | Kräver CAN-kontroller/transceiver och förståelse för bussens meddelandemodell |
| LoRa | Mycket lång räckvidd med små datamängder och låg uppdateringstakt | Låg bandbredd, regulatoriska begränsningar och längre sändtider |

En praktisk tumregel är att välja den enklaste kommunikation som löser problemet. Behöver du bara fjärrstyra ett relä på några meter är Wi-Fi ofta onödigt. Behöver du logga data från flera sensornoder utomhus kan LoRa vara mer relevant. Behöver du flera mikrokontrollers i en kapsling kan I2C, SPI eller UART räcka. Behöver du robust kabel över längre avstånd är RS485 ofta ett bättre första val än långa I2C-kablar.

### nRF24L01

nRF24L01 är en billig 2,4 GHz-radiomodul som ofta används för små sensornoder, fjärrkontroller och enkla nät av mikrokontrollers. Den är attraktiv eftersom den är billig och snabb nog för många hobbyprojekt.

Den vanligaste fallgropen är matningen. Modulen använder 3,3 V och kan vara känslig för spänningsdippar. Många problem som ser ut som kodfel beror i praktiken på för svag 3,3 V-regulator, långa kablar eller avsaknad av kondensator nära modulen.

### 433 MHz-moduler

433 MHz-sändare och mottagare är vanliga i enkla fjärrkontroller, väderstationer och billiga kit. De passar bäst när informationen är enkel och när du kan acceptera att kommunikationen inte är lika robust som en modern tvåvägslänk.

Använd dem inte som första val för kritiska styrningar. De är bättre som enkla signalmoduler än som generell datakommunikation.

### RS485

RS485 är inte ett protokoll utan ett elektriskt gränssnitt för robust seriell kommunikation över kabel. Det används ofta när signaler behöver gå längre än vad UART, I2C eller SPI klarar praktiskt.

För Arduino-projekt används RS485 ofta med en transceivermodul och ett enkelt seriellt protokoll ovanpå. Det viktiga är att tänka på terminering, kabeldragning, gemensam referens och att bara en nod sänder åt gången om bussen är halvduplex.

### CAN

CAN är byggt för robust kommunikation mellan flera noder, särskilt i fordon och industriella system. För Arduino-projekt krävs normalt en CAN-kontroller eller ett kort med inbyggt CAN-stöd samt en CAN-transceiver.

CAN är överdrivet för en enkel sensor på skrivbordet, men mycket intressant när flera noder ska dela status och kommandon i ett mer robust system.

### LoRa

LoRa passar när du vill skicka små datamängder långt, till exempel från en batteridriven sensor utomhus. Det är inte ett snabbt nätverk och ska inte behandlas som Wi-Fi med längre räckvidd.

LoRa är ofta rätt när räckvidd och låg energiförbrukning är viktigare än bandbredd och låg fördröjning.


## Felsökningsmetod

När en buss inte fungerar, felsök från det enklaste till det mest specifika.

### Steg 1: Kontrollera det fysiska

Kontrollera:

- VCC till rätt spänning
- GND gemensam
- rätt pinnar
- inga lösa kablar
- rätt orientering på modul
- inga uppenbara kortslutningar
- modulen blir inte varm

Mät gärna spänningen på modulen, inte bara vid Arduino-kortet.

### Steg 2: Identifiera bussen

Fråga:

- Är modulen UART, I2C, SPI, 1-Wire eller något annat?
- Har den flera lägen?
- Behöver den särskilda pinnar för adress, mode eller boot?
- Är pinout på breakout-kortet samma som i biblioteksexemplet?

Många moduler finns i flera varianter med liknande namn men olika gränssnitt.

### Steg 3: Kör minimal testkod

Använd:

- I2C-scanner för I2C
- seriell brygga eller enkel `available()`-läsning för UART
- bibliotekets enklaste exempel för SPI-enheter
- sensorupptäckt för 1-Wire

Bygg inte vidare förrän minimal testkod fungerar.

### Steg 4: Isolera en enhet i taget

Koppla bort allt utom den aktuella modulen. Om den fungerar ensam men inte tillsammans med andra, misstänk:

- adresskonflikt
- chip select-konflikt
- strömförsörjningsproblem
- bibliotek som ändrar busshastighet
- pin-krock
- för stark eller för svag pullup
- för långa kablar

### Steg 5: Titta på signalen

En billig logikanalysator kan vara extremt värdefull. Den kan visa:

- om det kommer klockpulser
- om data faktiskt skickas
- vilken adress som används på I2C
- om UART har rätt baud rate
- om chip select går LOW vid rätt tillfälle
- om en buss är låst låg

Du behöver inte använda logikanalysator från början, men den är ett bra nästa steg när seriella utskrifter inte räcker.

## Vanliga misstag

- **Misstag: Att glömma gemensam jord.**
  - Varför det händer: Man fokuserar på TX/RX, SDA/SCL eller andra signaler och glömmer referensnivån.
  - Hur du undviker det: Koppla alltid GND mellan enheter som ska kommunicera, om de inte är galvaniskt isolerade.

- **Misstag: Att koppla TX till TX och RX till RX på UART.**
  - Varför det händer: Namnen läses ur den egna enhetens perspektiv.
  - Hur du undviker det: Kom ihåg att sändning på ena sidan ska gå till mottagning på andra sidan.

- **Misstag: Att anta att alla I2C-moduler har unika adresser.**
  - Varför det händer: Varje modul fungerar ensam på bänken.
  - Hur du undviker det: Kör I2C-scanner med alla moduler inkopplade och kontrollera adresser tidigt.

- **Misstag: Att ha pullups till fel spänning.**
  - Varför det händer: Breakout boards kan redan ha pullups monterade till modulens VCC.
  - Hur du undviker det: Kontrollera var pullups sitter och vilken spänning bussen dras upp till.

- **Misstag: Att blanda 5 V och 3,3 V utan nivåskiftning.**
  - Varför det händer: Det råkade fungera i ett tidigare projekt.
  - Hur du undviker det: Kontrollera logiknivåer som en del av kopplingsschemat, inte som eftertanke.

- **Misstag: Att flera SPI-enheter är valda samtidigt.**
  - Varför det händer: CS-pinnar flyter vid start eller initieras för sent.
  - Hur du undviker det: Sätt alla CS-pinnar som utgångar och HIGH tidigt i `setup()`.

- **Misstag: Att felsöka bibliotek innan hårdvaran är bekräftad.**
  - Varför det händer: Felmeddelandet syns i koden, medan kopplingsfelet är fysiskt.
  - Hur du undviker det: Kör minimal busstestkod först.

## Referensmönster: två I2C-enheter på samma buss

Det här referensmönstret använder I2C för att visa flera viktiga bussidéer: gemensamma ledningar, adresser, pullups och modulär kod.

### Vad mönstret visar

Mönstret visar hur två I2C-enheter kan anslutas på samma buss, hur adresser hittas och hur du bygger ett enkelt program som visar att båda kan användas utan konflikt.

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- två I2C-moduler, till exempel en OLED-display och en miljösensor, eller två sensorer med olika adresser
- kopplingskablar
- eventuell breadboard
- dator med Arduino IDE eller motsvarande miljö

### Koppling

Koppla:

- kortets SDA till SDA på båda modulerna
- kortets SCL till SCL på båda modulerna
- 3,3 V eller 5 V till VCC beroende på modulernas krav
- GND till GND på båda modulerna

Välj inte matningsspänning genom gissning. Kontrollera modulerna. Om en modul är 3,3 V-only ska du inte mata den med 5 V.

### Kör I2C-scanner

Använd scannern tidigare i kapitlet. Skriv gärna ned adresserna medan du felsöker:

| Modul | Förväntad adress | Hittad adress | Kommentar |
|---|---|---|---|
| Modul A | 0x__ | 0x__ |  |
| Modul B | 0x__ | 0x__ |  |

Om bara en modul hittas, koppla ur den som hittas och testa den andra ensam. Om båda hittas var för sig men inte tillsammans kan det vara adresskonflikt, pullup-problem eller strömförsörjning.

### Testa en modul i taget

Kör bibliotekets enklaste exempel för modul A. Kör sedan bibliotekets enklaste exempel för modul B.

Ändra inget annat samtidigt. Poängen är att bekräfta att varje modul fungerar ensam.

### Kombinera försiktigt

Skapa en sketch där båda biblioteken initieras. Håll första kombinerade testet enkelt:

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ;
  }

  Wire.begin();

  Serial.println("Combined I2C test");
  Serial.println("Initialize module A here");
  Serial.println("Initialize module B here");
}

void loop() {
  Serial.println("Read module A here");
  Serial.println("Read module B here");

  delay(1000);
}
```

Lägg in riktig bibliotekskod steg för steg. Efter varje ändring bör det vara tydligt vilken ändring som fick något att sluta fungera.

### Kontrollera detta

- Båda modulerna hittas av scannern.
- Adresserna krockar inte.
- Matningsspänningen passar båda modulerna.
- Pullups finns, men inte i orimligt många parallella moduler.
- Systemet fungerar med den kabellängd som projektet faktiskt ska använda.
- Varje modul fungerar ensam innan du felsöker den kombinerade sketchen.

## Referensmönster: UART-loopback

Det här korta testet kontrollerar UART-tänkande utan extern modul. Det passar bara på kort där du kan använda en seriell port utan att störa uppladdning eller USB-kommunikation, eller där du har tillgång till en extra UART.

### Vad testet visar

Testet visar att data som skickas från TX kan tas emot på RX när de kopplas ihop. Det bekräftar att port, baud rate och grundläggande seriell kod fungerar.

### Grundidé

Koppla TX till RX på samma seriella port enligt kortets dokumentation. Var försiktig så du inte kortsluter fel pinnar eller stör USB-uppladdning på klassiska kort.

Ett generellt exempel:

```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("Type text in the serial monitor");
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    Serial.print("Received: ");
    Serial.println(c);
  }
}
```

För en riktig loopback på en extra port behöver du använda den portens objekt, till exempel `Serial1`, och koppla dess TX till RX. Exakt kod beror på kortet.

### Kontrollera detta

- Använd rätt UART för kortet.
- Kontrollera om porten delas med USB eller uppladdning.
- Använd samma baud rate i båda ändar.
- Kontrollera vad som händer om baud rate ändras på ena sidan men inte den andra.
- Kontrollera om kortet har flera hårdvaru-UART:ar.

## Snabbreferens

| Fråga | Rekommendation |
|---|---|
| Många långsamma sensorer nära kortet | Börja med I2C |
| En GPS eller seriell modul | Börja med UART |
| Display, SD-kort eller snabb dataöverföring | Börja med SPI |
| Flera DS18B20-temperatursensorer | Börja med 1-Wire |
| Okänd I2C-modul | Kör I2C-scanner |
| Skräptecken på seriell port | Kontrollera baud rate och TX/RX |
| I2C fungerar ibland | Kontrollera pullups, kablar, adress och spänning |
| SPI-enheter stör varandra | Kontrollera chip select och initiering |
| 3,3 V-modul med 5 V-kort | Kontrollera behov av nivåskiftning |
| Problem efter att fler moduler kopplats in | Isolera en enhet i taget |

## Begreppsförklaring: nivåskiftning och bussdisciplin

**Nivåskiftning**, eller **level shifting**, används när två enheter arbetar med olika logiknivåer, till exempel 5 V och 3,3 V. Det räcker inte alltid att signalen verkar fungera på labbbänken; långsiktig robusthet kräver att ingångar inte utsätts för högre spänning än de är avsedda för.

Med **bussdisciplin** menas att alla enheter på en delad kommunikationsbuss följer samma elektriska och tidsmässiga regler: rätt pullups, rimlig kabellängd, unika adresser där det krävs och inga enheter som driver linjen på fel sätt.

## Relaterat

- När en modul inte hittas på I2C eller SPI, börja med bussens adress, ledningar och spänningsnivå innan du misstänker biblioteket.
- När flera display-, minnes- eller I/O-moduler delar buss, jämför med kapitel 30 och 32.
- När problemet egentligen handlar om 5 V mot 3,3 V, gå vidare till kapitel 33 om nivåskiftning och signalanpassning.
- När kommunikationen bara fallerar ibland, använd felsökningsordningen i kapitel 35.


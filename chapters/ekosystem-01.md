# 1. Arduino-kompatibla system som ekosystem

## Snabb överblick
Det här kapitlet ger dig kartan över Arduino-världen innan du börjar välja kort, installera bibliotek eller koppla moduler. Använd det när du vill förstå vad “Arduino-kompatibel” faktiskt kan betyda och vilka delar av ekosystemet som påverkar ett praktiskt projekt.

Kapitlet hjälper dig framför allt att skilja på:

- kortet du håller i handen
- mikrokontrollern på kortet
- Arduino-API:t och den core som implementerar det
- board package, bibliotek och exempelprojekt
- shields, breakout boards och färdiga moduler

Det praktiska målet är inte att memorera alla kort eller alla detaljer. Målet är att kunna läsa ett exempel, ett datablad eller en tutorialsida och snabbt se vilka antaganden som faktiskt följer med.

## Arduino är flera saker samtidigt

När någon säger “Arduino” kan ordet syfta på flera lager.

| Lager | Vad det betyder | Exempel |
|---|---|---|
| Hårdvara | Ett fysiskt utvecklingskort | Arduino UNO, Nano, Mega, MKR, Nano ESP32 |
| Programmeringsmodell | Ett enkelt sätt att strukturera mikrokontrollerkod | `setup()`, `loop()`, `pinMode()`, `digitalWrite()` |
| Utvecklingsmiljö | Verktyg för att skriva, bygga och ladda upp kod | Arduino IDE, Arduino CLI |
| Board package | Stöd för en viss kortfamilj | AVR, SAMD, ESP32, RP2040 |
| Core | Implementering av Arduino-API:t för en viss plattform | Hur `digitalWrite()` fungerar på just den mikrokontrollern |
| Bibliotek | Återanvändbar kod för sensorer, displayer eller protokoll | Sensorbibliotek, displaybibliotek, kommunikationsbibliotek |
| Ekosystem | Kombinationen av kort, moduler, exempel, forum, dokumentation och community | Hela Arduino-världen |

Det är viktigt att skilja på dessa lager. Ett kort kan vara Arduino-kompatibelt på programmeringsnivå utan att ha samma elektriska egenskaper som ett klassiskt Arduino UNO-kort. Ett annat kort kan ha UNO-liknande formfaktor men kräva en annan board package. Ett bibliotek kan fungera utmärkt på AVR-baserade kort men anta timing eller minnesmängder som passar sämre på en annan plattform.

### Exempel: samma kod, olika betydelse

Kod som denna ser enkel ut:

```cpp
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
  delay(500);
}
```

På ett klassiskt Arduino UNO-kort blinkar den inbyggda LED:en på pinne 13. På andra kort kan den inbyggda LED:en sitta på en annan pinne, ha inverterad logik eller saknas helt. Själva programmeringsmodellen är gemensam, men hårdvaruantagandet är inte säkert gemensamt.

Ett mer portabelt sätt är ofta att använda en symbol som kortets core definierar:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
```

Även här behöver du vara uppmärksam. `LED_BUILTIN` gör koden mer portabel, men det garanterar inte att LED:en beter sig exakt likadant på alla kort.

## Vad betyder Arduino-kompatibel?

“Arduino-kompatibel” är inte en exakt teknisk certifiering i vardagligt språk. Det är snarare en samling möjliga kompatibiliteter.

### Kompatibel med Arduino IDE

Det vanligaste är att kortet kan väljas i Arduino IDE eller användas via Arduino CLI. Det kräver att rätt board package är installerad. Då vet verktyget hur koden ska kompileras, vilken mikrokontroller som används och hur uppladdningen ska göras.

Det betyder däremot inte automatiskt att kortet har samma pinnar, samma spänningsnivåer eller samma bibliotekskompatibilitet som ett annat kort.

### Kompatibel med Arduino-API:t

Många kortfamiljer implementerar funktioner som:

```cpp
pinMode(pin, OUTPUT);
digitalWrite(pin, HIGH);
int value = analogRead(A0);
```

Det gör att enklare kod kan flyttas mellan kort. Men implementationen bakom funktionerna kan skilja sig. En ADC kan ha annan upplösning, PWM kan finnas på andra pinnar, `analogWrite()` kan fungera annorlunda och vissa pins kan ha specialfunktioner vid uppstart.

### Kompatibel med UNO-formfaktor

Vissa kort har samma ungefärliga layout som Arduino UNO och kan därför passa med många shields. Det är praktiskt, men inte tillräckligt. Ett shield som är byggt för 5 V-logik kanske inte passar ett 3,3 V-kort även om pinnarna råkar sitta på samma plats.

### Kompatibel med befintliga bibliotek

Det här är ofta den kompatibilitet som spelar störst roll i praktiken. Om du vill använda en viss sensor, display eller motorstyrning behöver biblioteket fungera på kortet du väljer. Ett bibliotek kan bero på I2C, SPI, timers, interrupt, minne eller låg nivå-kod som inte är lika portabel som den ser ut.

### Kompatibel med exempel och tutorials

Många projekt fungerar för att tutorialen råkar använda samma kort, samma modul, samma biblioteksversion och samma kopplingsantaganden. När du byter kort, modul eller bibliotek kan små skillnader bli stora.

Ett professionellt arbetssätt är därför att alltid fråga:

- Vilken del av kompatibiliteten gäller här?
- Är det programmeringsmiljön, API:t, pinouten, spänningsnivån, formfaktorn eller biblioteket?
- Vilka antaganden gör exempelprojektet?

## Kort, moduler, shields och breakout boards

Arduino-ekosystemet består inte bara av mikrokontrollerkort. Mycket av värdet kommer från kringkomponenterna.

### Utvecklingskort

Ett utvecklingskort innehåller normalt en mikrokontroller, USB-anslutning, spänningsregulator, pinnar och ibland extra funktioner som Wi-Fi, Bluetooth, laddkrets, sensorer eller displaykontakt.

Exempel på utvecklingskort är:

- Arduino UNO och UNO-liknande kort.
- Arduino Nano och Nano-liknande kort.
- Arduino Mega.
- ESP8266-baserade NodeMCU- och D1 mini-varianter.
- ESP32 DevKit-kort.
- Raspberry Pi Pico-liknande RP2040-kort.
- Småkort som Seeed XIAO och Adafruit Feather-varianter.

Utvecklingskort är gjorda för att vara praktiska att experimentera med. De är inte alltid optimala för slutprodukter, men de är utmärkta för prototyper.

### Shields

Ett shield är ett tilläggskort som monteras ovanpå ett kompatibelt Arduino-kort, ofta i UNO- eller Mega-formfaktor. Shields kan ge motorstyrning, Ethernet, prototypyta, reläer, display, datalogging eller annan funktionalitet.

Fördelen med shields är att de kan vara snabba att använda och kräver lite kabeldragning. Nackdelen är att de ofta antar specifika pinnar, spänningsnivåer och formfaktorer. Två shields kan också krocka om de använder samma pinnar eller samma I2C-adress utan möjlighet att ändra den.

### Breakout boards

En breakout board gör en komponent enklare att använda på breadboard eller med kablar. Den kan bryta ut små pinnar till 2,54 mm-stift, lägga till pull-up-motstånd, regulator, nivåskiftning eller skyddskomponenter.

Exempel är en BME280-breakout, en OLED-breakout eller en IMU-breakout. Breakout boards är ofta mer flexibla än shields eftersom du själv väljer vilka pinnar du kopplar till.

### Moduler

En modul är ett lite bredare begrepp. Den kan vara en breakout board, men också en färdig funktionell enhet med flera komponenter. En relämodul kan till exempel innehålla transistor, diod, optokopplare, skruvterminaler och status-LED. En motor driver-modul kan innehålla drivkrets, terminaler och kylfläns.

Moduler är praktiska, men de kan dölja viktiga detaljer. Du behöver fortfarande förstå matningsspänning, logiknivå, strömkrav och gränssnitt.

## Board packages och cores

När du installerar stöd för ett nytt kort i Arduino IDE installerar du normalt en board package. Den talar om för verktyget hur kod ska kompileras och laddas upp till en viss kortfamilj.

En board package kan innehålla:

- Definitioner för olika kort.
- Kompilatorinställningar.
- Uppladdningsverktyg.
- Pin-mappning.
- En Arduino core för plattformen.
- Exempel och variantfiler.

En core är den del som implementerar Arduino-programmeringsmodellen för en viss mikrokontrollerfamilj. Det är därför `digitalWrite()` kan finnas både på ett AVR-baserat UNO-kort och på ett ESP32-kort, trots att hårdvaran under ytan är helt annorlunda.

### Varför cores spelar roll

När du använder högnivåfunktioner känns korten lika. När du gör mer avancerade saker syns skillnaderna tydligare.

Exempel på områden där core och plattform spelar roll:

- ADC-upplösning och analog referens.
- PWM-frekvens och vilka pinnar som stöder PWM.
- Timerresurser.
- Interrupt-stöd.
- Standardnamn för pinnar.
- Hur I2C- och SPI-bussar väljs.
- Stöd för USB, Wi-Fi eller Bluetooth.
- Sleep modes och energiförbrukning.
- Hur seriella portar namnges.

Det betyder inte att du ska undvika Arduino-kompatibla kort. Det betyder att du ska veta när du arbetar på Arduino-nivå och när du arbetar nära hårdvaran.

## Bibliotek: den stora accelerationen och den vanliga fallgropen

Bibliotek är en av Arduino-ekosystemets största styrkor. De gör det möjligt att snabbt använda sensorer, displayer, motorstyrningar, kommunikationsmoduler och filsystem utan att skriva all låg nivå-kod själv.

Ett bibliotek kan ge dig:

- En klass för att initiera och läsa en sensor.
- Färdiga funktioner för att rita på en display.
- Hantering av I2C- eller SPI-kommunikation.
- Exempel som visar minimal koppling och minimal kod.
- Högre abstraktion, till exempel “readTemperature()” i stället för registerläsning.

Men bibliotek kan också skapa problem:

- De kan anta en viss arkitektur.
- De kan vara gamla eller övergivna.
- De kan blockera länge i en funktion.
- De kan använda mycket minne.
- De kan krocka med andra bibliotek om båda använder samma timer eller interrupt.
- De kan dölja felhantering.
- De kan fungera med en modulvariant men inte en annan.

### Läs alltid exemplen, inte bara API:t

För sensorer och moduler är bibliotekets exempel ofta lika viktiga som dokumentationen. De visar vilka include-filer som behövs, hur objekt skapas, vilken `begin()`-funktion som används och hur fel kontrolleras.

Ett bra minimalt testprogram för en sensor bör göra tre saker:

```cpp
#include <Wire.h>
// Include the sensor library here.

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // Useful on some USB-native boards.
  }

  Serial.println("Starting sensor test");

  // Initialize the sensor here.
  // Print a clear error message if initialization fails.
}

void loop() {
  // Read one or more values.
  // Print raw or converted values.
  delay(1000);
}
```

Poängen är inte exakt denna kod, utan strukturen: starta seriell kommunikation, initiera komponenten, rapportera fel tydligt och skriv ut mätvärden långsamt nog för att kunna läsa dem.

## Pinout är en del av dokumentationen, inte dekoration

När du arbetar med Arduino-kompatibla kort behöver du ofta läsa pinout-diagram. Det gäller särskilt för tredjepartskort, ESP8266/ESP32-kort, småkort och kort med flera specialfunktioner.

Ett pinout-diagram kan visa:

- GPIO-nummer.
- Kortets tryckta pinnamn.
- Analoga ingångar.
- PWM-stöd.
- I2C-, SPI- och UART-pinnar.
- Boot-relaterade pinnar.
- Touch-pinnar.
- Strömpinnar.
- 3,3 V och 5 V.
- Begränsningar eller varningar.

Det är vanligt att samma fysiska pinne har flera namn. På ett kort kan det stå `D1`, medan core och bibliotek vill att du använder ett GPIO-nummer eller en konstant. På ett annat kort kan `A0` vara en analog kanal men även en digital pinne. Ibland är det tryckta namnet på kortet inte samma sak som det nummer du använder i koden.

En enkel regel är att alltid dokumentera dina projekt med både fysisk pinne och kodnamn.

Exempel:

```cpp
// OLED display:
// SDA: board pin D2, code pin SDA
// SCL: board pin D3, code pin SCL
//
// Button:
// One side to GND
// Other side to board pin D7, code pin 7
// Uses INPUT_PULLUP
```

Det sparar mycket tid när du senare byter kort eller felsöker.

## Spänningsnivåer är inte valfria detaljer

Många klassiska Arduino-kort använder 5 V-logik. Många moderna kort använder 3,3 V-logik. Vissa kort kan matas från USB med 5 V men har mikrokontrollerpinnar som inte tål 5 V.

Det här är en av de vanligaste orsakerna till förstörda kort och opålitliga projekt.

Fråga alltid:

- Vilken spänning matar jag kortet med?
- Vilken logiknivå använder GPIO-pinnarna?
- Tål sensorns I/O den logiknivån?
- Krävs nivåskiftning?
- Har breakout boarden redan nivåskiftning?
- Är I2C-pullup-motstånden dragna till 3,3 V eller 5 V?
- Hur mycket ström kan regulatorn leverera?
- Hur mycket ström drar modulen i toppar?

Det räcker inte att en modul “fungerade för någon på internet”. Den måste fungera elektriskt i just din koppling.

## Ett första sätt att klassificera Arduino-kompatibla projekt

När du ser ett projekt, en tutorial eller en komponentbeskrivning kan du klassificera den utifrån fyra frågor.

### 1. Vilken typ av kort antas?

Exemplet kan anta ett klassiskt UNO-kort, ett ESP8266-kort, ett ESP32-kort eller något annat. Leta efter tecken som Wi-Fi-kod, `D1`-pinnar, `A0`, `LED_BUILTIN`, många seriella portar eller särskilda board-inställningar.

### 2. Vilket gränssnitt används?

Sensorn eller modulen kan använda analog signal, digital signal, I2C, SPI, UART, 1-Wire eller ett specialprotokoll. Det påverkar koppling, bibliotek och felsökning.

### 3. Vilka elektriska krav finns?

Matningsspänning, logiknivå, ström, pullups och kabeldragning kan vara viktigare än själva koden.

### 4. Vilka bibliotek och versioner används?

Samma komponent kan ha flera bibliotek. Vissa är officiella från komponenttillverkaren, andra är community-baserade, och några är gamla men fortfarande vanliga i tutorials.

## Vanliga misstag

- **Misstag: Att tro att Arduino-kompatibel alltid betyder elektriskt kompatibel.**
  - **Varför det händer:** Programmeringsmodellen kan se likadan ut även när spänningsnivåer och pinnar skiljer sig.
  - **Hur man undviker det:** Kontrollera alltid GPIO-spänning, matning och modulens I/O-nivå.

- **Misstag: Att kopiera kod utan att kopiera antagandena.**
  - **Varför det händer:** Tutorials visar ofta fungerande kod men inte alltid kortmodell, biblioteksversion, pinout och modulvariant.
  - **Hur man undviker det:** Dokumentera vilket kort, vilken board package, vilket bibliotek och vilken koppling exemplet bygger på.

- **Misstag: Att lita på pinnamnen på kortet utan att läsa pinout.**
  - **Varför det händer:** Olika kortfamiljer använder olika namnkonventioner för fysiska pinnar och GPIO-nummer.
  - **Hur man undviker det:** Skriv alltid både tryckt pinnamn och kodens pinnamn i dina projektanteckningar.

- **Misstag: Att installera många bibliotek med nästan samma namn.**
  - **Varför det händer:** Library Manager kan innehålla flera bibliotek för samma sensor eller display.
  - **Hur man undviker det:** Välj bibliotek med aktivt underhåll, tydliga exempel och stöd för din plattform. Dokumentera valet.

- **Misstag: Att börja med hela systemet direkt.**
  - **Varför det händer:** Det är lockande att koppla sensor, display, motor och nätverk samtidigt.
  - **Hur man undviker det:** Testa ett kort, en buss och en modul i taget. Kombinera först när varje del fungerar separat.

## Snabb sammanfattning

- Arduino är inte bara ett kort, utan ett ekosystem av hårdvara, verktyg, cores, bibliotek, moduler och community.
- “Arduino-kompatibel” kan betyda kompatibel med IDE, API, formfaktor, bibliotek eller exempel, men inte nödvändigtvis allt samtidigt.
- Board packages och cores gör att olika mikrokontrollerfamiljer kan programmeras med Arduino-liknande kod.
- Bibliotek gör utvecklingen snabbare, men kan dölja antaganden om plattform, timing, minne och gränssnitt.
- Pinout, spänningsnivå och matningskrav är lika viktiga som koden.
- Ett säkert arbetssätt är att testa kort, buss och modul var för sig innan de kombineras.

## Begreppsförklaring: Arduino-kompatibel

I den här boken betyder **Arduino-kompatibel** inte att alla kort är elektriskt eller tekniskt likadana. Det betyder att kortet kan programmeras med Arduino-liknande arbetsflöde, bibliotek och kodmodell.

Tre begrepp är särskilt viktiga:

- **Arduino core:** den kod och de funktioner som gör att `digitalWrite()`, `analogRead()`, `Wire`, `SPI` och andra Arduino-API:er fungerar på en viss mikrokontrollerfamilj.
- **Board package:** paketet som installeras i utvecklingsmiljön för att den ska känna igen ett visst kort, dess processor, klockfrekvens, USB-stöd, minneslayout och uppladdningsmetod.
- **Bibliotek:** återanvändbar kod som gör det enklare att tala med en sensor, display, motorstyrning eller nätverksfunktion.

Det praktiska rådet är att alltid skilja på **kortet du håller i handen**, **mikrokontrollern på kortet** och **Arduino-stödet som gör kortet programmerbart i miljön**.

## Relaterat

- När du ska välja kort i stället för att bara förstå ekosystemet, gå vidare till kapitel 2.
- När skillnaden mellan kort, shield, modul och bibliotek blir praktisk, använd kapitel 3 som arbetsstart.
- När projektet växer till flera moduler, jämför med integrationsmönstret i kapitel 37.

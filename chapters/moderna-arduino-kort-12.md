# 12. Moderna Arduino-kort

## Kortprofil i korthet
De klassiska Arduino-korten är fortfarande användbara, men Arduino-ekosystemet har blivit betydligt bredare. I dag finns officiella Arduino-kort med 32-bitars mikrokontroller, inbyggd trådlös kommunikation, bättre minne, USB-C, realtidsfunktioner, säkrare molnanslutning och formfaktorer som är mer lämpade för små inbyggda system än den klassiska UNO-layouten.

Det gör moderna Arduino-kort intressanta för dig som redan kan programmera. De ger ofta mer marginal för större program, fler bibliotek, mer avancerade sensorer, nätverkskommunikation och bättre integration med moderna moduler. Samtidigt betyder modernare inte automatiskt enklare. Ett kort med Wi-Fi, Bluetooth, USB HID, flera seriella portar och mer avancerad mikrokontroller kan också ge fler specialfall än ett klassiskt UNO-kort.

Det här kapitlet fokuserar på moderna officiella Arduino-kort och när de är ett rimligt val jämfört med klassiska kort, kloner, ESP8266, ESP32, RP2040/RP2350 och specialkort. Vi tittar särskilt på kortfamiljer och egenskaper snarare än att försöka göra en evig produktkatalog. Exakta modeller förändras, men beslutsfrågorna är stabila:

- Behöver projektet mer minne än ett klassiskt ATmega328P-kort?
- Behöver projektet Wi-Fi eller Bluetooth?
- Behöver projektet modern USB-funktionalitet?
- Behöver projektet liten formfaktor?
- Behöver projektet bättre analog utgång eller DAC?
- Behöver projektet fungera med många Arduino-exempel och bibliotek?
- Behöver projektet vara lätt att rekommendera, köpa och dokumentera över tid?

Ett modernt Arduino-kort är ofta ett bra val när du vill ha mer kapacitet men fortfarande vill stanna i en relativt väl dokumenterad Arduino-miljö. Det är däremot inte alltid bästa valet om priset är viktigast, om du behöver maximal kontroll över ESP32-funktioner, om du vill experimentera med RP2040 PIO eller om ett klassiskt 5 V-kort passar komponenterna bättre.

## Bedöm kortet med detta i åtanke

Moderna Arduino-kort ska bedömas utifrån mer än processorkraft. Titta särskilt på logiknivå, minne, trådlös kommunikation, analog mätning, bibliotek, strömförbrukning och hur väl kortets funktioner stöds i Arduino-miljön.

## Kortfamiljen i praktiken

Ett modernt Arduino-kort kan betyda flera saker. Det kan vara modernt för att det har en nyare mikrokontroller, för att det har Wi-Fi eller Bluetooth, för att det använder en mindre formfaktor, för att det har bättre USB-stöd eller för att det är tänkt för mer professionella och uppkopplade tillämpningar.

Ett klassiskt UNO-kort är i praktiken en enkel mikrokontrollerplattform: ett ATmega328P-baserat system med digitala pinnar, analoga ingångar, USB-uppladdning och 5 V-logik. Det är begripligt och stabilt, men begränsat.

Ett modernt Arduino-kort kan i stället ha:

- 32-bitars Arm- eller ESP32-baserad mikrokontroller
- betydligt mer flash och RAM
- 3,3 V-logik eller blandade nivåer beroende på kort
- USB-C och bättre USB-funktioner
- inbyggd Wi-Fi och Bluetooth
- säkrare moln- eller IoT-integration
- Qwiic-, STEMMA QT- eller liknande I2C-kontakt på vissa kort
- DAC, bättre timers eller fler hårdvaruperiferier
- mindre formfaktor för inbyggda projekt
- bättre stöd för batteri och låg strömförbrukning på vissa serier

Men moderna kort kan också ha mer komplexitet:

- färre exempel är skrivna direkt för just kortet
- vissa bibliotek antar AVR eller klassisk UNO-pinout
- analoga funktioner kan skilja sig mycket mellan kort
- Wi-Fi/Bluetooth kan ligga på en separat modul
- 5 V-tolerans får aldrig antas utan dokumentation
- pinout och specialpinnar kan vara mer komplexa
- vissa funktioner kräver firmware, board package eller biblioteksversioner som måste passa ihop

Det viktigaste är därför att inte välja modernt för att det låter bättre. Välj modernt när projektets krav gör den extra kapaciteten användbar.

## Fyra huvudskäl att välja ett modernt Arduino-kort

Det finns många modeller, men de vanligaste skälen kan grupperas i fyra kategorier.

### Mer marginal för kod och bibliotek

Klassiska ATmega328P-baserade kort kan bli trånga när du kombinerar flera bibliotek, stränghantering, display, kommunikation och sensordata. Ett modernt kort med mer RAM och flash ger större marginal.

Det märks särskilt när projektet innehåller:

- displaybibliotek
- nätverksstack
- JSON-hantering
- kryptering eller TLS
- många sensorer
- buffring av mätdata
- mer strukturerad C++-kod
- flera återanvändbara moduler

För en erfaren programmerare kan detta vara den största praktiska skillnaden. Du behöver inte längre optimera bort varje textsträng eller undvika rimlig struktur bara för att RAM tar slut.

### Inbyggd uppkoppling

Många moderna projekt behöver Wi-Fi, Bluetooth eller molnanslutning. Du kan lägga till nätverk med externa moduler, men det ökar koppling, bibliotekskomplexitet och felsökning. Ett kort med integrerad uppkoppling kan vara enklare.

Det passar särskilt när projektet ska:

- skicka sensordata via Wi-Fi
- fungera som enkel webserver
- ansluta till MQTT
- prata med telefon via BLE
- använda Arduino Cloud eller liknande tjänst
- uppdateras eller övervakas på distans

Samtidigt ska du vara uppmärksam på arkitekturen. På vissa kort är Wi-Fi/Bluetooth en separat modul som samarbetar med huvudmikrokontrollern. På andra kort är mikrokontrollern själv en ESP32-baserad SoC. Det påverkar vilka bibliotek som fungerar och hur nära du kommer nätverkskretsens egna funktioner.

### Mindre och mer praktisk formfaktor

UNO-formfaktorn är bra för undervisning, shields och labbmiljö, men den är ofta stor i färdiga byggen. Nano-, MKR- och mindre formfaktorer passar bättre när projektet ska in i en låda, monteras på en liten prototyp eller kombineras med breadboard.

Mindre kort är särskilt användbara när:

- projektet ska byggas in
- breadboardvänlighet är viktig
- du vill ha flera identiska noder
- vikten spelar roll
- en sensorstation ska vara kompakt
- många kort ska användas i parallella experiment

Nackdelen är att mindre kort ofta har tätare pinnar, mindre text på kortet, färre anslutningar eller större behov av dokumenterad pinout.

### Modernare periferier

Modernare mikrokontroller kan ge funktioner som klassiska kort saknar eller har i enklare form:

- fler UART-portar
- fler PWM-kanaler
- bättre timers
- DAC på vissa kort
- USB-enhet eller USB-host på vissa plattformar
- snabbare I2C eller SPI
- bättre interruptmöjligheter
- DMA eller avancerade periferier på lägre nivå

I Arduino-boken behöver vi inte gå djupt i alla interna periferier, men vi behöver känna igen när de gör skillnad. Om projektet exempelvis ska styra många LED, läsa snabba sensorer eller logga data med högre hastighet kan moderna periferier vara viktigare än själva klockfrekvensen.

## Vad moderna kort ofta ger dig utöver klassiska kort

Ett modernt Arduino-kort är inte automatiskt bättre i alla projekt, men det ger ofta mer marginal än ett klassiskt AVR-baserat kort.

Vanliga praktiska vinster är:

- mer minne för större bibliotek, displaykod, nätverkskod och buffertar
- inbyggd uppkoppling på vissa modeller
- 3,3 V-logik som passar många moderna sensorer och moduler
- bättre USB- eller HID-möjligheter på vissa kort
- fler eller mer flexibla periferier för I2C, SPI, UART, PWM och timers
- bättre marginal när flera moduler används samtidigt

Det finns också nya saker att kontrollera. ADC-skala, PWM-beteende, pinnamn, USB-start och bibliotek som antar AVR kan skilja sig från klassiska UNO-/Nano-projekt.

## UNO R4-generationen

UNO R4 är intressant eftersom den behåller mycket av UNO-känslan men byter ut den klassiska 8-bitarskärnan mot en modernare 32-bitarsplattform. Den är därför ett bra exempel på ett modernt Arduino-kort som försöker vara bekant snarare än radikalt annorlunda.

Det finns två huvudidéer i UNO R4-generationen:

- behåll UNO-formfaktorn och mycket av användningsmodellen
- ge mer minne, modernare mikrokontroller och fler funktioner

UNO R4 Minima är den enklare varianten. UNO R4 WiFi lägger till trådlös kommunikation och extra funktioner. För många projekt är UNO R4-familjen ett naturligt steg upp från UNO R3: mer marginal, modernare mikrokontroller och fortsatt tydlig Arduino-identitet.

### När UNO R4 är ett bra val

UNO R4 är ofta ett bra val när du vill:

- behålla UNO-formfaktor
- använda shields eller UNO-liknande kopplingsmönster
- få mer minne och modernare processor
- stanna nära officiell Arduino-dokumentation
- undervisa eller dokumentera med en välkänd layout
- skapa experiment där klassisk UNO känns för begränsad
- ha ett modernt kort utan att direkt gå in i ESP32- eller RP2040-specifika detaljer

Det är också ett bra jämförelsekort. Om ett projekt fungerar på UNO R4 men inte på UNO R3 kan skillnaden handla om minne, timing, bibliotek eller elektriska detaljer. Om det fungerar på UNO R3 men inte på UNO R4 kan det handla om bibliotek som antog AVR-detaljer.

### När UNO R4 inte är bästa val

UNO R4 är inte automatiskt bästa val i alla moderna projekt.

Välj hellre något annat när:

- projektet måste vara extremt billigt
- du behöver mycket liten formfaktor
- du vill använda ESP32-specifika funktioner direkt
- projektet är batteridrivet och kräver mycket låg viloström
- du behöver ett kort som redan är vanligt i ett specifikt community-exempel
- du behöver exakt kompatibilitet med äldre AVR-bibliotek
- du vill ha många fler pinnar än UNO-layouten erbjuder

UNO R4 är alltså ett bra moderniserat standardkort, inte en universallösning.

## UNO R4 WiFi och skillnaden mellan huvudkrets och radiomodul

UNO R4 WiFi är särskilt pedagogiskt intressant eftersom kortet kombinerar en huvudmikrokontroller med en separat ESP32-S3-baserad radiomodul. Det gör att kortet kan erbjuda Wi-Fi och Bluetooth-liknande funktioner utan att hela användarprogrammet nödvändigtvis körs som ett vanligt ESP32-program.

Det här är en viktig skillnad.

På ett Arduino Nano ESP32 kör din Arduino-sketch i ESP32-S3-miljön. På UNO R4 WiFi är huvudprogrammet däremot kopplat till Renesas RA4M1-sidan, medan ESP32-S3-modulen främst hanterar uppkoppling. För många Arduino-exempel spelar det ingen större roll. Du använder rätt Wi-Fi-bibliotek och följer dokumentationen. Men om du förväntar dig att alla ESP32-exempel ska fungera rakt av på UNO R4 WiFi blir du besviken.

Tänk så här:

- UNO R4 WiFi är ett modernt UNO-kort med ansluten nätverksmodul.
- Nano ESP32 är ett Nano-kort där ESP32-S3 är huvudplattformen.
- ESP32 DevKit är ett generellt ESP32-kort där du ofta arbetar närmare ESP32-ekosystemet.

Detta påverkar val av bibliotek, exempel, pinout och felsökning.

### Praktiska konsekvenser

När du använder UNO R4 WiFi bör du dokumentera:

- vilken board package-version du använder
- vilket Wi-Fi-bibliotek exemplet bygger på
- om radiomodulens firmware behöver uppdateras
- vilka pinnar som används av inbyggda funktioner
- om exempel är skrivna för UNO R4 WiFi eller för generella ESP32-kort
- om projektet behöver BLE, Wi-Fi eller bara lokal körning

Det är också klokt att först bygga ett litet uppkopplingstest innan nätverket blandas med sensorer, display, motorstyrning och datalogging.

## Nano-familjen som modern formfaktor

Nano-formfaktorn är praktisk eftersom den är liten, breadboardvänlig och lätt att bygga in. Moderna Nano-kort kan därför vara mycket användbara när du vill ha mer kapacitet utan att använda ett stort UNO-kort.

Arduino Nano ESP32 är ett tydligt exempel. Det kombinerar Nano-formfaktor med ESP32-S3-baserad funktionalitet. Det gör kortet intressant för IoT, BLE, Wi-Fi, MicroPython-experiment och små uppkopplade projekt.

Men Nano-formfaktorn finns också i andra varianter. Det viktiga är inte att alla Nano-kort fungerar likadant, utan att du inte ska låta namnet lura dig. “Nano” beskriver ofta formfaktorn, inte exakt mikrokontroller, spänning, minne eller bibliotek.

### När ett modernt Nano-kort är ett bra val

Välj ett modernt Nano-liknande kort när:

- projektet ska byggas på breadboard
- formfaktorn ska vara liten
- du vill ha ett officiellt kort med tydlig dokumentation
- du behöver mer än klassisk Nano men inte UNO-storlek
- projektet ska använda Wi-Fi eller BLE i kompakt format
- du vill kunna bygga flera små noder

### När ett modernt Nano-kort inte är bästa val

Välj något annat när:

- du behöver UNO-shield-kompatibilitet
- du behöver mycket enkel 5 V-logik
- du vill ha stora skruvterminaler eller robusta industrikontakter
- du behöver många lättåtkomliga pinnar
- du ofta byter kopplingar och vill ha mer fysisk marginal
- du behöver maximal billig massanvändning och accepterar tredjepartskort

Nano-formfaktorn är stark i små projekt, men inte alltid bekväm i större labbkopplingar.

## MKR-serien och uppkopplade projekt

MKR-serien representerar en annan tanke än UNO och Nano. Den är mer inriktad på uppkopplade, kompakta och ibland batterinära projekt. Olika MKR-kort har historiskt erbjudit varianter för Wi-Fi, GSM/LTE, LoRa, NB-IoT eller andra kommunikationsformer.

Det viktiga för den här boken är inte att memorera varje MKR-modell. Det viktiga är att förstå vad en sådan serie försöker lösa:

- kompakt formfaktor
- uppkopplade projekt
- shields och tillbehör anpassade för serien
- ofta 3,3 V-logik
- mer inriktning mot IoT än klassisk labb-UNO

MKR-kort kan vara bra när projektet faktiskt handlar om uppkoppling och fältplacering. De är mindre självklara om du bara vill testa en sensor på skrivbordet eller om du behöver mycket billig prototypmiljö.

### När MKR-liknande kort passar

MKR-liknande kort passar när:

- projektet är en uppkopplad sensor- eller styrnod
- formfaktor och batterinära användning spelar roll
- du vill ha officiella tillbehör i samma serie
- du vill undvika att själv kombinera lösa radiomoduler
- du behöver dokumenterad Arduino-väg till IoT-projekt

### När något annat passar bättre

Välj något annat när:

- du vill ha billigaste möjliga Wi-Fi-kort
- du vill använda ett brett ESP32-community direkt
- du behöver UNO-shields
- du bygger ren labbelektronik utan uppkoppling
- du behöver mycket specifika radiofunktioner utanför Arduino-lagret

MKR-serien är alltså ofta projektnära, men mindre generell som första testplattform.

## Portenta och mer avancerade Arduino-kort

Arduino har också mer avancerade kortfamiljer för professionella, industriella eller beräkningsintensiva användningar. Portenta-liknande kort är inte samma typ av produkt som UNO eller Nano. De riktar sig ofta mot mer avancerade tillämpningar där mikrokontrollern bara är en del av ett större system.

I en bok om Arduino och elektronikkretsar behöver vi inte använda Portenta som standardkort. Däremot är det viktigt att veta att sådana kort finns, eftersom de förändrar gränsen mellan hobbyplattform, prototypplattform och professionell inbyggd utveckling.

De kan vara relevanta när du behöver:

- högre prestanda
- mer avancerad nätverkskommunikation
- kamera, AI eller edge computing
- industriella gränssnitt
- robustare hårdvaruplattform
- integration med mer avancerad mjukvara
- flera processorer eller mer komplex arkitektur

Men de är ofta fel val för första kontrollen med en sensor, en LED-strip eller en enkel motor. De är dyrare, mer komplexa och ger mindre pedagogisk enkelhet.

En bra tumregel är:

> Börja inte med avancerat kort för att göra ett enkelt problem imponerande. Välj avancerat kort när problemet faktiskt kräver avancerad hårdvara.

## Jämförelse mellan moderna Arduino-kort och andra kortfamiljer

För att välja rätt behöver du se moderna Arduino-kort i relation till andra alternativ.

| Val | Styrka | Begränsning | Typiskt användningsfall |
|---|---|---|---|
| Klassisk UNO/Nano/Mega | Enkelhet, 5 V, mycket exempelmaterial | Lite minne, ingen inbyggd uppkoppling | Grundexperiment, felsökning, undervisning |
| UNO R4-liknande | Modernare UNO-känsla, mer minne, bekant formfaktor | Inte alltid AVR- eller ESP32-kompatibel på låg nivå | Uppgraderad UNO-plattform |
| Nano ESP32-liknande | Kompakt, Wi-Fi/BLE, modern prestanda | 3,3 V, ESP32-specifika detaljer | Små IoT-projekt |
| MKR-liknande | Uppkopplade projekt, kompakt, officiellt ekosystem | Modellberoende radio, ofta dyrare | Sensor- och fältnoder |
| ESP8266/NodeMCU | Billig Wi-Fi, mycket communitymaterial | Äldre, begränsade resurser, pinout-fällor | Enkla Wi-Fi-projekt |
| ESP32 DevKit | Kraftfullt, billigt, stort ekosystem | Många varianter, mer specialfall | IoT, BLE, prestanda, prototyper |
| RP2040/Pico | Mycket I/O, bra timing, låg kostnad | Ingen Wi-Fi på grundmodellen, eget ekosystem | Timingnära I/O, många GPIO |
| Portenta/specialkort | Avancerade funktioner och professionell inriktning | Kostnad och komplexitet | Industri, edge, AI, avancerade prototyper |

Tabellen är inte en topplista. Den är en påminnelse om att varje kortfamilj har en tydlig plats.

## Vanliga skillnader som påverkar kodportering

Att en sketch kompilerar på ett modernt kort betyder inte att projektet är färdigporterat. Portering handlar både om kod och hårdvara.

### Pinnummer och fysisk pinout

Arduino API:t låter dig skriva `digitalWrite(LED_PIN, HIGH)`, men vad `LED_PIN` betyder beror på kortet. På ett UNO-kort är många exempel skrivna med direkt förväntan på klassisk pinout. På ett modernt Nano- eller MKR-kort kan samma pinnummer finnas, men fysisk placering, alternativa funktioner och spänningsnivå kan skilja sig.

Använd därför alltid namngivna pinnar:

```cpp
const int STATUS_LED_PIN = 13;
const int SENSOR_POWER_PIN = 7;
const int BUTTON_PIN = 2;
```

Ännu bättre är att samla kortspecifika pinnar i ett tydligt block:

```cpp
// Board profile: Arduino UNO R4 WiFi
const int STATUS_LED_PIN = LED_BUILTIN;
const int BUTTON_PIN = 2;
const int SENSOR_INTERRUPT_PIN = 3;
const int SENSOR_I2C_SDA_PIN = SDA;
const int SENSOR_I2C_SCL_PIN = SCL;
```

Då blir porteringen en fråga om att ändra kortprofil, inte att leta igenom hela programmet.

### Spänningsnivåer

Klassiska UNO- och Mega-kort arbetar ofta med 5 V-logik. Många modernare kort arbetar med 3,3 V-logik, även om de kan matas via USB eller Vin. Det är en vanlig källa till felkoppling.

Fråga alltid:

- Är kortets I/O 5 V eller 3,3 V?
- Är pinnarna 5 V-toleranta?
- Vilken spänning kräver sensorn?
- Behövs nivåskiftning?
- Delas common ground?
- Har modulen egen regulator och nivåanpassning?

Om du är osäker, anta inte tolerans. Kontrollera dokumentationen.

### Analog läsning

ADC-upplösning, referensspänning, linearitet och brus skiljer sig mellan kortfamiljer. Ett tröskelvärde som fungerade på UNO kan ge annan skala på ett modernare kort.

Skriv därför inte kod som gömmer antagandet:

```cpp
if (analogRead(A0) > 512) {
  // Antagande: 10-bitars ADC och ungefär halva referensspänningen
}
```

Gör hellre antagandet synligt:

```cpp
const int ADC_MAX_VALUE = 1023;
const float THRESHOLD_RATIO = 0.50;

int raw = analogRead(A0);
float ratio = raw / static_cast<float>(ADC_MAX_VALUE);

if (ratio > THRESHOLD_RATIO) {
  // Signal is above half scale for this configured ADC range
}
```

På vissa moderna kort kan du dessutom konfigurera upplösning med Arduino-funktioner eller kortspecifika funktioner. Dokumentera det i kontrollen.

### PWM och timers

PWM-pinnar, frekvenser och timerbeteende kan skilja sig mycket. Ett servoexempel, en motorstyrning eller en LED-effekt kan därför bete sig annorlunda vid portering.

Testa PWM separat innan du kombinerar det med:

- servobibliotek
- motorstyrning
- ljud via `tone()`
- tidskritiska LED-bibliotek
- avbrott
- energisparlägen

Om ett bibliotek manipulerar timers kan det påverka andra funktioner.

### Bibliotek som antar AVR

Vissa äldre bibliotek är skrivna med antaganden om AVR-register, programminne eller klassiska Arduino-pinnar. De kan fungera fint på UNO och Mega men misslyckas på modernare kort.

Tecken på detta är:

- kompilatorfel med registernamn som inte finns
- användning av `PROGMEM` på sätt som inte är portabelt
- direkt portmanipulation
- timing som bygger på en specifik klockfrekvens
- antaganden om timerregister
- hårdkodade pinnar för SPI eller I2C

Det betyder inte att moderna kort är sämre. Det betyder att bibliotekets abstraktionsnivå är lägre än Arduino API:t.

## När moderna officiella kort passar bättre än kloner och lågkostnadskort

Kapitel 11 betonade att lågkostnadskort ofta är mycket användbara. Moderna officiella kort har ändå flera styrkor.

Välj ett modernt officiellt Arduino-kort när:

- boken, kursen eller dokumentationen ska vara lätt att följa
- du vill minska variationen mellan exemplar
- du behöver stabil och tydlig dokumentation
- kortet ska rekommenderas till andra
- projektet ska fungera länge
- bibliotek och board packages bör vara enkla att installera
- du vill ha en support- och dokumentationsväg
- kortet ska användas i utbildning eller workshop

Välj lågkostnadskort när:

- priset är avgörande
- du behöver många noder
- du accepterar mer egen felsökning
- du redan har dokumenterat exakt kortidentitet
- du bygger experiment, inte undervisningsmaterial
- du vill testa riskabla kopplingar utan att offra dyrare kort

Det professionella valet är inte alltid dyrast. Det professionella valet är det som gör projektet mest reproducerbart och minst överraskande i sitt sammanhang.

## Valguide

Här är en praktisk valguide för vanliga situationer.

| Projektkrav | Titta först på | Varför |
|---|---|---|
| Jag vill ha UNO-känsla men mer minne | UNO R4-liknande kort | Bekant formfaktor och modernare mikrokontroller |
| Jag vill ha Wi-Fi i officiellt Arduino-format | UNO R4 WiFi, Nano ESP32 eller MKR Wi-Fi-variant | Dokumenterad uppkoppling utan lös extern modul |
| Jag vill ha kompakt IoT-nod | Nano ESP32 eller MKR-liknande kort | Mindre formfaktor och nätverksstöd |
| Jag vill undervisa med modern hårdvara | UNO R4-liknande kort | Fysisk tydlighet och nära Arduino-identitet |
| Jag vill bygga många billiga Wi-Fi-noder | ESP8266/ESP32 tredjepartskort | Lägre pris och stort community |
| Jag behöver många pinnar men enkelhet | Mega eller modernare alternativ med många GPIO | Välj efter bibliotek och formfaktor |
| Jag behöver industriell eller avancerad lösning | Portenta- eller specialkort | Högre prestanda och mer professionell inriktning |
| Jag vill testa timingnära I/O | RP2040/RP2350-liknande kort | Bra I/O-möjligheter och PIO-koncept |

## Referensmönster: portering från klassiskt till modernt Arduino-kort

Det här referensmönstret visar vad som ofta förändras när ett enkelt projekt flyttas från ett klassiskt Arduino-kort till ett modernt kort. Det är inte bara ett funktionstest, utan ett sätt att hitta skillnader i logiknivå, ADC-skala, PWM, I2C-pinnar, USB-beteende och bibliotekskompatibilitet.

### Vad mönstret visar

Mönstret kontrollerar fyra saker som ofta påverkas vid portering:

- digital knapp- och LED-logik
- analog läsning från potentiometer eller sensor
- PWM-baserad LED-dimning
- I2C-scanner med en känd modul

### Det här används i exemplet

- ett klassiskt kort, till exempel UNO, Nano eller Mega
- ett modernt Arduino-kort, till exempel UNO R4, UNO R4 WiFi, Nano ESP32 eller liknande
- en LED med seriemotstånd, om du inte använder inbyggd LED
- en knapp
- en potentiometer
- eventuellt en I2C-sensor som du redan testat i kapitel 9
- USB-kabel och Arduino IDE

### Definiera kortprofil

Skapa först ett tydligt konfigurationsblock.

```cpp
// Board profile: Arduino UNO or modern Arduino-compatible board

const int STATUS_LED_PIN = LED_BUILTIN;
const int BUTTON_PIN = 2;
const int ANALOG_INPUT_PIN = A0;
const int PWM_OUTPUT_PIN = 9;

const unsigned long PRINT_INTERVAL_MS = 500;

bool lastButtonState = HIGH;
unsigned long lastPrintTime = 0;
```

`LED_BUILTIN`, `A0`, `SDA` och `SCL` är mer portabla än hårdkodade antaganden. De ersätter ändå inte en kort kortprofil där fysisk pinne, logiknivå och matning sparas.

### Testa digitalt, analogt och PWM

```cpp
const int STATUS_LED_PIN = LED_BUILTIN;
const int BUTTON_PIN = 2;
const int ANALOG_INPUT_PIN = A0;
const int PWM_OUTPUT_PIN = 9;

const unsigned long PRINT_INTERVAL_MS = 500;

unsigned long lastPrintTime = 0;

void setup() {
  pinMode(STATUS_LED_PIN, OUTPUT);
  pinMode(PWM_OUTPUT_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Serial.begin(115200);
  while (!Serial) {
    // Useful on boards with native USB. On some boards this waits for the monitor.
    // Remove this block if you need standalone startup.
  }

  Serial.println("Board portability pattern started.");
}

void loop() {
  bool buttonPressed = digitalRead(BUTTON_PIN) == LOW;
  int rawAnalog = analogRead(ANALOG_INPUT_PIN);

  int pwmValue = map(rawAnalog, 0, 1023, 0, 255);
  pwmValue = constrain(pwmValue, 0, 255);

  digitalWrite(STATUS_LED_PIN, buttonPressed ? HIGH : LOW);
  analogWrite(PWM_OUTPUT_PIN, pwmValue);

  unsigned long now = millis();

  if (now - lastPrintTime >= PRINT_INTERVAL_MS) {
    lastPrintTime = now;

    Serial.print("button=");
    Serial.print(buttonPressed ? "pressed" : "released");
    Serial.print(" rawAnalog=");
    Serial.print(rawAnalog);
    Serial.print(" pwmValue=");
    Serial.println(pwmValue);
  }
}
```

Kör sketchen på det klassiska kortet först och sedan på det moderna kortet. Jämför särskilt:

- valt board i Arduino IDE
- om `while (!Serial)` påverkar fristående start
- råvärden från analog ingång
- om PWM-pinnen fungerar som väntat
- om LED-pinnen motsvarar rätt fysisk LED
- om knappens logik är oförändrad

### Kontrollera ADC-skala

Koden ovan använder `map(rawAnalog, 0, 1023, 0, 255)`. Det fungerar som startpunkt, men är inte alltid korrekt på moderna kort om ADC-upplösningen skiljer sig. Gör därför skalan explicit när du vet vilket kort du använder.

```cpp
const int ADC_MAX_VALUE = 1023;

int pwmFromAnalog(int rawAnalog) {
  int pwmValue = map(rawAnalog, 0, ADC_MAX_VALUE, 0, 255);
  return constrain(pwmValue, 0, 255);
}
```

Om det moderna kortet använder annan ADC-upplösning i aktuell konfiguration ändrar du `ADC_MAX_VALUE` och sparar det i kortprofilen.

### Kör I2C-scanner på båda korten

Använd I2C-scannern från kapitel 9 och kör den på båda korten. Kontrollera särskilt:

- vilka pinnar som är SDA och SCL
- om kortet har en separat I2C-kontakt
- om modulen behöver 3,3 V eller 5 V
- om pull-up-motstånd redan finns på modulen
- om samma I2C-adress hittas på båda korten

Om scannern fungerar på ett kort men inte det andra är det nästan alltid en konkret skillnad i koppling, spänning, pinnar eller biblioteksversion. Behandla det som ett porteringstecken, inte som ett mysterium.

## Vanliga misstag

- **Misstag: Att anta att ett modernt Arduino-kort är en snabbare UNO.**
  - Varför det händer: Kortet kan ha liknande formfaktor och samma Arduino API.
  - Hur du undviker det: Kontrollera mikrokontroller, logiknivå, pinout, ADC, PWM och biblioteksstöd separat.

- **Misstag: Att använda ESP32-exempel på UNO R4 WiFi utan att kontrollera arkitekturen.**
  - Varför det händer: Kortet innehåller en ESP32-S3-modul för uppkoppling.
  - Hur du undviker det: Behandla UNO R4 WiFi som ett UNO R4 WiFi-kort och följ dokumentation och bibliotek för just det kortet.

- **Misstag: Att koppla 5 V-signaler till 3,3 V-pinnar.**
  - Varför det händer: USB-matning och modulmärkning kan ge falsk trygghet.
  - Hur du undviker det: Kontrollera I/O-logiknivå och 5 V-tolerans innan koppling. Använd nivåskiftare när det behövs.

- **Misstag: Att lita på att analogvärden har samma skala på alla kort.**
  - Varför det händer: Många äldre exempel antar 10-bitars ADC.
  - Hur du undviker det: Dokumentera ADC-upplösning och referensspänning. Normalisera värden där det passar.

- **Misstag: Att välja avancerat kort för ett enkelt test.**
  - Varför det händer: Mer minne, Wi-Fi och snabbare CPU känns framtidssäkert.
  - Hur du undviker det: Välj minsta kort som gör kontrollen tydligt, men inte så begränsat att det hindrar lärandet.

- **Misstag: Att missa att vissa bibliotek är plattformsberoende.**
  - Varför det händer: Arduino API ser portabelt ut, men bibliotek kan använda låg nivå.
  - Hur du undviker det: Kontrollera bibliotekets dokumentation, exempel och issues för den aktuella kortfamiljen.

- **Misstag: Att glömma USB-beteende på kort med native USB.**
  - Varför det händer: Seriell monitor och reset kan bete sig annorlunda än på klassiska USB-serie-baserade kort.
  - Hur du undviker det: Testa uppstart utan seriell monitor och använd timeout om programmet inte får fastna i `while (!Serial)`.

## Snabbreferens

- Moderna Arduino-kort ger mer minne, modernare mikrokontroller, bättre formfaktorer och ofta uppkoppling.
- Modernare är inte automatiskt bättre. Rätt kort beror på projektets krav.
- UNO R4-liknande kort är bra när du vill behålla UNO-känslan men få mer marginal.
- UNO R4 WiFi ska inte behandlas som ett generellt ESP32-kort bara för att det innehåller en ESP32-S3-baserad radiomodul.
- Nano ESP32-liknande kort passar kompakta IoT-projekt där ESP32-funktioner och liten formfaktor är viktiga.
- MKR-liknande kort är intressanta för uppkopplade och mer projektnära lösningar.
- Portenta- och specialkort passar avancerade krav men är ofta onödiga för enkla tester.
- Portering kräver kontroll av pinout, logiknivå, ADC, PWM, seriell kommunikation och bibliotek.
- Officiella moderna kort är ofta bra när dokumentation, utbildning och reproducerbarhet är viktigare än lägsta pris.
- Ett praktiskt porteringstest ger bättre beslutsunderlag än att bara läsa specifikationer.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V-logik, men kontrollera alltid datablad |
| Typiskt gränssnitt | Digital I/O, analog in, USB, I2C, SPI, UART och ibland Wi-Fi/BLE |
| Välj när | du vill ha modernare hårdvara med Arduino-arbetssätt |
| Välj inte när | du behöver maximal kompatibilitet med äldre 5 V-shields |
| Vanliga fel | fel spänningsantagande, bibliotek som bara testats på AVR, otydlig Wi-Fi-arkitektur |
| Alternativ att överväga | klassiska Arduino-kort, ESP32 DevKit, RP2040-kort |

Använd referensrutan som en snabb kontroll innan du bygger kontrollen. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När du väljer mellan moderna Arduino-kort, ESP32 och Pico, jämför med kapitel 2 och kapitel 13–15.
- När 3,3 V-logik påverkar sensorer eller äldre moduler, använd kapitel 4, 9 och 33.
- När kortet ska gå på batteri eller anslutas till strömkrävande moduler, gå vidare till kapitel 34.

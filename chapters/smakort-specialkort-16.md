# 16. Småkort, specialkort och avancerade utvecklingskort

## Kortprofil i korthet
Efter att ha gått igenom klassiska Arduino-kort, kloner, ESP8266, ESP32 och Raspberry Pi Pico är det lätt att tänka att kortvalet alltid handlar om några få stora familjer. I praktiken finns det en stor grupp Arduino-kompatibla kort som inte passar perfekt i någon av de tidigare kategorierna.

Det kan vara mycket små kort som Seeed Studio XIAO, Adafruit QT Py och Arduino Nano-liknande specialvarianter. Det kan vara kort i Adafruit Feather-format med batteriladdning och tilläggskort. Det kan vara mycket snabba kort som Teensy. Det kan vara kamerakort som ESP32-CAM. Det kan också vara avancerade Arduino-kort som Portenta, Nicla eller industriinriktade kort där målet inte bara är att blinka en LED utan att bygga mer professionella inbyggda system.

Det här kapitlet finns för att ge dig en valkarta över dessa specialkort. Målet är inte att täcka varje modell på marknaden. Målet är att du ska kunna känna igen olika typer av specialisering och förstå när specialiseringen är värdefull.

Du bör efter kapitlet kunna tänka ungefär så här:

- “Det här projektet behöver liten fysisk storlek, alltså bör jag titta på XIAO/QT Py-liknande kort.”
- “Det här projektet ska vara batteridrivet, alltså är Feather-format eller kort med bra laddningsstöd intressanta.”
- “Det här projektet kräver snabb signalbehandling eller många exakta pulser, alltså kan Teensy eller ett RP2040/RP2350-kort passa bättre än UNO.”
- “Det här projektet behöver kamera, alltså bör jag titta på ESP32-CAM eller XIAO ESP32S3 Sense-liknande kort.”
- “Det här projektet behöver robusthet, industriell integration eller mer avancerad programmiljö, alltså kan Portenta- eller Nicla-liknande kort vara relevanta.”
- “Det här projektet är fortfarande oklart, alltså bör jag inte börja med ett specialkort.”

Specialkort kan vara fantastiska när kraven är tydliga. De kan också göra ett enkelt test onödigt svårt om du väljer dem för tidigt.

## Bedöm kortet med detta i åtanke

Småkort och specialkort är praktiska när formfaktor, låg strömförbrukning, inbyggd radio, många sensorer eller industriella gränssnitt är viktigare än generell nybörjarvänlighet. Bedöm alltid logiknivå, tillgängliga GPIO, boot-pinnar, dokumentation, bibliotek och hur lätt kortet är att felsöka.

## Korttypen i praktiken

I den här boken använder vi **specialkort** som en praktisk kategori, inte som en exakt teknisk standard.

Ett kort är specialiserat om det har något av följande:

- mycket liten fysisk storlek
- inbyggd batteriladdning
- inbyggd radio, kamera, mikrofon eller display
- extra hög prestanda
- särskild formfaktor med tillbehörssystem
- industriella eller professionella funktioner
- ovanligt många eller ovanligt snabba I/O-funktioner
- säkerhetsfunktioner eller edge-AI-inriktning
- stark koppling till ett visst ekosystem av tilläggskort

Det betyder att ett specialkort inte nödvändigtvis är mer avancerat på alla sätt. Ett mycket litet kort kan vara mindre kapabelt än ett stort kort, men ändå vara rätt val eftersom det får plats i en liten kapsling. Ett kamerakort kan vara perfekt för bildinsamling men sämre för breadboardtest. Ett Portenta-kort kan vara kraftfullt men onödigt dyrt och komplext för en enkel LED-installation.

## Tre huvudfrågor vid specialkort

När du utvärderar ett specialkort bör du börja med tre frågor.

### Vad är kortets superkraft?

Varje specialkort bör ha en tydlig anledning att väljas.

Exempel på superkrafter:

- mycket liten storlek
- mycket låg energiförbrukning
- inbyggd batteriladdning
- Wi-Fi och BLE i liten formfaktor
- kamera och mikrofon
- hög CPU-prestanda
- många snabba I/O-möjligheter
- bra tillbehörsekosystem
- industriell formfaktor
- stöd för TinyML eller mer avancerad lokal analys

Om du inte kan formulera kortets superkraft är det ofta bättre att välja ett mer generellt kort.

### Vad offrar kortet?

Specialisering kostar nästan alltid något.

Vanliga kompromisser:

- färre pinnar
- sämre breadboard-vänlighet
- mindre fysisk robusthet
- mer komplicerad pinout
- 3,3 V-logik där gamla 5 V-moduler inte passar direkt
- färre färdiga exempel
- dyrare kort
- mer komplicerad uppladdning
- större beroende av en viss Arduino core
- högre strömförbrukning än väntat
- sämre analog precision än marknadsföringen antyder

Ett kort med kamera kan ha färre fria pinnar. Ett mycket litet kort kan vara svårt att koppla till många sensorer utan lödning. Ett avancerat kort kan ha mycket kapacitet men kräva mer noggrann projektstruktur.

### Är projektet moget nog?

Specialkort passar bäst när projektets krav är tydliga.

Om projektet fortfarande är i utforskande fas är det ofta bättre att börja med ett större och mer lättfelsökt kort. När sensorn, biblioteket, kopplingen och koden fungerar kan du flytta lösningen till ett mindre eller mer specialiserat kort.

Ett vanligt arbetsflöde är därför:

1. Prova sensorn eller aktuatorn på ett lättfelsökt kort.
2. Dokumentera spänning, pinnar, bibliotek och strömförbrukning.
3. Välj specialkort utifrån faktiska krav.
4. Portera koden stegvis.
5. Verifiera varje pinne och varje buss igen.
6. Mät strömförbrukningen på hela systemet, inte bara i databladet.

## Småkort: XIAO, QT Py och liknande

Småkort är kort där fysisk storlek är ett huvudargument. De används ofta i bärbara projekt, små kapslingar, sensornoder, tangentbord, diskreta installationer och prototyper där ett UNO-kort är för stort.

Typiska exempel är:

- Seeed Studio XIAO-serien
- Adafruit QT Py-serien
- vissa Arduino Nano-liknande specialkort
- små ESP32-C3, ESP32-S3 eller RP2040-kort
- små SAMD21- eller nRF52840-kort

Småkort finns ofta med olika mikrokontroller i samma fysiska familj. En XIAO-modell kan bygga på SAMD21, RP2040, ESP32-C3, ESP32-S3, nRF52840 eller RP2350. Det gör att formfaktorn kan se bekant ut samtidigt som egenskaperna skiljer sig kraftigt.

### När småkort passar

Småkort är bra när:

- kapslingen är liten
- projektet ska bäras på kroppen
- kortet ska sitta nära en sensor
- du behöver USB-C i liten formfaktor
- du vill ha ett kompakt kort för permanent installation
- du bara behöver ett begränsat antal pinnar
- du redan vet vilken sensor eller aktuator som ska användas

Exempel:

- en liten temperatur- och luftfuktighetsnod
- ett tangentbords- eller makropadsprojekt
- en liten LED-badge
- en diskret närvarosensor
- en batteridriven BLE-sensor
- ett litet kamera- eller mikrofonexperiment

### När småkort inte passar

Småkort är ofta sämre när:

- du fortfarande experimenterar mycket på breadboard
- du behöver många pinnar
- du behöver robusta skruvterminaler
- du vill koppla många moduler samtidigt
- du är osäker på spänningsnivåer
- du vill att elever eller kollegor enkelt ska kunna följa kopplingen
- du behöver mycket fysisk hållbarhet

Ett litet kort kan vara svårare att felsöka eftersom anslutningarna är täta och märkningen ibland är minimal.

### Praktiska kontroller för småkort

Innan du bygger vidare med ett småkort bör du dokumentera:

| Kontroll | Varför den behövs |
|---|---|
| Exakt modell | Samma formfaktor kan innehålla olika mikrokontroller |
| Logiknivå | Många småkort är 3,3 V |
| Pinout | Silkscreen-namn kan skilja sig från GPIO och Arduino-namn |
| I2C-pinnar | Småkort har ofta rekommenderade standardpinnar |
| Batteristöd | Vissa har laddning, andra inte |
| Boot-knappar | Småkort kan kräva särskilda knappsekvenser |
| Interna enheter | LED, flash, radio, kamera eller mikrofon kan använda pinnar |
| Antennplacering | Viktigt för Wi-Fi och BLE |
| Lödytor | Vissa pinnar finns bara som pads, inte headers |

### Kodmönster: dokumentera pinout tidigt

För småkort är det extra viktigt att inte sprida pinnummer över hela koden.

```cpp
// Board profile: compact sensor node
// Board: Example XIAO-style ESP32-S3 board
// Logic level: 3.3 V
// Notes: Verify actual pin mapping against the board documentation.

constexpr int STATUS_LED_PIN = 21;
constexpr int SENSOR_POWER_PIN = 7;
constexpr int BUTTON_PIN = 6;

constexpr unsigned long BLINK_INTERVAL_MS = 500;

void setup() {
  pinMode(STATUS_LED_PIN, OUTPUT);
  pinMode(SENSOR_POWER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  digitalWrite(SENSOR_POWER_PIN, HIGH);
}

void loop() {
  static unsigned long lastToggle = 0;
  static bool ledState = false;

  const unsigned long now = millis();

  if (now - lastToggle >= BLINK_INTERVAL_MS) {
    lastToggle = now;
    ledState = !ledState;
    digitalWrite(STATUS_LED_PIN, ledState ? HIGH : LOW);
  }
}
```

Kommentaren längst upp är inte prydnad. Den är en del av projektets dokumentation. På specialkort är sådan dokumentation ofta skillnaden mellan ett experiment som går att återskapa och ett experiment som bara fungerar på ditt skrivbord.

## Feather-formatet

Adafruit Feather är både en formfaktor och ett ekosystem. Feather-kort är ofta små men inte extremt små. De är vanligen utformade för batteriprojekt och har ofta LiPo-anslutning, laddkrets och ett stort utbud av tilläggskort, så kallade FeatherWings.

Det finns Feather-kort med många olika mikrokontroller och radiofunktioner:

- SAMD-baserade kort
- RP2040-baserade kort
- ESP32-S2/S3-baserade kort
- nRF52840-baserade BLE-kort
- LoRa-radio
- displayvarianter
- sensorkort
- datalogging-tillägg

### När Feather passar

Feather-formatet passar när:

- batteridrift är viktigt
- du vill ha ett tillbehörsekosystem
- du vill bygga något mer permanent än ett löst breadboardtest
- du vill kunna stapla eller kombinera tillägg
- du vill ha en tydligare projektformfaktor än ett generiskt DevKit-kort

Exempel:

- bärbar miljölogger
- trådlös sensornod
- liten displayenhet
- prototyp med LiPo-laddning
- portabel mätutrustning

### När Feather inte passar

Feather är inte alltid rätt val.

Välj något annat om:

- du behöver lägsta möjliga pris
- du behöver UNO-shield-kompatibilitet
- du vill ha maximal breadboard-yta
- projektet kräver fler pinnar än kortet exponerar
- du vill undvika beroende av ett visst tillbehörsekosystem
- du inte behöver batteridrift

Feather är ofta mer genomtänkt än många billiga utvecklingskort, men också dyrare. Det kan vara ett mycket bra val när byggkvalitet, dokumentation och batteristöd sparar tid.

## Teensy: när prestanda och timing är huvudfrågan

Teensy-korten från PJRC är Arduino-kompatibla i den meningen att de används med Arduino IDE via Teensyduino, men de har ofta betydligt högre prestanda än klassiska Arduino-kort.

Teensy är särskilt intressanta för:

- ljudprojekt
- snabba LED-installationer
- många samtidiga signaler
- USB-MIDI och USB-HID
- realtidsnära styrning
- mätprojekt med höga datatakter
- projekt där CPU-prestanda och timing är viktigare än Wi-Fi

Teensy 4.x-familjen är kraftfull jämfört med klassiska Arduino-kort. Den kan därför vara ett mycket bra val när ett projekt är för tungt för UNO/Nano men inte behöver ESP32:s trådlösa funktioner.

### När Teensy passar

Välj Teensy när:

- projektet behöver hög prestanda
- timing är viktig
- ljud eller USB-funktioner är centrala
- du behöver många pinnar i liten formfaktor
- du vill ha ett moget ekosystem för avancerade mikrokontrollerprojekt
- du kan acceptera 3,3 V-logik och läsa dokumentationen noggrant

### När Teensy inte passar

Välj något annat när:

- projektet är enkelt och undervisningsinriktat
- du behöver inbyggt Wi-Fi
- du vill ha billigaste möjliga kort
- du vill ha maximal Arduino-nybörjarkompatibilitet
- du behöver 5 V-logik på I/O
- du inte vill hantera en separat tilläggsmiljö

### Typisk fallgrop

En vanlig fallgrop är att välja Teensy för att kortet är snabbt, men sedan koppla in 5 V-moduler som om det vore en klassisk Arduino UNO. Många moderna högprestandakort använder 3,3 V-logik och kan skadas av fel nivåer.

Prestanda ersätter inte nivåkontroll.

## ESP32-CAM och kamerakort

ESP32-CAM och liknande kamerakort är populära eftersom de kombinerar låg kostnad, Wi-Fi och kamera. De är också en av de vanligaste källorna till frustration i Arduino-projekt.

Kamerakort har ofta flera kompromisser:

- få fria pinnar
- svag eller känslig strömförsörjning
- ibland ingen inbyggd USB-serieadapter
- boot-pinnar som redan är svåra att hantera
- kamera och SD-kort som använder många interna signaler
- behov av stabil 5 V- eller 3,3 V-matning beroende på kortets konstruktion
- mer komplicerad uppladdning än vanliga DevKit-kort

### När ESP32-CAM passar

Välj ESP32-CAM eller liknande när:

- projektet faktiskt behöver bild
- låg kostnad är viktig
- Wi-Fi-baserad bildöverföring räcker
- du accepterar begränsad I/O
- du kan lägga tid på strömförsörjning och felsökning

Exempel:

- enkel övervakningskamera i testmiljö
- bildbaserad närvarodetektion
- tidsstyrd bildtagning
- lokal bildinsamling till SD-kort
- demonstrationsprojekt kring kamera och Wi-Fi

### När ESP32-CAM inte passar

Välj något annat när:

- du bara behöver en sensor utan bild
- du behöver många pinnar till annat
- du vill ha enkel breadboard-uppkoppling
- du behöver stabil produktion med minimal felsökning
- du behöver hög bildkvalitet eller avancerad bildanalys
- du inte vill hantera extern USB-serieadapter eller uppladdningsläge

För mer avancerade kamera- och ML-prototyper kan ett modernare ESP32-S3-baserat kort med kamera, PSRAM, USB-C och bättre dokumentation vara lättare att arbeta med än en klassisk ESP32-CAM-modul.

## Kort med kamera, mikrofon och TinyML-inriktning

Vissa moderna småkort kombinerar mikrokontroller, kamera, mikrofon, PSRAM och ibland SD-kort. Exempel är XIAO ESP32S3 Sense-liknande kort och andra ESP32-S3-baserade vision-kort.

De är intressanta när projektet behöver:

- enkel bildinsamling
- ljudinsamling
- lokal klassificering
- TinyML-prototyper
- kompakt sensormodul
- låg kostnad jämfört med större Linux-baserade kort

Men de kräver ett annat tänk än vanliga sensorer. Bild och ljud skapar mycket mer data än temperatur, ljus eller knapptryckningar. Det påverkar minne, strömförbrukning, lagring, överföring och felsökning.

### Arduino passar inte alltid bäst

Även om kortet kan programmeras med Arduino IDE är Arduino inte alltid bästa miljön för allt som rör kamera och maskininlärning. Ibland passar tillverkarens exempel, ESP-IDF, MicroPython, CircuitPython eller ett färdigt ML-ramverk bättre.

Det betyder inte att du ska undvika Arduino. Det betyder att du ska vara tydlig med målet:

- Vill du snabbt testa kamera och Wi-Fi?
- Vill du bygga en robust produkt?
- Vill du förstå varje rad kod?
- Vill du använda färdiga ML-bibliotek?
- Vill du undervisa principen snarare än optimera prestanda?

Valet av miljö bör följa målet.

## Portenta, Nicla och mer professionella Arduino-kort

Arduino-ekosystemet innehåller även kort som inte främst riktar sig till enkla hobbyprojekt. Portenta- och Nicla-liknande kort är exempel på mer avancerade plattformar med fokus på industri, edge computing, maskininlärning, avancerad kommunikation, kompakt professionell formfaktor eller integrerade sensorer.

Dessa kort kan innehålla eller stödja:

- kraftfullare mikrokontroller
- flera kärnor
- Wi-Fi och Bluetooth
- säkerhetskretsar
- industriella anslutningar via carrier boards
- kamera- eller displaygränssnitt
- sensorer för rörelse, miljö eller ljud
- stöd för både Arduino-liknande kod och andra miljöer

### När avancerade Arduino-kort passar

Välj avancerade Arduino-kort när:

- projektet behöver professionell formfaktor
- du vill hålla dig inom Arduino-ekosystemet men behöver mer kapacitet
- du vill kombinera realtidsnära styrning med mer avancerad analys
- du behöver bättre dokumentation och längre livscykel än billiga kloner
- du vill bygga prototyper som liknar en industriell lösning
- kostnaden är mindre viktig än robusthet och utvecklingstid

### När de inte passar

Välj enklare kort när:

- du bara ska lära dig en sensor
- projektet är kostnadskänsligt
- du behöver många enkla testkort
- du vill ha maximal community-mängd kring varje problem
- du inte behöver professionella funktioner
- du inte vill hantera mer avancerad dokumentation

Avancerade kort är ofta bäst när problemet redan är välformulerat. De är sällan bästa startpunkt för att förstå en enkel sensor.

## Specialkort med radio: LoRa, BLE och mobilnät

Vissa kort är specialiserade på kommunikation. Det kan handla om LoRa, BLE, Thread, Zigbee-liknande radio, mobilnät eller annan långdistanskommunikation.

Arduino-kompatibla radiokort används ofta för:

- sensornätverk
- utomhusmätningar
- batteridrivna noder
- fjärrövervakning
- gateway-projekt
- lokal kommunikation utan Wi-Fi
- låg bandbredd över längre avstånd

Radiokort kräver extra omsorg.

Du behöver kontrollera:

- frekvensband och regionala regler
- antenntyp och antennkontakt
- sändningseffekt
- strömförbrukning vid sändning
- bibliotekets nätverksmodell
- kryptering och identifiering
- räckvidd i verklig miljö
- om gateway eller mottagare krävs

Ett radiokort är sällan bara “ett Arduino-kort med extra funktion”. Radion påverkar hela systemdesignen.

## Specialkort med inbyggda sensorer

Det finns kort som redan har sensorer monterade: accelerometer, IMU, mikrofon, temperatur, tryck, ljus, färg, gester eller miljödata. De kan vara mycket praktiska när du snabbt vill bygga en demonstrator.

Fördelar:

- färre lösa kopplingar
- snabbare start
- ofta färdiga exempel
- kompakt konstruktion
- mindre risk för felkopplade sensorer

Nackdelar:

- sensorn sitter där kortet sitter, inte nödvändigtvis där mätningen bör göras
- svårare att byta sensor
- intern värme kan påverka temperaturmätning
- färre fria pinnar
- ibland sämre dokumentation kring intern pinanvändning
- risk att kortet blir för dyrt för enkla projekt

Exempel: Ett kort med inbyggd IMU är perfekt för att prova rörelse. Det är inte alltid perfekt om IMU:n behöver sitta mekaniskt isolerad från mikrokontrollern eller monteras i en viss riktning långt från USB-kabeln.

## Jämförelse: specialkort i praktiken

| Korttyp | Styrka | Typisk kompromiss | Bra första test |
|---|---|---|---|
| XIAO/QT Py-liknande småkort | Mycket liten formfaktor | Få pinnar och tät pinout | Kompakt I2C-sensor |
| Feather | Batteri och tillbehörsekosystem | Dyrare än lågkostnadskort | Batteridriven datalogger |
| Teensy | Prestanda och timing | Ingen inbyggd Wi-Fi på de flesta modeller | Snabb LED- eller ljuddemo |
| ESP32-CAM | Kamera och Wi-Fi billigt | Få fria pinnar och känslig uppladdning | Enkel kameraserver |
| ESP32-S3 Sense-liknande kort | Kamera, mikrofon och PSRAM | Mer minnes- och biblioteksfrågor | Enkel bild- eller ljudtrigger |
| Portenta-liknande kort | Professionell kapacitet | Kostnad och komplexitet | Edge- eller industriell prototyp |
| LoRa/BLE-specialkort | Kommunikationsprofil | Radio kräver systemdesign | Enkel fjärrsensor |
| Kort med inbyggda sensorer | Snabb demonstrator | Mindre flexibel placering | Rörelse- eller miljödemo |

Tabellen ska inte användas som en absolut regel. Den ska hjälpa dig att ställa rätt första frågor.

## Att skapa en kortprofil

För specialkort bör du alltid skapa en kortprofil innan du bygger större kod.

En kortprofil kan se ut så här:

```text
Kortprofil

Kortmodell: Seeed Studio XIAO ESP32S3 Sense
Mikrokontroller: ESP32-S3
Logiknivå: 3,3 V
Matning under experiment: USB-C
Batteristöd: kontrollera aktuell kortdokumentation
Inbyggda funktioner: kamera, mikrofon, PSRAM, SD-stöd beroende på variant
Arduino board-val: kontrollera installerad ESP32 core och vald board
I2C-pinnar: dokumentera enligt aktuell pinout
SPI-pinnar: dokumentera enligt aktuell pinout
Boot-/strap-pinnar: undvik i första versionen
Intern LED: kontrollera om den finns och om logiken är inverterad
Fria pinnar i projektet: lista explicit
Risker: kamera/SD kan använda pinnar; 3,3 V-logik; strömspikar
```

Det viktiga är inte exakt format. Det viktiga är att du tvingar dig själv att kontrollera kortets verkliga egenskaper.

### Kodmönster: profilbaserad konfiguration

I kod kan du samla kortspecifika val på ett ställe.

```cpp
// Board profile: portable sensor display
// Board: Feather-style ESP32-S3
// Logic level: 3.3 V
// Power: USB during development, LiPo in field test
// Interfaces: I2C display + digital button

constexpr int STATUS_LED_PIN = 13;
constexpr int USER_BUTTON_PIN = 0;
constexpr int SENSOR_ENABLE_PIN = 12;

constexpr unsigned long SENSOR_WARMUP_MS = 100;
constexpr unsigned long SAMPLE_INTERVAL_MS = 1000;

void enableSensorPower() {
  digitalWrite(SENSOR_ENABLE_PIN, HIGH);
  delay(SENSOR_WARMUP_MS);
}

void setup() {
  Serial.begin(115200);

  pinMode(STATUS_LED_PIN, OUTPUT);
  pinMode(USER_BUTTON_PIN, INPUT_PULLUP);
  pinMode(SENSOR_ENABLE_PIN, OUTPUT);

  enableSensorPower();

  Serial.println("Board profile loaded: portable sensor display");
}

void loop() {
  static unsigned long lastSample = 0;
  const unsigned long now = millis();

  if (now - lastSample >= SAMPLE_INTERVAL_MS) {
    lastSample = now;

    const bool buttonPressed = digitalRead(USER_BUTTON_PIN) == LOW;

    Serial.print("Button pressed: ");
    Serial.println(buttonPressed ? "yes" : "no");

    digitalWrite(STATUS_LED_PIN, buttonPressed ? HIGH : LOW);
  }
}
```

Detta är inte en avancerad sketch. Poängen är strukturen. När kortet senare byts ut behöver du ändra profilen, inte leta pinnummer överallt.

## Valguide

### Välj småkort när fysisk storlek styr

Småkort är rätt när kortet ska få plats i en liten kapsling, bäras på kroppen eller monteras nära sensorn. Kontrollera bara att antalet pinnar räcker och att lödning eller kontakter passar ditt arbetssätt.

### Välj Feather-liknande kort när batteridrift och tillbehör spelar roll

Feather-formatet är ofta bra när du vill göra en portabel prototyp med laddbart batteri och tilläggskort. Det är mindre bra om du bara vill ha billigast möjliga mikrokontroller.

### Välj Teensy när prestanda och timing är viktigare än radio

Teensy passar när du behöver snabb I/O, ljud, USB eller mycket beräkning i mikrokontrollerformat. Det är inte första valet för enkla Wi-Fi-sensorer.

### Välj ESP32-CAM när bild är själva poängen

Om du inte behöver kamera är ESP32-CAM ofta mer besvärligt än nödvändigt. Om du behöver kamera kan det däremot vara en fantastisk testplattform.

### Välj Portenta/Nicla-liknande kort när projektet börjar likna professionell prototyp

Dessa kort är motiverade när du behöver robustare ekosystem, mer kapacitet, industriell anslutning, integrerade sensorer eller edge-inriktning. De är sällan motiverade för första kontrollen med en enkel sensor.

### Välj radiokort när kommunikation är huvudkravet

LoRa, BLE och andra radioprofiler ska väljas utifrån systemets kommunikationskrav, inte bara för att kortet verkar spännande. Börja med att definiera räckvidd, bandbredd, strömförbrukning och mottagarsida.

## Referensmönster: kortprofil innan specialkortet byggs in

Ett specialkort bör få en kort profil innan det blir del av ett större projekt. Profilen bekräftar uppladdning, seriell monitor, grundläggande I/O, logiknivå och den buss projektet behöver. Det minskar risken att du felsöker applikationskod när problemet egentligen är pinout, USB-beteende, bootläge eller matning.

### Det här behöver du kontrollera

- exakt kortmodell, inte bara kortfamilj
- mikrokontroller, modul och eventuell radiokrets
- logiknivå och tillåten matning
- Arduino board-val och eventuell särskild uppladdningssekvens
- USB-beteende och seriell monitor
- säkra testpinnar
- boot-, strap- eller riskpinnar att undvika
- den buss projektet behöver, till exempel I2C, SPI eller UART

### Identifiera kortet

Spara en enkel kortprofil innan kopplingen växer.

```text
Kortmodell:
Mikrokontroller:
Logiknivå:
Matning:
Arduino board-val:
USB-beteende:
Inbyggda enheter:
Valda testpinnar:
Riskpinnar att undvika:
Första projektidé:
```

Undvik generiska namn som “ESP32-kort” eller “litet Arduino-kort”. Exakt modell är viktig när du väljer pinout, board package och matning.

### Kontrollera USB och seriell monitor

Ladda upp en minimal sketch innan externa moduler ansluts.

```cpp
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Special board profile started");
}

void loop() {
  static unsigned long counter = 0;

  Serial.print("Counter: ");
  Serial.println(counter++);

  delay(1000);
}
```

Notera om kortet behöver manuell reset, särskild boot-knapp, annan port efter uppladdning eller extra väntetid innan seriell monitor fungerar.

### Välj säkra testpinnar

Testa först en dokumenterat säker utgång. Byt `TEST_OUTPUT_PIN` till en pinne som verkligen är säker för ditt kort.

```cpp
constexpr int TEST_OUTPUT_PIN = 13;

void setup() {
  pinMode(TEST_OUTPUT_PIN, OUTPUT);
}

void loop() {
  digitalWrite(TEST_OUTPUT_PIN, HIGH);
  delay(250);
  digitalWrite(TEST_OUTPUT_PIN, LOW);
  delay(250);
}
```

Om kortet har inbyggd LED kan du använda den, men kontrollera om LED-logiken är inverterad.

Testa sedan en säker ingång med intern pull-up.

```cpp
constexpr int BUTTON_PIN = 6;

void setup() {
  Serial.begin(115200);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  const bool pressed = digitalRead(BUTTON_PIN) == LOW;

  Serial.print("Button: ");
  Serial.println(pressed ? "pressed" : "released");

  delay(100);
}
```

Välj inte en boot-relaterad pinne eller en pinne som används av intern hårdvara.

### Kontrollera bussen projektet behöver

Om kortet ska användas med sensorer, testa I2C med en scanner innan du använder ett sensorbibliotek.

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  delay(1000);

  Wire.begin();

  Serial.println("I2C scan started");

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    const byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Found I2C device at 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.println(address, HEX);
    }
  }

  Serial.println("I2C scan finished");
}

void loop() {
}
```

Om inget hittas, kontrollera SDA/SCL-pinnar, matningsspänning, gemensam jord, pull-up-motstånd, kabeldragning och sensoradress innan bibliotekskoden felsöks.

### Beslut före integration

Innan specialkortet byggs in i projektet bör du veta:

| Fråga | Praktisk betydelse |
|---|---|
| Fungerar uppladdning stabilt? | annars blir varje fel svårare att felsöka |
| Är pinout tydlig? | annars riskerar du fel koppling |
| Fungerar seriell monitor efter reset? | annars saknas grunddiagnostik |
| Passar logiknivån modulerna? | annars behövs nivåskiftning eller annat kort |
| Räcker antalet säkra pinnar? | annars blir specialkortet snabbt en begränsning |
| Finns riskpinnar som stör projektet? | annars kan kortet starta i fel läge |
| Finns bra bibliotek för huvudfunktionen? | annars ökar integrationsrisken |
| Behöver matningen testas mer? | särskilt för radio, kamera, motorer och displayer |

Det viktiga är inte att kortet får “ja” på allt. Det viktiga är att du vet vilka risker du tar med dig.

## Vanliga misstag

- **Misstag: Att välja ett specialkort för att det verkar häftigt.**
  - **Varför det händer:** Små, snabba eller kamera-/AI-inriktade kort känns inspirerande.
  - **Hur man undviker det:** Skriv projektets krav först och välj kort efter kraven.

- **Misstag: Att anta att samma formfaktor betyder samma egenskaper.**
  - **Varför det händer:** XIAO-, Feather- och Nano-liknande kort kan se likadana ut.
  - **Hur man undviker det:** Kontrollera mikrokontroller, logiknivå, pinout och Arduino board-val för exakt modell.

- **Misstag: Att använda fel pinne för att silkscreen och GPIO blandas ihop.**
  - **Varför det händer:** Småkort har ofta flera namn för samma fysiska anslutning.
  - **Hur man undviker det:** Dokumentera fysisk pinne, silkscreen-namn och kodens pinnummer i kortprofilen.

- **Misstag: Att glömma att intern hårdvara använder pinnar.**
  - **Varför det händer:** Kamera, SD-kort, PSRAM, LED, laddkrets eller radio syns inte alltid i enkel pinout.
  - **Hur man undviker det:** Läs avsnitt om intern pinanvändning innan du väljer pinnar.

- **Misstag: Att underskatta strömförsörjning.**
  - **Varför det händer:** Kortet fungerar via USB på skrivbordet men blir instabilt med batteri eller Wi-Fi.
  - **Hur man undviker det:** Mät ström i flera driftlägen och kontrollera regulatorns kapacitet.

- **Misstag: Att börja med kamera eller radio innan grundtesterna fungerar.**
  - **Varför det händer:** Man vill snabbt testa kortets mest spännande funktion.
  - **Hur man undviker det:** Verifiera först uppladdning, seriell monitor, LED, knapp och eventuell I2C-buss.

## Snabbreferens

- Specialkort är bäst när projektets krav matchar kortets specialisering.
- Småkort passar när fysisk storlek är viktig, men kräver mer noggrann pinout-kontroll.
- Feather-liknande kort är ofta starka för batteridrivna och modulära projekt.
- Teensy passar när prestanda, timing, ljud eller USB-funktioner är viktigare än radio.
- ESP32-CAM och liknande kort är bra när kamera är huvudfunktionen, men de kan vara svåra som allmänna utvecklingskort.
- ESP32-S3 Sense-liknande kort öppnar för kamera, mikrofon och TinyML, men kräver mer minnes- och biblioteksmedvetenhet.
- Portenta- och Nicla-liknande kort passar när projektet börjar likna professionell prototyp eller edge-system.
- Radiokort ska väljas utifrån kommunikationskrav, inte bara för att radio verkar användbart.
- För varje specialkort bör du skapa en kortprofil innan du bygger större projekt.
- Om du inte kan formulera varför specialkortet behövs är ett mer generellt kort ofta bättre.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V-logik |
| Typiskt gränssnitt | Varierar: USB, I2C, SPI, UART, kamera, radio eller snabb I/O |
| Välj när | formfaktor eller specialfunktion är avgörande |
| Välj inte när | du fortfarande utforskar kraven och behöver enkel breadboard-felsökning |
| Vanliga fel | svårläst pinout, små lödpads, begränsad dokumentation, värme |
| Alternativ att överväga | UNO/Nano, ESP32 DevKit, Feather/XIAO-varianter |

Använd referensrutan som en snabb kontroll innan du bygger kontrollen. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När specialkortet väljs för formfaktor, ström eller inbyggda funktioner, jämför med kapitel 2.
- När kortet har ovanlig pinout eller annan logiknivå, kontrollera kapitel 4 och kapitel 3.
- När kortet blir del av en permanent modul, gå vidare till kapitel 36.

# 10. Klassiska Arduino-kort: UNO, Nano och Mega

## Kortprofil i korthet
De klassiska Arduino-korten är fortfarande en av de bästa ingångarna till praktiska elektronikprojekt, även när modernare kort har mer minne, snabbare processor, Wi-Fi, Bluetooth och bättre energilägen. UNO, Nano och Mega är enkla att förstå, enkla att koppla till vanliga moduler och väl dokumenterade. Många exempel på nätet, många bibliotek och många shields är skrivna med just dessa kort i åtanke.

Det gör dem värdefulla även för dig som redan kan programmera. När du vill testa en sensor, förstå en buss, felsöka en modul eller bygga ett snabbt experiment är ett klassiskt Arduino-kort ofta ett bra första val. Det är inte alltid det bästa slutliga valet, men det kan vara den snabbaste vägen till fungerande kunskap.

Det här kapitlet fokuserar på tre välkända korttyper:

- Arduino UNO
- Arduino Nano
- Arduino Mega

De har olika formfaktor och olika mängd I/O, men de delar mycket av samma programmeringsmodell och mycket av samma pedagogiska styrka. De är tillräckligt begränsade för att vara begripliga och tillräckligt användbara för att fortfarande dyka upp i riktiga projekt.

Samtidigt är det viktigt att inte romantisera dem. Klassiska AVR-baserade Arduino-kort har begränsat minne, begränsad processorkraft, ingen inbyggd nätverkskommunikation, relativt enkel ADC och ofta sämre energiegenskaper än specialiserade moderna alternativ. Om du väljer ett klassiskt kort bör det vara för att dess styrkor passar projektet, inte för att det råkar vara det första kortet du hittade i lådan.

## Bedöm kortet med detta i åtanke

Jämför klassiska Arduino-kort utifrån projektets verkliga krav: antal pinnar, logiknivå, minne, analog mätning, fysisk formfaktor och hur mycket extra elektronik som krävs runt kortet.

## Kortfamiljen i praktiken

Ett klassiskt Arduino-kort ger dig en liten mikrokontroller med ett standardiserat sätt att skriva, kompilera och ladda upp kod. Du skriver en sketch med `setup()` och `loop()`, väljer kort i utvecklingsmiljön och laddar upp via USB.

Det är en mycket enkel modell:

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

För nybörjare är detta lätt att förstå. För en erfaren programmerare är styrkan en annan: modellen gör det snabbt att isolera ett hårdvaruproblem. Du kan skriva en minimal sketch, testa en pinne, läsa en sensor, skriva ut värden till seriell monitor och veta att väldigt få lager ligger mellan din kod och hårdvaran.

Det är en stor skillnad mot mer komplexa plattformar där Wi-Fi-stack, RTOS, flera kärnor, avancerade drivrutiner eller energilägen kan påverka beteendet. De klassiska kortens enkelhet gör dem till bra referenskort.

## UNO som referenskort

Arduino UNO är ofta det kort som exempel, tutorials, shields och bibliotek antar implicit. Även när ett exempel inte säger UNO är det ofta skrivet med UNO-liknande pinout och begränsningar i åtanke.

UNO passar särskilt bra när du vill ha:

- enkel koppling på breadboard eller med dupontkablar
- tydlig fysisk layout
- många kompatibla shields
- 5 V-logik
- stabilt bibliotekstöd
- en pedagogisk referensplattform
- snabb felsökning av sensorer och enkla moduler

UNO är däremot inte alltid ett bra slutligt val. Kortet är relativt stort, har begränsat minne, saknar inbyggd nätverkskommunikation och har färre pinnar än större kort. Om projektet ska bli kompakt, batteridrivet, uppkopplat eller ha många sensorer kan ett annat kort vara lämpligare.

Ett bra sätt att tänka på UNO är: välj UNO när du vill förstå och verifiera. Byt kort när projektets krav tydligt pekar åt ett annat håll.

## Nano som kompakt klassiker

Arduino Nano fyller ungefär samma pedagogiska roll som UNO men i ett mindre format. Många Nano-varianter är breadboardvänliga och passar bättre i prototyper där kortet ska sitta kvar på en kopplingsplatta eller i en liten låda.

Nano passar särskilt bra när du vill ha:

- liten formfaktor
- UNO-liknande programmeringsmodell
- många exempel som fungerar med små ändringar
- kort som kan sitta på breadboard
- enkel permanent prototyp
- låg kostnad, särskilt med kompatibla varianter

Nano har ofta samma typ av begränsningar som UNO om den bygger på ATmega328P: begränsat SRAM, begränsat flashminne, begränsad klockfrekvens och ingen inbyggd trådlös kommunikation. Dess lilla format innebär också att pinout och märkning kan vara svårare att läsa, särskilt på kloner.

Nano är ofta ett bra val när du har testat ett experiment på UNO och vill göra det mer kompakt utan att byta programmeringsmodell.

## Mega när du behöver många pinnar

Arduino Mega är det klassiska valet när UNO-liknande enkelhet inte räcker för att du behöver många I/O-pinnar, flera seriella portar eller mer minne. Mega bygger typiskt på ATmega2560 och har betydligt fler digitala pinnar, fler analoga ingångar och flera hårdvaru-UART:ar.

Mega passar särskilt bra när du vill ha:

- många digitala pinnar
- många analoga ingångar
- flera seriella portar
- många anslutna moduler samtidigt
- kompatibilitet med delar av Arduino-shield-ekosystemet
- enkelhet framför modern prestanda

Mega är vanligt i projekt med displayer, knappsatser, reläbanker, många sensorer, enklare robotik och undervisningsmiljöer där det är praktiskt att ha många pinnar synliga.

Det är däremot viktigt att förstå att Mega inte är en modernare Arduino i alla avseenden. Den ger fler resurser än UNO, men den är fortfarande en klassisk AVR-plattform. Om du behöver Wi-Fi, Bluetooth, högre beräkningsprestanda eller bättre energilägen är ESP32, RP2040/Pico eller ett modernare Arduino-kort ofta mer rimligt.

## Jämförelse mellan UNO, Nano och Mega

Tabellen nedan är en praktisk sammanfattning. Exakta specifikationer kan variera mellan officiella kort och kompatibla varianter, men jämförelsen räcker för de flesta designbeslut.

| Korttyp | Typisk styrka | Typisk begränsning | Bra när |
|---|---|---|---|
| UNO | Tydlig referensplattform | Stor formfaktor och begränsat minne | Du vill testa, lära, felsöka eller använda shields |
| Nano | Kompakt UNO-liknande format | Små pinnar och ofta klonvariationer | Du vill bygga kompakt breadboardprototyp |
| Mega | Många pinnar och flera seriella portar | Fortfarande klassisk AVR utan nätverk | Du behöver mycket I/O men vill behålla enkel Arduino-modell |

En annan viktig skillnad är arbetsflödet. UNO är ofta bäst på skrivbordet när du provar saker. Nano är bra när experimentet ska bli en liten prototyp. Mega är bra när du vill koppla in mycket samtidigt utan att direkt behöva I/O-expanders.

## 5 V-logik som styrka och risk

Många klassiska Arduino-kort använder 5 V-logik. Det är praktiskt eftersom många äldre moduler, relämoduler, LCD-displayer, enklare sensorer och hobbyelektronik är byggda för 5 V. En 5 V-Arduino kan därför vara mycket lätt att kombinera med klassiska komponenter.

Men 5 V-logik är också en risk. Många moderna sensorer, breakout boards, ESP-baserade moduler, IMU:er och displayer är 3,3 V-enheter. En 5 V-signal in i en 3,3 V-krets kan skada komponenten om modulen inte har nivåskiftning eller skydd.

Grundregeln är enkel:

- En 5 V-Arduino kan ofta läsa 3,3 V som HIGH, men kontrollera gränserna.
- En 5 V-Arduino ska inte automatiskt skriva 5 V till en 3,3 V-ingång.
- I2C mellan 5 V och 3,3 V kräver särskild uppmärksamhet eftersom pull-up-motstånd bestämmer bussens nivå.
- Färdiga moduler kan ha nivåskiftning, men anta inte det utan att kontrollera.

Det här är ett av de vanligaste skälen att välja ett modernare 3,3 V-kort i projekt där många moderna sensorer används. Om alla sensorer redan är 3,3 V kan ett 3,3 V-native kort ge färre risker än ett 5 V-kort med många nivåskiftare.

## Minnesbegränsningar

För en erfaren programmerare kan det vara lätt att underskatta hur lite minne klassiska kort har. En ATmega328P-baserad UNO eller Nano har mycket begränsat SRAM jämfört med moderna mikrokontrollers. Det påverkar särskilt projekt med:

- stora strängar
- JSON
- buffertar
- displaygrafik
- många bibliotek samtidigt
- tabeller och lookup-data
- nätverkskod via extern modul
- datalogging med större rader

När minnet tar slut beter sig programmet inte alltid på ett snyggt sätt. Det kan bli omstarter, konstiga mätvärden, korrupt text, hängningar eller fel som bara dyker upp ibland.

Praktiska råd:

- Undvik stora globala buffertar om de inte behövs.
- Var försiktig med dynamiska `String`-objekt i långkörande program.
- Skriv ut ledigt minne vid felsökning om projektet beter sig märkligt.
- Dela upp experiment så du vet vilket bibliotek eller vilken funktion som ökar minnestrycket.
- Välj Mega, ESP32, RP2040 eller annan plattform om projektet naturligt kräver mer minne.

I den här boken kommer klassiska kort ofta användas för små, tydliga experiment. När experimenten blir mer nätverksorienterade, displaytunga eller datatunga kommer andra kortfamiljer ofta vara bättre.

## Pinout och specialpinnar

På klassiska Arduino-kort är inte alla pinnar likvärdiga. Vissa pinnar har särskilda funktioner:

- UART använder särskilda RX/TX-pinnar.
- I2C ligger på särskilda pinnar eller duplicerade kontaktpunkter.
- SPI ligger på bestämda pinnar och ofta även på ICSP-headern.
- PWM finns bara på vissa digitala pinnar.
- Externa interrupt finns bara på vissa pinnar på mindre AVR-kort.
- Den inbyggda LED:en är kopplad till en viss pinne.

Det här betyder att ett projekt kan fungera på UNO men behöva små ändringar på Mega, eller tvärtom. Det betyder också att en shield kan anta en viss pinout medan din egen koppling använder samma pinnar till något annat.

Ett återkommande arbetssätt i boken är därför att alltid skapa en pin mapping i början av experimentkoden.

```cpp
const uint8_t PIN_STATUS_LED = 13;
const uint8_t PIN_BUTTON = 2;
const uint8_t PIN_SENSOR_POWER = 7;
```

Det är bättre än att sprida råa pinnummer genom koden. När du senare byter från UNO till Nano, Mega eller ESP32 blir det tydligare vad som behöver ändras.

## Shields och formfaktor

UNO och Mega har en fysisk formfaktor som gjort shields populära. Ett shield är ett tilläggskort som monteras ovanpå Arduino-kortet och ger funktioner som motorstyrning, reläer, Ethernet, prototypyta, display eller sensorer.

Shields kan vara mycket praktiska, men de har tre vanliga fallgropar:

- De använder pinnar utan att det alltid är tydligt.
- De kan vara designade för 5 V-logik.
- De kan krocka med andra shields eller egna kopplingar.

När du använder ett shield bör du dokumentera vilka pinnar det använder innan du lägger till fler moduler. Det är samma princip som beroenden i mjukvara: ett shield konsumerar resurser i hårdvaran.

Nano har inte samma shield-formfaktor, men är ofta enklare att använda på breadboard eller i mindre prototyper. Mega kan använda många UNO-liknande shields, men alla shields är inte fullt kompatibla med Mega eftersom vissa buss- eller pinnantaganden kan skilja sig.

## När klassiska kort är rätt val

Ett klassiskt Arduino-kort är ofta rätt val när projektets kärna är enkel I/O, tydlig koppling och snabb förståelse.

Välj UNO, Nano eller Mega när:

- du vill testa en sensor eller modul snabbt
- du följer exempel som är skrivna för klassisk Arduino
- du behöver 5 V-logik
- du undervisar eller dokumenterar på ett sätt som många kan följa
- du vill felsöka hårdvara med så få plattformsdetaljer som möjligt
- du använder äldre shields eller 5 V-moduler
- du behöver många pinnar och Mega räcker
- du vill göra en robust enkel prototyp utan nätverk

Klassiska kort är särskilt bra som testplattformar. Även om slutprojektet senare hamnar på ESP32 eller Pico kan du först förstå sensorn på UNO. När sensorn fungerar där kan du portera till det mer avancerade kortet med färre okända faktorer.

## När du bör välja något annat

Klassiska kort är inte fel, men de är ofta fel val när projektkraven pekar mot moderna funktioner.

Välj något annat när:

- projektet behöver Wi-Fi eller Bluetooth
- du behöver mycket SRAM eller flash
- du ska hantera JSON, webbsidor, TLS eller nätverksprotokoll
- du behöver högre CPU-prestanda
- du behöver avancerad grafik
- du behöver mycket låg energiförbrukning i sleep
- du använder många 3,3 V-sensorer
- du behöver USB-funktioner utöver enkel seriell uppladdning
- du behöver mer exakt timing eller specialiserad I/O
- kortet ska bli mycket kompakt och energieffektivt

I sådana fall är ESP32, RP2040/Pico, moderna Arduino-kort eller specialkort ofta bättre. Det viktiga är inte att klassiska kort är gamla, utan att de har en annan profil.

## Referensmönster: samma lilla projekt på UNO, Nano och Mega

Det här referensmönstret visar vad som brukar vara gemensamt mellan UNO, Nano och Mega, och vad du behöver kontrollera när samma lilla projekt flyttas mellan korten. Mönstret är enkelt med avsikt: en knapp, en LED, en analog signal och seriell utskrift räcker för att avslöja skillnader i pinout, fysisk layout och board-val.

### Vad mönstret visar

Mönstret visar att:

- UNO och Nano ofta är kodmässigt nära, men har olika fysisk formfaktor
- Mega ger fler pinnar och fler hårdvaruseriella portar
- `LED_BUILTIN`, konfigurationsblock och tydliga funktionsnamn gör portering enklare
- pinout, fysisk placering och seriella portar ändå måste kontrolleras för varje kort
- en enkel referenssketch kan avslöja portabilitetsproblem innan projektet växer

### Det här används i exemplet

- ett UNO-liknande kort
- ett Nano-liknande kort
- ett Mega-liknande kort, om du har tillgång till ett
- en potentiometer eller enkel analog sensor
- en LED med seriemotstånd
- en knapp
- breadboard och kopplingskablar
- USB-kablar som passar korten

Om du bara har två av korten kan du ändå använda mönstret. Poängen är att se vilka antaganden som följer med koden när den flyttas.

### Kopplingsidé

Använd följande funktioner:

- en analog ingång för potentiometer eller sensor
- en digital ingång för knapp
- en digital utgång för LED
- seriell monitor för utskrift

För ett UNO-/Nano-liknande kort kan du börja med:

```cpp
const uint8_t PIN_LED = LED_BUILTIN;
const uint8_t PIN_BUTTON = 2;
const uint8_t PIN_ANALOG_SENSOR = A0;
```

På Mega fungerar detta ofta också, men kontrollera alltid fysisk pinout och vilken seriell port projektet faktiskt behöver.

### Kod

```cpp
const uint8_t PIN_LED = LED_BUILTIN;
const uint8_t PIN_BUTTON = 2;
const uint8_t PIN_ANALOG_SENSOR = A0;

const unsigned long SAMPLE_INTERVAL_MS = 250;

unsigned long lastSampleMs = 0;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUTTON, INPUT_PULLUP);

  Serial.begin(9600);
  while (!Serial) {
    ; // Har oftast ingen effekt på klassiska UNO/Nano, men är ofarligt här.
  }

  Serial.println("Classic Arduino portability pattern");
}

void loop() {
  unsigned long now = millis();

  bool buttonPressed = digitalRead(PIN_BUTTON) == LOW;
  digitalWrite(PIN_LED, buttonPressed ? HIGH : LOW);

  if (now - lastSampleMs >= SAMPLE_INTERVAL_MS) {
    lastSampleMs = now;

    int rawValue = analogRead(PIN_ANALOG_SENSOR);

    Serial.print("button=");
    Serial.print(buttonPressed ? "pressed" : "released");
    Serial.print(" raw=");
    Serial.println(rawValue);
  }
}
```

### Kontrollera vid portering

Kontrollera detta när mönstret flyttas mellan kort:

- att rätt board definition är vald i Arduino IDE
- att USB-porten och uppladdningen fungerar stabilt
- att `LED_BUILTIN` motsvarar den LED du tänker använda
- att knappens fysiska pinne motsvarar `PIN_BUTTON`
- att analogingången verkligen är analog ingång på kortet
- att potentiometervärdet ändras som förväntat
- att seriell monitor visar utskrifter med rätt baud rate
- att Mega-projekt som behöver flera seriella portar använder rätt `Serial`, `Serial1`, `Serial2` eller `Serial3`

### Förväntat resultat

I seriell monitor ska du se utskrifter ungefär som:

```text
Classic Arduino portability pattern
button=released raw=512
button=released raw=517
button=pressed raw=520
```

Värdena kommer att variera. Det viktiga är att du kan se knappens tillstånd, analogvärdet och att LED följer knappen på varje kort.

### Anpassningar

Byt ut potentiometern mot en analog ljussensor eller annan enkel analog modul. Flytta sedan LED från den inbyggda LED-pinnen till en annan pinne och se hur mycket enklare porteringen blir när all pin mapping ligger samlad i början av koden.

## Felsökning

Om uppladdningen inte fungerar, kontrollera först att rätt kort och port är valda i utvecklingsmiljön. Om du använder en Nano-klon kan den kräva annan processorinställning, annan bootloader eller drivrutin. Det behandlas mer i nästa kapitel.

Om seriell monitor visar konstiga tecken, kontrollera baud rate. Koden använder `9600`, och seriell monitor ska matcha det.

Om knappen alltid verkar nedtryckt eller aldrig reagerar, kontrollera att du använder `INPUT_PULLUP` på rätt sätt. Med intern pull-up ska knappen normalt koppla pinnen till GND när den trycks ned. Det betyder att logiken blir inverterad: `LOW` betyder nedtryckt.

Om analogvärdet inte ändras, kontrollera potentiometerns tre ben. Ett ytterben ska gå till 5 V, det andra till GND och mittenbenet till A0. Om bara två ben används kan beteendet bli annorlunda än du tänkt.

Om LED inte lyser, kontrollera polaritet och seriemotstånd. Om du använder den inbyggda LED:en på pinne 13 behövs ingen extern LED.

Om koden fungerar på UNO men inte på Nano eller Mega, kontrollera fysisk pinout. Samma pinnamn kan sitta på annan plats, och vissa kortvarianter har märkning som är lätt att misstolka.

## Vanliga misstag

- **Misstag: Att välja UNO bara för att det är standard.**
  - **Varför det händer:** Många exempel utgår från UNO och det känns tryggt.
  - **Hur man undviker det:** Använd kapitel 2:s kortvalsfrågor. Välj UNO när enkelhet och referensvärde är viktigast, inte av vana.

- **Misstag: Att glömma minnesbegränsningar.**
  - **Varför det händer:** Erfarna programmerare är vana vid betydligt större minnesmiljöer.
  - **Hur man undviker det:** Var försiktig med stora buffertar, strängar, displaybibliotek och flera samtidiga bibliotek.

- **Misstag: Att blanda 5 V och 3,3 V utan nivåskiftning.**
  - **Varför det händer:** Moduler ser ofta kompatibla ut fysiskt även när de inte är elektriskt kompatibla.
  - **Hur man undviker det:** Kontrollera logiknivå, matningsspänning och om modulen har inbyggd nivåskiftning.

- **Misstag: Att tro att Mega löser alla problem.**
  - **Varför det händer:** Mega har många pinnar och mer minne än UNO.
  - **Hur man undviker det:** Välj Mega för I/O och klassisk enkelhet. Välj modernare kort för nätverk, prestanda, energilägen eller 3,3 V-ekosystem.

- **Misstag: Att kopiera pinnummer från ett exempel utan att kontrollera kortet.**
  - **Varför det händer:** Arduino API gör pinnummer enkla, men fysisk pinout varierar.
  - **Hur man undviker det:** Samla pinnummer i namngivna konstanter och dokumentera fysisk koppling.

## Snabbreferens

| Fråga | UNO | Nano | Mega |
|---|---|---|---|
| Bäst som | Referenskort och testkort | Kompakt prototypkort | Stort I/O-kort |
| Typisk logiknivå | 5 V | 5 V på klassiska varianter | 5 V |
| Formfaktor | Stor och shieldvänlig | Liten och breadboardvänlig | Stor med många pinnar |
| Styrka | Dokumentation och enkelhet | Kompakt UNO-känsla | Många pinnar och flera UART |
| Begränsning | Få resurser och stort format | Pinout/klonvariationer | Inte modern trots fler resurser |
| Passar sämre för | IoT, avancerad grafik, låg effekt | Mycket I/O, stora projekt | Kompakta och uppkopplade projekt |

## Sammanfattande valbild

- UNO, Nano och Mega är fortfarande viktiga eftersom de är enkla, väldokumenterade och bra för experiment.
- UNO är ofta bäst som referensplattform och felsökningskort.
- Nano ger UNO-liknande arbetssätt i kompakt form.
- Mega är användbart när du behöver många pinnar eller flera seriella portar.
- 5 V-logik kan vara praktiskt med äldre moduler men riskabelt med moderna 3,3 V-sensorer.
- Minnesbegränsningar är en praktisk faktor, särskilt med strängar, buffertar, displayer och flera bibliotek.
- Klassiska kort är ofta rätt för lärande, test och enkel prototyp.
- Moderna kort passar bättre för nätverk, låg effekt, hög prestanda, 3,3 V-ekosystem och mer komplexa system.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 5 V-logik |
| Typiskt gränssnitt | Digital I/O, analog in, UART, I2C och SPI |
| Välj när | du vill ha enkelhet, robusthet och mycket exempelmaterial |
| Välj inte när | du behöver Wi-Fi, mycket minne eller avancerad energihantering |
| Vanliga fel | för lite minne, fel shield-antagande, blandad 3,3 V/5 V-logik |
| Alternativ att överväga | moderna Arduino-kort, ESP32, RP2040 |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När du väljer mellan UNO, Nano, Mega och modernare kort, börja med valguiden i kapitel 2.
- När USB-chip, bootloader eller klonbeteende påverkar uppladdning, jämför med kapitel 11.
- När kortets strömgränser påverkar sensorer, LED eller motorer, gå vidare till kapitel 34.

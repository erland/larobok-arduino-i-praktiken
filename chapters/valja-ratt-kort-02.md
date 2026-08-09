# 2. Att välja rätt kort för rätt projekt

## Beslutsöversikt
Det här kapitlet är bokens praktiska beslutsstöd för kortval. Använd det när du har en projektidé men är osäker på om du ska börja med ett klassiskt Arduino-kort, ett modernt Arduino-kort, ESP8266, ESP32, Raspberry Pi Pico eller ett specialkort.

Kapitlet hjälper dig framför allt att:

- utgå från projektets krav i stället för från ett favoritkort
- väga in pinnar, spänning, minne, kommunikation, analog mätning, strömförbrukning och fysisk formfaktor
- se när ett enkelt kort är bättre än ett kraftfullt kort
- dokumentera varför ett kort valdes

## Börja med projektets verkliga krav

Många kortval börjar i fel ände: man jämför klockfrekvens, flashminne, antal pinnar och trådlösa funktioner innan man har beskrivit vad projektet faktiskt ska göra. Det är som att välja server innan man vet om systemet ska hantera tio användare eller tio miljoner.

Börja i stället med en kort kravprofil. Den behöver inte vara formell, men den ska vara konkret.

Exempel:

> Projektet ska mäta temperatur och luftfuktighet i ett förråd, visa status med en LED, drivas från USB och logga data till seriell monitor under testfasen.

Det här projektet kräver troligen inte Wi-Fi, många pinnar, mycket minne eller avancerad timing. Ett enkelt UNO-, Nano- eller motsvarande kort kan vara tillräckligt.

Jämför med detta:

> Projektet ska mäta temperatur, luftfuktighet och batterispänning utomhus, vakna var femte minut, skicka data via Wi-Fi och gå tillbaka till sleep.

Nu är kraven annorlunda. Nätverk och strömförbrukning påverkar kortvalet kraftigt. Ett ESP-baserat kort kan vara naturligt, men bara om dess sleep-läge, regulator och kringkomponenter fungerar för batteridrift.

Ett tredje exempel:

> Projektet ska läsa flera snabba digitala signaler, styra LED-effekter och reagera med låg latens.

Då kan timing, antal pinnar och specialfunktioner väga tyngre än Wi-Fi. Ett RP2040-baserat kort, ett Teensy-liknande kort eller ett annat snabbare kort kan vara mer intressant än en klassisk UNO.

## De viktigaste beslutsdimensionerna

Ett bra kortval brukar kunna förklaras med ett fåtal dimensioner. Du behöver sällan maximera alla. Du behöver förstå vilka som är viktiga för just projektet.

## I/O: antal pinnar är inte hela sanningen

Det första många tittar på är antal GPIO-pinnar. Det är rimligt, men det är bara början.

Fråga:

- Hur många digitala ingångar behövs?
- Hur många digitala utgångar behövs?
- Behövs analoga ingångar?
- Behövs PWM på flera pinnar?
- Behövs flera UART-, I2C- eller SPI-bussar?
- Är vissa pinnar reserverade för USB, boot-läge, flashminne eller inbyggda funktioner?
- Är pinnarna 5 V-toleranta eller bara 3,3 V?
- Är pinouten tydlig och stabil?

Ett kort kan ha många fysiska pinnar men ändå vara olämpligt om vissa pinnar har specialbeteenden. På ESP-baserade kort finns till exempel ofta boot-relaterade pinnar som kan påverka uppstart om de dras till fel nivå. På småkort kan vissa pinnar delas med inbyggda LED, laddkretsar, flash eller USB-funktioner.

Ett vanligt misstag är att räkna pinnar utan att räkna funktioner. Om du behöver fyra PWM-kanaler, två analoga ingångar och en I2C-buss är det inte säkert att “tolv GPIO” betyder att allt får plats på ett rent sätt.

## Spänningsnivå: 5 V och 3,3 V påverkar allt

Logiknivå är en av de viktigaste praktiska skillnaderna mellan kortfamiljer.

Klassiska Arduino UNO- och Nano-liknande kort använder ofta 5 V-logik. Många moderna kort, särskilt ESP32-, ESP8266- och RP2040-baserade kort, använder 3,3 V-logik. Det påverkar både vad kortet kan läsa och vad det kan driva.

En 5 V-sensor kan skicka en digital HIGH-signal på 5 V. Ett 3,3 V-kort kan skadas om den signalen kopplas direkt till en pinne som inte är 5 V-tolerant. Omvänt kan en 3,3 V-signal ibland, men inte alltid, läsas som HIGH av en 5 V-ingång. Det beror på gränsvärden, komponent och marginaler.

Kortvalet ska därför göras tillsammans med komponentvalet. Det är inte ovanligt att ett projekt blir enklare om kortet och sensorerna använder samma logiknivå.

Som tumregel:

- Välj 5 V-kort när du arbetar med äldre shields, vissa relämoduler, klassiska Arduino-exempel och komponenter som är gjorda för 5 V.
- Välj 3,3 V-kort när du arbetar med moderna sensormoduler, ESP/RP2040-kort, låg strömförbrukning eller digitala moduler som ändå är 3,3 V-baserade.
- Använd nivåskiftning när signalnivåerna inte matchar och du inte säkert vet att kopplingen är tillåten.

## Minne och processorkraft: mer är inte alltid enklare

Moderna mikrokontrollerkort kan vara mycket kraftfullare än klassiska Arduino-kort. Mer RAM och flash gör det möjligt att använda större bibliotek, nätverksstackar, JSON-hantering, displayer, buffertar och mer avancerad logik.

Men mer kraft betyder inte automatiskt enklare projekt. Kraftfullare kort kan ha mer komplex bootprocess, fler specialpinnar, 3,3 V-logik, fler beroenden och mer plattformsspecifika bibliotek.

För små tester är det ofta en fördel att börja med ett enkelt kort. När något inte fungerar finns färre rörliga delar.

Prestanda är viktigt när projektet kräver:

- nätverk och kryptering
- större displayer eller grafik
- ljud- eller signalbehandling
- många samtidiga uppgifter
- hög datatakt
- stora bibliotek
- lokal filtrering eller beräkning
- många sensorer med buffring

Prestanda är mindre viktigt när projektet bara ska:

- läsa en långsam sensor
- styra några LED
- reagera på knappar
- logga enkla värden
- driva ett servo långsamt
- demonstrera grundprinciper

Ett kort som är “för svagt” visar sig ofta genom minnesbrist, instabilitet när bibliotek kombineras eller att programmet blir svårt att utöka. Ett kort som är “för kraftfullt” visar sig ofta genom onödig komplexitet, fler specialfall och sämre pedagogisk tydlighet.

## Kommunikation: välj kort efter hur projektet pratar med världen

Kommunikation är ofta en starkare kortvalsdrivare än CPU-prestanda.

Fråga:

- Behöver projektet Wi-Fi?
- Behöver projektet Bluetooth eller BLE?
- Behöver det USB som seriell port, tangentbord, MIDI eller masslagring?
- Behöver det flera seriella portar?
- Behöver det CAN, RS-485, Ethernet eller LoRa via modul?
- Behöver det många I2C-enheter?
- Behöver det snabb SPI till display eller SD-kort?

Om projektet ska vara uppkopplat är ESP8266 eller ESP32 ofta naturliga alternativ. Om projektet inte behöver nätverk kan ett enklare kort vara mer robust och lättare att förstå. Om projektet ska vara pedagogiskt i en klassrumsmiljö kan det vara bättre att undvika nätverkskonfiguration i tidiga kapitel.

Vissa funktioner kan läggas till med externa moduler. Du kan koppla en Wi-Fi-modul till ett klassiskt kort, men det blir ofta mer komplext än att använda ett kort som redan har nätverk. Du kan koppla en I/O-expander till ett kort med få pinnar, men om projektet från början behöver många pinnar kan ett större kort vara enklare.

## Analog mätning: alla ADC:er är inte lika

Analoga ingångar är ett område där kort kan skilja sig mycket. Antal ADC-kanaler, upplösning, stabilitet, linearitet, referensspänning och brus påverkar resultatet.

Ett klassiskt Arduino-exempel kan anta att `analogRead()` ger ett värde mellan 0 och 1023 och att referensen är 5 V. På andra kort kan upplösningen vara högre eller konfigurerbar, referensen vara 3,3 V och ingångsegenskaperna annorlunda.

Om projektet bygger på noggrann analog mätning ska kortvalet inte göras slentrianmässigt. Du kan behöva:

- stabil referensspänning
- filtrering
- kalibrering
- extern ADC
- differentialmätning
- förstärkare eller signalanpassning
- bättre jordning och layout

Om analog mätning bara används för potentiometrar, enkla ljusvärden eller relativa nivåer är kraven lägre.

## Strömförbrukning och matning

Kortets strömförbrukning spelar liten roll när projektet alltid drivs från USB på arbetsbänken. Den spelar stor roll när projektet ska drivas från batteri, solcell eller en liten regulator.

Titta inte bara på mikrokontrollerns sleep-läge i databladet. Ett utvecklingskort innehåller ofta regulator, USB-seriekrets, power-LED, laddkrets och andra komponenter som förbrukar ström även när mikrokontrollern sover.

För batteriprojekt behöver du fråga:

- Hur ofta ska kortet vara vaket?
- Hur länge ska det sova?
- Kan sensorer och moduler stängas av?
- Hur mycket drar regulatorn i vila?
- Finns power-LED som kan kopplas bort?
- Hur stabil är matningen vid radiosändning eller motorstart?
- Klarar kortet brownout och återstart på ett kontrollerat sätt?

Ett kort som är perfekt för USB-experiment kan vara dåligt för batteridrift. Om batteritid är central bör du välja kort och moduler med detta som huvudkrav, inte som eftertanke.

## Fysisk formfaktor och kopplingssätt

Formfaktor påverkar mer än estetik. Den påverkar koppling, felsökning, kapsling och återanvändning.

UNO-formfaktorn är praktisk för shields och undervisning, men den är stor. Nano-liknande kort är breadboardvänliga men kan ha trång pinout. Feather-, XIAO- och Pico-liknande kort kan vara bättre för kompakta projekt men kräver ofta mer noggrann dokumentation av pinnar och funktioner.

Fråga:

- Ska kortet sitta på breadboard?
- Ska det passa i kapsling?
- Ska det använda shields?
- Ska det lödas fast?
- Ska det enkelt kunna bytas ut?
- Behöver det skruvterminaler eller Grove/Qwiic/STEMMA QT-liknande anslutningar?
- Ska en annan person kunna koppla upp det utan att läsa hela koden?

För snabba tester är synlighet och felsökningsbarhet ofta viktigare än liten storlek. För färdig konstruktion är det tvärtom.

## Bibliotek och community

Ett kort kan vara tekniskt imponerande men ändå vara ett dåligt val om bibliotek och exempel saknas för de komponenter du vill använda. Det gäller särskilt i Arduino-världen, där bibliotek ofta är skrivna med antaganden om en viss arkitektur, timer, pinmodell eller kommunikationsimplementation.

Kontrollera:

- Finns aktivt stöd för kortet i Arduino IDE eller vald miljö?
- Fungerar de bibliotek du behöver på kortfamiljen?
- Finns exempel för just den kombinationen av kort och modul?
- Finns kända konflikter mellan bibliotek?
- Kräver biblioteket AVR-specifika register?
- Kräver det en viss timer eller interruptfunktion?
- Har kortet rimlig dokumentation och pinout?

För en erfaren programmerare är det frestande att tänka “det kan jag porta själv”. Det kan du ofta. Men frågan är om det är rätt användning av projektets tid. Om målet är att lära sig en sensor eller bygga ett experiment är ett välstött kort ofta bättre än ett tekniskt elegant men ensamt val.

## Kostnad, tillgänglighet och reproducerbarhet

Ett billigt kort kan vara perfekt för experiment. Men om projektet ska användas i undervisning, dokumenteras i en bok eller byggas av flera personer blir reproducerbarhet viktigare.

Ett problem med lågkostnadskort är att samma produktnamn kan säljas i flera revisioner med olika USB-chip, regulator, pinout eller komponentkvalitet. Det betyder inte att korten är dåliga, men det betyder att du måste dokumentera vad du faktiskt använder.

För reproducerbara projekt bör du notera:

- exakt kortmodell eller åtminstone kortfamilj
- mikrokontroller
- logiknivå
- USB-seriechip om det spelar roll
- board package och version
- pinoutkälla
- eventuella avvikelser från standard
- varningspinnar och boot-relaterade pinnar

Ett officiellt kort eller ett väldokumenterat tredjepartskort kan vara dyrare men spara tid i felsökning och dokumentation.

## Ett praktiskt beslutsflöde

När du väljer kort kan du använda följande ordning. Den är avsiktligt praktisk och något konservativ.

1. Beskriv projektets funktion med en mening.
2. Lista alla sensorer, utenheter och kommunikationsbehov.
3. Räkna nödvändiga pinnar och gränssnitt.
4. Identifiera spänningsnivåer: 5 V, 3,3 V eller blandat.
5. Avgör om nätverk är ett grundkrav eller bara en framtida möjlighet.
6. Avgör om batteridrift är ett grundkrav eller bara en bonus.
7. Bedöm minne, CPU och biblioteksbehov.
8. Välj enklaste kort som uppfyller de viktiga kraven.
9. Kontrollera bibliotek och pinout innan du bygger.
10. Dokumentera varför kortet valdes och vad som skulle få dig att byta.

Det sista steget är viktigt. Ett bra kortval är inte bara ett val utan en motivering.

## Vanliga kortfamiljer som beslutsalternativ

Följande översikt är avsedd som orientering. Senare kapitel går djupare in på respektive familj.

| Kortfamilj | Typisk styrka | Typisk begränsning | Välj när |
|---|---|---|---|
| Klassisk UNO/Nano/Mega | Enkelhet, 5 V, mycket exempel | Begränsat minne och prestanda | Du vill ha tydlig Arduino-känsla och enkel felsökning |
| ATmega-baserade kloner | Billiga och välkända | Varierande kvalitet och USB-chip | Du experimenterar och kan kontrollera pinout och drivrutiner |
| ESP8266/NodeMCU | Billig Wi-Fi | Färre pinnar och vissa boot-pin-fällor | Du vill ha enkel uppkoppling till låg kostnad |
| ESP32 | Wi-Fi, BLE, prestanda, många varianter | 3,3 V, plattformsspecifika detaljer | Du bygger IoT, nätverk eller mer avancerade experiment |
| RP2040/RP2350/Pico-liknande | Mycket I/O och bra prestanda | Ofta inget inbyggt Wi-Fi på enklare kort | Du vill ha snabb och flexibel I/O utan radio som huvudkrav |
| Småkort | Kompakt formfaktor | Färre pinnar och svårare felsökning | Projektet ska bli litet eller bärbart |
| Avancerade kort | Mycket prestanda och specialfunktioner | Kostnad och komplexitet | Projektet verkligen behöver funktionerna |

Tabellen ska inte läsas som en rangordning. Den ska hjälpa dig att välja utifrån projektets viktigaste begränsning.

## Exempel 1: Enkel väderstation på arbetsbänken

Krav:

- mäta temperatur, luftfuktighet och tryck
- visa data i seriell monitor
- drivas från USB
- vara lätt att förstå och modifiera
- inga krav på batteridrift
- inga krav på Wi-Fi i första versionen

Ett klassiskt UNO- eller Nano-liknande kort kan passa bra. Om sensorn är I2C-baserad och fungerar med både 3,3 V och 5 V blir kopplingen enkel. Om du senare vill lägga till nätverk kan du byta kort, men i första versionen är enkelheten en fördel.

Ett ESP32-kort skulle också fungera, men det lägger till fler plattformsdetaljer än projektet kräver. Det är inte fel, men det är inte nödvändigt.

## Exempel 2: Uppkopplad miljölogger

Krav:

- mäta miljödata
- skicka data via Wi-Fi
- kanske använda MQTT eller HTTP
- hantera anslutningsfel
- eventuellt drivas från batteri senare

Här blir ESP32 eller ESP8266 mer naturligt. Wi-Fi är inte ett tillägg utan en grundfunktion. Om batteridrift är viktig bör ESP32-variant, utvecklingskortets regulator och sleep-ström granskas noga.

Ett klassiskt UNO-kort plus extern Wi-Fi-modul kan vara lärorikt, men det är ofta mer komplicerat än nödvändigt.

## Exempel 3: Många LED och tydlig visuell feedback

Krav:

- styra många LED
- reagera på sensorvärden
- kanske använda adresserbara LED
- extern strömförsörjning till LED behövs
- timing kan spela roll

Här kan flera kort fungera. En klassisk Arduino kan räcka för ett mindre antal LED, men ett modernare kort med mer minne och högre prestanda ger mer utrymme för effekter. Om projektet använder adresserbara LED behöver du kontrollera att biblioteket fungerar på kortfamiljen och att logiknivån är rätt för LED-strippen.

Kortvalet är bara halva frågan. Strömförsörjning, jordning och nivåskiftning kan vara viktigare än CPU.

## Exempel 4: Robot eller mekaniskt projekt

Krav:

- styra motorer eller servon
- läsa sensorer
- hantera strömtoppar och störningar
- kanske läsa encoders
- vara lätt att felsöka

Kortet ska inte driva motorerna direkt. Det ska styra drivare. Därför behöver du pinnar, timers/PWM och robust matning, men motorströmmen ska hanteras separat.

Ett UNO-, Mega-, ESP32- eller RP2040-baserat kort kan fungera beroende på antal motorer och sensorer. Om många pinnar behövs kan Mega eller I/O-expansion vara enklare. Om nätverk eller BLE behövs kan ESP32 vara mer relevant. Om snabb I/O eller många samtidiga signaler är centralt kan RP2040-liknande kort vara intressant.

## Exempel 5: Batteridriven sensor

Krav:

- läsa sensor sällan
- sova större delen av tiden
- drivas länge på batteri
- kanske skicka data trådlöst
- starta om säkert efter spänningsfall

Här är kortets kringkomponenter avgörande. Många utvecklingskort är gjorda för bekväm USB-utveckling, inte för minimal strömförbrukning. Power-LED, regulator och USB-seriechip kan dra mer än själva mikrokontrollern i sleep.

Välj inte bara utifrån att mikrokontrollern har deep sleep. Välj utifrån hela kortets strömförbrukning och hur sensorerna kan stängas av.

## När du bör välja ett enkelt kort

Ett enkelt kort är ofta bäst när projektet är pedagogiskt, experimentellt eller fokuserar på en enskild komponent.

Välj ett enkelt UNO- eller Nano-liknande kort när:

- du vill förstå komponenten snarare än plattformen
- 5 V-logik är praktiskt
- du vill använda klassiska Arduino-exempel
- du vill minimera plattformsdetaljer
- projektet inte behöver nätverk
- minne och prestanda räcker
- felsökning och synlighet är viktigare än formfaktor

Ett enkelt kort är inte ett “sämre” val. Det är ofta ett mer kontrollerat val.

## När du bör välja ESP8266 eller ESP32

Välj ESP8266 eller ESP32 när nätverk är en del av projektets kärna.

ESP8266 passar ofta för billiga, enkla Wi-Fi-projekt med begränsad I/O. ESP32 passar bättre när du behöver fler pinnar, mer prestanda, Bluetooth/BLE, mer flexibilitet eller modernare varianter.

Var dock uppmärksam på:

- 3,3 V-logik
- boot-relaterade pinnar
- ADC-beteende
- strömspikar vid radiosändning
- bibliotek som beter sig annorlunda än på AVR
- sleep-ström för just utvecklingskortet, inte bara mikrokontrollern

ESP-kort är mycket kraftfulla i Arduino-världen, men de är inte bara “Arduino med Wi-Fi”. De är en egen plattform med Arduino-kompatibelt arbetssätt.

## När du bör välja RP2040/RP2350 eller Pico-liknande kort

RP2040- och RP2350-baserade kort är intressanta när du vill ha mycket I/O, bra prestanda och flexibel timingnära funktionalitet utan att nätverk nödvändigtvis är huvudkravet.

De kan passa bra för:

- LED-projekt
- många digitala signaler
- experiment med timing
- USB-orienterade projekt
- utbildning där man vill ha modern mikrokontroller men inte radiokomplexitet
- projekt där många pinnar behövs till låg kostnad

Om projektet kräver Wi-Fi kan du välja en variant med trådlöst stöd eller välja ESP32 i stället.

## När du bör välja ett specialkort

Specialkort är rätt när deras specialisering matchar projektet tydligt.

Exempel:

- ESP32-CAM-liknande kort för enkla kameraprojekt
- Feather-liknande kort när batteri och expansionskort passar ekosystemet
- XIAO-liknande kort när liten formfaktor är viktig
- Teensy-liknande kort när hög prestanda och avancerad I/O behövs
- Portenta-liknande kort när projektet kräver mer industriell eller avancerad kapacitet

Specialkort är mindre lämpliga när du fortfarande utforskar problemet och inte vet vilka krav som är viktigast. Börja då hellre med ett större, tydligare och mer lättfelsökt kort.

## Kortval och sensorer hör ihop

Eftersom boken senare går igenom många sensorer och IC-kretsar är det viktigt att redan nu se att sensorn kan styra kortvalet.

En I2C-sensor med 3,3 V-logik passar ofta naturligt med ESP32, RP2040 och moderna kort. En äldre 5 V-modul eller shield kan passa bättre med UNO/Mega. En analog sensor med svag signal kan behöva extern signalanpassning oavsett kort. En snabb SPI-display kan kräva mer minne och högre datahastighet.

Fråga alltid:

- Vilken spänning kräver sensorn?
- Vilken logiknivå använder den?
- Vilket gränssnitt använder den?
- Finns bibliotek för mitt kort?
- Hur mycket data producerar den?
- Hur ofta behöver den läsas?
- Kräver den timing, interrupt eller buffertar?
- Hur påverkar den strömförbrukningen?

Det är bättre att byta kort tidigt än att bygga ett helt projekt runt ett dåligt första val.

## Kortval och utenheter hör också ihop

Utenheter som LED-strippar, servon, motorer, buzzers, reläer och displayer kan ställa större krav än sensorer. De kan kräva extern matning, högre ström, PWM, timers, snabb SPI eller noggrann timing.

Ett kort kan läsa en sensor utan problem men ändå vara fel val för att styra projektets utgångar.

Exempel:

- Många servon kräver genomtänkt PWM och separat matning.
- DC-motorer kräver drivkrets och skydd mot störningar.
- Adresserbara LED kan kräva mycket ström och timingkänsliga bibliotek.
- TFT-displayer kan kräva mer RAM, snabb SPI och fler pinnar.
- Relämoduler kan kräva rätt styrnivå och ibland mer ström än en GPIO bör ge.

När du väljer kort ska du därför lista både ingångar och utgångar. Ett projekt är ett system, inte bara en samling sensorer.

## Dokumentera kortvalet

Ett kortval som inte dokumenteras kommer att glömmas. Det blir särskilt problematiskt i en bok, en kurs eller ett projekt som ska återanvändas.

En enkel kortvalsnotering kan se ut så här:

```text
Projekt: Miljölogger på arbetsbänk
Valt kort: Arduino Nano-kompatibelt ATmega328P-kort
Motivering:

- Tillräckligt antal pinnar
- I2C räcker för BME280-displaykombinationen
- USB-matning och seriell monitor är enkel
- 5 V-logik är acceptabel eftersom modulen har regulator/nivåstöd
- Inget Wi-Fi-krav i första versionen

Risker:

- Begränsat RAM om displaybiblioteket växer
- Klonkortet använder CH340, drivrutin kan behövas
- Om projektet ska bli uppkopplat bör ESP32 övervägas
```

Det här är inte byråkrati. Det är felsökning i förväg.

## Vanliga misstag

- **Misstag: Att välja kort efter flest funktioner.**
  - Varför det händer: Det känns tryggt att ha Wi-Fi, mycket minne och många pinnar från början.
  - Hur du undviker det: Välj efter projektets huvudkrav och välj bort komplexitet som inte behövs.

- **Misstag: Att räkna fysiska pinnar i stället för användbara pinnar.**
  - Varför det händer: Pinouten ser generös ut på bilden.
  - Hur du undviker det: Kontrollera vilka pinnar som är reserverade, boot-känsliga, input-only eller delade med andra funktioner.

- **Misstag: Att ignorera logiknivå.**
  - Varför det händer: Alla moduler ser ut att ha samma Dupont-kablar och 2,54 mm-stift.
  - Hur du undviker det: Kontrollera alltid om signalerna är 5 V eller 3,3 V innan du kopplar.

- **Misstag: Att anta att alla Arduino-bibliotek fungerar överallt.**
  - Varför det händer: Koden kompilerar ofta likadant på ytan.
  - Hur du undviker det: Kontrollera arkitekturstöd, issues, exempel och eventuella timer- eller interruptberoenden.

- **Misstag: Att glömma strömförsörjningen.**
  - Varför det händer: USB räcker under test, men inte nödvändigtvis när motorer, LED-strippar eller radio används.
  - Hur du undviker det: Gör en enkel strömbudget och skilj mellan mikrokontrollerns matning och lastens matning.

- **Misstag: Att välja kort för slutprodukten innan experimentet är förstått.**
  - Varför det händer: Man vill optimera formfaktor eller kostnad tidigt.
  - Hur du undviker det: Börja med ett felsökningsvänligt kort och byt till mindre eller billigare kort när kraven är stabila.

## Snabb sammanfattning

- Det finns inget bästa Arduino-kompatibla kort, bara kort som passar olika krav.
- Börja med projektets funktion, sensorer, utenheter, kommunikation, ström och spänningsnivåer.
- Antal pinnar är bara relevant om pinnarna faktiskt kan användas till de funktioner du behöver.
- 5 V kontra 3,3 V är ett praktiskt systemval, inte en detalj.
- Nätverk, batteridrift, analog noggrannhet och motor-/LED-laster är starka kortvalsdrivare.
- Bibliotek och community kan vara lika viktiga som tekniska specifikationer.
- Ett enkelt kort är ofta bäst för förståelse och felsökning.
- Ett kraftfullt kort är bäst när projektet verkligen behöver dess funktioner.
- Dokumentera alltid varför du valde ett kort och när du skulle byta.

## Relaterat

- När kortvalet beror på utvecklingsmiljö, bibliotek eller exempelprojekt, gå vidare till kapitel 3.
- När du jämför klassiska Arduino-kort, kloner, ESP32 eller Pico, använd kapitel 10–15 som kortprofiler.
- När valet påverkas av strömförsörjning, batteridrift eller många laster, jämför med kapitel 34.

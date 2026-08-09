# Canon: Återkommande exempel och experiment

## Pedagogisk profil

Boken använder praktiska experiment med tydlig valguide och felsökning. Experimenten ska vara inspirerande men reproducerbara.

## Återkommande slutprojekt

### Modulär sensor- och styrstation

**Syfte:** Knyta ihop kortval, sensorer, aktuatorer, kommunikation, strömförsörjning och felsökning.

**Möjliga funktioner:**

- läsa miljödata
- visa status på display eller LED
- styra en utenhet
- logga data
- skicka data via nätverk på ESP-baserat kort
- jämföra kortval och sensoralternativ

## Regler för experiment

- Ange kort, spänningsnivå och gränssnitt.
- Ange tydligt när extern matning behövs.
- Separera kopplingsbeskrivning, kod och förväntat resultat.
- Avsluta med felsökning och variationsidéer.

## Introducerade experiment

### Kapitel 1: Kartlägg två kort och en modul

**Syfte:** Träna på att bedöma Arduino-kompatibilitet innan koppling och kodning.

**Återanvändbara principer:**

- dokumentera både fysiskt pinnamn och kodens pinnamn
- identifiera board package och core
- kontrollera GPIO-spänning före inkoppling
- testa kort, buss och modul var för sig
- avsluta experiment med slutsats om vilket kort som passar bäst

### Kapitel 2: Kortval för tre projekt

**Syfte:** Träna på att välja kort innan koppling och kodning börjar.

**Återanvändbara principer:**

- börja med projektets krav, inte kortets specifikationer
- lista både sensorer och utenheter
- skilj mellan fysiska pinnar och användbara pinnar
- kontrollera logiknivå, matning och bibliotek innan inkoppling
- dokumentera valt kort, alternativ, risker och skäl att byta


### Kapitel 3: Återanvändbart analogt experimentprojekt

**Syfte:** Träna på att skapa reproducerbara Arduino-experiment med tydlig projektstruktur.

**Återanvändbara principer:**

- dokumentera kortmodell, board-val, pinout och logiknivå i experimentet
- samla konfiguration före huvudlogik
- testa komponenter i minimal sketch före integration
- använd seriell monitor som logg och seriell plotter för mättrender
- undvik magiska tal i huvudlogiken
- använd `millis()` för återkommande mätning i stället för att bygga vidare på `delay()`

### Kapitel 4: LED, knapp och spänningsdelare

**Syfte:** Träna på att koppla och mäta grundläggande elektriska principer innan mer avancerade sensorer och aktuatorer används.

**Återanvändbara principer:**

- mät matningsspänning och GND innan kodfelsökning
- använd seriemotstånd för LED och beräkna ström med Ohms lag
- använd intern pull-up för enkla knappar
- kontrollera viloläge och aktivt läge med multimeter
- använd spänningsdelare bara när signaltyp och hastighet gör det lämpligt
- kontrollera 5 V och 3,3 V innan kort och moduler blandas
- håll experiment på säker lågspänning

### Kapitel 5: Robust knappmodul utan delay

**Syfte:** Träna på digital I/O, intern pull-up, aktiv LOW-logik, kontaktstuds och icke-blockerande knapphantering.

**Återanvändbara principer:**

- använd `INPUT_PULLUP` för enkla knappar mot GND
- kapsla aktiv LOW-logik bakom tydliga funktionsnamn
- filtrera kontaktstuds med `millis()` i stället för `delay()`
- skilj mellan stabilt tillstånd och händelse, exempelvis `wasPressed()`
- dokumentera vald pinne, logiknivå och om pinnen är boot-relaterad
- låt GPIO styra signaler men använd drivkretsar för större laster
- testa samma digitala koppling på flera kort för att hitta pinout- och boot-skillnader

### Kapitel 6: Kalibrerad analog läsning med potentiometer

**Syfte:** Skapa ett återanvändbart arbetssätt för analoga mätningar med råvärde, filtrering, kalibrering och hysteresis.

**Återanvändbara principer:**

- kontrollera referensspänning och tillåtet ingångsområde innan mätning
- logga råvärde innan värdet översätts till procent eller fysisk enhet
- använd uppmätta min- och maxvärden i stället för idealiserade gränser
- filtrera först när koppling och råvärde är begripliga
- använd hysteresis när analoga mätvärden styr digitala beslut
- dokumentera kortfamilj, ADC-upplösning, referensspänning och kalibreringsvärden


### Kapitel 7: Icke-blockerande PWM-fade

**Syfte:** Träna på PWM, duty cycle och tidsstyrning med `millis()` utan att blockera huvudloopen.

**Återanvändbara principer:**

- använd `analogWrite()` för enkel PWM-styrning men dokumentera att signalen inte är äkta analog spänning
- kontrollera att vald pinne stöder PWM på aktuellt kort
- håll LED-experiment strömbegränsade med seriemotstånd
- använd `millis()` och subtraktionsmönstret `now - lastRunMs >= intervalMs`
- dela upp flera tidsstyrda aktiviteter i små funktioner som returnerar snabbt
- undvik timerändringar och bibliotekskombinationer utan att testa sidokonsekvenser
- använd drivkretsar för motorer, reläer, LED-strippar och andra större laster

### Kapitel 8: Pulser med polling och interrupt

**Syfte:** Träna på att jämföra polling och avbrott för digitala händelser samt hantera delad data säkert.

**Återanvändbara principer:**

- börja med polling om signalen är långsam och enkel
- använd avbrott när korta eller snabba pulser annars riskerar att missas
- håll ISR-funktioner korta och fria från seriell utskrift, väntan och tung logik
- deklarera delad interruptdata som `volatile`
- kopiera räknare och större värden i korta kritiska sektioner
- använd timeouts för väntelägen som annars kan låsa systemet
- definiera säkra standardlägen för motorer, reläer och andra laster innan fel uppstår
- behandla watchdog som sista skyddsnivå, inte som ersättning för felsökning

### Kapitel 9: Två I2C-enheter på samma buss

**Syfte:** Träna på att identifiera I2C-enheter, dokumentera adresser och kombinera flera moduler på samma buss.

**Återanvändbara principer:**

- kör I2C-scanner innan sensorspecifik bibliotekskod används
- dokumentera SDA, SCL, spänning, adress och bibliotek för varje modul
- testa en modul i taget innan flera kombineras
- kontrollera pull-up-motstånd och spänningsnivåer tidigt
- behandla adresskonflikter som ett hårdvaru-/designproblem, inte bara ett kodproblem
- använd korta kablar och låg busshastighet som startläge vid felsökning
- lägg till moduler stegvis och spara fungerande minimitester

### Kapitel 9: UART-loopback och seriell portkontroll

**Syfte:** Träna på att skilja mellan seriell port, baud rate, TX/RX-koppling och USB-seriell debug.

**Återanvändbara principer:**

- kontrollera om den seriella porten är delad med USB eller finns som extra hårdvaru-UART
- dokumentera TX, RX, GND och baud rate
- korsa TX och RX mellan två enheter
- använd hårdvaru-UART framför mjukvaru-UART när kortet erbjuder det
- felsök skräptecken genom att först kontrollera baud rate
- bygg seriella bryggor och loopback-test innan mer komplex modulkommunikation

### Kapitel 10: Portera samma sensorprojekt mellan UNO, Nano och Mega

**Syfte:** Träna på att skilja mellan Arduino API-portabilitet, fysisk pinout och kortspecifika begränsningar.

**Återanvändbara principer:**

- samla pinnummer i namngivna konstanter
- dokumentera fysisk pinout separat från kodens funktionsnamn
- testa en sensor, en knapp och en LED innan projektet växer
- använd UNO som referensplattform när enkel felsökning är viktig
- välj Nano för kompakt prototyp och Mega när många pinnar behövs
- kontrollera 5 V kontra 3,3 V innan moderna sensorer kopplas in



### Kapitel 11: Identifiera ett okänt kompatibelt kort

**Syfte:** Träna på att göra kloner, lågkostnadskort och tredjepartsvarianter begripliga innan sensorer och moduler kopplas in.

**Återanvändbara principer:**

- skilj mellan formfaktor, mikrokontroller, Arduino API och faktisk elektrisk kompatibilitet
- dokumentera kortidentitet innan experimentet byggs vidare
- kontrollera USB-seriechip, port, boardval och bootloader vid uppladdningsproblem
- dokumentera både silkscreen-namn och faktisk GPIO på ESP-baserade kort
- kontrollera logiknivå och matningsspänning innan 5 V- och 3,3 V-delar blandas
- undvik boot-relaterade pinnar i första versionen av ett experiment
- välj lågkostnadskort när experimentvärde och pris är viktigast, men bättre dokumenterade kort när reproducerbarhet är viktig



### Kapitel 12: Jämför samma sketch på klassiskt och modernt kort

**Syfte:** Träna på att upptäcka vilka antaganden som förändras när ett experiment flyttas från klassiskt Arduino-kort till modernare Arduino-kort.

**Återanvändbara principer:**

- välj inte modernt kort bara för att det är modernare; matcha kortet mot projektets krav
- dokumentera kortprofil för varje kort som används i experiment
- skilj mellan huvudmikrokontroller och separat radiomodul på kombinerade kort
- kontrollera logiknivå, pinout, ADC-skala, PWM-pinnar och bussar vid portering
- behandla UNO R4 WiFi som en egen plattform, inte som ett generellt ESP32-kort
- använd namngivna pinnar och kortspecifika konfigurationsblock
- testa digital I/O, analog läsning, PWM och I2C separat innan projektet byggs ihop
- välj officiella moderna kort när dokumentation och reproducerbarhet väger tyngre än lägsta pris


### Kapitel 13: Wi-Fi-baserad sensorindikator med ESP8266

**Syfte:** Träna på att använda ESP8266 som uppkopplad Arduino-kompatibel plattform utan att tappa kontroll över pinout, logiknivå och nätverksfel.

**Återanvändbara principer:**

- behandla ESP8266 som egen plattform, inte som UNO med Wi-Fi
- dokumentera både silkscreen-namn och faktisk GPIO
- undvik boot-relaterade pinnar i första versionen av projektet
- verifiera A0-spänningsområde innan analog signal kopplas in
- använd timeout vid Wi-Fi-anslutning
- låt projektet ha ett lokalt reservläge när nätverket saknas
- använd I2C-scanner innan sensorbibliotek felsöks
- mät faktisk strömförbrukning på hela utvecklingskortet vid batteriprojekt


### Kapitel 14: ESP32 som Wi-Fi-baserad sensorindikator

**Syfte:** Träna på att använda ESP32-familjen som kraftfull Arduino-kompatibel IoT-plattform utan att tappa kontroll över variant, pinout, 3,3 V-logik och nätverksfel.

**Återanvändbara principer:**

- dokumentera chip, modul, utvecklingskort och board-val, inte bara “ESP32”
- skilj mellan ESP32-chip, ESP32-modul och ESP32-utvecklingskort
- utgå från 3,3 V-logik och kontrollera nivåskiftning innan 5 V-moduler kopplas in
- undvik boot-relaterade pinnar i första versionen av ett experiment
- dokumentera I2C-, SPI- och UART-pinnar explicit när kort kan mappa om bussar
- använd timeout vid Wi-Fi-anslutning
- låt projektet ha ett lokalt reservläge när nätverket saknas
- mät hela utvecklingskortets strömförbrukning innan batteridrift bedöms

### Kapitel 15: Pico som lokal sensor- och styrnod

**Syfte:** Träna på att använda Raspberry Pi Pico, Pico W, Pico 2 eller liknande RP2040/RP2350-kort som Arduino-kompatibel mät- och styrplattform.

**Återanvändbara principer:**

- dokumentera kortmodell, mikrokontroller och Arduino core
- skriv både GPIO-namn och kodens pin-nummer
- kontrollera 3,3 V-logik innan sensorer och moduler kopplas in
- börja med minimala tester: LED, seriell monitor och en pinne eller buss
- jämför Pico med ESP32 och klassisk Arduino utifrån projektets faktiska krav
- använd PIO som framtida möjlighet, inte som första lösning


### Kapitel 16: Specialkort som kravstyrt kortval

**Syfte:** Träna på att välja småkort, Feather-liknande kort, Teensy, ESP32-CAM, Portenta-liknande kort eller andra specialkort utifrån faktiska projektkrav.

**Återanvändbara principer:**

- välj specialkort först när projektets specialkrav är tydliga
- formulera kortets superkraft innan det väljs
- dokumentera exakt kortmodell, mikrokontroller och board-val
- kontrollera pinout, intern hårdvara och logiknivå innan moduler kopplas in
- börja med uppladdning, seriell monitor, LED, knapp och eventuell I2C-scanner
- använd kortprofil för att göra experimentet reproducerbart
- välj hellre ett generellt kort om specialiseringen inte behövs


### Kapitel 17: LED som statusljus

**Syfte:** Träna på att använda LED och RGB-LED som tydlig, strömsnål och icke-blockerande återkoppling i Arduino-projekt.

**Återanvändbara principer:**

- använd seriemotstånd för lös LED
- börja med låg LED-ström för statusindikatorer
- använd `LED_BUILTIN` för snabba korttester
- bygg blink och fade med `millis()` i stället för `delay()`
- samla färg- och blinklogik i funktioner eller en liten klass
- använd konsekventa färger: grön för OK, gul/orange för väntan eller varning, röd för fel
- kontrollera common anode/common cathode innan RGB-kod felsöks
- använd extern drivning när LED-lasten växer

### Kapitel 18: Adresserbar LED-ring som sensorvisning

**Syfte:** Träna på att använda NeoPixel/WS2812-liknande adresserbara LED som tydlig och icke-blockerande visuell återkoppling.

**Återanvändbara principer:**

- räkna på strömförbrukning innan ljusstyrkan höjs
- använd extern matning när LED-lasten växer
- koppla alltid gemensam jord mellan mikrokontroller och LED-matning
- kontrollera DIN/DOUT och pilar på strippen innan felsökning av kod
- använd seriemotstånd på dataledningen och kondensator nära LED-lasten
- begränsa global ljusstyrka i experiment
- använd nivåskiftning från 3,3 V till 5 V när robusthet behövs
- skriv LED-effekter med `millis()` i stället för `delay()`
- använd färg konsekvent som systeminformation, inte bara som dekoration

### Kapitel 19: Ljudsignaler för systemstatus

**Syfte:** Skapa återanvändbara ljudmönster som kan visa startklar, varning och fel utan att blockera resten av programmet.

**Återanvändbara principer:**

- skilj mellan aktiv och passiv buzzer innan du skriver kod
- använd korta och konsekventa ljudmönster som betyder samma sak i hela projektet
- undvik `delay()` i ljudkod som ska köras tillsammans med sensorer och displayer
- använd `tone()` för passiva buzzers men dokumentera möjliga timerkonflikter
- använd drivsteg när ljudutgången kräver mer ström än en GPIO-pinne bör leverera
- testa ljudstyrka och frekvens i den miljö där projektet ska användas

### Kapitel 20: Servo som fysisk sensorindikator

**Syfte:** Träna på att använda rörelse som återkoppling genom att låta en servo visa ett analogt mätvärde utan att blockera resten av programmet.

**Återanvändbara principer:**

- välj servo när begränsad positionsrörelse är huvudkravet
- välj DC-motor när kontinuerlig rotation är huvudkravet
- välj stegmotor när kontrollerad stegvis rörelse är viktig
- driv aldrig motorer direkt från GPIO-pinnar
- använd separat matning för motorer när lasten kan bli mer än minimal
- koppla gemensam jord mellan mikrokontroller, drivare och extern matning
- tolka PWM som styrd effekt, inte garanterad hastighet
- skriv rörelsekod med `millis()` eller tillstånd i stället för `delay()`
- börja utan mekanisk last och öka belastningen stegvis
- felsök först matning, jord och drivare när motorer ger slumpmässiga fel

### Kapitel 21: Säker styrning av lågspänd last

**Syfte:** Träna på att låta Arduino styra en last via relä eller MOSFET utan att GPIO-pinnen bär lastströmmen.

**Återanvändbara principer:**

- skilj alltid mellan styrsignal och lastström
- välj relä för enkel av/på-styrning och galvanisk separation
- välj MOSFET för lågspänd DC-last, PWM och tyst snabb styrning
- kontrollera logic-level-egenskaper, särskilt vid 3,3 V-kort
- använd flyback-diod eller motsvarande skydd för induktiva laster
- testa aktiv hög/låg logik innan en riktig last ansluts
- koppla gemensam jord när styrsignalen inte är galvaniskt isolerad
- bygg säker startlogik så att lasten är av vid reset och power-on
- dokumentera modulens märkdata och lämna marginal
- använd `millis()` och max-tider för laster som inte får vara på för länge



### Kapitel 22: Liten mätpanel med OLED och knapp

**Syfte:** Träna på att bygga ett enkelt lokalt användargränssnitt där display, knapp, mätvärde och UI-tillstånd hålls isär.

**Återanvändbara principer:**

- välj display efter informationsbehov, inte efter vad som ser mest avancerat ut
- dokumentera displayens adress, gränssnitt, matningsspänning och pinout
- använd I2C-scanner vid osäker displayadress
- håll mätning, tillstånd och presentation separerade i koden
- uppdatera displayen med intervall eller när information ändras
- använd en enkel enum för vyer och menyer
- behåll seriell loggning även när projektet har display
- kontrollera RAM-kostnad för OLED- och grafikbibliotek på små kort

### Kapitel 23: Miljölogger med jämförelse

**Syfte:** Träna på att välja, placera, läsa och jämföra miljösensorer för temperatur, fukt och tryck.

**Återanvändbara principer:**

- börja med vad projektet behöver veta, inte med vilken sensor som råkar finnas i lådan
- dokumentera sensor, modul, gränssnitt, bibliotek, mätintervall och fysisk placering
- använd `millis()` för mätintervall i stället för att läsa sensorn varje varv i `loop()`
- skilj mellan sensorläsning, rimlighetskontroll, bearbetning och presentation
- visa bara meningsfull precision, inte alla decimaler biblioteket kan skriva ut
- placera miljösensorer bort från värmekällor, tät kapsling och dåligt luftflöde
- använd hysteresis när temperatur eller fukt styr en utenhet
- jämför flera sensorer bredvid varandra innan du drar slutsatser om absolut noggrannhet


### Kapitel 24: Sensorstyrd RGB-status och optisk sensorprofil

**Syfte:** Träna på att använda ljus som mätstorhet och styrsignal, samt dokumentera placering och optiska antaganden.

**Återanvändbara principer:**

- skilj mellan relativ ljusnivå, lux, färg, UV och optisk detektion
- använd LDR för enkla relativa beslut, inte som exakt luxmätare
- välj digital ljussensor när värden ska jämföras över tid eller mellan miljöer
- dokumentera placering, riktning, ljuskälla, avstånd och kapsling
- använd filtrering och hysteresis innan ljusvärden styr LED, display eller annan utenhet
- testa färgsensorer med fast avstånd och kontrollerad belysning
- använd UV-sensorer för pedagogik och trend, inte som säkerhetskritisk mätning
- testa IR-reflektion med projektets faktiska material och vinklar

### Kapitel 25: Jämför avstånd och närvaro

**Syfte:** Träna på skillnaden mellan avståndsmätning, rörelsedetektion och tolkad närvaro.

**Återanvändbara principer:**

- skilj mellan rå sensorobservation och systemstatus
- använd hysteresis för avståndsgränser
- använd närvarohållning för rörelsesensorer
- dokumentera mätområde, falska positiva och falska negativa
- välj enkel brytare eller ljusbarriär när fysisk status är tydligare än avstånd

### Kapitel 26: Lutnings- och skakindikator

**Syfte:** Träna på skillnaden mellan enkel händelsedetektering, lutningslogik och kontinuerlig rörelsedata.

**Återanvändbara principer:**

- dokumentera sensoraxlar och faktisk montering
- skilj mellan råvärde, filtrerat värde och systemstatus
- använd debouncing eller tidslogik för tilt- och vibrationssensorer
- använd trösklar, hysteresis och tidsfönster innan rörelsedata styr en utenhet
- välj enkel sensor när kravet bara är lutat/inte lutat eller skakat/inte skakat
- använd IMU först när projektet faktiskt behöver flera rörelseaxlar eller orienteringsdata


### Kapitel 27: Ljudstyrd statusindikator

**Syfte:** Träna på skillnaden mellan ljudhändelse, relativ ljudnivå och mer avancerad ljudsampling.

**Återanvändbara principer:**

- använd tidsfönster för ljudmätning i stället för enskilda råvärden
- skilj mellan relativ ljudnivå och kalibrerad decibelmätning
- använd hysteresis och hålltid innan ljud styr systemstatus
- dokumentera mikrofonplacering, avstånd, bakgrundsljud och förstärkning
- välj digital ljudtrigger när projektet bara behöver händelser
- välj analog mikrofonmodul när projektet behöver relativ nivå
- välj I2S-mikrofon först när projektet faktiskt behöver digital ljuddata
- undvik akustisk återkoppling när projektet både lyssnar och låter

### Kapitel 28: Batteri- och lastmonitor

**Syfte:** Träna på att mäta säker lågspänd DC-spänning, tolka batteristatus och förstå skillnaden mellan spänning, ström, effekt och energi.

**Återanvändbara principer:**

- mät aldrig okänd eller för hög spänning direkt på en analog ingång
- dimensionera spänningsdelare med marginal till kortets maxnivå
- kalibrera Arduino-mätning mot multimeter när värdena ska användas för beslut
- skilj mellan rå batterispänning och tolkad batteristatus
- använd hysteresis för att undvika att batteristatus hoppar nära gränser
- välj shuntbaserad digital mätmodul när både spänning och ström ska loggas
- använd Hall-effektsensor när strömmen är högre eller isolation är viktig
- behandla energiberäkning som en uppskattning som påverkas av sampling, toppströmmar och mätfel
- mät inte nätspänning med Arduino-prototyper

### Kapitel 29: Tidsstämplad identitetshändelse

**Syfte:** Träna på att kombinera tid, nod-ID och händelseinformation så att data blir användbar som logg och referens.

**Återanvändbara principer:**

- skilj mellan tid sedan start och verklig kalender-/klocktid
- använd RTC, NTP eller GNSS när loggar behöver riktiga tidsstämplar
- spara helst loggtid i UTC om data ska jämföras eller analyseras senare
- behandla GNSS som utomhuspositionering som kräver fix och bra antennläge
- använd RFID/NFC för kortdistansidentifiering, men kalla inte UID-jämförelse för stark autentisering
- ge varje mätpunkt ett tydligt nod-ID
- skapa händelser som innehåller tid, nod, händelsetyp, värde och status
- välj kort med extra UART om GNSS och seriell debug ska användas samtidigt


### Kapitel 30: I/O-expansion med 74HC595 och MCP23017

**Syfte:** Visa hur ett Arduino-kompatibelt kort kan få fler digitala in- och utgångar utan att byta mikrokontroller.

**Återanvändbara principer:**

- använd shift register för många enkla utgångar
- använd I2C-expander för flexibel panel-I/O
- dokumentera bitnummer, fysisk pinne och funktion
- skilj mellan att styra en signal och att driva en last
- kapsla in expanderad I/O bakom tydliga funktioner
- kontrollera logiknivåer, pullups och strömgränser innan koppling


### Kapitel 31: Samma last med flera drivlösningar

**Syfte:** Träna på att skilja mellan mikrokontrollerns styrsignal, drivkretsen och lastens elektriska krav.

**Återanvändbara principer:**

- behandla GPIO som styrsignal, inte kraftutgång
- dokumentera lastspänning, lastström, drivkrets och gemensam jord
- välj MOSFET, transistorarray, H-brygga eller LED-drivare utifrån lastens beteende
- använd skydd mot induktiva spänningsspikar när lasten är relä, motor eller solenoid
- jämför färdig modul med lös drivkrets innan designen låses


### Kapitel 32: Datalogger med statusdisplay

**Syfte:** Visa hur ett Arduino-kompatibelt system kan skilja mellan direkt visning, konfiguration och historisk loggning.

**Återanvändbara principer:**

- använd EEPROM eller motsvarande för små inställningar som ändras sällan
- använd FRAM när små data behöver skrivas ofta och överleva omstart
- använd SD-kort för större mätloggar som ska kunna läsas på dator
- skriv loggar med tydliga kolumnnamn, tidsinformation, nod-ID och statusfält
- separera mätning, statusmodell, loggning och displaykod
- kontrollera displaybibliotekets RAM-krav innan display och kort väljs
- behandla displayen som en statusyta och loggen som historik
- planera för strömavbrott när SD-kort används i fält


### Kapitel 33: Analog tröskeldetektor och signalanpassning

**Syfte:** Visa hur samma analoga signal kan förstås som rå mätning, filtrerat mätvärde och digitalt tröskelbeslut.

**Återanvändbara principer:**

- mät eller uppskatta signalens verkliga min- och maxnivå innan den kopplas till ADC
- använd spänningsdelare när signalen kan överstiga kortets tillåtna ADC-område
- använd RC-filter och programvarufilter när signalen är långsam men brusig
- använd op-förstärkare för buffring, förstärkning eller aktiv filtrering när enkla passiva lösningar inte räcker
- använd komparator när systemet behöver ett snabbt och tydligt digitalt beslut
- använd hysteres för att undvika fladdrande utgångar nära tröskelvärdet
- välj färdig modul för mycket små signaler, differenssignaler eller mätningar där noggrannhet och layout är kritiska


### Kapitel 34: Strömbudget och robust matning

**Syfte:** Träna på att analysera ett Arduino-projekts matning, mäta spänning under belastning och förbättra stabilitet med separat lastmatning och bättre kopplingsdisciplin.

**Återanvändbara principer:**

- dela upp systemet i logik, mätning och laster
- gör strömbudget innan lasten kopplas in
- mät spänning vid kortet och lasten, inte bara vid adaptern
- använd separat matning för servon, motorer, LED-strippar och andra större laster
- behåll gemensam jord när styrsignaler delas mellan Arduino och extern matning
- dokumentera regulatorval, batterival och möjliga toppströmmar


## Kapitel 35: Diagnostiska testsketcher

Återkommande felsökningsexempel:

- Startdiagnostik med `Serial.begin()`, `LED_BUILTIN` och uptime via `millis()`.
- Knapptest med `INPUT_PULLUP` och loggning bara vid tillståndsändring.
- Analog råvärdesläsning innan filtrering eller kalibrering.
- I2C-scanner som standardverktyg för att kontrollera buss och adress.
- Heartbeat-funktion som visar att huvudloopen fortfarande kör.
- Boot marker som avslöjar oväntade omstarter.

Pedagogisk regel: felsökningskapitlet ska återanvändas som metodstöd i senare projektkapitel, särskilt vid integration av flera sensorer, aktuatorer och strömkrävande laster.


## Kapitel 36: Återanvändbara moduler

Återkommande exempel från kapitlet:

- miljösensormodul med VCC, GND, SDA, SCL, I2C-adress och diagnostisk testsketch
- status-LED som kapslas i en enkel `StatusLed`-klass
- `HardwareConfig.h` som samlar pinnummer, adresser och intervall
- `EnvironmentSensor` som wrapper runt ett befintligt sensorbibliotek
- fläktstyrning som exempel på en aktuator med `begin()`, `setSpeed()` och `stop()`
- dokumenterad övergång från breadboard till lödbart prototypkort

Pedagogisk regel: när ett experiment återkommer i flera kapitel ska det göras mer modulärt genom tydlig pinout, konfiguration och separat testsketch innan det integreras i större system.


### Kapitel 37: Modulär sensor- och styrstation

**Syfte:** Knyta ihop bokens tidigare delar i ett större projekt där sensorer, status, display, ljud/ljus, styrutgång och diagnostik samverkar.

**Återanvändbara principer:**

- dela upp systemet i mätning, status, utgångar, presentation och diagnostik
- testa med stubbar innan alla verkliga komponenter är inkopplade
- skilj mellan sensorvärde och systemstatus
- låt display, buzzer och styrutgång använda samma centrala statuslogik
- integrera projektet stegvis och testa även felvägar
- dokumentera pinout, I2C-adresser, matning, bibliotek och gränsvärden
- använd `millis()`-baserad tidsstyrning för mätning, blink, ljud och uppdateringar

### Kapitel 38: Egen projektspecifik valguide

**Syfte:** Träna på att använda bokens snabbvalstabeller för att skapa ett konkret beslutsunderlag för ett eget projekt.

**Återanvändbara principer:**

- börja med projektbeskrivning utan komponentnamn
- lista krav innan kort och sensorer väljs
- dokumentera förstaval, alternativ och risk
- skriv pin mapping innan koppling
- skapa testordning innan integration
- avsluta med en kort beslutstext

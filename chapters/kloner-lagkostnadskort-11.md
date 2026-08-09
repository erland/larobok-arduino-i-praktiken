# 11. Kloner, lågkostnadskort och tredjepartsvarianter

## Kortprofil i korthet
I praktiska Arduino-projekt möter du snabbt fler kort än de officiella Arduino-modellerna. Ett labb, en hobbylåda eller en webbutik kan innehålla UNO-kloner, Nano-kloner, Pro Mini-varianter, ATmega328P-kort utan tydlig märkning, CH340-baserade USB-serieadaptrar, NodeMCU, Wemos/Lolin D1 mini, ESP8266-moduler och ESP32 DevKit-kort från flera olika tillverkare.

Det är inte ett sidospår. Det är en stor del av den faktiska Arduino-världen.

Många lågkostnadskort är utmärkta för experiment. De gör det billigt att bygga flera prototyper, lämna ett kort i ett pågående projekt, testa riskabla kopplingar eller jämföra plattformar utan att varje försök blir dyrt. De kan också ge funktioner som de klassiska korten saknar, till exempel Wi-Fi, liten formfaktor eller fler moderna mikrokontrolleralternativ.

Samtidigt kan tredjepartsvarianter skapa förvirring. Två kort som ser nästan identiska ut kan ha olika USB-chip, olika regulator, olika bootloader, olika pinout, olika flashstorlek eller olika logiknivå. Ett exempel på nätet kan fungera på en officiell UNO men misslyckas på en Nano-klon med gammal bootloader. En NodeMCU kan ha pinnamn tryckta som `D1`, `D2` och `D5`, medan koden eller biblioteket förväntar sig GPIO-nummer. Ett ESP8266-kort kan vägra starta om en boot-relaterad pinne hålls i fel nivå vid uppstart.

Det här kapitlet handlar därför inte om att välja “äkta” eller “billigt”. Det handlar om att kunna identifiera vad du faktiskt har, förstå vilka risker som följer med kortet och avgöra när ett lågkostnadskort är ett bra val.

## Bedöm kortet med detta i åtanke

När du bedömer ett lågkostnadskort är det viktigaste inte priset utan hur väl det matchar projektets krav: logiknivå, USB-krets, bootloader, dokumentation, pinout, strömförsörjning och bibliotekskompatibilitet.

## Kortfamiljerna i praktiken

När någon säger “Arduino-klon” kan det betyda flera olika saker. Det är bra att skilja dem åt.

### 1. Formfaktorklon

En formfaktorklon försöker likna ett känt kort fysiskt. En UNO-klon har ofta samma pinplacering som en UNO. En Nano-klon har ofta samma smala modulformat som en Nano. Tanken är att den ska passa i samma kopplingar, shields eller breadboardupplägg.

Formfaktorn säger däremot inte allt. En UNO-formad ESP8266-baserad variant kan ha UNO-liknande headers men ändå använda 3,3 V-logik, annan mikrokontroller och andra bootregler. Då är den inte elektriskt samma sak som en UNO.

### 2. Mikrokontrollerkompatibilitet

En del kort använder samma eller mycket liknande mikrokontroller som originalet. En klassisk Nano-klon med ATmega328P beter sig ofta mycket likt en Arduino Nano i kod och periferi. Då är det rimligt att välja `Arduino Nano` eller en närliggande boarddefinition i utvecklingsmiljön.

Men även här finns detaljer: bootloader, klockfrekvens, USB-seriechip och matningslösning kan skilja.

### 3. Arduino API-kompatibilitet

NodeMCU, D1 mini och ESP32 DevKit är inte UNO-kloner, men de kan programmeras med Arduino-liknande funktioner som `pinMode()`, `digitalWrite()`, `analogRead()` och `Serial`. Det är Arduino API-kompatibilitet, inte nödvändigtvis hårdvarukompatibilitet.

Det betyder att koden kan se bekant ut, men antaganden om spänning, pinnar, ADC, PWM, timers och avbrott kan vara helt annorlunda.

### 4. Shield- eller modulkompatibilitet

Vissa kort försöker vara kompatibla med Arduino-shields. Det kan fungera för enkla shields, men det är inte garanterat. Ett shield kan anta 5 V-logik, vissa SPI-pinnar, en viss I2C-placering, en viss resetpinne eller mer ström än kortets regulator klarar.

Shield-kompatibel form betyder därför inte att alla shields är säkra eller meningsfulla att använda.

## Varför lågkostnadskort är användbara

Det är lätt att börja med riskerna, men lågkostnadskort har tydliga styrkor.

De är särskilt användbara när du vill:

- bygga flera parallella experiment
- lämna ett kort permanent i en prototyp
- testa sensorer där kopplingsfel är möjliga
- jämföra ATmega, ESP8266, ESP32 och RP2040 praktiskt
- lära dig felsökning på verkliga variationer
- bygga små IoT-noder billigt
- använda ett kort där formfaktor är viktigare än varumärke
- ha reservkort till workshops, kurser eller labbmiljöer

För en erfaren programmerare är de också pedagogiskt intressanta. De tvingar dig att sluta tänka “Arduino” som en enda specifik hårdvara och i stället tänka i lager:

- mikrokontroller
- USB-seriegränssnitt
- regulator
- bootloader
- board package
- pinout
- bibliotek
- elektriska begränsningar

När du kan identifiera dessa lager blir du mycket bättre på att felsöka alla Arduino-kompatibla projekt.

## När du bör vara försiktig

Lågkostnadskort blir problematiska när projektet kräver reproducerbarhet, långsiktig tillgång, tydlig dokumentation eller robusthet i fält. Det betyder inte att de inte går att använda, men du behöver dokumentera mer och testa hårdare.

Var extra försiktig när:

- kortet saknar tydlig tillverkare eller modellbeteckning
- pinout-bilden från säljaren inte matchar kortet du har
- USB-chipet kräver drivrutin som inte finns installerad
- uppladdning bara fungerar med “old bootloader”
- regulatorn blir varm vid extern matning
- sensorer eller moduler kräver mer ström än kortet kan leverera
- kortet blandar 5 V-matning och 3,3 V-logik på otydligt sätt
- viktiga pinnar används vid boot
- projektet ska dokumenteras för andra
- projektet ska byggas i många exemplar

I sådana lägen är det ofta bättre att välja ett kort med tydlig dokumentation, stabil produktlivscykel och välkänd pinout.

## Vanliga ATmega328P-baserade varianter

ATmega328P är mikrokontrollern som många klassiska Arduino UNO- och Nano-liknande kort bygger på. Den är enkel, välkänd och stöds av mycket exempelmaterial.

Typiska varianter är:

- UNO-kloner
- Nano-kloner
- Pro Mini-varianter
- egna små ATmega328P-kort
- färdiga sensorkort eller styrkort med Arduino-liknande bootloader

Styrkan är att mycket klassisk Arduino-kod fungerar utan större ändringar. Begränsningen är att mikrokontrollern fortfarande är liten: begränsat SRAM, begränsat flashminne, enkel ADC, inga inbyggda nätverksfunktioner och relativt få resurser jämfört med moderna kort.

### UNO-kloner

En UNO-klon är ofta det enklaste lågkostnadskortet att börja med. Den har vanligtvis USB, regulator, resetknapp, headers och UNO-liknande pinout. Den kan ofta väljas som `Arduino Uno` i utvecklingsmiljön.

Kontrollera särskilt:

- vilket USB-seriechip kortet har
- om drivrutin behövs
- om pinout verkligen följer UNO
- om kortet har 5 V-logik
- hur mycket ström regulatorn klarar
- om kvaliteten på USB-kontakt och lödningar verkar rimlig

UNO-kloner passar bra för experiment där storlek inte spelar roll och där du vill ha en stabil referensplattform.

### Nano-kloner

Nano-kloner är mycket vanliga eftersom de är små, billiga och passar på breadboard. De är ofta ATmega328P-baserade och kan användas i många projekt där en UNO vore för stor.

Kontrollera särskilt:

- om du ska välja `Arduino Nano` eller annan boarddefinition
- om processoralternativet behöver sättas till gammal eller ny bootloader
- om USB-chipet är CH340, CP210x eller något annat
- om A6 och A7 finns och bara fungerar som analoga ingångar
- hur kortet matas säkert via USB, 5 V eller VIN
- om pinnarna är lödda och sitter mekaniskt stabilt

Nano-kloner är bra när du vill gå från breadboard till kompakt prototyp. De är mindre bra när du behöver nätverk, mycket minne eller avancerad strömhantering.

### Pro Mini och liknande små ATmega-kort

Pro Mini-liknande kort saknar ofta inbyggd USB. De programmeras via extern USB-serieadapter. Det gör dem mindre bekväma men kan vara en fördel i inbyggda projekt där du vill ha liten storlek och låg strömförbrukning.

Kontrollera särskilt:

- om kortet är 5 V/16 MHz eller 3,3 V/8 MHz
- att USB-serieadaptern matchar logiknivån
- att `TX`, `RX`, `VCC`, `GND`, `DTR` eller `RTS` kopplas rätt
- att vald boarddefinition matchar klockfrekvens och spänning
- att du inte matar kortet fel väg

Pro Mini är ett bra exempel på varför “Arduino-kompatibel” inte betyder “koppla bara in USB”. Ibland måste du förstå bootloader och seriell programmering mer konkret.

## USB-seriechip: CH340, CP210x och FTDI

Många lågkostnadskort använder ett separat USB-seriechip för att översätta USB på datorn till UART på mikrokontrollern. På officiella eller dyrare kort kan andra lösningar användas, men på kloner är CH340 och CP210x mycket vanliga.

Det här påverkar främst tre saker:

- om datorn känner igen kortet som seriell port
- vilken drivrutin som behövs
- hur stabil uppladdning och seriell kommunikation blir

När ett kort inte dyker upp i Arduino IDE är det lätt att börja felsöka sketch, board eller kabel. Men felet kan vara mycket enklare: datorn har inte rätt drivrutin, USB-kabeln saknar dataledare, eller porten har inte valts.

### Praktisk kontrollista för USB-problem

Börja med detta:

- använd en USB-kabel som du vet fungerar för data
- kontrollera att kortet får ström
- kontrollera om en ny seriell port dyker upp när du ansluter kortet
- identifiera USB-chipet visuellt om det går
- installera rätt drivrutin om operativsystemet kräver det
- välj rätt port i utvecklingsmiljön
- stäng seriell monitor innan uppladdning
- testa med en minimal blink-sketch

Om porten syns men uppladdningen misslyckas kan problemet vara bootloader, boardval, fel processorval eller reset-timing.

## Bootloader och uppladdningsproblem

Bootloadern är ett litet program i mikrokontrollern som gör det möjligt att ladda upp ny kod via seriell kommunikation. På officiella kort märker du normalt inte bootloadern. På kloner märker du den när uppladdningen inte fungerar.

Typiska symptom är:

- `avrdude: stk500_recv(): programmer is not responding`
- uppladdningen startar men timeoutar
- kortet syns som port men tar inte emot kod
- koden laddas upp bara med ett visst processorval
- man måste trycka reset vid exakt rätt tidpunkt

På vissa Nano-kloner behöver du välja ett processorval som motsvarar gammal bootloader. På andra kort räcker det med vanlig Nano- eller UNO-inställning. Poängen är inte att memorera alla kombinationer, utan att känna igen bootloader som ett eget felsökningslager.

### Bootloader som felsökningslager

Tänk i den här ordningen:

1. Ser datorn USB-serieporten?
2. Är rätt port vald?
3. Är rätt kort valt?
4. Finns ett processor- eller bootloaderalternativ som passar kortet?
5. Fungerar uppladdning med en minimal sketch?
6. Behöver kortet manuell reset vid uppladdning?
7. Är bootloadern skadad eller felaktig?
8. Behöver bootloadern brännas om med programmerare?

För de flesta experiment räcker steg 1 till 5. Att bränna om bootloader är möjligt, men bör inte vara första felsökningsåtgärd.

## NodeMCU och ESP8266 som Arduino-kompatibel plattform

NodeMCU är ett vanligt utvecklingskort baserat på ESP8266. D1 mini och liknande kort bygger ofta också på ESP8266. De är inte klassiska Arduino-kloner, men de är mycket vanliga i Arduino-kompatibla IoT-projekt.

ESP8266 är intressant eftersom det ger Wi-Fi till låg kostnad. Det gör kort som NodeMCU och D1 mini attraktiva för mätstationer, enkla webbsidor, MQTT, datalogging över nätverk och små uppkopplade experiment.

Men ESP8266 skiljer sig tydligt från en UNO:

- logiknivån är normalt 3,3 V
- pinnamn på kortet matchar inte alltid GPIO-nummer i koden
- vissa pinnar påverkar boot
- ADC-funktionen är begränsad och varierar mellan kort
- Wi-Fi påverkar timing, ström och kodstruktur
- kortet kan dra tydliga strömtoppar vid sändning
- alla Arduino-bibliotek fungerar inte direkt

### NodeMCU-pinnar och GPIO-nummer

En vanlig källa till fel är att kortet är märkt med `D0`, `D1`, `D2` och så vidare, medan mikrokontrollern har GPIO-nummer. På många NodeMCU-kort motsvarar `D1` exempelvis en annan GPIO än siffran 1. Bibliotek och exempel kan använda antingen kortets `D`-namn eller råa GPIO-nummer.

Därför bör varje NodeMCU-experiment dokumentera båda:

```cpp
// Board: NodeMCU ESP8266
// LED signal: D5 on board silkscreen
// GPIO: GPIO14
const int LED_PIN = D5;
```

Om ett exempel använder `14` men din pinoutbild använder `D5` måste du veta att de avser samma fysiska signal på just ditt kort.

### Boot-relaterade pinnar på ESP8266

ESP8266 har pinnar vars nivå vid uppstart påverkar bootläget. Det betyder att en sensor, knapp, relämodul eller LED-koppling kan göra att kortet inte startar om den håller en sådan pinne i fel nivå.

Som praktisk regel: använd en pinoutkälla för just ditt kort och undvik boot-känsliga pinnar i tidiga experiment. När du senare använder dem medvetet ska du dokumentera varför kopplingen inte stör uppstart.

## D1 mini och små ESP8266-kort

D1 mini och liknande kort är mycket populära eftersom de är små, billiga och lätta att bygga in. De har ofta micro-USB eller USB-C, 3,3 V-regulator, ESP8266 och en kompakt pinrad.

De passar särskilt bra för:

- små Wi-Fi-sensorer
- enklare dataloggers
- MQTT-noder
- webbaserade statusindikatorer
- hemautomationsprojekt
- batteriexperiment med försiktig strömbudget

De passar sämre när du behöver många pinnar, mycket RAM, Bluetooth, många ADC-kanaler eller enkel 5 V-kompatibilitet. Då är ESP32 ofta ett bättre val.

## ESP32 DevKit-varianter

ESP32 DevKit-kort är också tredjeparts- och lågkostnadskort i praktisk mening, även när de bygger på välkända moduler. De är ofta kraftfullare än ESP8266 och har fler funktioner: Wi-Fi, Bluetooth eller BLE på många varianter, mer minne, fler pinnar och fler periferiområden.

Samtidigt finns många ESP32-varianter. Ett kort kan använda ESP32, ESP32-S2, ESP32-S3, ESP32-C3 eller annan medlem i familjen. Pinout, USB-funktioner, ADC, touch, Bluetooth-stöd och antal användbara pinnar kan skilja.

I det här kapitlet räcker det att se ESP32 DevKit som en typisk tredjepartsplattform där du måste kontrollera:

- exakt chip eller modul
- boarddefinition
- USB-chip eller native USB
- 3,3 V-logik
- vilka pinnar som är säkra som GPIO
- vilka pinnar som används av flash, PSRAM, USB eller boot
- regulatorns kapacitet
- antennplacering och Wi-Fi-strömförbrukning

ESP32 får ett eget kapitel senare i boken. Här är huvudpoängen att ESP32 DevKit inte är ett enda kort, utan en familj av kort som ofta säljs under mycket liknande namn.

## Skillnaden mellan pinout, silkscreen och kod

På tredjepartskort är pinout en av de vanligaste felkällorna. Silkscreen är texten tryckt på kortet. Den är praktisk, men den är inte alltid komplett och ibland inte konsekvent mellan tillverkare.

Du behöver kunna skilja mellan:

- fysisk pinne
- tryckt pinnamn på kortet
- mikrokontrollerns GPIO-nummer
- Arduino-namn i board package
- alternativ funktion som I2C, SPI, UART, ADC eller PWM

Ett bra experiment dokumenterar minst två nivåer: vad som står på kortet och vad koden använder.

Exempel:

```cpp
// Board: Wemos/Lolin D1 mini compatible
// Board label: D2
// ESP8266 GPIO: GPIO4
// Function: I2C SDA
const int I2C_SDA_PIN = D2;
```

På ett UNO-liknande ATmega-kort är detta ofta enklare eftersom `D2` och digital pin 2 brukar vara mer intuitivt kopplade. På ESP-baserade kort är det viktigare att vara explicit.

## Matning och regulatorer

Ett billigt kort kan fungera perfekt via USB men bli instabilt via VIN eller extern matning. Orsaken är ofta regulatorn, värme, spänningsfall eller att lasten drar mer än kortet är avsett för.

Kontrollera alltid:

- vilken spänning USB matar
- vilken spänning kortets logik använder
- vilken pinne som är 5 V, 3,3 V, VIN eller RAW
- om 5 V-pinnen är ingång, utgång eller båda beroende på kort
- hur mycket ström 3,3 V-regulatorn klarar
- om externa moduler ska matas från kortet eller separat
- om common ground behövs mellan separata matningar

En särskilt vanlig fälla är att använda kortets 3,3 V-pinne för att mata moduler med Wi-Fi, motorer, LED-strippar eller många sensorer. En annan är att mata via VIN med för hög spänning så att regulatorn blir varm.

Som grundregel: låt kortet styra signaler, men dimensionera matningen efter lasten.

## Logiknivåer och 5 V-fällan

Många klassiska ATmega-baserade kort använder 5 V-logik. Många ESP8266- och ESP32-kort använder 3,3 V-logik. Det är en av de viktigaste skillnaderna i hela boken.

Ett 5 V-kort kan ofta läsa och styra många äldre moduler direkt. Ett 3,3 V-kort är mer naturligt ihop med moderna sensorer, men kan skadas av 5 V-signaler på ingångar om de inte är toleranta.

Du behöver därför kontrollera:

- vilken logiknivå kortets GPIO använder
- vilken matningsspänning sensorn eller modulen kräver
- om modulens signaler följer matningen
- om I2C-pullups går till 5 V eller 3,3 V
- om nivåskiftning behövs
- om en breakout board redan har nivåskiftning

Särskilt I2C-moduler kan lura dig. En modul kan ha en sensor som egentligen är 3,3 V, men breakoutkortet kan ha regulator och nivåskiftning. En annan modul med samma sensor kan sakna detta. Läs modulens dokumentation eller mät pullup-spänningen innan du kopplar till ett 3,3 V-kort.

## Kvalitetsskillnader som spelar roll

Alla lågkostnadskort är inte lika. Vissa är mycket välgjorda. Andra fungerar men har brister som blir tydliga först när projektet växer.

Titta särskilt på:

- tydlig märkning av pinnar
- lödkvalitet
- mekaniskt stabil USB-kontakt
- regulatorns storlek och värmeutveckling
- dokumentation och pinoutbild
- tillgång till schema
- om tillverkaren anger exakt mikrokontroller
- om kortet har skyddsdioder eller säkringar
- om breadboardbredden är praktisk
- om headers följer standardavstånd

För ett snabbt experiment kanske detta spelar liten roll. För en bok, kurs, workshop eller produktliknande prototyp spelar det mycket större roll.

## Valguide

Välj lågkostnadskort när:

- du vill bygga många experiment billigt
- projektet är personligt, labbmässigt eller utforskande
- du kan acceptera variation mellan exemplar
- du är beredd att dokumentera pinout och boardval
- du vill lära dig felsökning på verkliga kort
- kortet har tillräcklig dokumentation för det du ska göra
- det finns ett aktivt community kring kortfamiljen

Välj ett bättre dokumenterat eller officiellt kort när:

- andra ska reproducera projektet
- projektet ska användas i undervisning
- felsökningstid är dyrare än hårdvaran
- projektet ska finnas länge
- du behöver stabil leverans av samma modell
- säkerhet, robusthet eller support är viktigt
- du ska skriva instruktioner som många ska följa

Det handlar alltså inte om moral eller varumärke. Det handlar om risk, dokumentation och sammanhang.

## Exempel: kortidentitet för en Nano-klon

```text
Kortidentitet
Namn på kortet: Nano V3 compatible
Trolig kortfamilj: ATmega328P/Nano
Mikrokontroller/modul: ATmega328P
USB-seriechip: CH340
Logiknivå: 5 V
Matning via USB: fungerar
Boardval i IDE: Arduino Nano
Processorval: ATmega328P eller ATmega328P Old Bootloader beroende på exemplar
Särskilda bootpinnar: inga ESP-liknande bootpinnar
Källa till pinout: Nano-kompatibel pinout, verifierad med test
Kommentar: A6/A7 används endast som analoga ingångar på denna variant.
```

Den här dokumentationen gör att du senare vet att problemet med en sensor troligen inte handlar om ESP-liknande bootpinnar, men kan handla om 5 V-logik, gammal bootloader eller USB-drivrutin.

## Exempel: kortidentitet för D1 mini

```text
Kortidentitet
Namn på kortet: D1 mini compatible
Trolig kortfamilj: ESP8266
Mikrokontroller/modul: ESP8266
USB-seriechip: CH340
Logiknivå: 3,3 V
Matning via USB: fungerar
Boardval i IDE: LOLIN(WEMOS) D1 R2 & mini eller motsvarande
Särskilda bootpinnar: ja, kontrollera pinout
Källa till pinout: D1 mini pinout för exakt variant
Kommentar: Dokumentera både D-namn och GPIO-nummer i all kod.
```

Här är de viktigaste riskerna annorlunda: 3,3 V-logik, bootpinnar, Wi-Fi-ström och pinoutnamn.

## Praktisk kontroll: identifiera kortet innan du felsöker koden

När ett lågkostnads- eller klonkort beter sig oväntat bör första kontrollen vara kortidentitet, inte applikationskod. En enkel kortprofil sparar tid senare.

Kontrollera särskilt:

- exakt kortmodell eller modulnamn
- mikrokontroller och eventuell radiomodul
- USB-seriechip och drivrutin
- valt board package och processorval i Arduino IDE
- fysisk pinout jämfört med pinnamnen i koden
- logiknivå och matning
- om kortet behöver särskild reset-, boot- eller uppladdningssekvens

Börja med en minimal uppladdning och seriell utskrift innan du kopplar in sensorer, displayer eller laster. Om den enkla kontrollen inte fungerar är det oftast kortval, drivrutin, kabel, bootloader eller board definition som ska felsökas först.

## Vanliga misstag

- **Misstag: Att anta att en klon är elektriskt identisk med originalet.**
  - Varför det händer: Kortet ser likadant ut och har liknande pinnamn.
  - Hur man undviker det: Kontrollera mikrokontroller, logiknivå, USB-chip, regulator och pinout innan inkoppling.

- **Misstag: Att felsöka kod när problemet är USB-kabel eller drivrutin.**
  - Varför det händer: Kortet får ström och ser därför “anslutet” ut.
  - Hur man undviker det: Kontrollera att en seriell port faktiskt dyker upp och använd en känd datakabel.

- **Misstag: Att välja fel bootloader- eller processorinställning.**
  - Varför det händer: Nano-kloner och äldre ATmega-varianter kan kräva annat uppladdningsval än nya exemplar.
  - Hur man undviker det: Testa minimal sketch med rätt kortval och dokumentera inställningen som fungerade.

- **Misstag: Att blanda D-namn och GPIO-nummer på ESP8266-kort.**
  - Varför det händer: Silkscreen, bibliotek och exempel använder olika namnstandarder.
  - Hur man undviker det: Dokumentera både kortets tryckta namn och faktisk GPIO i kodkommentarer.

- **Misstag: Att koppla 5 V-signaler till 3,3 V-kort.**
  - Varför det händer: Kortet matas via USB och har kanske en 5 V-pinne, vilket blandas ihop med GPIO-nivå.
  - Hur man undviker det: Behandla GPIO-logiknivå som separat från matningsspänning och använd nivåskiftning vid behov.

- **Misstag: Att använda boot-relaterade pinnar till knappar, reläer eller sensorer utan kontroll.**
  - Varför det händer: Pinnen fungerar efter uppstart men påverkar startläget.
  - Hur man undviker det: Läs pinout för kortet och undvik bootpinnar i första versionen.

- **Misstag: Att mata för många moduler från kortets regulator.**
  - Varför det händer: Det finns en 3V3- eller 5V-pinne och modulen verkar liten.
  - Hur man undviker det: Gör strömbudget och använd separat matning för laster, Wi-Fi-toppar och många moduler.

- **Misstag: Att köpa tio liknande kort och anta att alla är samma revision.**
  - Varför det händer: Webbutiker använder ibland samma produktbild för flera varianter.
  - Hur man undviker det: Märk exemplar, dokumentera testad revision och gör snabb identitetskontroll på varje ny batch.

## Snabbreferens

- Kloner och tredjepartsvarianter är en normal del av Arduino-ekosystemet.
- Ett kort kan vara formfaktorkompatibelt utan att vara elektriskt eller kodmässigt identiskt.
- ATmega328P-baserade UNO- och Nano-kloner är ofta enkla att använda men kan ha USB- och bootloaderdetaljer som behöver kontrolleras.
- CH340, CP210x och andra USB-seriechip påverkar hur kortet dyker upp på datorn.
- NodeMCU och D1 mini är Arduino-kompatibla i programmeringsmodell men skiljer sig tydligt från klassiska Arduino-kort.
- ESP8266- och ESP32-baserade kort kräver extra uppmärksamhet kring 3,3 V-logik, pinout, bootpinnar och ström.
- Dokumentera både kortets tryckta pinnamn och faktisk GPIO när det behövs.
- Lågkostnadskort är utmärkta för experiment, men sämre dokumentation kan kosta tid.
- För reproducerbara projekt är kortidentitet lika viktig som koden.
- Välj inte kort efter pris ensamt. Välj efter projektets krav, risknivå och hur mycket felsökning du är beredd att göra.

## Begreppsförklaring: bootloader, USB-seriechip och pinout

När du arbetar med kloner och lågkostnadskort behöver du ofta identifiera tre saker:

- **Bootloader:** liten programkod i mikrokontrollern som tar emot ny firmware via USB eller seriell anslutning.
- **USB-seriechip:** kretsen som gör att datorn kan prata seriellt med kortet. Vanliga exempel är CH340, CP210x och FTDI-varianter.
- **Pinout:** kartan mellan märkningen på kortet och de faktiska mikrokontrollerpinnarna.

Om uppladdning misslyckas är problemet ofta inte din sketch, utan fel board-val, fel bootloader, saknad USB-drivrutin eller en pinout som inte matchar exemplet du följer.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | 5 V eller 3,3 V beroende på kort |
| Typiskt gränssnitt | Beror på kortfamilj |
| Välj när | pris, tillgänglighet och experiment är viktigast |
| Välj inte när | reproducerbarhet, dokumentation och långsiktigt underhåll är viktigast |
| Vanliga fel | fel board package, CH340-drivrutin, pinout-avvikelse, bootloaderproblem |
| Alternativ att överväga | officiella Arduino-kort eller väldokumenterade tredjepartskort |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När ett billigt kort inte beter sig som ett originalkort, jämför med kapitel 10 och kapitel 3.
- När pinout, USB-seriechip eller bootloader styr risken, använd kortvalet i kapitel 2.
- När felet bara visar sig vid uppladdning eller seriell kommunikation, felsök enligt kapitel 35.

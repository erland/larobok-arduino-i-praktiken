# [PLAN] Kapiteltypologi

Datum: 2026-06-30  
Plansteg: 2. Skapa kapiteltypologi  
Status: Fastställd som redaktionellt styrdokument.

## Syfte

Detta dokument delar in kapitlen i *Arduino i praktiken* i praktiska kapiteltyper. Syftet är att kommande justeringar ska kunna göras mer träffsäkert än om alla kapitel följer samma kursboksmall.

Boken ska fortfarande ha tydlig progression, men varje kapitel ska redigeras efter sin funktion:

- orientera,
- förklara en grundfunktion,
- hjälpa läsaren välja plattform,
- visa hur en komponent eller sensor används,
- stärka robusthet och felsökning,
- vägleda från experiment till användbar lösning,
- fungera som snabb referens.

## Typologisk huvudprincip

Kapiteltypen avgör vilka sektioner kapitlet bör ha.

Formella rubriker som `Lärandemål`, `Quiz/reflektionsfrågor` och `Nästa steg` ska inte vara standardsvar i alla kapitel. I stället ska kapitlen få rubriker som passar läsarens användningssituation, till exempel `Snabb orientering`, `När du använder detta`, `Valguide`, `Felsökning`, `Praktiskt test`, `Snabbreferens` och `Se också`.

## Kapiteltyper

| Kapiteltyp | Kapitel | Funktion |
|---|---:|---|
| Orienteringskapitel | 1–4 | Ge läsaren rätt karta: ekosystem, kortval, verktyg och elektronikgrunder. |
| Grundfunktionskapitel | 5–9 | Förklara återkommande Arduino-funktioner som används i resten av boken. |
| Kort- och plattformskapitel | 10–16 | Hjälpa läsaren välja mellan kortfamiljer, kloner och specialplattformar. |
| Komponent- och aktuator-kapitel | 17–22 | Visa hur utenheter, ljus, ljud, motorer, laster och displayer används praktiskt. |
| Sensor- och mätkapitel | 23–29 | Visa hur mätvärden samlas in, tolkas och begränsas av verkliga förhållanden. |
| Robusthets- och kretskapitel | 30–34 | Stärka projekt med expansion, drivkretsar, minne, signalanpassning och strömförsörjning. |
| Metod- och projektkapitel | 35–37 | Hjälpa läsaren felsöka, modularisera och bygga sammanhängande lösningar. |
| Referenskapitel | 38 | Samla snabbval, jämförelser och praktiska beslutstabeller. |

## Kapitelindelning

### Orienteringskapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 1 | Arduino-kompatibla system som ekosystem | Ge mental karta över Arduino-världen. |
| 2 | Att välja rätt kort för rätt projekt | Hjälpa läsaren göra ett första praktiskt kortval. |
| 3 | Utvecklingsmiljö, bibliotek och projektstruktur | Skapa arbetsflöde för kod, bibliotek och projekt. |
| 4 | Elektriska grunder för programmerare | Repetera elektronik på den nivå som behövs för resten av boken. |

Redaktionell riktning:
- Behåll mer förklarande text än i referenskapitlen.
- Minska formella kursmarkörer.
- Använd `Snabb orientering`, `Grundidé`, `Viktiga begrepp`, `Praktiskt exempel`, `Vanliga misstag`, `Kontrollera att du hänger med`, `Snabb sammanfattning` och `Se också`.

### Grundfunktionskapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 5 | Digital I/O, knappar och logiska signaler | Grundmönster för in- och utgångar. |
| 6 | Analog läsning, ADC och mätosäkerhet | Förstå analoga värden och begränsningar. |
| 7 | PWM, timers och tidsstyrning | Styra tid, pulsbredd och återkommande beteenden. |
| 8 | Avbrott, watchdog och robust körning | Göra program mer responsiva och robusta. |
| 9 | Kommunikation: UART, I2C, SPI och 1-Wire | Förstå de bussar som återkommer i sensor- och modulkapitel. |

Redaktionell riktning:
- Dessa kapitel är bryggor mellan teori och referens.
- Behåll praktiska kodmönster och felsökning.
- Ersätt `Övningar` med `Praktiskt test`.
- Använd `Se också` för att peka till komponent- och sensorkapitel där funktionen används.

### Kort- och plattformskapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 10 | Klassiska Arduino-kort: UNO, Nano och Mega | Visa när klassiska 8-bitarskort fortfarande passar. |
| 11 | Kloner, lågkostnadskort och tredjepartsvarianter | Hjälpa läsaren förstå risker, drivrutiner och kompatibilitet. |
| 12 | Moderna Arduino-kort | Visa nya officiella kort och deras praktiska användning. |
| 13 | ESP8266 och NodeMCU | Placera ESP8266 i Arduino-världen och IoT-sammanhang. |
| 14 | ESP32-familjen i Arduino-världen | Visa styrkor, varianter och fallgropar i ESP32-familjen. |
| 15 | Raspberry Pi Pico, RP2040 och RP2350 i Arduino-miljö | Förklara Pico/RP-serien som Arduino-plattform. |
| 16 | Småkort, specialkort och avancerade utvecklingskort | Hjälpa läsaren bedöma nischade och avancerade kort. |

Redaktionell riktning:
- Dessa kapitel ska vara tydligt jämförande.
- Prioritera `När kortet passar`, `När du bör välja något annat`, `Viktiga egenskaper`, `Ström, pinnar och spänningsnivåer`, `Bibliotek och stöd`, `Vanliga misstag`, `Snabbval` och `Se också`.
- Undvik quiz. Läsaren vill främst välja rätt kort.

### Komponent- och aktuator-kapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 17 | LED, RGB-LED och ljuseffekter | Bygga grundläggande visuella utgångar. |
| 18 | Adresserbara LED: NeoPixel, WS2812 och liknande | Hantera LED-strips, timing och strömkrav. |
| 19 | Buzzers, ljudsignaler och enkla ljudutgångar | Skapa ljudåterkoppling. |
| 20 | Servon, DC-motorer och stegmotorer | Välja och styra olika motorer. |
| 21 | Reläer, MOSFET:ar, solenoider och andra laster | Styra laster säkert och robust. |
| 22 | Displayer och enkla användargränssnitt | Visa information och bygga enkel interaktion. |

Redaktionell riktning:
- Dessa kapitel ska vara mycket praktiska.
- Standardrubriker bör vara `Snabb orientering`, `När du använder detta`, `Varianter`, `Koppling`, `Kod och bibliotek`, `Elektriska krav`, `Valguide`, `Vanliga misstag`, `Felsökning`, `Praktiskt test`, `Snabbreferens` och `Se också`.
- Säkerhets- och strömfrågor ska prioriteras där laster, motorer och LED-strips ingår.

### Sensor- och mätkapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 23 | Temperatur, fukt, tryck och miljösensorer | Mäta miljövärden och förstå rimlighet. |
| 24 | Ljus, färg, UV och optiska sensorer | Mäta ljus och optiska fenomen. |
| 25 | Avstånd, närvaro och objektupptäckt | Välja avstånds- och närvaroteknik. |
| 26 | Rörelse, orientering och vibration | Tolka accelerometer, gyro och rörelse. |
| 27 | Ljud, mikrofoner och enkla signalmätningar | Mäta ljud på en praktisk nivå. |
| 28 | Ström, spänning, energi och batterimätning | Mäta elektriska storheter säkert och användbart. |
| 29 | Position, tid och identitet | Hantera GNSS, RTC, RFID och liknande identitets-/tidsfunktioner. |

Redaktionell riktning:
- Dessa kapitel ska svara på: vad kan sensorn faktiskt mäta, hur exakt är den, när luras mätvärdet och hur felsöker man?
- Prioritera `Mätprincip`, `När sensorn passar`, `Begränsningar`, `Koppling`, `Kod och bibliotek`, `Kalibrering och rimlighetskontroll`, `Felsökning`, `Praktiskt test`, `Snabbreferens` och `Se också`.
- Quiz bör normalt tas bort.

### Robusthets- och kretskapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 30 | I/O-expansion, shift registers och multiplexers | Få fler in- och utgångar. |
| 31 | Drivkretsar för LED, motorer och laster | Förstå när mikrokontrollern behöver hjälp. |
| 32 | Displaykretsar, minne och datalagring | Hantera specialkretsar, minne och lagring. |
| 33 | Analog signalanpassning, op-förstärkare och komparatorer | Anpassa signaler innan de når mikrokontrollern. |
| 34 | Strömförsörjning, batteridrift och robust konstruktion | Göra projekt elektriskt stabila och användbara över tid. |

Redaktionell riktning:
- Dessa kapitel är mer erfarna och ska få tydliga tradeoffs.
- Prioritera `Problem som kapitlet löser`, `När tekniken behövs`, `Grundprincip`, `Dimensionering`, `Koppling`, `Vanliga misstag`, `Felsökning`, `Säkerhetsruta`, `Checklista` och `Se också`.
- Här kan korta fördjupningsrutor vara motiverade.

### Metod- och projektkapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 35 | Felsökning med metod | Ge arbetsmetod för att hitta fel. |
| 36 | Från breadboard till återanvändbar modul | Visa hur experiment blir mer hållbara moduler. |
| 37 | Sammanhängande projekt: modulär sensor- och styrstation | Knyta ihop kort, sensorer, styrning och struktur. |

Redaktionell riktning:
- Dessa kapitel ska kännas som praktiska arbetsguider.
- Använd `Snabb orientering`, `Arbetssättet`, `Steg för steg`, `Beslutspunkter`, `Vanliga misstag`, `Praktiskt arbetspass`, `Checklista` och `Se också`.
- Här kan reflektionsfrågor förekomma, men bara om de stödjer designbeslut.

### Referenskapitel

| Kapitel | Titel | Primär funktion |
|---:|---|---|
| 38 | Referens: snabbvalsguider och jämförelsetabeller | Hjälpa läsaren fatta snabba beslut och hitta tillbaka i boken. |

Redaktionell riktning:
- Kapitel 38 ska inte behandlas som ett vanligt kapitel.
- Det bör ha en ren referensstruktur: `Så använder du referensen`, `Snabbval: kort`, `Snabbval: sensorer`, `Snabbval: aktuatorer`, `Snabbval: kommunikation`, `Snabbval: strömförsörjning`, `Felsökningsöversikt` och `Säkerhetsöversikt`.
- Inga lärandemål, övningar eller quiz.

## Konsekvenser för nästa plansteg

Nästa steg är att definiera mall per kapiteltyp. Denna typologi ska då användas för att ta fram konkreta strukturmallar för varje grupp.

När pilotkapitel väljs bör de representera flera kapiteltyper. Rekommenderade pilotkapitel är:

| Syfte | Föreslaget kapitel |
|---|---|
| Orientering | Kapitel 2 eller 3 |
| Grundfunktion | Kapitel 8 eller 9 |
| Plattform | Kapitel 13 eller 15 |
| Komponent/sensor | Kapitel 20 eller 23 |
| Referens | Kapitel 38 |

## Redaktionsregel

Vid kommande omskrivningar ska varje kapitel först identifieras med kapiteltyp innan rubriker ändras. Kapiteltypen avgör vilka sektioner som tas bort, slås ihop, döps om eller förstärks.

## Relaterade styrdokument

- `docs/editorial-target.md` beskriver den övergripande redaktionella målbilden.
- `docs/chapter-templates-by-type.md` definierar mallarna som ska användas för respektive kapiteltyp.


## Pilotstatus

Kapitel 2, 8, 13, 20 och 38 har pilotjusterats enligt respektive kapiteltyp. Resultatet dokumenteras i `docs/pilot-adjustment-log.md`.

## Slutlig strukturregel

Från och med `[PLAN]` steg 6 ska detta dokument läsas tillsammans med `docs/final-structure-rule.md`, som fastställer hur kapiteltypsanpassade rubriker ska användas i den fortsatta batchjusteringen.



## Batchstatus för plansteg 7

| Batch | Kapitel | Kapiteltyp | Status |
|---:|---:|---|---|
| 1 | 1–4 | Orienteringskapitel | Genomförd |
| 2 | 5–9 | Grundfunktionskapitel | Genomförd |
| 3 | 10–16 | Kort- och plattformskapitel | Genomförd |
| 4 | 17–22 | Komponent- och aktuator-kapitel | Genomförd |
| 5 | 23–29 | Sensor- och mätkapitel | Ej påbörjad |
| 6 | 30–34 | Robusthets- och kretskapitel | Ej påbörjad |
| 7 | 35–38 | Metod-, projekt- och referenskapitel | Ej påbörjad |

# [ANALYSPLAN] steg 5 – Kapitel 16–20

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–4 genomförda  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar kapitel 16–20 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 16 | `chapters/smakort-specialkort-16.md` | Kort och plattform | Hjälpa läsaren förstå specialkort, småkort, Feather/XIAO/QT Py, Teensy, ESP32-CAM och mer avancerade kort. |
| 17 | `chapters/led-rgb-ljuseffekter-17.md` | Praktisk komponent / utenhet | Förklara vanlig LED, RGB-LED, statusljus, strömbegränsning och enkla ljuseffekter. |
| 18 | `chapters/adresserbara-led-18.md` | Praktisk komponent / utenhet | Förklara NeoPixel/WS2812-liknande LED, strömbudget, nivåer, bibliotek och icke-blockerande effekter. |
| 19 | `chapters/buzzers-ljudsignaler-19.md` | Praktisk komponent / utenhet | Förklara buzzers, piezo, små högtalare, LM386, enkla ljudmönster och ljud som systemstatus. |
| 20 | `chapters/servon-motorer-20.md` | Praktisk komponent / aktuator | Hjälpa läsaren välja mellan servo, DC-motor, stegmotor och vanliga drivmoduler. |

Analysen har läst faktisk kapiteltext och fokuserar särskilt på övergången från kortvalskapitel till praktiska utenheter och aktuatorer. Blocket är viktigt eftersom det är här boken börjar kännas som en komponenthandbok snarare än en introduktionskurs.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Det du kan använda kapitlet till` | `Praktiskt test` | `Prova vidare` | Kontrollsektion | `Valguide` | `Snabbval` |
|---:|---:|---:|---:|---:|---|---|---|---|---|---|
| 16 | 4292 | 21 | 36 | 8 | Nej | Ja | Ja | Ja: `Kontrollera ditt val` | Ja | Ja |
| 17 | 4766 | 35 | 12 | 23 | Ja | Ja | Nej | Ja: `Kontrollera ditt val` | Nej | Ja |
| 18 | 3861 | 31 | 10 | 6 | Ja | Ja, två förekomster | Nej | Ja: `Kontrollera ditt val` | Ja | Ja |
| 19 | 4310 | 27 | 16 | 10 | Ja | Ja, två förekomster | Nej | Ja: `Kontrollera ditt val` | Nej | Ja |
| 20 | 4660 | 18 | 27 | 11 | Nej | Ja, två förekomster | Nej | Ja: `Kontrollera ditt val` | Nej | Ja |

Tolkning: blocket är mycket praktiskt och ämnesmässigt väl placerat. Samtidigt visar översikten en tydlig strukturell signal: kapitel 17–20 använder många kursmarkörer även när innehållet egentligen är handboksnära. Särskilt `Praktiskt test` används både för fullständiga exempelprojekt och för kortare kontrollmoment, vilket gör rubrikfunktionen oklar.

## Övergripande slutsats

Kapitel 16–20 är ett starkt block. Det för läsaren från specialiserade kort till konkreta utenheter: ljus, adresserbart ljus, ljud och rörelse. Det är ett naturligt skifte i boken. Efter att ha valt plattform behöver läsaren kunna ge projektet återkoppling och fysisk verkan.

Blockets största redaktionella styrka är att det innehåller verkliga, återanvändbara projektmönster:

- kortprofil för specialkort,
- statusljus med LED eller RGB-LED,
- LED-ring som visuell mätare,
- ljudmönster för systemstatus,
- servo som fysisk indikator,
- motorval som jämförelse mellan rörelsetyper.

Det redaktionella problemet är inte att blocket är praktiskt. Praktiken är central här. Problemet är att praktiken ibland presenteras som **experiment, test och kontrollfrågor** snarare än som **verifiering, referensmönster, beslutsguide och felsökning**. Det gör att boken fortfarande kan upplevas som en kursbok, trots att innehållet egentligen är mycket handboksnära.

För `[PLAN-H]` bör detta block därför behandlas med en annan regel än de rena teorikapitlen. I kapitel 17–20 ska praktiska moment i regel behållas, men byta funktion och rubrik:

- `Praktiskt test` bör i komponentkapitel ofta bli `Minsta fungerande koppling`, `Referensmönster`, `Verifiera kopplingen` eller `Bygg ett återanvändbart exempel`.
- Dubbla `Praktiskt test`-sektioner bör undvikas. Ett kapitel bör normalt ha högst ett huvudexempel och därefter eventuella `Kontroller`, `Varianter` eller `Felsökning`.
- `Kontrollera ditt val` bör byta från quizfrågor till beslutschecklista, felsökningschecklista eller `Innan du väljer`.
- Kravformuleringar som `Efter kapitlet ska du kunna` bör ersättas med handboksnära nytta, till exempel `Kapitlet hjälper dig att`, `Du får stöd för att` eller `Efter genomgången blir det lättare att`.

## Kapitel 16 – Småkort och specialkort

### Det fungerar väl

Kapitlet är en naturlig fortsättning på plattformskapitlen 10–15. Det fångar upp kort som annars lätt hamnar utanför huvudkategorierna: småkort, Feather/XIAO/QT Py-liknande kort, Teensy, ESP32-CAM, Portenta, Nicla och mer specialiserade kort.

Handbokskänslan är stark eftersom kapitlet hjälper läsaren med ett verkligt valproblem: kortet har en särskild formfaktor eller specialfunktion, men det kan också innebära svårare pinout, annan logiknivå, sämre breadboardvänlighet, annan USB-hantering, mer värme eller mer beroende av dokumentation.

Särskilt bra är att kapitlet inte försöker katalogisera varje modell. Det presenterar specialisering som ett valmönster. Det är rätt nivå för en handbok, eftersom marknaden ändras snabbare än bokens huvudprinciper.

`Praktiskt test: utvärdera ett specialkort` är ett av blockets mest handboksnära praktiska moment. Det fungerar egentligen som en metod: skapa kortprofil, testa I/O, testa seriell loggning och bedöm kortet mot ett tänkt projekt. Det är inte ett skoltest utan ett professionellt arbetsmönster.

### Läroboksspår

Kapitlet har fortfarande `Kontrollera ditt val` i form av tio frågor. Flera av frågorna är relevanta, men formen gör att avsnittet delvis känns som avslutande kontrollfrågor.

Exempel på frågor som är användbara men bör byta format:

- varför ett specialkort kan vara svårare trots fler funktioner,
- när småkort är bättre än UNO/ESP32 DevKit,
- risker med samma formfaktor men olika mikrokontroller,
- varför batteristöd inte är samma sak som låg energiförbrukning,
- vad som bör ingå i en kortprofil.

Dessa passar bättre som `Beslutschecklista för specialkort` eller `Kontroll före köp eller projektstart`.

### Rekommendation för PLAN-H

- Behåll kapitlet i stort sett intakt.
- Byt `Praktiskt test: utvärdera ett specialkort` till en mer handboksnära rubrik, till exempel `Skapa en kortprofil` eller `Verifiera ett specialkort innan projektstart`.
- Omvandla `Kontrollera ditt val` till en checklista.
- Behåll `Snabbval`, eftersom den passar mycket väl för kortkapitel.
- Bevara tonen: kapitlet är ett positivt exempel på hur specialiserad hårdvara kan presenteras utan att bli produktkatalog.

### Bedömning

- Handbokskänsla: 4,5/5
- Läroboksspår: låg till medel
- Behov av redaktionell åtgärd: låg
- Risk vid ändring: låg

## Kapitel 17 – LED, RGB-LED och ljuseffekter

### Det fungerar väl

Kapitlet markerar en bra övergång från plattformar till konkreta utenheter. LED är en enkel komponent, men kapitlet behandlar den på rätt praktiska nivå: polaritet, seriemotstånd, pinström, PWM, RGB-varianter, statusmönster, `delay()`-problem och när MOSFET eller drivkrets behövs.

Det är en styrka att LED inte bara behandlas som “första Arduino-exemplet” utan som systemåterkoppling. Kapitlet förklarar att LED kan visa start, väntan, aktivitet och fel. Det är en mycket handboksnära vinkel eftersom läsaren kan använda detta i nästan alla senare projekt.

`Praktiskt test: bygg ett statusljus med flera lägen` är relevant och bör i någon form behållas. Det är inte ett teoriexperiment utan ett återanvändbart komponentmönster.

### Läroboksspår

Kapitlet har `Det du kan använda kapitlet till` men inleder sedan med `Efter kapitlet ska du kunna`. Det är exakt den typ av formulering som användaren tidigare reagerat på. Den är korrekt, men tonen är kursmål snarare än handbok.

Avsnittet listar många mål:

- förklara strömbegränsning,
- välja seriemotstånd,
- skilja mellan LED-typer,
- använda digital utgång och PWM,
- bygga statusmönster,
- resonera om direkt pin-styrning kontra drivsteg,
- identifiera vanliga fel.

Innehållet är bra, men bör formuleras som användningsstöd, inte prestationskrav.

`Kontrollera ditt val` består av tio frågor. Flera är tekniskt värdefulla, men formen gör att kapitlet avslutas mer som ett kunskapsprov än som en handbokssida. Frågorna om seriemotstånd, RGB-motstånd, common anode, `delay()` och MOSFET bör hellre bli `Vanliga misstag`, `Snabb kontroll före koppling` eller `Felsök om LED inte beter sig rätt`.

### Rekommendation för PLAN-H

- Byt `Efter kapitlet ska du kunna` till en mjukare formulering, till exempel `Kapitlet hjälper dig att använda LED som tydlig och säker återkoppling i projekt`.
- Behåll huvudexemplet med statusljus, men byt rubrik från `Praktiskt test` till `Referensmönster: statusljus med flera lägen` eller `Bygg ett återanvändbart statusljus`.
- Omvandla `Kontrollera ditt val` till två mer handboksnära avsnitt:
  - `Snabb kontroll före koppling`
  - `Vanliga misstag med LED och RGB-LED`
- Behåll `Snabbval`, men ta bort standardfrasen `Använd referensrutan som en snabb kontroll innan du bygger experimentet` eller gör den mer neutral, eftersom alla kapitel inte bör kallas experiment.

### Bedömning

- Handbokskänsla: 3,5/5
- Läroboksspår: medel
- Behov av redaktionell åtgärd: medel
- Risk vid ändring: låg till medel

## Kapitel 18 – Adresserbara LED: NeoPixel, WS2812 och liknande

### Det fungerar väl

Kapitlet är praktiskt viktigt och placerat rätt efter vanlig LED/RGB-LED. Det gör en tydlig distinktion mellan vanliga LED och adresserbara LED: dataledning, inbyggd styrkrets, datapaket, timing, strömförsörjning, minnesanvändning, nivåskiftning och bibliotek.

Det är särskilt bra att kapitlet inte behandlar NeoPixel/WS2812 som “bara fler LED”. Det betonar att adresserbara LED fungerar mer som digitala utenheter med särskilda krav. Det ger stark handbokskänsla.

Säkerhetsrutan om strömbudget är mycket viktig och bör behållas. Den påminner läsaren om att LED-strippar snabbt kan dra flera ampere och att separat matning, grövre ledare, gemensam jord och säkring kan behövas.

### Läroboksspår och överlapp

Kapitlet har två `Praktiskt test`-nivåer:

1. `Praktiskt test: sensorstyrd LED-ring`
2. Ett senare `Praktiskt test` med `Test 1: Färgtest och färgordning`, `Test 2: Strömbudget`, `Test 3: Icke-blockerande indikator`, `Test 4: Sensorvisualisering` och fördjupning.

Här blir strukturen otydlig. Det första är ett huvudexempel. Det andra är egentligen en samling verifierings- och felsökningsmoment. När båda heter `Praktiskt test` får kapitlet kursbokskänsla och rubrikens betydelse blir mindre tydlig.

`Det du kan använda kapitlet till` använder också `Efter kapitlet ska du kunna`, vilket bör justeras.

`Kontrollera ditt val` innehåller åtta frågor. De är relevanta men bör omformas till exempelvis:

- `Innan du kopplar en LED-strip`
- `Felsök om strippen flimrar eller visar fel färger`
- `Välj rätt typ av adresserbar LED`

### Rekommendation för PLAN-H

- Byt första praktiska avsnittet till `Referensmönster: sensorstyrd LED-ring` eller `Bygg en visuell mätare med LED-ring`.
- Byt det andra `Praktiskt test` till `Verifiera strippen steg för steg`.
- Gör `Test 1–4` till verifieringspunkter snarare än övningar.
- Omvandla `Kontrollera ditt val` till en praktisk besluts- och felsökningschecklista.
- Behåll säkerhetsrutan och gör den gärna ännu mer framträdande.
- Bevara kopplingen till kapitel 34 om strömförsörjning och kapitel 21 om laststyrning.

### Bedömning

- Handbokskänsla: 3,5/5
- Läroboksspår: medel
- Behov av redaktionell åtgärd: medel
- Risk vid ändring: medel, eftersom praktiska avsnitt behöver omstruktureras utan att tappa värdefullt innehåll

## Kapitel 19 – Buzzers, ljudsignaler och enkla ljudutgångar

### Det fungerar väl

Kapitlet fyller en tydlig praktisk funktion. Ljud är en annan typ av återkoppling än LED och display, och kapitlet förklarar bra varför ljud kan vara användbart när användaren inte tittar på projektet.

Det är starkt att kapitlet skiljer mellan aktiv buzzer, passiv buzzer, piezoelement, liten högtalare och förstärkt ljudmodul. Det är ett område där många nybörjare tror att alla små ljudkomponenter fungerar likadant. Här ger boken verklig praktisk hjälp.

PLAN5-tillägget om LM386 passar väl in i kapitlets handboksidentitet. Det ger en rimlig brygga mellan enkel buzzer och liten högtalare utan att göra kapitlet till en ljudteorikurs.

`Praktiskt test: ljudsignaler för systemstatus` är ett bra exempel. Det bygger ett användbart ljudspråk med start, varning och fel. Det passar bokens återkommande idé om systemstatus.

### Läroboksspår och överlapp

Även här finns två praktiska nivåer:

1. `Praktiskt test: ljudsignaler för systemstatus`
2. Ett senare `Praktiskt test` med `Test 1: Identifiera dina ljudkomponenter`, `Test 2: Skapa ett ljudspråk`, `Test 3: Koppla ljud till sensorvärde` och fördjupning.

Det andra avsnittet är egentligen inte ett nytt praktiskt test utan en blandning av identifiering, vidarearbete och tillämpningsvarianter. Det bör byta namn.

`Det du kan använda kapitlet till` använder `Efter kapitlet ska du kunna`. Här blir det särskilt skolmässigt eftersom listan är lång och innehåller både begrepp, kod, felsökning och experiment.

`Kontrollera ditt val` består av frågor som skulle fungera bättre som beslutsstöd:

- aktiv eller passiv buzzer,
- direktdrivning eller drivsteg,
- när `delay()` är acceptabelt,
- timerkonflikter med `tone()`,
- ljudmönstrets användbarhet,
- gemensam jord,
- val för larm, knappbekräftelse eller tal.

### Rekommendation för PLAN-H

- Byt `Praktiskt test: ljudsignaler för systemstatus` till `Referensmönster: ljudsignaler för systemstatus`.
- Byt andra `Praktiskt test` till `Verifiera ljudkomponenten` eller `Bygg vidare med ljudmönster`.
- Omvandla `Kontrollera ditt val` till `Välj rätt ljudutgång` eller `Snabb kontroll före koppling`.
- Behåll innehållet om timerkonflikter och direktdrivning, men placera det mer som felsöknings- och riskinformation.
- Bevara LM386-tillägget, eftersom det gör kapitlet mer användbart utan att bli för teoretiskt.

### Bedömning

- Handbokskänsla: 3,5/5
- Läroboksspår: medel
- Behov av redaktionell åtgärd: medel
- Risk vid ändring: låg till medel

## Kapitel 20 – Servon, DC-motorer och stegmotorer

### Det fungerar väl

Kapitlet har stark handboksidentitet redan från början. `Snabb orientering` säger tydligt vad läsaren använder kapitlet till: välja och använda rörelse i Arduino-projekt. Det är en bättre formulering än `Efter kapitlet ska du kunna`.

Kapitlet gör en viktig uppdelning mellan servo, kontinuerlig servo, DC-motor och stegmotor. Det är precis den typ av valstöd en handbok ska ge. Tabeller och jämförelser är relevanta och praktiskt användbara.

PLAN5-tilläggen om PCA9685, L298N, DRV8833, L9110S, ULN2003, A4988 och DRV8825 verkar väl integrerade i kapitlets syfte. Snabbvalstabellen är särskilt värdefull eftersom den samlar flera vanliga motor- och drivmodulsval på ett ställe.

Säkerhetsrutan `motorer är inte logiska laster` är mycket viktig och bör behållas. Den sammanfattar ett centralt handboksbudskap: motorer är induktiva, drar startström och kräver ofta separat drivning.

### Läroboksspår och överlapp

Kapitlet saknar `Det du kan använda kapitlet till` och undviker därmed den värsta målformuleringen. Det är positivt.

Däremot har kapitlet två praktiska nivåer:

1. `Praktiskt test: servo som fysisk sensorindikator`
2. Ett senare `Praktiskt test` med test 1–4: servovisare, motortypval, DC-motor med säker start och stegmotor med acceleration.

Det första är ett huvudexempel. Det andra är en samling validerings- och fördjupningsscenarier. Rubriken `Praktiskt test` blir därför överanvänd.

`Kontrollera ditt val` består av tio frågor. Frågorna är relevanta, men i ett motor-/aktuator-kapitel bör de snarare fungera som riskkontroll och beslutschecklista:

- ryckande servo,
- standardservo kontra kontinuerlig servo,
- direktdrivning av motor,
- H-brygga,
- PWM och verklig hastighet,
- tappade steg,
- gemensam jord,
- svag matning,
- icke-blockerande servokod.

### Rekommendation för PLAN-H

- Bevara kapitlets övergripande struktur; det fungerar redan som handbok.
- Byt `Praktiskt test: servo som fysisk sensorindikator` till `Referensmönster: servo som fysisk indikator`.
- Byt det andra `Praktiskt test` till `Verifiera rörelse och matning` eller `Praktiska kontroller för motorprojekt`.
- Omvandla `Kontrollera ditt val` till `Riskkontroll före motorprojekt` eller `Felsök rörelseproblem`.
- Lyft gärna fram snabbvalstabellen tidigare eller hänvisa till den före den avslutande kontrollsektionen.
- Behåll säkerhetsrutan oförändrad eller förstärk den.

### Bedömning

- Handbokskänsla: 4/5
- Läroboksspår: låg till medel
- Behov av redaktionell åtgärd: låg till medel
- Risk vid ändring: medel, eftersom motoravsnittens säkerhets- och verifieringsmoment inte får försvagas

## Mönster i blocket

### 1. Praktiska moment är motiverade, men rubriken `Praktiskt test` gör för mycket

I detta block ska praktiska moment inte tas bort. LED, adresserbara LED, ljud och motorer behöver konkreta kopplingar och kod. Däremot bör rubriken `Praktiskt test` inte användas för både huvudexempel, felsökning, verifiering, validering och fördjupning.

För `[PLAN-H]` bör rubriken ersättas beroende på funktion:

| Nuvarande funktion | Rekommenderad handboksrubrik |
|---|---|
| Ett återanvändbart exempel | `Referensmönster` |
| Första kopplingen | `Minsta fungerande koppling` |
| Säkerhets- eller funktionskontroll | `Verifiera innan du bygger vidare` |
| Felsökning | `Om det inte fungerar` |
| Val mellan alternativ | `Välj rätt lösning` |
| Frivillig utökning | `Bygg vidare vid behov` |

### 2. `Kontrollera ditt val` är bättre än quiz, men bör bli ännu mer handboksnära

I blocket används `Kontrollera ditt val` i alla fem kapitel. Det är bättre än `Kontrollera att du hänger med`, men formen är fortfarande ofta en numrerad frågelista.

I `[PLAN-H]` bör dessa avsnitt normalt omvandlas till:

- `Snabb kontroll före koppling`,
- `Beslutschecklista`,
- `Riskkontroll`,
- `Vanliga misstag`,
- `Felsök om...`.

### 3. Kravformuleringen finns främst i kapitel 17–19

Kapitel 16 och 20 undviker i stort sett `Efter kapitlet ska du kunna`. Kapitel 17, 18 och 19 använder den däremot tydligt under `Det du kan använda kapitlet till`.

Detta ger en tydlig PLAN-H-regel: komponentkapitel bör beskriva **vad kapitlet hjälper läsaren göra**, inte vad läsaren ska kunna prestera efteråt.

### 4. Blocket har starka säkerhets- och robusthetsbudskap

Kapitel 18 och 20 har särskilt viktiga säkerhetsrutor. Kapitel 17, 19 och 20 betonar ström, drivsteg, pinbegränsningar och `delay()`-problem. Detta är mycket bra och bör inte tonas ned i redigeringen.

### 5. Kapitel 16 och 20 fungerar som positiva modeller

Kapitel 16 visar hur ett praktiskt test kan vara en arbetsmetod: skapa kortprofil och verifiera kortet. Kapitel 20 visar hur `Snabb orientering` kan uttrycka användningsnytta utan att låta som lärandemål.

PLAN-H bör använda dessa två kapitel som stilreferenser för andra delar av boken.

## Förslag till PLAN-H-regler från steg 5

1. **Praktik i komponentkapitel ska behållas men funktionsmärkas.**  
   Byt generiska `Praktiskt test` mot rubriker som säger vad läsaren får: referensmönster, minsta koppling, verifiering, felsökning eller vidarebyggnad.

2. **Undvik dubbla `Praktiskt test` i samma kapitel.**  
   Om ett kapitel har ett huvudexempel och flera kortare tester ska huvudexemplet få en tydlig rubrik och de kortare testerna samlas som `Verifiera`, `Kontrollera` eller `Bygg vidare`.

3. **Byt kravmål mot användningsnytta.**  
   Formuleringen `Efter kapitlet ska du kunna` bör ersättas i kapitel 17–19 och eventuellt i andra kapitel som identifieras senare.

4. **Omvandla kontrollfrågor till handboksverktyg.**  
   `Kontrollera ditt val` bör inte vara en quizlista. Den bör bli beslutschecklista, riskkontroll, felsökningshjälp eller vanliga misstag.

5. **Säkerhetsrutor och robusthetsvarningar ska prioriteras.**  
   Redigering får inte ta bort varningar om ström, extern matning, gemensam jord, nivåskiftning, motorstörningar, flyback/induktiva laster eller timerkonflikter.

6. **Standardfrasen efter `Snabbval` bör ses över.**  
   Frasen `Använd referensrutan som en snabb kontroll innan du bygger experimentet` återkommer och gör även handboksavsnitt till experiment. I komponentkapitel kan den ersättas med `Använd rutan när du snabbt vill kontrollera om komponenten passar ditt projekt`.

## Sammanfattande bedömning för blocket

- Handbokskänsla: 4/5
- Läroboksspår: medel
- Behov av redaktionell åtgärd: medel
- Risk vid ändring: medel

Kapitel 16–20 bör inte förenklas genom att praktiken tas bort. Tvärtom är praktiken blockets styrka. Det viktiga inför `[PLAN-H]` är att ge praktiken rätt redaktionell funktion. Läsaren ska känna att avsnitten är återanvändbara arbetsmönster och kontroller, inte övningar som ska klaras av.

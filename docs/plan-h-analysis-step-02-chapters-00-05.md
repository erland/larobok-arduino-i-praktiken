# [ANALYSPLAN] steg 2 – Kapitel 00–05

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1 genomfört  
Status: Genomförd  
Resultattyp: Redaktionell analys. Inga kapitel eller bokmanus har ändrats.

## Omfattning

Detta steg analyserar inledningen och kapitel 1–5 enligt projektets kapitelordning:

| Nr | Fil | Kapiteltyp enligt steg 1 | Funktion i boken |
|---:|---|---|---|
| 00 | `chapters/00-inledning.md` | Inledning | Förklara bokens användning och positionera handboksidentiteten. |
| 01 | `chapters/ekosystem-01.md` | Orientering | Ge karta över Arduino-ekosystemet. |
| 02 | `chapters/valja-ratt-kort-02.md` | Orientering | Hjälpa läsaren välja kort utifrån projektkrav. |
| 03 | `chapters/utvecklingsmiljo-bibliotek-03.md` | Orientering | Göra verktyg, bibliotek och projektstruktur reproducerbara. |
| 04 | `chapters/elektriska-grunder-04.md` | Orientering | Ge elektrisk grundmodell för resten av boken. |
| 05 | `chapters/digital-io-05.md` | Grundfunktion | Förklara robust digital I/O, knappar och logiska signaler. |

Analysen har läst faktisk kapiteltext och bedömt både struktur, rubriker, ton, praktiska moment, kontrollfrågor och handbokskänsla.

## Snabb kvantitativ översikt

| Kapitel | Ord | H2 | H3 | Kodblock | `Praktiskt test` | `Prova själv` | Kontroll-/quizsektion |
|---:|---:|---:|---:|---:|---:|---:|---|
| 00 | 891 | 8 | 0 | 0 | Nej | Nej | Nej |
| 01 | 3159 | 15 | 27 | 7 | Ja | Ja | Ja: `Kontrollera att du hänger med` |
| 02 | 4253 | 37 | 4 | 4 | Ja | Ja | Ja: `Kontrollera ditt val` |
| 03 | 3791 | 26 | 11 | 19 | Ja | Nej | Ja: `Kontrollera att du hänger med` |
| 04 | 4089 | 26 | 8 | 17 | Ja | Ja | Ja: `Kontrollera att du hänger med` |
| 05 | 3909 | 25 | 9 | 13 | Ja | Nej | Ja: `Kontrollera att du hänger med` |

Tolkning: blocket är innehållsrikt och praktiskt användbart, men kapitel 1–5 bär tydliga spår av kurs-/läroboksmall. Det gäller framför allt kombinationen av `Praktiskt test`, `Prova själv` och kontrollfrågor i orienteringskapitel.

## Övergripande slutsats

Kapitel 00–05 fungerar innehållsmässigt väl som första delen av boken. De ger läsaren en bra startpunkt och täcker rätt frågor: vad Arduino-kompatibilitet betyder, hur man väljer kort, hur utvecklingsmiljön fungerar, vilka elektriska risker som är vanliga och hur digital I/O bör förstås.

Den redaktionella svagheten är inte innehållet utan **ramen runt innehållet**. Flera kapitel låter fortfarande som kurskapitel med mål, test, uppgifter och kontrollfrågor. Det gör att boken ibland signalerar att läsaren ska examineras, trots att v4:s identitet är en praktisk handbok.

För `[PLAN-H]` bör fokus därför vara att behålla innehållsnyttan men ändra formen:

- från lärandemål till användningsnytta,
- från quiz till vanliga missförstånd eller snabb självkontroll,
- från teoriexperiment till praktisk tillämpning när det faktiskt behövs,
- från mekaniska kapitelmallar till kapiteltypanpassade strukturer.

## Kapitel 00 – Inledning

### Det fungerar väl

Inledningen positionerar boken tydligt för läsare som redan kan programmera och har viss Arduino-erfarenhet. Den förklarar att boken inte är en ren nybörjarbok och att målet är att hjälpa läsaren känna igen mönster, välja rimliga lösningar och kontrollera praktiska krav innan koppling och kod.

Avsnitten `Vad boken handlar om`, `Vem boken är för`, `Hur boken är upplagd`, `Säkerhet och rimliga gränser` och `Välj din väg` fungerar väl för en handbok.

### Problem

Inledningen innehåller en intern projektartefakt i läsartexten:

> `docs/lookup-index.md` fungerar som projektets tematiska uppslagsindex och redaktörsstöd när kapitel flyttas, döps om eller får nytt fokus.

Detta bör inte finnas i boken. Det är sant för projektarbetet, men irrelevant och förvirrande för läsaren. Det avslöjar också redaktionell infrastruktur som inte hör hemma i EPUB/PDF.

Inledningen säger dessutom:

> Boken är både en lärobok och en referens.

Det är begripligt, men det riskerar att legitimera just de läroboksspår som analysen försöker minska. För v5/PLAN-H bör bokens läsaridentitet hellre formuleras som praktisk handbok med pedagogiska förklaringar, inte som lärobok.

Avsnittet `Bokens återkommande arbetssätt` säger att många kapitel har ett praktiskt test eller en praktisk tillämpning. Det kan behöva justeras om PLAN-H tar bort teoriexperiment från rena orienteringskapitel.

### Rekommendation för PLAN-H

- Ta bort alla interna filreferenser ur läsartexten.
- Byt formuleringen `Boken är både en lärobok och en referens` till en tydligare handboksformulering.
- Uppdatera beskrivningen av återkommande arbetssätt så att den inte utlovar `Praktiskt test` i kapitel där det inte behövs.
- Behåll `Kapitel 38` som läsarens snabbväg, eftersom det är en riktig bokreferens.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 1 – Arduino-kompatibla system som ekosystem

### Det fungerar väl

Kapitlet ger en mycket användbar karta över vad Arduino-kompatibilitet betyder. Det gör en viktig distinktion mellan kort, mikrokontroller, Arduino-API, core, board package, bibliotek, exempel, shields, breakout boards och moduler. Detta är starkt handboksinnehåll eftersom det hjälper läsaren tolka tutorials, produkttexter och kompatibilitetsproblem.

Avsnitten om pinout, spänningsnivåer, cores och bibliotek är särskilt relevanta för praktiska projekt.

### Problem

`Snabb orientering` innehåller formuleringen:

> Efter kapitlet ska du framför allt kunna skilja på:

Det är en tydlig läroboksmarkör. Den är inte katastrofal, eftersom den följs av praktiska distinktioner, men den signalerar krav och mål snarare än nytta.

Kapitlet innehåller både:

- `Praktiskt test: kartlägg två kort och en modul`
- `Prova själv`
- `Kontrollera att du hänger med`

Det blir tre separata elev-/övningsramar. Innehållet i dem är i grunden användbart, men mängden rubrikramar gör kapitlet mer kurslikt än handbokslikt.

`Praktiskt test` är delvis motiverat, eftersom det tränar läsaren att läsa kort, board package och modulkrav. Däremot överlappar `Prova själv` med samma funktion. Quizet bör inte ligga kvar som provfrågor.

### Rekommendation för PLAN-H

- Ersätt kravformuleringen i `Snabb orientering` med något i stil med:
  - `Kapitlet hjälper dig att känna igen skillnaden mellan:`
  - eller `Efter genomgången blir det lättare att skilja mellan:`
- Slå ihop `Praktiskt test` och relevanta delar av `Prova själv` till en handbokssektion, till exempel `Praktisk användning: kartlägg ett nytt kort`.
- Ersätt `Kontrollera att du hänger med` med `Vanliga missförstånd` eller `Snabb kontroll innan du går vidare`.
- Bevara checklisteliknande innehåll, men tona ned testkänslan.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 3/5 |
| Läroboksspår | Hög |
| Behov av redaktionell åtgärd | Hög |
| Risk vid ändring | Medel |

## Kapitel 2 – Att välja rätt kort för rätt projekt

### Det fungerar väl

Detta är ett av blockets mest handboksmässiga kapitel. Det är direkt användbart som beslutsstöd och innehåller många relevanta valdimensioner: I/O, spänning, minne, kommunikation, analog mätning, strömförbrukning, formfaktor, bibliotek, community, kostnad och reproducerbarhet.

Kapitlet passar mycket väl med bokens referensidentitet. Rubriker som `När du bör välja ett enkelt kort`, `När du bör välja ESP8266 eller ESP32`, `När du bör välja RP2040/RP2350 eller Pico-liknande kort` och `Dokumentera kortvalet` är tydligt handboksorienterade.

### Problem

Kapitlet har många H2-rubriker, vilket gör det lätt att navigera men också ganska fragmenterat. Det fungerar troligen i EPUB som uppslagsstruktur, men i läsflöde kan det kännas hackigt.

`Praktiskt test: välj kort för tre projekt` är inte ett praktiskt test i fysisk mening utan ett beslutsövningsmoment. Det är inte fel, men rubriken `Praktiskt test` kan skapa fel förväntan. Här skulle `Användning: välj kort för tre projekttyper` eller `Beslutsövning: välj kort för tre projekt` vara mer exakt.

`Prova själv` överlappar med `Praktiskt test`. Även här är innehållet användbart, men sektionerna konkurrerar om samma roll.

`Kontrollera ditt val` är bättre än `Kontrollera att du hänger med`, eftersom det låter mer handboksnära. Men frågorna är fortfarande quizformulerade. De skulle kunna bli en praktisk checklista.

### Rekommendation för PLAN-H

- Behåll kapitel 2:s grundstruktur som modell för beslutsstödskapitel.
- Byt `Praktiskt test` till `Beslutsstöd i praktiken` eller `Exempel: välj kort för tre projekt`.
- Slå ihop `Prova själv` med beslutsstödet eller flytta det till en kortare `Använd på ditt projekt`.
- Gör `Kontrollera ditt val` till en checklista, inte en frågelista.
- Undvik att göra kapitlet längre; redigera genom konsolidering.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 3 – Utvecklingsmiljö, bibliotek och projektstruktur

### Det fungerar väl

Kapitlet är mycket praktiskt. Det ger läsaren konkret vägledning kring Arduino IDE, board manager, library manager, serial monitor, serial plotter, sketchstruktur, pinout-kommentarer, konfigurationsblock, README och minimal testsketch. Detta är typiskt handboksinnehåll.

Särskilt starkt är kapitlets betoning på reproducerbarhet: att dokumentera kort, bibliotek, koppling, förväntat resultat och felsökning.

### Problem

Kapitlet innehåller en lång praktisk sektion med kod och projektrutin. Det är i sig relevant, men rubriken `Praktiskt test: skapa ett återanvändbart experimentprojekt` placerar innehållet i en undervisningsram.

`Kontrollera att du hänger med` är tydligt läroboksspråk. Frågorna är bra, men formatet bör ändras.

Kapitlet har inget `Prova själv`, vilket gör det mindre överlastat än kapitel 1 och 4. Däremot skulle slutet kunna göras mer handboksnära genom att ersätta kontrollfrågorna med en praktisk checklista:

- Har projektet pinout-kommentar?
- Är board package dokumenterat?
- Är bibliotek dokumenterade?
- Finns minimal testsketch?
- Finns förväntat resultat?

Det är också värt att notera att kapitlet innehåller ett README-exempel i ett kodblock med H1/H2-markdown. Det är korrekt eftersom det ligger i kodblock, men exportkontrollen bör även fortsättningsvis skilja mellan rubriker i kodexempel och riktiga kapitelrubriker.

### Rekommendation för PLAN-H

- Byt `Praktiskt test` till `Exempel: återanvändbart experimentprojekt`.
- Ersätt `Kontrollera att du hänger med` med `Checklista för ett reproducerbart experiment`.
- Behåll kod och README-exempel.
- Bevara kapitlets praktiska karaktär; det behöver inte förkortas kraftigt.
- Säkerställ att exportvalidering inte feltolkar markdownrubriker i kodblock.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Kapitel 4 – Elektriska grunder för programmerare

### Det fungerar väl

Kapitlet är viktigt och innehållet är väl valt. Det täcker spänning, ström, resistans, effekt, gemensam jord, logiknivåer, nivåskiftning, pull-up/pull-down, open drain, kondensatorer, flyback-dioder, spänningsdelare, multimeter och säkerhetsgränser.

`Snabb orientering` är bättre än i kapitel 1 eftersom den säger:

> Målet är inte att göra dig till analogelektronikkonstruktör.

Det sänker kravnivån och ligger nära den formulering användaren efterfrågat: läsaren ska förstå, inte examineras.

### Problem

Kapitel 4 är ett tydligt teorikapitel, men det innehåller både:

- `Praktiskt test: LED, knapp och spänningsdelare`
- `Prova själv`
- `Kontrollera att du hänger med`

Det gör kapitlet tungt och lärobokslikt. Här är användarens observation särskilt relevant: teoriexperiment kan kännas fel i en handbok, särskilt om kapitlet egentligen ska ge begrepp och riskförståelse.

Samtidigt är vissa praktiska moment faktiskt nyttiga. LED med seriemotstånd, knapp med intern pull-up och spänningsdelare är klassiska första verifieringar. Problemet är inte att de finns, utan att de presenteras som fullständig lektionssekvens plus ytterligare övningar och quiz.

### Rekommendation för PLAN-H

- Behåll ett kortare praktiskt avsnitt som `Mät detta när något är fel`, snarare än ett fullskaligt `Praktiskt test`.
- Flytta eller kondensera delar av LED/knapp/spänningsdelare till checklistor eller praktiska exempel.
- Ta bort eller omvandla `Prova själv` till `Praktiska kontroller`.
- Ersätt `Kontrollera att du hänger med` med `Vanliga missförstånd`.
- Kapitel 4 bör få en tydligare begrepps-/säkerhetsmall, inte komponentkapitelmall.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 3/5 |
| Läroboksspår | Hög |
| Behov av redaktionell åtgärd | Hög |
| Risk vid ändring | Medel |

## Kapitel 5 – Digital I/O, knappar och logiska signaler

### Det fungerar väl

Kapitel 5 är mer praktiskt än kapitel 1–4 och fungerar bra som första grundfunktionskapitel. Det har tydlig koppling till verkliga problem: flytande ingångar, pull-up, aktiv LOW, debounce, open drain, digitala sensormoduler, interruptsignaler, långa kablar, störningar och pin-konflikter.

`Praktiskt test: robust knappmodul utan delay` är motiverat. Detta är inte ett teoriexperiment utan ett återanvändbart praktiskt mönster som kan användas i senare projekt.

Kapitlet har redan handboksnära avsnitt som `Det du kan använda kapitlet till`, `När digital I/O är rätt val`, `Vanliga misstag`, `Snabbreferens` och `Relaterat`.

### Problem

`Snabb orientering` är lång och saknar den tydliga listform som gör kapitel 2–4 snabbare att skanna. Den fungerar som introduktion, men som snabb orientering är den mer essälik.

`Kontrollera att du hänger med` bör omvandlas. Frågorna är relevanta, men rubriken och frågeformen ger kurskänsla.

Kapitlet har inget `Prova själv`, vilket är bra eftersom det undviker överlapp. `Praktiskt test` fyller här en rimlig funktion.

### Rekommendation för PLAN-H

- Behåll det praktiska testet, men överväg rubriken `Praktiskt mönster: robust knappmodul utan delay`.
- Omstrukturera `Snabb orientering` till kortare navigerbar form:
  - när kapitlet är relevant,
  - vad du kommer att förstå,
  - vad du bör kontrollera i praktiken.
- Ersätt `Kontrollera att du hänger med` med `Snabb kontroll i praktiken` eller `Vanliga missförstånd`.
- Låt kapitel 5 fungera som modell för när ett praktiskt moment faktiskt är motiverat.

### Bedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 4/5 |
| Läroboksspår | Medel |
| Behov av redaktionell åtgärd | Medel |
| Risk vid ändring | Låg |

## Återkommande mönster i kapitel 00–05

### 1. Innehållet är starkare än formen

De analyserade kapitlen innehåller mycket relevant och praktiskt material. Det som drar ned handbokskänslan är framför allt rubrikramarna runt materialet: `Efter kapitlet ska du`, `Praktiskt test`, `Prova själv` och `Kontrollera att du hänger med`.

### 2. `Snabb orientering` behöver tre olika mallar

Samma rubrik används i alla kapitel, men funktionen bör variera:

| Kapiteltyp | Rekommenderad funktion för `Snabb orientering` |
|---|---|
| Inledning | Behövs inte som återkommande kapitelrubrik. |
| Orientering | Förklara när kapitlet är relevant och vad det hjälper läsaren att förstå. |
| Beslutsstöd | Lista beslutsfrågor och valdimensioner. |
| Grundfunktion | Beskriv praktiska symptom, begrepp och mönster som kapitlet hjälper med. |

PLAN-H bör därför inte bara ersätta en fras globalt. Den bör ange kapiteltypsanpassade formuleringar.

### 3. `Praktiskt test` och `Prova själv` bör inte samexistera mekaniskt

I kapitel 1, 2 och 4 finns både `Praktiskt test` och `Prova själv`. Det skapar överlapp och kursbokskänsla. I kapitel 3 och 5 finns `Praktiskt test` utan `Prova själv`, vilket fungerar bättre.

PLAN-H bör införa en regel:

> Ett kapitel bör normalt ha högst en praktisk aktiveringssektion. Den ska heta olika beroende på kapiteltyp: `Exempel`, `Praktiskt mönster`, `Använd på ditt projekt`, `Checklista` eller `Mät detta först`.

### 4. Quiz bör ersättas med handboksformat

`Kontrollera att du hänger med` förekommer i kapitel 1, 3, 4 och 5. Kapitel 2 har den mildare varianten `Kontrollera ditt val`.

För en handbok bör dessa inte vara quiz. Frågorna kan ofta återanvändas, men bör omformas till:

- `Vanliga missförstånd`
- `Snabb kontroll i praktiken`
- `Checklista innan du går vidare`
- `Om det inte fungerar`
- `Beslutsfrågor`

### 5. Teorikapitel bör ha mindre experimentkänsla

Kapitel 4 visar tydligast att teorikapitel kan bli tunga om de får både experiment, övningar och quiz. I sådana kapitel bör praktiken vara mät- och felsökningsnära, inte kursövningsnära.

### 6. Kapitel 2 och 5 visar bra handboksspår

Kapitel 2 fungerar väl som beslutsstöd. Kapitel 5 fungerar väl som praktiskt grundfunktionskapitel. Dessa bör användas som positiva referenser i PLAN-H, men med justering av quiz- och testetiketter.

## Föreslagna generella regler för [PLAN-H]

### Regel H-01: Inga interna projektartefakter i boktext

Ta bort eller ersätt referenser till interna filer, exempelvis:

- `docs/lookup-index.md`
- `canon`
- `project-status`
- `build/book.md`
- redaktörsstöd
- projektets interna filstruktur

Läsaren ska hänvisas till bokdelar, kapitel och referenskapitel, inte till projektfiler.

### Regel H-02: Ersätt kravliknande lärandemål med användningsnytta

Formuleringar som `Efter kapitlet ska du kunna` bör ersättas med mjukare och mer handboksnära språk:

- `Kapitlet hjälper dig att förstå...`
- `Här får du en praktisk karta över...`
- `Du kommer att känna igen...`
- `Efter genomgången blir det lättare att...`
- `Använd kapitlet när du behöver avgöra...`

Det ska inte göras som global sök-och-ersätt, utan anpassas per kapiteltyp.

### Regel H-03: En praktisk aktiveringssektion per kapitel

Kapitel bör normalt inte ha både `Praktiskt test` och `Prova själv`. Välj en form:

| Kapiteltyp | Rekommenderad sektion |
|---|---|
| Orientering | `Använd detta i ditt projekt` eller ingen praktisk sektion |
| Beslutsstöd | `Beslutsstöd i praktiken` |
| Teori/begrepp | `Mät detta först` eller `Vanliga missförstånd` |
| Grundfunktion | `Praktiskt mönster` |
| Komponent/sensor | `Praktiskt test` eller `Koppla och testa` |
| Referens | Ingen övningssektion |

### Regel H-04: Quizfrågor ska omvandlas, inte nödvändigtvis raderas

Frågorna innehåller ofta bra innehåll. Problemet är formen. PLAN-H bör omvandla dem till checklistor, missförstånd, felsökningspunkter eller beslutsfrågor.

### Regel H-05: Orienteringskapitel ska inte kännas som laborationer

Kapitel 1–4 bör framför allt hjälpa läsaren orientera sig och undvika fel. Praktiska delar ska därför vara korta, situationsbaserade och handboksnära.

### Regel H-06: Bevara pedagogiken men ta bort skolramen

Bokens styrka är att den förklarar tydligt. PLAN-H ska inte göra texten torrare. Målet är att behålla förklaringen men minska signaler om kurs, prov, plikt och övningsbok.

## Prioriterade åtgärder som bör ingå i [PLAN-H]

| Prioritet | Åtgärd | Berörda kapitel i detta block |
|---|---|---|
| Kritisk | Ta bort intern referens till `docs/lookup-index.md` ur inledningen. | 00 |
| Kritisk | Ersätt `Efter kapitlet ska du framför allt kunna` i kapitel 1. | 01 |
| Rekommenderad | Omvandla `Kontrollera att du hänger med` till handboksformat. | 01, 03, 04, 05 |
| Rekommenderad | Omvandla `Kontrollera ditt val` till checklista. | 02 |
| Rekommenderad | Slå ihop eller omforma `Praktiskt test` och `Prova själv` där båda finns. | 01, 02, 04 |
| Rekommenderad | Byt rubriken `Praktiskt test` i orienteringskapitel till mer exakt rubrik. | 01, 02, 03, 04 |
| Valfri | Kortare och mer skannbar `Snabb orientering` i kapitel 5. | 05 |
| Valfri | Minska antalet H2-rubriker i kapitel 2 om läsflödet prioriteras över uppslagsbarhet. | 02 |

## Sammanfattande blockbedömning

| Mått | Bedömning |
|---|---|
| Handbokskänsla | 3,7/5 |
| Läroboksspår | Medel till hög |
| Behov av redaktionell åtgärd | Hög |
| Risk vid ändring | Låg till medel |

## Slutsats för steg 2

Kapitel 00–05 är en stark inledande del, men den behöver en redaktionell omramning för att fullt ut motsvara v4:s handboksidentitet. Innehållet bör i huvudsak bevaras. De viktigaste ändringarna inför PLAN-H är att ta bort intern projekttext, ersätta läroboksliknande formuleringar, minska quizkänslan och göra praktiska moment mer kapiteltypanpassade.

Detta block ger en tydlig första riktning för PLAN-H: nästa utvecklingsfas bör inte handla om mer innehåll, utan om att göra befintligt innehåll mer handboksmässigt.

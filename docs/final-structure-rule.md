# [PLAN] Slutlig strukturregel

Datum: 2026-06-30  
Plansteg: 6. Fastställ slutlig strukturregel  
Status: Fastställd som styrande redaktionell regel.

## Syfte

Detta dokument fastställer den slutliga strukturregel som ska styra fortsatt justering av *Arduino i praktiken*.

Regeln bygger på den redaktionella målbilden, kapiteltypologin, kapitelmallarna och utvärderingen av pilotkapitlen.

## Slutlig strukturregel

> *Arduino i praktiken* ska använda kapiteltypsanpassade rubriker. Formella lärandemål, quiz och kursliknande introduktionssektioner används bara där de tillför tydligt värde. Praktiska tester, felsökning, snabbval, snabbreferenser och korsreferenser prioriteras eftersom boken ska fungera både som lärobok och som praktisk handbok.

## Huvudprinciper

### 1. Kapiteltypen styr strukturen

Alla kapitel ska inte följa samma mall. Varje kapitel ska redigeras utifrån sin funktion:

- orientera,
- förklara grundfunktion,
- hjälpa läsaren välja kort eller plattform,
- visa hur en komponent eller sensor används,
- stärka robusthet och felsökning,
- vägleda från experiment till lösning,
- fungera som referens.

Kapitelmallarna i `docs/chapter-templates-by-type.md` är vägledande, inte mekaniska tvångsmallar.

### 2. Inledningen ska vara snabb och praktisk

Standardinledningen i kapitel ska vara `Snabb orientering`.

Den ska kort svara på:

- vad kapitlet hjälper läsaren med,
- när ämnet är relevant,
- vilken praktisk situation kapitlet löser.

Följande rubriker ska inte längre användas som standard:

- `Varför detta kapitel finns`
- `Lärandemål`
- `Innan vi börjar`

De får bara användas undantagsvis om kapitlet verkligen behöver dem.

### 3. Förutsättningar används sparsamt

Rubriken `Förutsättningar` får användas när kapitlet kräver något särskilt, till exempel:

- specifik hårdvara,
- tidigare begrepp,
- särskild bibliotekskunskap,
- risk för felkoppling eller skada.

Om förutsättningarna är självklara ska de bakas in i `Snabb orientering` eller utelämnas.

### 4. Praktiska tester ersätter skolövningar

Rubriken `Övningar` ska som huvudregel ersättas med någon av:

- `Praktiskt test`
- `Prova själv`
- `Bygg vidare`
- `Kontrollera ditt val`

Syftet är att behålla aktivt lärande utan att kapitlet känns som en kurslektion.

### 5. Quiz används bara i grundkapitel

`Quiz/reflektionsfrågor` ska tas bort i de flesta kapitel.

I grundkapitel kan ett kort avsnitt användas om det hjälper läsaren att kontrollera förståelse, men då med en mer praktisk rubrik, exempelvis:

- `Kontrollera att du hänger med`
- `Kontrollera din förståelse`

### 6. Korsreferenser används selektivt

`Se också` ska inte längre vara en obligatorisk avslutande sektion i varje kapitel.

Korsreferenser ska bara finnas där de hjälper läsaren att lösa ett konkret problem, förstå ett faktiskt beroende eller välja mellan närliggande tekniker. Om hänvisningen bara binder ihop kapitlet med nästa kapitel i ordningen ska den tas bort.

När en hänvisning behövs används i första hand någon av följande former:

- en kort hänvisning i löptexten,
- en liten `Relaterat`-sektion när flera ämnen verkligen hör ihop,
- samlad navigering i kapitel 38 och `docs/lookup-index.md`.

### 7. Snabb sammanfattning används selektivt

`Snabb sammanfattning` kan behållas i pedagogiska kapitel där den hjälper läsaren repetera.

I mer uppslagsverkslika kapitel ska den ofta ersättas av:

- `Snabbreferens`
- `Snabbval`
- `Checklista`
- `Felsökningsöversikt`

### 8. Handboksnyttan ska förstärkas

Vid fortsatt redigering ska följande sektioner prioriteras när de passar kapitlet:

- `Valguide`
- `När du använder detta`
- `När du bör välja något annat`
- `Vanliga misstag`
- `Felsökning`
- `Elektriska krav`
- `Kod och bibliotek`
- `Snabbreferens`
- `Säkerhetsruta`

### 9. Pedagogisk progression ska bevaras

Även om boken blir mer handboksnära ska den fortfarande fungera från början till slut.

Vid varje batchjustering ska redigeringen kontrollera att:

- begrepp inte används innan de förklarats,
- grundkapitlen fortfarande bär resten av boken,
- tekniska förklaringar inte blir för korta,
- praktiska kapitel kan läsas fristående,
- korsreferenser bara finns där de tillför konkret nytta.

### 10. Rubriknivåer och markdown ska följa projektstandarden

Alla kapitel ska fortsatt följa canonical markdown:

- exakt en H1-rubrik per kapitel,
- H2 för huvudsektioner,
- H3 för undersektioner,
- inga H4-rubriker,
- korrekta listor,
- korrekta tabeller,
- stängda kodblock,
- inga råa markdownmarkörer som riskerar synas i export.

## Godkänd riktning efter pilotutvärdering

Pilotutvärderingen visar att den nya strukturen fungerar bättre för bokens syfte.

Följande bedömning gäller för fortsatt arbete:

- Riktningen är godkänd.
- Pilotkapitlens struktur ska användas som stilreferens.
- Kapitelmallarna ska följas flexibelt.
- Resten av boken kan batchjusteras enligt plansteg 7.

## Nästa steg

Nästa redaktionella arbetssteg är:

**[PLAN] 7. Batchjustera resten av kapitlen**

Rekommenderad ordning:

1. Kapitel 1–4
2. Kapitel 5–9
3. Kapitel 10–16
4. Kapitel 17–22
5. Kapitel 23–29
6. Kapitel 30–34
7. Kapitel 35–38

Efter varje batch ska projekt-zippen uppdateras och ändrade filer listas.


## Normaliseringsstatus

`[PLAN]` steg 8 har genomförts. Kapitelmanuset har kontrollerats och kvarvarande äldre standardrubriker har ersatts eller omformulerats enligt strukturregeln.

Se `docs/section-normalization.md`.


## [PLAN2] Tillägg: Se också och korsreferenser

Från och med `[PLAN2]` granskas återkommande `Se också`-sektioner kapitelvis. Målet är att undvika mekaniska hänvisningar som upprepar nästa kapitels `Snabb orientering`.

Batch 1 i `[PLAN2]` har justerat inledningen och kapitel 1–4. I dessa kapitel togs de linjära `Se också`-avsnitten bort eftersom de främst beskrev nästa kapitel i ordningen. Inledningen fick i stället en mer uppslagsvänlig `Välj din väg`-sektion.

## [PLAN2] Justering av korsreferenser

Efter granskning enligt `[PLAN2]` ska `Se också` inte användas som obligatorisk slutsektion.

När korsreferenser behövs ska de vara korta, problemorienterade och helst använda rubriken `Relaterat`. En sådan sektion ska bara finnas när den hjälper läsaren att välja rätt teknik, felsöka, förstå ett verkligt beroende eller hitta en relevant fördjupning.

Korsreferenser som bara leder vidare till nästa kapitel tas bort.

## [PLAN2] Förtydligande om plattformskapitel

Efter granskning i `[PLAN2]` batch 3 ska plattformskapitel inte avslutas med mekaniska `Se också`-övergångar till nästa kortfamilj.

Valhjälp mellan kortfamiljer ska i första hand ligga i:

- `Snabbval` i respektive kapitel,
- kapitel 38,
- `docs/lookup-index.md`,
- punktvisa brödtextreferenser när ett faktiskt tekniskt beroende behöver förklaras.

## Tillägg efter [PLAN2] batch 4

`Se också` ska inte användas som mekanisk slutsektion i komponent- och aktuator-kapitlen. När hänvisningar behövs ska de formuleras som `Relaterat` och fokusera på praktisk nytta: PWM, strömförsörjning, drivning, säkerhet, felsökning eller tydliga alternativ.

## [PLAN2] Tillägg: korsreferenser

`Se också` ska inte användas som obligatorisk avslutande sektion. Hänvisningar ska bara finnas där de hjälper läsaren med ett konkret problem, ett faktiskt beroende, ett val mellan tekniker eller en tydlig felsökningssituation.

När en korsreferens behövs används i första hand:

- en kort hänvisning i löptexten,
- en selektiv `Relaterat`-sektion,
- samlad navigering i kapitel 38 och `docs/lookup-index.md`.

Batch 1–7 i `[PLAN2]` är genomförda för inledningen och kapitel 1–38.

## [PLAN2] Tillägg efter batch 6

För robusthets- och kretskapitel ska korsreferenser bara finnas när de hjälper läsaren att hantera ett konkret beroende: kommunikationsbussar, drivning, strömförsörjning, signalanpassning, jordning, störningar eller systematisk felsökning. Linjära `Se också`-övergångar mellan kapitel ska tas bort.


## [PLAN2] Tillägg efter batch 7

Metod-, projekt- och referenskapitel ska inte avslutas med linjära `Se också`-övergångar. Kapitel 35–36 ska fungera som fristående arbetskapitel, kapitel 37 kan ha selektiv `Relaterat` för konkreta projektberoenden, och kapitel 38 ska bära den breda navigeringen genom snabbindex, snabbvalsguider och tabeller.

## [PLAN3] Regel för `Förutsättningar`

`Förutsättningar` är inte en obligatorisk kapitelrubrik.

Rubriken används bara när den hjälper läsaren att förstå vilka tidigare begrepp, praktiska verktyg, säkerhetsgränser eller elektriska samband som kapitlet faktiskt bygger på.

I kapitel som främst fungerar som valguider, särskilt kort- och plattformskapitel, används hellre en mer handboksnära rubrik som `Bedöm kortet med detta i åtanke`.

## [PLAN3] Tillägg: `Det du kan använda kapitlet till`

Rubriken `Det du kan använda kapitlet till` ska inte användas som obligatorisk ersättning för formella lärandemål.

Den får vara kvar när den ger snabb praktisk orientering i grund-, komponent-, sensor- eller robusthetskapitel. Den bör tas bort när `Snabb orientering`, `Snabbval`, `Valguide`, `Arbetssättet` eller kapiteltypen redan gör samma arbete.


## [PLAN3] Regel för Snabb sammanfattning och Snabbreferens

Efter `[PLAN3]` steg 3 gäller följande:

- `Snabb sammanfattning` används när kapitlet främst är förklarande eller undervisande.
- `Snabbreferens` används när kapitlet främst ska fungera som uppslag.
- Ett kapitel ska normalt inte ha både `Snabb sammanfattning` och `Snabbreferens` om de överlappar.
- Om båda behövs måste de ha tydligt olika funktion.


## [PLAN3] Förtydligande: `Relaterat`

Efter `[PLAN3]` steg 4 gäller följande regel:

`Relaterat` ska inte vara en mekanisk slutsektion. Den får användas när hänvisningen hjälper läsaren att lösa ett konkret problem, förstå ett tekniskt beroende, göra ett bättre val eller felsöka en praktisk situation.

Generiska listor över närliggande eller efterföljande kapitel ska undvikas. Den breda navigeringen ska i stället bäras av inledningen, kapitel 38 och `docs/lookup-index.md`.


## [PLAN3] Tillägg: Navigeringsansvar inför v2

Datum: 2026-07-01

Bokens navigering ska inte spridas ut som mekaniska avslut i varje kapitel. Den ska bäras av tre nivåer:

- Inledningen förklarar hur boken kan läsas.
- Kapitel 38 fungerar som läsarens praktiska snabbguide.
- `docs/lookup-index.md` fungerar som redaktionellt uppslagsindex för framtida uppdateringar.

Kapitlen får fortfarande använda `Relaterat`, men bara när hänvisningen hjälper läsaren att lösa ett konkret problem, förstå ett tekniskt beroende eller välja mellan alternativ.

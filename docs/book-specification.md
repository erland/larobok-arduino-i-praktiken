# Bokspecifikation

## Titel

Arbetstitel: Arduino i praktiken

## Undertitel

Din guide till Arduino och elektronikkretsar

## Författare

Erland Lindmark

## Projektversion

handbokstruktur-v5. Skapad 2026-07-01 som slutversion efter `[PLAN-H]` redaktionell handbokskonsolidering.

Denna version bygger vidare på `handbokstruktur-v4` och inkluderar hela `[PLAN-H]`-rundan: rensning av interna projektspår i läsartext, mjukare handboksformuleringar i stället för kravliknande lärandemål, omvandling av quiz- och kontrollfrågor till checklistor och praktiska kontroller, omklassificering av praktiska moment, kapiteltypsspecifik rubriknormalisering, förstärkt beslutsstöd, riskkontroller, vanliga misstag, korsreferenser och en mer verktygsorienterad avslutande referensdel.

Se `docs/project-version-handbokstruktur-v5.md`.

## PLAN-H-konsolidering

`[PLAN-H]` är genomförd och gör boken mer konsekvent som praktisk handbok och referens utan att ändra kapitelordningen eller lägga till nya komponentgrupper. Kompletteringen omfattar främst språk, rubriker, läsarvägledning, checklistor, beslutsstöd, riskkontroller och referensstruktur.

Bokens tekniska bredd från `handbokstruktur-v4` är bevarad, men presentationen är mer handboksnära och mindre kurs- eller lärobokslik.


## PLAN5-komplettering

`[PLAN5]` är genomförd och kompletterar boken med vanliga kretsar, moduler och induktiva laster utan att ändra kapitelstrukturen. Kompletteringen omfattar LM393 och digital tröskelmodul/digitala tröskelmoduler, DRV8833, L9110S, I2C logic level converter, LM386, KY-037, APDS-9960/GY-9960, PCF8575, analog Hall-sensor och 49E-typ samt elektromagneter, solenoider och annan induktiv last/andra induktiva laster.

Dessa tillägg behandlas som praktiska förstärkningar av befintliga kapitel och som uppslagsbara komponenttyper i kapitel 38, inte som nya huvudkapitel.


## Språk

Svenska. Källkod får använda engelska identifierare, kommentarer och etablerade engelska begrepp när det är naturligt.

## Ämne

Boken fungerar som praktisk handbok och referens för användning av Arduino-kompatibla kort, sensorer, utenheter, aktuatorer, vanliga IC-kretsar och elektroniska moduler.

## Syfte

Boken ska hjälpa läsaren att välja lämpligt Arduino-kompatibelt kort, förstå centrala skillnader mellan kortfamiljer, koppla in och använda vanliga sensorer och kretsar, genomföra praktiska experiment och felsöka systematiskt.

## Målgrupp

Erfarna programmerare med viss Arduino-vana och viss praktisk erfarenhet av sensorer eller elektroniska moduler. Boken ska fungera som praktisk handbok, referens och lärobok och inspirerande referens.

## Förkunskaper

Läsaren antas kunna programmera, förstå grundläggande kodstruktur och ha provat enklare Arduino-sketcher. Grundläggande elektronik repeteras praktiskt, men boken är inte en komplett elektronikgrundkurs.

## Svårighetsgrad

Erfaren.

## Boktyp

Stor praktisk lärobok, handbok och referens.

## Redaktionell målbild

Boken ska redigeras som en praktisk Arduino-handbok med lärobokskvalitet. Den ska kunna läsas från början till slut, men också fungera som uppslagsverk för läsare som vill förstå ett visst kort, en viss komponent, sensor, modul, krets eller felsökningssituation.

Den redaktionella riktningen prioriterar praktisk orientering, valhjälp, felsökning, snabbreferenser och korsreferenser framför formella kursmarkörer i varje kapitel. Se `docs/editorial-target.md` för fastställd målbild.


## Kapiteltypologi

Boken använder från och med [PLAN] steg 2 en redaktionell kapiteltypologi. Kapitel ska inte längre behandlas som om de hade samma funktion, utan delas in i orienteringskapitel, grundfunktionskapitel, kort- och plattformskapitel, komponent-/aktuator-kapitel, sensor-/mätkapitel, robusthets-/kretskapitel, metod-/projektkapitel och referenskapitel.

Typologin styr kommande strukturjusteringar och finns dokumenterad i `docs/chapter-typology.md`.


## Kapitelmallar per kapiteltyp

Boken använder från och med [PLAN] steg 3 kapiteltypsanpassade mallar. Mallarna styr hur kommande kapiteljusteringar ska göras och ersätter den tidigare principen att alla kapitel följer samma traditionella läroboksstruktur.

Grundregeln är att formella kursrubriker som `Varför detta kapitel finns`, `Lärandemål`, `Innan vi börjar`, `Quiz/reflektionsfrågor` och `Nästa steg` inte längre ska vara standard i varje kapitel. De ersätts i stället av mer praktiska rubriker som passar kapiteltypen, exempelvis `Snabb orientering`, `När du använder detta`, `Valguide`, `Felsökning`, `Praktiskt test`, `Snabbreferens` och `Se också`.

Mallarna finns dokumenterade i `docs/chapter-templates-by-type.md`.


## Slutlig strukturregel

Från och med `[PLAN]` steg 6 gäller `docs/final-structure-rule.md` som styrande redaktionell regel för fortsatt justering.

Boken ska använda kapiteltypsanpassade rubriker. Formella lärandemål, quiz och kursliknande introduktionssektioner används bara där de tillför tydligt värde. Praktiska tester, felsökning, snabbval, snabbreferenser och korsreferenser prioriteras eftersom boken ska fungera både som lärobok och praktisk handbok.



## Normalisering av återkommande sektioner

Från och med `[PLAN]` steg 8 är de återkommande kapitelrubrikerna normaliserade mot den fastställda handboksstrukturen.

Gamla standardrubriker som `Varför detta kapitel finns`, `Lärandemål`, `Innan vi börjar`, `Övningar`, `Quiz/reflektionsfrågor`, `Praktiskt experiment`, `Referenssammanfattning` och `Nästa steg` ska inte längre användas som standardrubriker i kapitelmanus. I stället används praktiska, kapiteltypsanpassade rubriker som `Snabb orientering`, `Det du kan använda kapitlet till`, `Förutsättningar`, `Praktiskt test`, `Prova vidare`, `Kontrollera ditt val`, `Snabbreferens`, `Snabbval` och `Se också`.

Normaliseringen finns dokumenterad i `docs/section-normalization.md`.


## Genomförd batchjustering 3

Kapitel 10–16 har harmoniserats enligt den slutliga strukturregeln för kort- och plattformskapitel. Kapitlen använder nu mer valguideorienterade rubriker, med `Snabb orientering`, `Det du kan använda kapitlet till`, `Förutsättningar`, `Praktiskt test`, `Prova vidare`, `Kontrollera ditt val`, `Snabbreferens`, `Snabbval` och `Se också` där det passar.

Batchen finns dokumenterad i `docs/batch-adjustment-03-plattformskapitel.md`.

## Pedagogisk stil

Praktisk, modulär och referensvänlig. Varje teknikområde bör snabbt orientera läsaren, visa när lösningen passar, när något annat passar bättre, vilka elektriska eller praktiska begränsningar som gäller, vilka fel som är vanliga och hur problemet felsöks. Formella lärandemål och quiz ska bara användas där de tillför tydligt värde.

## Genomförd batchjustering 1

Kapitel 1–4 har harmoniserats enligt den slutliga strukturregeln. Orienteringskapitlen använder nu handboksnära inledningar och avslutningar, med `Snabb orientering`, korta `Förutsättningar` där de behövs, praktiska tester och `Se också` i stället för generella kursmarkörer.

Se `docs/batch-adjustment-01-orienteringskapitel.md`.

## Omfattning

Stor, modulär bok med cirka 38 kapitel plus inledning.

## Avgränsningar

Boken fokuserar på Arduino-kompatibel programmering och praktisk elektronikanvändning. Den ska inte bli en fullständig elektroniklärobok, en djup C++-bok eller en heltäckande manual för varje tillverkares alla kort.

## Återkommande exempel eller projekt

Ett återkommande slutprojekt är en modulär sensor- och styrstation. Mindre experiment används löpande för varje kort-, sensor-, aktuator- och IC-kategori.

## Ton och stil

Vänlig, erfaren, praktisk, konkret och inspirerande. Läsaren tilltalas som tekniskt kunnig men inte nödvändigtvis elektronikexpert.

## Omslag

Projektet ska innehålla en omslagsprompt. Omslagsbilden är ännu inte genererad.

## Inre illustrationer

Inre illustrationer är inte aktiverade i denna version. Kopplingsbeskrivningar, tabeller och kodexempel kan användas i texten.


## Pilotjustering enligt [PLAN]

Som första manusprov har kapitel 2, 8, 13, 20 och 38 justerats enligt de nya kapiteltypsmallarna. Syftet är att testa en mer handboksnära struktur innan hela boken batchjusteras.

Se `docs/pilot-adjustment-log.md` för genomförda ändringar och utvärderingsfrågor.


## Batchjustering 2: grundfunktionskapitel

Kapitel 5–9 har justerats enligt den fastställda strukturregeln. Grundfunktionskapitlen ska fortfarande ge tydliga förklaringar eftersom de bär upp resten av boken, men de ska presenteras som praktiska verktygskapitel snarare än kurslektioner. Rubriker som `Snabb orientering`, `Förutsättningar`, `Praktiskt test`, `Prova själv`, `Snabbreferens` och `Se också` prioriteras framför generella kursmarkörer.



## Batchjustering 4

[PLAN] steg 7, batch 4 har genomförts för komponent- och aktuator-kapitlen 17–22. Kapitlen har harmoniserats mot en praktisk handboksstruktur där `Praktiskt test`, `Snabbval`, `Snabbreferens`, `Kontrollera ditt val` och `Se också` ersätter mer kurslika avslut.

Se `docs/batch-adjustment-04-komponent-aktuatorer.md`.


## Batchjustering 5

[PLAN] steg 7, batch 5 har genomförts för sensor- och mätkapitlen 23–29. Kapitlen har harmoniserats mot en praktisk uppslags- och handboksstruktur där läsaren snabbt kan hitta sensortyp, kopplingsidé, kodmönster, mätbegränsningar, felsökning och snabbval.

Se `docs/batch-adjustment-05-sensor-matkapitel.md`.


## [PLAN] Batchjustering 6

Batchjustering 6 är genomförd för kapitel 30–34, det vill säga robusthets- och kretskapitlen. Kapitlen har justerats mot en mer praktisk handboksstruktur med tydligare snabb orientering, praktiska test, felsökning, snabbreferenser, snabbval och `Se också`.

Se `docs/batch-adjustment-06-robusthets-kretskapitel.md`.



## Genomförd batchjustering 7

Metod-, projekt- och referenskapitlen 35–38 har batchjusterats enligt [PLAN] steg 7. Kapitlen använder nu en mer praktisk struktur med fokus på arbetssätt, checklistor, projektintegration, referensanvändning och korsreferenser.

Se `docs/batch-adjustment-07-metod-projekt-referens.md`.

## Uppslagsverksfunktion

Från och med `[PLAN]` steg 9 ska boken aktivt stödja uppslagsläsning. Det innebär att läsaren ska kunna gå från en praktisk fråga till rätt kapitel via snabbindex, snabbval, snabbreferenser, felsökning, säkerhetsrutor och korsreferenser.

Se `docs/reference-function-strengthening.md` och `docs/lookup-index.md`.



## Progressionskontroll

Från och med `[PLAN]` steg 10 är bokens progression kontrollerad efter batchjusteringarna. Kapitelordningen bedöms fungera både för linjär läsning och uppslagsläsning.

Kontrollen visar att:
- kapitel 1–4 bygger gemensam orientering och elektrisk grund,
- kapitel 5–9 introducerar grundfunktioner före komponent- och sensorkapitel,
- kapitel 10–16 ger kort- och plattformsval innan läsaren väljer praktiska moduler,
- kapitel 17–34 fungerar som uppslagsblock för komponenter, sensorer, kretsar och robust konstruktion,
- kapitel 35–38 binder ihop felsökning, modularisering, projektarbete och snabbvalsguider.

Se `docs/progression-review.md` och `docs/progression-check.md`.


## Markdown- och exportbarhetsstatus

Från och med `[PLAN]` steg 11 är projektets markdown- och exportbarhetskontroll godkänd. Kapitelordningen i metadata stämmer, kapitelmanus saknar H4-rubriker, kodblocken är balanserade, bildreferenserna är giltiga och de gamla kursrubrikerna förekommer inte längre som aktiva H2/H3-rubriker i kapitelmanus.

Se `docs/exportability-check.md`.


## [PLAN2] Korsreferenser och Se också

`Se också` ska inte längre användas som mekanisk standardsektion i varje kapitel. Varje förekomst ska bedömas kapitelvis mot bokens uppslagsverksfunktion.

I batch 1 enligt `[PLAN2]` har inledningen och kapitel 1–4 justerats. Linjära avslutningar som främst beskrev nästa kapitel har tagits bort. Boken ska i stället låta kapitel 38 och `docs/lookup-index.md` bära bred navigering, medan enskilda kapitel bara får korsreferenser när de hjälper ett konkret val, beroende eller felsökningsproblem.
## [PLAN2] Korsreferensprincip

`Se också` används inte som standardiserad avslutningssektion. I grundfunktionskapitel kan `Relaterat` användas när hänvisningarna är tekniskt motiverade, till exempel för PWM, ADC, avbrott, kommunikationsbussar, felsökning eller senare praktisk användning.

## [PLAN2] Korsreferensgranskning

`[PLAN2]` används för att granska återkommande `Se också`-sektioner kapitelvis. Syftet är att ta bort mekaniska övergångar mellan kapitel och bara behålla korsreferenser när de ger konkret uppslagsnytta.

Status:
- Batch 1: inledning och kapitel 1–4 genomförd.
- Batch 2: kapitel 5–9 genomförd.
- Batch 3: kapitel 10–16 genomförd. `Se också` togs bort ur plattformskapitlen eftersom `Snabbval`, kapitel 38 och `docs/lookup-index.md` ger bättre uppslagsnavigering.

## [PLAN2] Korsreferenser efter batch 4

Kapitel 17–22 har granskats enligt `[PLAN2]`. Mekaniska `Se också`-avsnitt har tagits bort. Praktiskt motiverade hänvisningar finns kvar som `Relaterat`, framför allt där de hjälper läsaren med PWM, strömförsörjning, drivning, säkerhet eller felsökning.

## [PLAN2] Korsreferenser efter batch 6

Kapitel 30–34 har granskats enligt `[PLAN2]`. Linjära `Se också`-avsnitt har tagits bort. Praktiskt motiverade hänvisningar finns kvar som `Relaterat`, framför allt där de hjälper läsaren med kommunikationsbussar, drivning, strömförsörjning, signalanpassning, jordning, störningar eller felsökning.

Status:
- Batch 6: kapitel 30–34 genomförd.


## [PLAN2] Korsreferenser efter batch 7

Kapitel 35–38 har granskats enligt `[PLAN2]`. Linjära `Se också`-avsnitt har tagits bort. Kapitel 35 och 36 avslutas nu med praktisk kontroll/checklista utan att leda vidare. Kapitel 37 har en selektiv `Relaterat`-sektion som stödjer arbetsflödet i slutprojektet. Kapitel 38 avslutas som referenskapitel utan projektadministrativ nästa-steg-text.

Status:
- Batch 7: kapitel 35–38 genomförd.

## [PLAN3] Finputsning inför v2

### Steg 1: Förutsättningar

`Förutsättningar` har granskats som återkommande kapitelrubrik. Sektionen är borttagen i tidiga orienteringskapitel där den främst upprepade `Snabb orientering`, omformulerad i kort- och plattformskapitel och behållen där den ger tekniskt eller praktiskt stöd.

Resultatet stärker bokens handboksidentitet och minskar känslan av mekanisk kursstruktur.

## [PLAN3] Steg 2: Praktisk nytta utan lärandemålskänsla

Sektionen `Det du kan använda kapitlet till` är inte längre standard i alla kapitel. Den används bara där den ger praktisk nytta och hjälper läsaren avgöra varför kapitlet är relevant.

Plattforms- och metodkapitel förlitar sig i stället på `Snabb orientering`, valguider, arbetssätt, checklistor och snabbreferenser.


## [PLAN3] Finputsning av avslut

I `[PLAN3]` steg 3 har överlapp mellan `Snabb sammanfattning` och `Snabbreferens` granskats. Kapitel ska inte avslutas med båda rubrikerna om de fyller samma funktion. Uppslagsnära kapitel prioriterar `Snabbreferens`; mer förklarande kapitel kan behålla `Snabb sammanfattning`.


## [PLAN3] Finputsning av `Relaterat`

I `[PLAN3]` steg 4 har kvarvarande `Relaterat`-sektioner granskats och skrivits om så att de inte fungerar som mekaniska övergångar mellan kapitel.

Korsreferenser ska nu vara problemorienterade: de ska hjälpa läsaren att lösa ett konkret tekniskt problem, välja rätt fördjupning eller felsöka ett samband mellan kapitel. Bred navigering hör främst hemma i inledningen, kapitel 38 och `docs/lookup-index.md`.

Se `docs/plan3-step-04-relaterat.md`.


## [PLAN3] Navigeringsmodell inför v2

Inledning, kapitel 38 och `docs/lookup-index.md` har granskats tillsammans enligt `[PLAN3]` steg 5.

Fastställd ansvarsfördelning:

- Inledningen beskriver bokens läslägen och när läsaren bör börja i kapitel 38.
- Kapitel 38 är den primära snabbguiden för läsaren i den färdiga boken.
- `docs/lookup-index.md` är ett tematiskt redaktörsindex för kvalitetskontroll och framtida uppdateringar.

Detta minskar upprepning och gör att kapitel 38 kan bära den breda uppslagsverksnavigeringen.


## [PLAN3] Exportstatus inför v2

`[PLAN3]` steg 6 är genomfört 2026-07-01. Markdown- och exportkontrollen är godkänd:

- `scripts/export-book.py validate` kördes utan varningar,
- `build/book.md` är ombyggd,
- EPUB är skapad,
- PDF är skapad,
- EPUB-navigationen är kontrollerad,
- PDF-rendering har stickprovskontrollerats.

Projektet kan versionssättas som `handbokstruktur-v2` i nästa steg.


## [PLAN3] finputsning inför v2

`[PLAN3]` är genomförd. Boken har finputsats för att minska kvarvarande mallkänsla, tydliggöra navigeringsansvaret mellan inledning, kapitel 38 och `docs/lookup-index.md`, samt säkerställa markdown- och exportbarhet inför `handbokstruktur-v2`.


## PLAN4 steg 7: samlad snabbguide

Kapitel 38 har uppdaterats så att tilläggen från PLAN4 steg 1–6 går att hitta i bokens samlade snabbguide. Snabbguiden omfattar nu även vanliga inmatningsmoduler, kit-sensorer, resistiva sensorer, vågceller/HX711, kommunikationsmoduler och vanliga motor-/drivmoduler.


## [PLAN4] genomförd

`[PLAN4]` är genomförd och projektet är versionssatt som `handbokstruktur-v3`.

Boken har kompletterats med vanliga elektronikbutiksmoduler och Arduino-kit-komponenter inom användargränssnitt, miljösensorer, analog mätning, kommunikation, motorstyrning och IR-inmatning. Kapitel 38, `lookup-index` och `canon-terminology` har uppdaterats så att komponenterna är sökbara och konsekvent beskrivna.

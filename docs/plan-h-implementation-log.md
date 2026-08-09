# [PLAN-H] genomförandelogg

## Steg H1 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-01-internal-project-traces.md`

Sammanfattning:
- Interna projektspår har rensats från läsartexten i kapitel.
- Referensen till `docs/lookup-index.md` i inledningen har ersatts med en läsarvänlig hänvisning till sakregister och snabbguider.
- `PLAN5` i kapitel 38 har ersatts med neutral handboksformulering.
- Hänvisning till projektets `canon` i kapitel 28 har ersatts med läsarvänlig dokumentationsrekommendation.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontrollsökning visar inga kvarvarande interna projektspår av typen `docs/`, `build/`, `canon`, `project-status`, `PLAN5` eller `[PLAN...]` i `chapters/`.


## Steg H2 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-02-learning-goal-language.md`

Sammanfattning:
- Kravliknande formuleringar som `Efter kapitlet ska du kunna` har ersatts med mer handboksnära formuleringar.
- Ersättningarna har varierats mellan kapitel för att undvika mekanisk upprepning.
- Punktlistornas tekniska innehåll har behållits.
- Även närliggande formuleringar som `ska du kunna säga`, `bör du kunna svara på` och `bör du kunna gå en nivå djupare` har mjukats upp.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontrollsökning visar inga kvarvarande förekomster av `Efter kapitlet ska`, `Efter kapitlet bör`, `ska du kunna`, `ska läsaren kunna` eller `bör du kunna` i `chapters/`.

## Steg H3 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-03-quiz-and-control-sections.md`

Sammanfattning:
- Rubrikerna `Kontrollera att du hänger med`, `Kontrollera ditt val` och `Kontrollera arbetssättet` har ersatts med handboksnära rubriker.
- Begreppsavslut har blivit `Snabb kontroll i praktiken`, `Viktiga samband att känna igen` eller `Arbetskontroll`.
- Val- och komponentavslut har blivit `Valchecklista`, `Riskkontroll`, `Arbetschecklista` eller `Användningschecklista` beroende på kapiteltyp.
- Numrerade frågelistor i dessa sektioner har gjorts om till punktlistor med läsarvänlig användningsrad.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontrollsökning visar att de gamla kontrollrubrikerna inte längre finns kvar i `chapters/`.

## Steg H4 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-04-practical-section-reclassification.md`

Sammanfattning:
- `Praktiskt test`, `Prova själv` och `Prova vidare` har omklassificerats till mer handboksnära rubriker.
- Ersättningarna har valts utifrån kapiteltyp: referensmönster, verifiering, riskkontroll, porteringstest, kortprofil, felsökningsmönster, vanliga varianter eller arbetsmall.
- Undersektioner med `### Test N:` har ersatts med `### Kontroll N:`.
- Tekniska fakta, kopplingar och komponentbeskrivningar har inte ändrats i sak.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontrollsökning visar inga kvarvarande förekomster av `## Praktiskt test`, `## Prova själv`, `## Prova vidare` eller `### Test ` i `chapters/`.

## Steg H5 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-05-heading-normalization-by-chapter-type.md`

Sammanfattning:
- Kapitelrubriken `Snabb orientering` har ersatts med kapiteltypsspecifika rubriker i alla berörda kapitel.
- Rubrikerna har valts utifrån kapiteltyp: orienteringskapitel, grundfunktionskapitel, kort-/plattformskapitel, komponent-/sensorkapitel, robusthetskapitel, metodkapitel och referenskapitel.
- Kvarvarande `Praktiskt arbetspass` i metodkapitlen har ersatts med `Arbetsmönster`.
- `docs/chapter-templates-by-type.md` har skapats som intern redaktionell stilreferens för framtida kapiteländringar.
- Tekniskt sakmaterial har inte ändrats.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontrollsökning visar inga kvarvarande förekomster av `## Snabb orientering` eller `## Praktiskt arbetspass` i `chapters/`.
## Steg H6 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-06-decision-support-and-quick-choice.md`

Sammanfattning:
- Befintliga valtabeller och snabbvalsdelar har förstärkts med korta beslutsrader.
- Beslutsstödet har lagts nära relevanta avsnitt i kapitel om motorer, laster, displayer, sensorer, mätning, I/O-expansion, drivkretsar, strömförsörjning, felsökning och slutreferensen.
- Inga nya komponentkategorier har lagts till.
- Tekniskt sakmaterial har inte ändrats i grunden.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontroll visar att inga H4-rubriker införts.
## Steg H7 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-07-risk-controls-and-common-mistakes.md`

Sammanfattning:
- Riskkontroller har förstärkts i kapitel om elektriska grunder, motorer, laster, mätning, drivkretsar, analog signalanpassning, strömförsörjning och felsökning.
- Nya eller tydligare riskavsnitt har lagts till där läsaren arbetar med ström, last, drivning, mätning eller längre drift.
- Fokus ligger på handlingsbara checklistor, inte på quiz eller kursfrågor.
- Inga nya komponenter eller tekniska huvudspår har lagts till.
- `build/book.md` har byggts om efter kapiteländringarna.
- Kontroll visar att inga H4-rubriker eller interna projektspår införts.

## Steg H8 – Slutblocket som verktygsdel

Status: Genomfört 2026-07-01

Ändrade filer:

- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`
- `chapters/referens-snabbvalsguider-38.md`
- `build/book.md`
- `docs/PLAN-H-step-08-end-block-tools.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

Sammanfattning: Slutblocket har gjorts mer verktygsorienterat. Kapitel 36 har fått tydligare modulchecklista, kapitel 37 tydligare projektmall och integrationsordning, och kapitel 38 renare referensmallar utan övningskänsla.

## Steg H9 – Läsarvänliga korsreferenser

Status: Genomfört 2026-07-01

Ändrade filer:

- 28 kapitel i `chapters/`
- `build/book.md`
- `docs/PLAN-H-step-09-reader-friendly-cross-references.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

Sammanfattning: Korsreferenserna har gjorts mer läsarvänliga och problembaserade. Flera befintliga `Relaterat`-avsnitt har kortats, förtydligats och knutits till konkreta problem som bussfel, nivåskiftning, strömproblem, drivning, mätbrus och systemintegration. Kapitel som saknade naturlig väg vidare har fått korta relaterat-avsnitt. Inga interna projektspår eller gamla kursrubriker har återinförts.

## Steg H10 – Intern redaktionell stilguide

Status: Genomfört 2026-07-01

Ändrade filer:

- `docs/handbook-editorial-style-guide.md`
- `docs/chapter-templates-by-type.md`
- `docs/PLAN-H-step-10-editorial-style-guide.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

Sammanfattning: En intern redaktionell stilguide har skapats för framtida ändringar. Den dokumenterar handbokston, fraser att undvika, ersättningsmönster, kapiteltyper, praktiska moment, beslutsstöd, riskkontroller, korsreferenser och kontrollpunkter inför ny projektversion. Inga kapiteltexter har ändrats.
## Steg H11 – Markdownbygge och kontroll

Status: Genomfört 2026-07-01

Ändrade filer:

- `chapters/00-inledning.md`
- `build/book.md`
- `docs/PLAN-H-step-11-markdown-build-check.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

Sammanfattning: `build/book.md` har byggts om från kapitelordningen i metadata. Projektets lokala markdownvalidering gav inga varningar. Kapiteltexterna har kontrollerats för H4-rubriker, obalanserade kodblock, interna projektspår och gamla kurs-/mallrubriker. En kvarvarande formulering i inledningen som nämnde den tidigare rubriken `Snabb orientering` har ersatts med en mer generell läsarformulering.


## Steg H12 – genomförd

Datum: 2026-07-01  
Resultatfil: `docs/PLAN-H-step-12-export-and-version.md`

Sammanfattning:
- Versionen har uppdaterats från `handbokstruktur-v4` till `handbokstruktur-v5`.
- `README.md`, `book.yaml`, `docs/export-metadata.yaml`, `docs/book-specification.md` och `docs/project-status.md` har uppdaterats.
- Ny versionsfil har skapats: `docs/project-version-handbokstruktur-v5.md`.
- Markdownvalidering har körts utan projektvarningar.
- `build/book.md` har byggts om.
- EPUB och PDF har skapats i `exports/`.
- Slutversionen är `arduino-i-praktiken-projekt-handbokstruktur-v5.zip`.

## Post-v5 justering – Kapitel 1

Status: Genomfört 2026-07-01

Ändrade filer:

- `chapters/ekosystem-01.md`
- `build/book.md`
- `docs/post-v5-chapter-01-adjustment.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

Sammanfattning: Kapitel 1 har gjorts mer koncentrerat genom att ta bort sektionerna `Kartläggning: två kort och en modul`, `Egen kontroll i praktiken` och `Viktiga samband att känna igen`. Ändringen är redaktionell och påverkar inte tekniska fakta eller komponentbeskrivningar.


## Post-v5 justering – Kapitel 2

Status: Genomfört 2026-07-01

Ändrade filer:

- `chapters/valja-ratt-kort-02.md`
- `build/book.md`
- `docs/post-v5-chapter-02-adjustment.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

Sammanfattning: Kapitel 2 har gjorts mer koncentrerat genom att ta bort sektionerna `Beslutsmönster: välj kort för tre projekt`, `Kortvalschecklista i praktiken` och `Valchecklista`. Ändringen är redaktionell och påverkar inte tekniska fakta eller kortrekommendationer.

## Post-v5-justering: kapitel 3

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-02-justering.zip`.
- Justerade `chapters/utvecklingsmiljo-bibliotek-03.md`.
- Bytte `Kodstil för bokens experiment` till `Kodstil`.
- Tog bort första meningen i `Konfigurationsblock för flera kort`.
- Tog bort `Arbetskontroll`.
- Byggde om `build/book.md`.

## Post-v5-justering: kapitel 4

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-03-justering.zip`.
- Justerade `chapters/elektriska-grunder-04.md`.
- Tog bort `Riskkontroll i praktiken`.
- Tog bort `Viktiga samband att känna igen`.
- Flyttade `Begreppsförklaring: logiknivå och gemensam jord` före `Snabb sammanfattning`.
- Byggde om `build/book.md`.

## Post-v5-justering: kapitel 5

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-04-justering.zip`.
- Justerade `chapters/digital-io-05.md`.
- Vävde in `Det du kan använda kapitlet till` i `Grundfunktion i praktiken`.
- Justerade formuleringen om avslutande experiment till `referensmönster`.
- Tog bort `Snabb kontroll i praktiken`.
- Byggde om `build/book.md`.


## Post-v5-justering: kapitel 6

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-05-justering.zip`.
- Justerade `chapters/analog-lasning-adc-06.md`.
- Vävde in `Det du kan använda kapitlet till` i `Mätfunktion i praktiken`.
- Tog bort `Vanliga varianter`.
- Tog bort `Snabb kontroll i praktiken`.
- Byggde om `build/book.md`.

## Post-v5-justering: kapitel 7

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-06-justering.zip`.
- Justerade `chapters/pwm-timers-07.md`.
- Vävde in `Det du kan använda kapitlet till` i `Tidsstyrning i praktiken`.
- Tog bort `Snabb kontroll i praktiken`.
- Byggde om `build/book.md`.

## Post-v5-justering: kapitel 8

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-07-justering.zip`.
- Justerade `chapters/avbrott-watchdog-08.md`.
- Tog bort `Valchecklista och vidare kontroll`.
- Byggde om `build/book.md`.

## Post-v5-justering: kapitel 9

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-08-justering.zip`.
- Justerade `chapters/kommunikation-bussar-09.md`.
- Vävde in `Det du kan använda kapitlet till` i `Kommunikationsval i praktiken`.
- Tog bort `Snabb kontroll i praktiken`.
- Tog bort `Egen bussreferens och felsökningsfall`.
- Byggde om `build/book.md`.


## Post-v5-justering: kapitel 10–16

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-09-export.zip`.
- Justerade kapitel 10–16.
- Tog bort kurslika `Valchecklista`-avsnitt i kapitel 10–16 där de förekom.
- Tog bort dokumentations- och övningsliknande praktiska kontrollavsnitt i kapitel 11, 12 och 16.
- Omformade praktiska referensmönster i kapitel 12–16 så att de fungerar mer som handboksnära verifieringar än som läroboksövningar.
- Byggde om `build/book.md`.
- Dokumenterade ändringen i `docs/post-v5-chapters-10-16-adjustment.md`.



## Post-v5-justering: kapitel 17–21

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-10-16-justering.zip`.
- Justerade kapitel 17–21.
- Vävde in `Det du kan använda kapitlet till` i kapitelöversikterna där sektionen förekom.
- Tog bort kurslika `Valchecklista`-avsnitt och `Valchecklista för laster`.
- Omformade praktiska verifieringsavsnitt till handboksnära kontrollpunkter och felsökningsstöd.
- Behöll säkerhetsnära kontroller i motor- och lastkapitel, men tog bort dokumentationsmallar och frågeformat.
- Byggde om `build/book.md`.
- Dokumenterade ändringen i `docs/post-v5-chapters-17-21-adjustment.md`.


## Post-v5-justering: kapitel 22–26

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-17-21-justering.zip`.
- Justerade kapitel 22–26.
- Vävde in `Det du kan använda kapitlet till` i kapitelöversikterna.
- Tog bort kurslika `Valchecklista`-avsnitt.
- Tog bort dokumentations- och övningsliknande avsnitt som `Verifiera display och gränssnitt`, `Dokumentera en optisk sensorprofil`, `Dokumentera en avstånds- eller närvarosensorprofil` och `Vanliga varianter`.
- Behöll praktiska referensmönster som mäter, verifierar eller demonstrerar konkret funktion.
- Tonade ned experiment-, syftes- och dokumentationsspråk i berörda referensmönster.
- Byggde om `build/book.md`.
- Dokumenterade ändringen i `docs/post-v5-chapters-22-26-adjustment.md`.

## Post-v5-justering: kapitel 27–32

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-22-26-justering.zip`.
- Justerade kapitel 27–32.
- Vävde in `Det du kan använda kapitlet till` i kapitelöversikterna.
- Tog bort kurslika `Valchecklista`-avsnitt.
- Tog bort dokumentations- och övningsliknande avsnitt som `Vanliga varianter`, `Nästa praktiska kontroll` och `Valchecklista för nästa drivlösning`.
- Behöll säkerhetsnära riskkontroller i mät- och drivkretskapitel.
- Gjorde praktiska referensmönster mindre experimentlika och mer handboksnära.
- Byggde om `build/book.md`.
- Dokumenterade ändringen i `docs/post-v5-chapters-27-32-adjustment.md`.

## Post-v5-justering: kapitel 33–38

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-27-32-justering.zip`.
- Justerade kapitel 33–38.
- Vävde in `Det du kan använda kapitlet till` i kapitelöversikterna i kapitel 33 och 34.
- Tog bort kurslika `Nästa praktiska kontroll`- och `Valchecklista`-avsnitt.
- Behöll konkreta verifieringar, riskkontroller, felsökningsflöden och referensmaterial.
- Gjorde risk-, felsöknings-, modul- och projektavsnitt mer handboksnära.
- Renodlade kapitel 38 som referens genom att ta bort arbetsmallar och egna referensmallar.
- Byggde om `build/book.md`.
- Dokumenterade ändringen i `docs/post-v5-chapters-33-38-adjustment.md`.


## Post-v5 EPUB-export efter kapitel 1–38-justeringar

- Utgångspunkt: `arduino-i-praktiken-projekt-v5-kapitel-33-38-justering.zip`.
- Kördes via projektets exportpipeline.
- Markdownvalidering rapporterade inga projektvarningar.
- `exports/arduino-i-praktiken.epub` skapades på nytt.
- EPUB-navigation kontrollerades.
- Dokumenterade exporten i `docs/post-v5-epub-export.md`.

## 2026-07-02 – Post-v5 finputs kapitel 3, 7, 8, 9 och 13

- Rensade kvarvarande experiment-, mål-, material- och reflektionsspråk i kapitel 3, 7, 8, 9 och 13.
- Ersatte övningslika kontrollavsnitt med mer handboksnära referensmönster och kontrollpunkter.
- Byggde om `build/book.md`.


## 2026-07-02 – EPUB-export efter post-v5 finputs

- Utgångspunkt: post-v5-finputs-versionen efter kapitel 3, 7, 8, 9 och 13.
- Gjorde en sista exportnära språkputs i kapitel 5, 6, 23 och 28 för att ta bort kvarvarande `experimentlogg`/`I experimentet`-spår.
- Kördes via projektets exportpipeline med EPUB-standard: `--toc --toc-depth=1`.
- Kontrollerade att EPUB-navigation finns och att `nav.xhtml` inte ligger som vanlig lässida.
- Kontrollerade att exporterad EPUB saknar de äldre läroboksmarkörerna som listas i `docs/post-v5-finputs-epub-export.md`.
- Dokumenterade exporten i `docs/post-v5-finputs-epub-export.md`.

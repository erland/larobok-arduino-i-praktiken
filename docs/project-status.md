# Projektstatus

## Bok

Titel: Arduino i praktiken  
Undertitel: Din guide till Arduino och elektronikkretsar  
Språk: Svenska  
Författare: Erland Lindmark  
Version: plan-e-final-rubrikputs-github-actions-fix1  
Datum: 2026-08-10

## Nuvarande fas

- GitHub Actions-publicering införd efter RUBRIKPUTS: metadata, README och projektstatus är uppdaterade till `plan-e-final-rubrikputs-github-actions-fix1`.
- `.github/` ligger i projektroten på samma nivå som `README.md`.
- Workflows för Validate, Build Preview och Release har lagts till.
- Kapitel 23, 27, 28, 36 och 37 har fått riktade rubrik- och ordningsjusteringar för tydligare kapitelstruktur.
- FINAL-PUTS efter PLAN-E är fortsatt bas för handboksidentitet, språkputs och EPUB-standard.
- Inledningen har justerats så boken konsekvent presenteras som praktisk handbok och referens.
- Kvarvarande `lärobok`-formuleringar i läsartext har ersatts med handboks-/referensspråk.
- Kvarvarande `experiment`-språk har putsats selektivt där det gav kurs-/labbkänsla. Tekniskt rimliga användningar kan finnas kvar när de beskriver test, prototyp, experimentell modul eller utforskande arbete.
- `build/book.md` har byggts om.
- EPUB-export har skapats enligt projektstandard.
- GitHub Actions bygger preview-artifact med EPUB och PDF samt release-assets på `v*`-taggar.

## Senaste kontroller

- Kapitelordning i metadata är komplett.
- Varje kapitel har en H1-rubrik.
- Inga H4-rubriker hittades i kapitelmanus.
- Kodblock är balanserade.
- EPUB-navigation finns via `nav.xhtml`.
- Ingen synlig text-Innehållsförteckning ska ligga i EPUB-flödet.

## Historik

# Projektstatus

## Bok

Titel: Arduino i praktiken  
Undertitel: Din guide till Arduino och elektronikkretsar  
Språk: Svenska  
Författare: Erland Lindmark  
Version: handbokstruktur-v5  
Datum: 2026-07-01

## Nuvarande fas

- Post-v5 EPUB-export genomförd efter kapitel 1–38-justeringarna: markdownvalidering utan projektvarningar, `build/book.md` ombyggd och `exports/arduino-i-praktiken.epub` exporterad enligt projektstandard.
- Post-v5-justering kapitel 17–21 genomförd: kurslika checklistor och dokumentationsmoment har tagits bort eller omformats, praktiska kontroller har behållits som handboksnära kontrollpunkter och `build/book.md` har byggts om.
- `[PLAN-H]` steg H12 genomfört: exportkontroll, EPUB/PDF-export och versionssättning till `handbokstruktur-v5`. Ny stabil basversion: `arduino-i-praktiken-projekt-handbokstruktur-v5.zip`.
- `[PLAN-H]` steg H11 genomfört: `build/book.md` har byggts om, markdownvalidering har körts utan projektvarningar och en kvarvarande inledningsformulering om den tidigare rubriken `Snabb orientering` har normaliserats.
- `[PLAN-H]` steg H10 genomfört: intern redaktionell stilguide har skapats i `docs/handbook-editorial-style-guide.md` och kopplats till kapiteltypsreferensen.
- `[PLAN-H]` steg H5 genomfört: `Snabb orientering` har ersatts med kapiteltypsspecifika rubriker och metodkapitlens kvarvarande `Praktiskt arbetspass` har normaliserats till `Arbetsmönster`.
- `[PLAN-H]` steg H4 genomfört: `Praktiskt test`, `Prova själv`, `Prova vidare` och `### Test`-undersektioner har omklassificerats till handboksnära rubriker som referensmönster, verifiering, riskkontroll, porteringstest, vanliga varianter och arbetsmall.
- `[PLAN-H]` steg H3 genomfört: quiz- och kontrollfrågor har omvandlats till handboksnära checklistor och användningskontroller.
- `[ANALYSPLAN]` steg 11 genomfört: prioritering och åtgärdskarta har skapats inför `[PLAN-H]`, med kritiska, rekommenderade och valfria åtgärder samt föreslagen arbetsordning.
- `[ANALYSPLAN]` steg 10 genomfört: tväranalys av hela boken har sammanställt återkommande mönster från steg 1–9, inklusive läroboksspråk, `Snabb orientering`, `Praktiskt test`, `Prova själv`/`Prova vidare`, kontrollfrågor, interna projektartefakter och kapiteltypsspecifika mallar inför `[PLAN-H]`.
- `[ANALYSPLAN]` steg 9 genomfört: kapitel 36–38 har analyserats redaktionellt med fokus på övergången från breadboard till återanvändbar modul, sammanhängande projekt, referenskapitel, snabbvalsguider, interna planspråk som `PLAN5` i läsartext, och hur praktiska slutsektioner bör omformas till arbetsmönster, integrationsordning, mallar och checklistor.
- `[ANALYSPLAN]` steg 8 genomfört: kapitel 31–35 har analyserats redaktionellt med fokus på drivkretsar, display/minne, analog signalanpassning, strömförsörjning, felsökning, robusthetsmönster och hur praktiska moment bör omformas från kursövningar till referensmönster, verifiering, riskkontroll och felsökningsmetod.
- `[ANALYSPLAN]` steg 7 genomfört: kapitel 26–30 har analyserats redaktionellt med fokus på rörelse/orientering, ljud/mikrofoner, ström/spänning/energi, position/tid/identitet, I/O-expansion, sensorkontroll, säker mätning, systemmönster och hur praktiska moment bör omformas till referensmönster, verifiering, designmönster och felsökning.
- `[ANALYSPLAN]` steg 6 genomfört: kapitel 21–25 har analyserats redaktionellt med fokus på laster, displayer, miljösensorer, optiska sensorer, närvaro/avstånd, praktiska verifieringar, sensorprofiler, riskkontroller och hur `Praktiskt test`/`Kontrollera ditt val` bör göras mer handboksnära.
- `[ANALYSPLAN]` steg 5 genomfört: kapitel 16–20 har analyserats redaktionellt med fokus på specialkort, LED, adresserbara LED, ljud, motorer, praktiska referensmönster, dubbla `Praktiskt test`-sektioner, `Kontrollera ditt val` och hur praktiken kan göras mer handboksnära.
- `[ANALYSPLAN]` steg 4 genomfört: kapitel 11–15 har analyserats redaktionellt med fokus på kort- och plattformskapitel, kortval, kortprofil, praktiska verifieringar, `Prova vidare`, `Kontrollera ditt val` och hur slutdelarna kan göras mer handboksnära.
- `[ANALYSPLAN]` steg 3 genomfört: kapitel 6–10 har analyserats redaktionellt med fokus på grundfunktioner, praktiska test, `Prova själv`, kontrollfrågor, målformuleringar och övergången till kort-/plattformskapitel.
- `[ANALYSPLAN]` steg 2 genomfört: inledningen och kapitel 1–5 har analyserats redaktionellt med fokus på handbokskänsla, läroboksspår, interna filreferenser, praktiska moment och quiz-/kontrollsektioner.
- `[ANALYSPLAN]` steg 1 genomfört: metodkalibrering, bokidentitet, kapiteltypologi och spårningsområden inför PLAN-H har dokumenterats.
- `[PLAN5]` steg 1 genomfört: kapitel 21 har kompletterats med elektromagneter, solenoider och andra spolar som induktiva laster.
- `[PLAN5]` steg 2 genomfört: kapitel 31 har kompletterats med DRV8833 och L9110S, och kapitel 20 har fått en kort motorvalshänvisning.
- `[PLAN5]` steg 3 genomfört: kapitel 33 har kompletterats med LM393/digitala tröskelmoduler och I2C logic level converter; kapitel 4 och 9 har fått korta hänvisningar.
- `[PLAN5]` steg 4 genomfört: kapitel 27 har kompletterats med KY-037 och kapitel 19 med LM386 för små högtalare.
- `[PLAN5]` steg 5 genomfört: kapitel 24 har kompletterats med APDS-9960/GY-9960 för färg, ljus, närhet och enkla gester; kapitel 22 har fått en kort UI-hänvisning.
- `[PLAN5]` steg 6 genomfört: kapitel 30 har kompletterats med PCF8575 som 16-bitars I2C-I/O-expander.
- `[PLAN5]` steg 7 genomfört: kapitel 25 har kompletterats med analoga Hall-sensorer och 49E-typ för magnetisk position, magnetfält och rörelseindikering.
- Kapitel 38, `docs/lookup-index.md` och `docs/canon-terminology.md` har uppdaterats för samma begrepp.
- `[PLAN5]` steg 9 genomfört: lookup-index, canon, bokspecifikation och projektstatus har kontrollerats och kompletterats så att alla nya begrepp, inklusive digital tröskelmodul och induktiv last, används konsekvent.
- `[PLAN5]` steg 11 genomfört: ny slutversion `handbokstruktur-v4` skapad.

## Genomförda plansteg

| Plan | Status | Kommentar |
|---|---|---|
| `[PLAN]` | Genomförd | Handboksstruktur, kapiteltypologi, batchjustering och exportbarhetskontroll. |
| `[PLAN2]` | Genomförd | `Se också` togs bort eller ersattes med selektiva, problemorienterade `Relaterat`-sektioner. |
| `[PLAN3]` | Genomförd | Finputsning inför v2, navigeringsansvar, markdown/exportkontroll och version `handbokstruktur-v2`. |
| `[PLAN4]` | Genomförd | Komplettering av vanliga elektronikbutiksmoduler och Arduino-kit-komponenter samt version `handbokstruktur-v3`. |
| `[PLAN5]` | Genomförd | Komplettering av vanliga kretsar, drivmoduler, nivåomvandling, ljudmoduler, optiska moduler, I/O-expansion, analoga Hall-sensorer och induktiva laster samt version `handbokstruktur-v4`. |

## PLAN4-kompletteringar

| Steg | Status | Innehåll |
|---|---|---|
| 1 | Klart | Kapitel 22: rotary encoder, joystick, keypad, kapacitiv touch och IR-fjärr. |
| 2 | Klart | Kapitel 23: jordfukt, vattennivå, regnsensorer och MQ-gassensorer. |
| 3 | Klart | Kapitel 33: FSR, flexsensorer, vågceller och HX711. |
| 4 | Klart | Kapitel 9 och 38: nRF24L01, 433 MHz RF, RS485, CAN och LoRa. |
| 5 | Klart | Kapitel 20 och 31: PCA9685, ULN2003/28BYJ-48, L298N, A4988 och DRV8825. |
| 6 | Klart | Kapitel 22 och 24: tydligare IR-fjärrkontroll och IR-mottagarmoduler. |
| 7 | Klart | Kapitel 38 uppdaterat som samlad snabbguide. |
| 8 | Klart | `lookup-index` och canon/terminologi uppdaterade. |
| 9 | Klart | Markdown- och exportkontroll genomförd. |
| 10 | Klart | Ny projektversion `handbokstruktur-v3` skapad. |

## PLAN5-kompletteringar

| Steg | Status | Innehåll |
|---|---|---|
| 1 | Klart | Kapitel 21: elektromagneter, solenoider och andra spolar som induktiva laster. Kapitel 38, lookup-index och canon uppdaterade. |
| 2 | Klart | Kapitel 31: DRV8833 och L9110S. Kapitel 20, kapitel 38, lookup-index och canon uppdaterade. |
| 3 | Klart | Kapitel 33: LM393 och I2C logic level converter. Kapitel 4, kapitel 9, kapitel 38, lookup-index och canon uppdaterade. |
| 4 | Klart | Kapitel 27 och 19: KY-037 och LM386. Kapitel 38, lookup-index och canon uppdaterade. |
| 5 | Klart | Kapitel 24: APDS-9960/GY-9960. Kapitel 22, kapitel 38, lookup-index och canon uppdaterade. |
| 6 | Klart | Kapitel 30: PCF8575. Kapitel 38, lookup-index och canon uppdaterade. |
| 7 | Klart | Kapitel 25: analog Hall-sensor. Kapitel 38, lookup-index och canon uppdaterade. |
| 8 | Klart | Kapitel 38: samlad snabbguide för PLAN5-tillägg. |
| 9 | Klart | Lookup-index, canon, bokspecifikation och projektstatus kontrollerade och kompletterade med samtliga PLAN5-begrepp. |
| 10 | Klart | Markdown- och exportkontroll genomförd utan blockerande varningar. EPUB och PDF exporterade. |
| 11 | Klart | Ny projektversion `handbokstruktur-v4` skapad. |

## ANALYSPLAN-steg

| Steg | Status | Innehåll |
|---|---|---|
| 1 | Klart | Metodkalibrering, bokidentitet, kapiteltypologi och spårningsområden inför PLAN-H. |
| 2 | Klart | Kapitel 00–05: inledning, tidiga orienterings-/teorikapitel, interna filreferenser, praktiska moment och quiz-/kontrollsektioner. |
| 3 | Klart | Kapitel 06–10: grundfunktioner, signaler, kommunikation, praktiska test, målformuleringar och övergång till kort-/plattformskapitel. |
| 4 | Klart | Kapitel 11–15: kort- och plattformskapitel, kortval, kortprofil, praktiska verifieringar och kontrollsektioner. |
| 5 | Klart | Kapitel 16–20: specialkort, LED, adresserbara LED, ljud, motorer, referensmönster, dubbla praktiska test och risk-/valkontroller. |
| 6 | Klart | Kapitel 21–25: laster, displayer, miljösensorer, optiska sensorer, närvaro/avstånd, sensorprofiler, riskkontroller och handboksnära praktiska moment. |
| 7 | Klart | Kapitel 26–30: rörelse/orientering, ljud/mikrofoner, ström/spänning/energi, position/tid/identitet, I/O-expansion, praktiska referensmönster, säker mätning och felsökningsformat. |
| 8 | Klart | Kapitel 31–35: drivkretsar, display/minne, analog signalanpassning, strömförsörjning, felsökning och handboksnära robusthetsmönster. |
| 9 | Klart | Kapitel 36–38 samt referens, index, snabbguider, navigation, slutblock och interna planspråk i läsartext. |
| 10 | Klart | Tväranalys av återkommande mönster, ersättningskarta och kapiteltypsspecifika rekommendationer. |
| 11 | Klart | Prioritering av kritiska, rekommenderade och valfria åtgärder samt åtgärdskarta inför `[PLAN-H]`. |
| 12 | Klart | `[PLAN-H]` skapad som redaktionell handboksplan i `docs/PLAN-H.md`. |

## Kapitelstatus

| Område | Kapitel | Status |
|---|---|---|
| Inledning och orientering | 0–4 | Klart |
| Grundfunktioner | 5–9 | Klart |
| Kort och plattformar | 10–16 | Klart |
| Komponenter och aktuatorer | 17–22 | Klart |
| Sensorer och mätning | 23–29 | Klart |
| Robusthet och kretsar | 30–34 | Klart |
| Metod, projekt och referens | 35–38 | Klart |

## Exportstatus

| Export | Status |
|---|---|
| Validering | Godkänd utan varningar |
| `build/book.md` | Uppdaterad och ombyggd i PLAN5 steg 10 |
| EPUB | Skapad |
| PDF | Skapad |

## Slutlig projektversion

Ny projektversion skapad:

```text
arduino-i-praktiken-projekt-handbokstruktur-v4.zip
```

Se `docs/project-version-handbokstruktur-v4.md`.

## Nästa rekommenderade steg

- Nästa rekommenderade steg: genomför `[PLAN-H]` steg H8.

## [ANALYSPLAN]

Startad: 2026-07-01

Projektet utgår åter från `handbokstruktur-v4`. En ny analysplan har skapats för att stegvis analysera bokens handboksidentitet, kapitelstruktur, läroboksspår, praktiska moment, quiz/kontrollfrågor och interna projektartefakter innan `[PLAN-H]` skrivs.

Analysfasen ska inte ändra bokmanuset. Den ska endast skapa analysunderlag och därefter en separat `[PLAN-H]`.

Aktuella analysdokument:

- `docs/ANALYSPLAN.md`
- `docs/plan-h-analysis-log.md`
- `docs/plan-h-analysis-step-01-method-and-identity.md`
- `docs/plan-h-analysis-step-02-chapters-00-05.md`
- `docs/plan-h-analysis-step-03-chapters-06-10.md`
- `docs/plan-h-analysis-step-04-chapters-11-15.md`
- `docs/plan-h-analysis-step-05-chapters-16-20.md`
- `docs/plan-h-analysis-step-06-chapters-21-25.md`
- `docs/plan-h-analysis-step-07-chapters-26-30.md`
- `docs/plan-h-analysis-step-08-chapters-31-35.md`
- `docs/plan-h-analysis-step-09-chapters-36-38.md`
- `docs/plan-h-analysis-step-10-cross-analysis.md`
- `docs/plan-h-analysis-step-11-prioritization.md`



## [PLAN-H]

Skapad: 2026-07-01

Resultatfil:

- `docs/PLAN-H.md`

`[PLAN-H]` är en redaktionell handboksplan som bygger på hela `[ANALYSPLAN]`. Den ska genomföras först efter användarens godkännande.

## [PLAN-H] genomförande

Startad: 2026-07-01

| Steg | Status | Resultat |
|---|---|---|
| H1 – Rensa interna projektspår i läsartext | Klart | `docs/PLAN-H-step-01-internal-project-traces.md` |
| H2 – Ersätt kravliknande lärandemål i `Snabb orientering` | Klart | `docs/PLAN-H-step-02-learning-goal-language.md` |
| H3 – Omvandla quiz- och kontrollfrågor | Klart | `docs/PLAN-H-step-03-quiz-and-control-sections.md` |
| H4 – Omklassificera praktiska moment | Klart | `docs/PLAN-H-step-04-practical-section-reclassification.md` |
| H5 – Rubriknormalisering efter kapiteltyp | Klart | `docs/PLAN-H-step-05-heading-normalization-by-chapter-type.md` |
| H6 – Stärk beslutsstöd och snabbval | Klart | `docs/PLAN-H-step-06-decision-support-and-quick-choice.md` |
| H7 – Förstärk riskkontroller och vanliga misstag | Klart | `docs/PLAN-H-step-07-risk-controls-and-common-mistakes.md` |
| H8 – Gör slutblocket mer verktygsorienterat | Klart | `docs/PLAN-H-step-08-end-block-tools.md` |
| H9 – Uppdatera läsarvänliga korsreferenser | Klart | `docs/PLAN-H-step-09-reader-friendly-cross-references.md` |

Nästa rekommenderade steg: genomför `[PLAN-H]` steg H8.

## PLAN-H steg H8

Status: Genomfört 2026-07-01.

Slutblocket har gjorts mer verktygsorienterat:

- kapitel 36 fungerar tydligare som modul- och arbetschecklista,
- kapitel 37 fungerar tydligare som integrationsordning och projektmall,
- kapitel 38 fungerar tydligare som referens- och mallkapitel.

Nästa rekommenderade steg: genomför steg H11 enligt `[PLAN-H]`, bygg om `build/book.md` vid behov och gör markdownkontroll.


## PLAN-H steg H9

Status: Genomfört 2026-07-01.

Läsarvänliga korsreferenser har uppdaterats:

- befintliga `Relaterat`-avsnitt har gjorts mer problembaserade,
- flera långa hänvisningslistor har kortats och förtydligats,
- kapitel som saknade naturlig väg vidare har fått korta relaterat-avsnitt,
- inga interna projektspår har återinförts i kapiteltexterna.

Nästa rekommenderade steg: genomför steg H11 enligt `[PLAN-H]`, bygg om `build/book.md` vid behov och gör markdownkontroll.

## PLAN-H steg H10

Status: Genomfört 2026-07-01.

Intern redaktionell stilguide har skapats:

- `docs/handbook-editorial-style-guide.md` dokumenterar handbokston, fraser att undvika, ersättningsmönster, kapiteltyper, praktiska moment, beslutsstöd, riskkontroller och korsreferenser,
- `docs/chapter-templates-by-type.md` har kopplats till den nya stilguiden,
- inga kapiteltexter eller `build/book.md` har ändrats, eftersom steget enbart gäller intern redaktionell styrning.

Nästa rekommenderade steg: genomför steg H11 enligt `[PLAN-H]`, bygg om `build/book.md` vid behov och gör markdownkontroll.

## Post-v5 justering – Kapitel 1

Status: Genomfört 2026-07-01.

Kapitel 1 har justerats efter läsargranskning:

- sektionen `Kartläggning: två kort och en modul` har tagits bort,
- sektionen `Egen kontroll i praktiken` har tagits bort,
- sektionen `Viktiga samband att känna igen` har tagits bort,
- `build/book.md` har byggts om.

Motiv: justeringen gör kapitel 1 mindre lärobokslikt och mer koncentrerat som handbokskapitel.


## Post-v5 justering – Kapitel 2

Status: Genomfört 2026-07-01.

Kapitel 2 har justerats efter läsargranskning:

- sektionen `Beslutsmönster: välj kort för tre projekt` har tagits bort,
- sektionen `Kortvalschecklista i praktiken` har tagits bort,
- sektionen `Valchecklista` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlet innehåller redan det beslutsstöd som behövs i huvudtext, exempel och sammanfattning. De borttagna sektionerna gjorde avslutet mer lärobokslikt än handboksnära.



## Post-v5-justering kapitel 3

Kapitel 3 har redigerats redaktionellt: kodstilsrubriken har förenklats, konfigurationsblockets inledning har kortats och sektionen `Arbetskontroll` har tagits bort. `build/book.md` har byggts om.

## Post-v5-justering kapitel 4

Status: Genomfört 2026-07-01.

Kapitel 4 har redigerats redaktionellt:

- sektionen `Riskkontroll i praktiken` har tagits bort,
- sektionen `Viktiga samband att känna igen` har tagits bort,
- sektionen `Begreppsförklaring: logiknivå och gemensam jord` har flyttats före `Snabb sammanfattning`,
- `build/book.md` har byggts om.

Motiv: kapitlet blir mer koncentrerat som handbokskapitel och avslutas renare utan kursliknande kontrollmoment.

## Post-v5-justering kapitel 5

Status: Genomfört 2026-07-01.

Kapitel 5 har redigerats redaktionellt:

- sektionen `Det du kan använda kapitlet till` har vävts in i `Grundfunktion i praktiken`,
- formuleringen om kapitlets avslutande experiment har gjorts mer handboksnära,
- sektionen `Snabb kontroll i praktiken` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlet blir mer koncentrerat och mindre lärobokslikt utan att tekniskt sakmaterial tas bort.


## Post-v5-justering kapitel 6

Status: Genomfört 2026-07-01.

Kapitel 6 har redigerats redaktionellt:

- sektionen `Det du kan använda kapitlet till` har vävts in i `Mätfunktion i praktiken`,
- sektionen `Vanliga varianter` har tagits bort,
- sektionen `Snabb kontroll i praktiken` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlet blir mer koncentrerat och mindre lärobokslikt, samtidigt som det tekniska sakmaterialet finns kvar i huvudtext, referensmönster, felsökning och sammanfattning.

## Post-v5-justering kapitel 7

Status: Genomfört 2026-07-01.

Kapitel 7 har redigerats redaktionellt:

- sektionen `Det du kan använda kapitlet till` har vävts in i `Tidsstyrning i praktiken`,
- sektionen `Snabb kontroll i praktiken` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlet blir mer koncentrerat och mindre lärobokslikt, samtidigt som den praktiska nyttan finns kvar i inledningen, huvudtexten, referensmönstren och sammanfattningen.

## Post-v5-justering kapitel 8

Status: Genomfört 2026-07-01.

Kapitel 8 har redigerats redaktionellt:

- sektionen `Valchecklista och vidare kontroll` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlet blir mer koncentrerat och mindre lärobokslikt, samtidigt som kärninnehållet om polling, interrupt, timeouts, säkra standardlägen och watchdog finns kvar i huvudtext, exempel, snabbreferens och relaterade hänvisningar.

## Post-v5-justering kapitel 9

Status: Genomfört 2026-07-01.

Kapitel 9 har redigerats redaktionellt:

- sektionen `Det du kan använda kapitlet till` har vävts in i `Kommunikationsval i praktiken`,
- sektionen `Snabb kontroll i praktiken` har tagits bort,
- sektionen `Egen bussreferens och felsökningsfall` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlet blir mer koncentrerat och mindre lärobokslikt, samtidigt som kärninnehållet om UART, I2C, SPI, 1-Wire, nivåskiftning, felsökning och bussval finns kvar i inledning, huvudtext, verifieringsavsnitt och snabbreferens.


## Post-v5-justering kapitel 10–16

Status: Genomfört 2026-07-02.

Kapitel 10–16 har redigerats redaktionellt:

- kapitel 10: `Valchecklista` har tagits bort,
- kapitel 11: dokumentationsövningen `Kortprofil: identifiera ett okänt kompatibelt kort`, `Nästa praktiska kontroll` och `Valchecklista` har tagits bort,
- kapitel 12: porteringstestet har gjorts mer handboksnära och kurslika resultat-/kontrollsektioner har tagits bort,
- kapitel 13: referensmönstret har behållits men dokumentations- och jämförelseuppgifter har tagits bort,
- kapitel 14: referensmönstret har behållits men mål-/arbetsbladsformatet har förenklats,
- kapitel 15: referensmönstret har behållits men experimentloggsformuleringar har tonats ned,
- kapitel 16: specialkortsmomentet har gjorts om till `Minsta kontroll innan du använder ett specialkort`; `Nästa praktiska kontroll` och `Valchecklista` har tagits bort,
- `build/book.md` har byggts om.

Motiv: praktiska kontroller som verifierar verklig funktion behålls, medan dokumentationsövningar och avslutande kursfrågor tas bort för att stärka bokens handbokskänsla.


## Post-v5-justering kapitel 22–26

Status: Genomfört 2026-07-02.

Kapitel 22–26 har redigerats redaktionellt:

- kapitel 22: `Det du kan använda kapitlet till` har vävts in i översikten; `Verifiera display och gränssnitt` och `Valchecklista` har tagits bort,
- kapitel 23: `Det du kan använda kapitlet till` har vävts in i översikten; referensmönstret har gjorts mer handboksnära; `Vanliga varianter` och `Valchecklista` har tagits bort,
- kapitel 24: `Det du kan använda kapitlet till` har vävts in i översikten; sensorstyrd RGB-status har justerats från experimentform till mönsterform; dokumentations- och kontrollavsnitt har tagits bort,
- kapitel 25: `Det du kan använda kapitlet till` har vävts in i översikten; jämförelsemönstret har gjorts mer handboksnära; dokumentations- och kontrollavsnitt har tagits bort,
- kapitel 26: `Det du kan använda kapitlet till` har vävts in i översikten; referensmönstret har gjorts mer handboksnära; `Vanliga varianter` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlen behåller praktiska mönster som faktiskt mäter, verifierar och felsöker display-, miljö-, optik-, närvaro- och rörelsefunktioner, men tar bort dokumentationsövningar, frågelistor och kurslika kontrollblock.

## Post-v5-justering kapitel 27–32

Status: Genomfört 2026-07-02.

Kapitel 27–32 har redigerats redaktionellt:

- kapitel 27: `Det du kan använda kapitlet till` har vävts in i översikten; ljudindikatorn har gjorts mer handboksnära; `Vanliga varianter` och `Valchecklista` har tagits bort,
- kapitel 28: nyttosektionen har vävts in i översikten; mätkopplingen har behållits men syftes-/dokumentationsspråk har tonats ned; `Nästa praktiska kontroll` och den frågeformade slutsektionen `Riskkontroll` har tagits bort,
- kapitel 29: nyttosektionen har vävts in i översikten; referensmönstret har gjorts mer handboksnära; `Vanliga varianter` och `Valchecklista` har tagits bort,
- kapitel 30: nyttosektionen har vävts in i översikten; 74HC595- och MCP23017-mönstren har gjorts mer handboksnära; dokumentationsspråk och kurslika kontrollblock har tagits bort,
- kapitel 31: nyttosektionen har vävts in i översikten; jämförelsemönstret har gjorts mer handboksnära; `Valchecklista för nästa drivlösning` har tagits bort medan riskkontroll och säkerhetsruta har behållits,
- kapitel 32: nyttosektionen har vävts in i översikten; datalogger-mönstret har gjorts mer handboksnära; `Vanliga varianter` och `Valchecklista` har tagits bort,
- `build/book.md` har byggts om.

Motiv: kapitlen behåller praktiska mönster som mäter, verifierar eller felsöker ljud, mätning, tid/identitet, I/O-expansion, drivkretsar och datalagring, men tar bort dokumentationsövningar, frågelistor och kurslika kontrollblock.

## Post-v5-justering kapitel 33–38

Status: Genomfört 2026-07-02.

Kapitel 33–38 har redigerats redaktionellt:

- kapitel 33: `Det du kan använda kapitlet till` har vävts in i översikten; `Nästa praktiska kontroll` och `Valchecklista` har tagits bort; tröskel- och filtermönster har behållits men gjorts mer handboksnära,
- kapitel 34: nyttosektionen har vävts in i översikten; strömbudget/riskkontroll har kortats och gjorts mer praktisk; kurslika kontrollsektioner har tagits bort medan säkerhetsnära innehåll har behållits,
- kapitel 35: I2C-felsökningsmönstret har behållits; dokumentationsspråk har ändrats till kontrollspråk; `Checklista` och `Arbetschecklista` har slagits ihop till `Felsökningschecklista`,
- kapitel 36: pinout- och modulavsnitt har gjorts mer handboksnära; `Modulmall i praktiken` har tagits bort eftersom den överlappade med modulchecklistan,
- kapitel 37: projektets dokumentationsavsnitt har omformulerats till praktiska beslut att spara; integrationsordningen har kortats och gjorts mindre workshoplik,
- kapitel 38: referenskapitlet har renodlats genom att `Arbetsmall: gör en egen valguide` och `Egen referensmall` har tagits bort; experiment-/dokumentationsspråk har ersatts med prototyp- och felsökningsnytta,
- `build/book.md` har byggts om.

Motiv: sista blocket ska fungera som praktiskt stöd, felsökningshjälp, modulmetodik, projektstruktur och ren referens utan att glida tillbaka till kursövningar, arbetsblad eller dokumentationsuppgifter.

## Statusuppdatering 2026-07-02

Post-v5-finputs för kapitel 3, 7, 8, 9 och 13 är genomförd. Kvarvarande tydliga läroboksspår i dessa kapitel har rensats eller omformulerats till testprojekt, referensmönster, praktiska tidsmönster och konkreta kontrollpunkter. `build/book.md` är uppdaterad.


## Statusuppdatering 2026-07-02

EPUB-export efter post-v5-finputs är genomförd via projektets lokala exportpipeline. Inför exporten gjordes en sista liten språkputs i kapitel 5, 6, 23 och 28 för att ta bort kvarvarande `experimentlogg`/`I experimentet`-spår. `build/book.md` och `exports/arduino-i-praktiken.epub` är uppdaterade. Exportkontrollen visar att EPUB-navigation finns och att äldre läroboksmarkörer inte finns kvar i EPUB-filen.

## Statusuppdatering 2026-07-02

PLAN-E steg E1 är genomfört för kapitel 1–8. Grundblockets praktiska referensmönster har förstärkts utan att återinföra övnings-/labbstruktur: kapitel 4 har fått ett tydligare säkert grundkopplingsmönster, kapitel 5 ett renare knappmönster, kapitel 6 en bro från potentiometer till verklig sensor, kapitel 7 en icke-blockerande analog PWM-variant och kapitel 8 ett generiskt timeout-/safe-mode-mönster. `build/book.md` är ombyggd.
## Statusuppdatering 2026-07-02

PLAN-E steg E2 är genomfört för kapitel 9–16. Kommunikations- och plattformskapitlen har förstärkts med tydligare teknikspecifika referensmönster: SPI med chip select, UNO/Nano/Mega-portering, kortidentifiering för kloner, portering till moderna Arduino-kort, ESP32 deep sleep, Pico/PIO-timing och kortprofil före specialkortsintegration. `build/book.md` är ombyggd.

## Statusuppdatering 2026-07-02

PLAN-E steg E3 är genomfört för kapitel 17–26. Komponentblocket har förstärkts med små, praktiska handboksrutor: strömtumregel för adresserbara LED, typiska ljudkoder, sensorplacering som del av miljömätning, ljuströskel med hysteresis och vanliga användningar av rörelse-/skakmönster. Kvarvarande `### Material`-rubriker i kapitel 17–26 har ersatts med `### Det här används i exemplet` och `build/book.md` är ombyggd.

## Statusuppdatering 2026-07-02

PLAN-E steg E4 är genomfört för kapitel 27–34. Mät- och systemblocket har förstärkts med små praktiska handboksrutor: typiska ljudmönster, typisk händelserad, tydligare 74HC595-gräns mellan logik och lastström, loggrad med status/fel samt mer återanvändbara referensmönster för analog tröskel och lågpassfiltrering. Kvarvarande `### Material`-rubriker och E4-relevanta labbmarkörer i kapitel 27–34 har rensats och `build/book.md` är ombyggd.

## Statusuppdatering 2026-07-02

PLAN-E steg E5 är genomfört för kapitel 35–38. De avslutande metod- och referenskapitlen har förstärkts med en tabell över typiska minimisketcher, en före/efter-ruta för modulgränssnitt, en tabell som visar hur slutprojektet återanvänder tidigare referensmönster samt en mindre språkputs i referenskapitlets snabbguide. `build/book.md` är ombyggd.


## 2026-07-02 – PLAN-E steg E6 genomfört

PLAN-E är genomförd och slutkontrollerad. Exempeltäckningen är sammanfattad i `docs/example-coverage-review.md`. EPUB-export har skapats enligt projektstandard och projektet är packat som final PLAN-E-zip.


## 2026-07-02 – RUBRIKPUTS efter PLAN-E-final

Riktad rubrikputs är genomförd efter helhetsgranskning av H1–H3. Kapitel 23, 27, 28, 36 och 37 har fått mindre rubrik- och ordningsjusteringar för tydligare slutstruktur och bättre konsekvens mellan snabbreferens, snabb sammanfattning, checklistor och projektkontroll. `build/book.md` är ombyggd och EPUB-export har skapats enligt projektstandard.


## GitHub Actions korrigering

Preview- och Release-workflows installerar nu `lmodern` och `texlive-lang-european` så PDF-export via XeLaTeX fungerar i GitHub Actions-runnern.

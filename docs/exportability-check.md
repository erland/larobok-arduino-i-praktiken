# [PLAN] Steg 11: Markdown- och exportbarhetskontroll

Datum: 2026-06-30

## Syfte

Detta dokument sammanfattar kontrollen av markdownstruktur och exportbarhet efter att kapitelstrukturen har justerats enligt `[PLAN]`.

Kontrollen gäller den version där:

- kapitel 1–38 har batchjusterats,
- återkommande sektioner har normaliserats,
- uppslagsverksfunktionen har stärkts,
- progressionen har godkänts.

## Kontrollerade områden

| Område | Resultat |
|---|---|
| Kapitelordning i metadata | Godkänd |
| Alla kapitel i metadata finns på disk | Godkänd |
| Extra kapitel utanför metadata | Inga hittade |
| H1-rubrik per kapitel | Godkänd |
| H4 eller djupare rubriker | Inga hittade |
| Obalanserade kodblock | Inga hittade |
| Bildreferenser till saknade filer | Inga hittade |
| Gamla kursrubriker som H2/H3 | Inga hittade |
| Lokal markdownvalidering via `scripts/export-book.py validate` | Godkänd utan varningar |
| Sammanslagen markdown i `build/book.md` | Uppdaterad |
| EPUB-rökexport | Godkänd |
| EPUB-navigation | `nav.xhtml` finns |
| EPUB-nav i spine | Satt till `linear="no"` |

## Gamla rubriker som kontrollerades

Följande tidigare standardrubriker kontrollerades och hittades inte längre som aktiva H2/H3-rubriker i kapitelmanus:

- `Varför detta kapitel finns`
- `Lärandemål`
- `Innan vi börjar`
- `Övningar`
- `Quiz/reflektionsfrågor`
- `Praktiskt experiment`
- `Referenssammanfattning`
- `Nästa steg`

## Exportbarhet

Projektets lokala exportpipeline är körbar för validering och markdownbygge.

Följande kommandon har kontrollerats:

```bash
python3 scripts/export-book.py validate
python3 scripts/export-book.py markdown
python3 scripts/export-book.py epub
```

Resultat:

- `validate` gav inga valideringsvarningar.
- `markdown` byggde om `build/book.md`.
- `epub` skapade `exports/arduino-i-praktiken.epub`.
- EPUB-filen innehåller EPUB-navigation och `nav` är markerad som icke-linjär i spine.

PDF-exportvägen är fortsatt definierad i scriptet med `xelatex`, `--toc` och `--toc-depth=3`. Ingen PDF-fil lades till som ny leverans i detta steg; kontrollen fokuserade på projektets markdown- och exportförberedelse samt EPUB-rökexport.

## Bedömning

Markdown- och exportbarhetskontrollen är **godkänd**.

Projektet är redo för nästa plansteg:

> **[PLAN] 12. Skapa ny projektversion**

## Rekommendation inför slutversion

Innan en slutlig EPUB/PDF levereras bör en separat exportpass göras där både EPUB och PDF öppnas visuellt och kontrolleras för:

- rubrikavstånd,
- tabellbrytningar,
- kodblockens läsbarhet,
- bildskalning,
- innehållsförteckning i PDF,
- att EPUB inte visar en synlig innehållsförteckningssida i läsflödet.


## Projektversion efter kontroll

Kontrollen ligger till grund för `arduino-i-praktiken-projekt-handbokstruktur-v1.zip`, skapad 2026-06-30 enligt `[PLAN]` steg 12.


## [PLAN3] Steg 6: förnyad markdown- och exportkontroll

Datum: 2026-07-01

Efter `[PLAN3]` steg 1–5 kördes en ny exportkontroll. Resultatet finns i `docs/plan3-step-06-markdown-exportkontroll.md`.

Sammanfattning:

- lokal validering godkänd utan varningar,
- `build/book.md` ombyggd,
- EPUB skapad,
- PDF skapad,
- EPUB-navigation kontrollerad,
- PDF renderades i stickprov,
- tecknet `≈` ersattes med svensk text där det gav fontvarningar i PDF-exporten.

Projektet är redo för `[PLAN3]` steg 7: skapa `handbokstruktur-v2`.


## [PLAN3] Steg 7: Versionssättning till v2

Datum: 2026-07-01

Efter godkänd markdown- och exportkontroll har projektet versionssatts till `handbokstruktur-v2`.

Ny basfil:

```text
arduino-i-praktiken-projekt-handbokstruktur-v2.zip
```

Metadata i `book.yaml` och `docs/export-metadata.yaml` är uppdaterad till version `handbokstruktur-v2` och datum `2026-07-01`.


## Efterkontroll för handbokstruktur-v2

Efter versionssättning kördes validering, markdownbygge, EPUB-export och PDF-export på nytt.

Resultat:

- `validate`: godkänd utan varningar.
- `markdown`: `build/book.md` uppdaterad.
- `epub`: `exports/arduino-i-praktiken.epub` uppdaterad.
- `pdf`: `exports/arduino-i-praktiken.pdf` uppdaterad.


## [PLAN4] Steg 2: Efterkontroll

Datum: 2026-07-01

Efter komplettering av kapitel 23 med jordfukt, vattennivå, regnsensorer och MQ-gassensorer kördes projektets exportkontroll på nytt.

Resultat:

- `validate`: godkänd utan varningar.
- `markdown`: `build/book.md` uppdaterad.
- `epub`: `exports/arduino-i-praktiken.epub` uppdaterad.
- `pdf`: `exports/arduino-i-praktiken.pdf` uppdaterad.

Notering: miljö- och kit-sensorerna behandlas som praktiska indikatorer och experimentmoduler. De beskrivs inte som säkerhetskritiska eller certifierade mätinstrument.


## [PLAN4] Steg 3 efterkontroll

Datum: 2026-07-01

Efter komplettering av kapitel 33 med resistiva sensorer, FSR, flexsensorer, vågceller och HX711 kördes projektets exportkontroll igen.

| Kontroll | Resultat |
|---|---|
| `scripts/export-book.py validate` | Godkänd utan varningar |
| `build/book.md` | Ombyggd |
| EPUB-export | Godkänd |
| PDF-export | Godkänd |

Notering: PDF/EPUB skapades om efter ändringen så att exporterna innehåller de nya kapitelavsnitten.


## [PLAN4] steg 4

Efter kompletteringen av kommunikationsmoduler kontrollerades markdown, kapitelordning och exportbarhet på nytt. Kapitel 9 och kapitel 38 ingår i den uppdaterade sammanslagna boken.


## [PLAN4] Steg 5 efterkontroll

Efter kompletteringen av kapitel 20 och 31 med vanliga motor- och drivmoduler kördes projektets lokala exportpipeline igen.

| Kontroll | Resultat |
|---|---|
| `scripts/export-book.py validate` | Godkänd utan varningar |
| `scripts/export-book.py markdown` | `build/book.md` ombyggd |
| `scripts/export-book.py epub` | `exports/arduino-i-praktiken.epub` skapad |
| `scripts/export-book.py pdf` | `exports/arduino-i-praktiken.pdf` skapad |

Kompletteringen introducerade inga H4-rubriker, inga obalanserade kodblock och inga list-/tabellvarningar efter korrigering.


## [PLAN4] Steg 6 efterkontroll

Efter kompletteringen av IR-fjärrkontroll och IR-mottagarmoduler i kapitel 22 och 24 kördes projektets lokala exportpipeline igen.

| Kontroll | Resultat |
|---|---|
| `scripts/export-book.py validate` | Godkänd utan varningar |
| `scripts/export-book.py all` | EPUB och PDF skapade |
| `build/book.md` | Ombyggd |
| H4 eller djupare rubriker | Inga hittade av valideringen |
| Obalanserade kodblock | Inga hittade av valideringen |
| Bildreferenser | Inga saknade bildreferenser rapporterade |

Kompletteringen introducerade inga markdown- eller exportvarningar.


## PLAN4 steg 7 exportkontroll

Efter uppdateringen av kapitel 38 som samlad snabbguide kördes exporten om.

Resultat:

- `scripts/export-book.py all` slutfördes utan valideringsfel.
- `build/book.md` uppdaterades.
- `exports/arduino-i-praktiken.epub` skapades om.
- `exports/arduino-i-praktiken.pdf` skapades om.

Notering: ett miljömeddelande från spreadsheet-runtime skrevs till stderr under Python-start, men exportscriptet avslutades med statuskod 0 och skapade exportfilerna.

## [PLAN4] steg 8

- Lookup-index och canon/terminologi kontrollerade mot PLAN4-tillägg.
- Inga kapitelmanus ändrades i detta steg.
- `build/book.md` behålls uppdaterad från senaste kapiteländringen.


## [PLAN4] Steg 9: kompletterande markdown- och exportkontroll

Datum: 2026-07-01

Efter `[PLAN4]` steg 1–8 kördes en ny markdown- och exportkontroll. Resultatet finns i `docs/plan4-step-09-markdown-exportkontroll.md`.

Sammanfattning:

| Kontroll | Resultat |
|---|---|
| Lokal validering | Godkänd utan varningar |
| `build/book.md` | Ombyggd |
| EPUB-export | Godkänd |
| PDF-export | Godkänd |
| EPUB-navigation | Godkänd |
| PDF-stickprov | Renderat utan fel |

Projektet är redo för `[PLAN4]` steg 10: skapa `handbokstruktur-v3`.


## [PLAN4] Steg 10: Versionssättning till v3

Datum: 2026-07-01

Efter godkänd `[PLAN4]` markdown- och exportkontroll har projektet versionssatts till `handbokstruktur-v3`.

Ny basfil:

```text
arduino-i-praktiken-projekt-handbokstruktur-v3.zip
```

Metadata i `book.yaml` och `docs/export-metadata.yaml` är uppdaterad till version `handbokstruktur-v3` och datum `2026-07-01`.

Efter versionssättningen kördes validering, markdownbygge, EPUB-export och PDF-export på nytt.

Resultat:

- `validate`: godkänd utan varningar.
- `markdown`: `build/book.md` uppdaterad.
- `epub`: `exports/arduino-i-praktiken.epub` uppdaterad.
- `pdf`: `exports/arduino-i-praktiken.pdf` uppdaterad.

# Arduino i praktiken

**Undertitel:** Din guide till Arduino och elektronikkretsar  
**Författare:** Erland Lindmark  
**Språk:** Svenska  
**Version:** plan-e-final-rubrikputs  
**Datum:** 2026-07-02

Detta är projektmappen för boken *Arduino i praktiken*. Projektet är strukturerat för att kunna underhållas redaktionellt och exporteras lokalt till EPUB och PDF.

## Projektversion

Denna zip är den rubrikputsade slutversionen efter genomförda `[PLAN]`, `[PLAN2]`, `[PLAN3]`, `[PLAN4]`, `[PLAN5]`, `[ANALYSPLAN]`, `[PLAN-H]`, post-v5-finputs, `[PLAN-E]` och riktad RUBRIKPUTS.

- Projektversion: `arduino-i-praktiken-plan-e-final-rubrikputs.zip`
- Version i metadata: `plan-e-final-rubrikputs`
- Datum: 2026-07-02

Se `docs/final-puts-plan-e-final.md` och `docs/rubrikputs-plan-e-final.md`.


## PLAN-H: redaktionell handbokskonsolidering

`[PLAN-H]` är genomförd. Boken har inte fått en ny komponentkatalog i denna runda, utan har konsoliderats redaktionellt som praktisk handbok och referens.

Genomförda förbättringar:

- interna projektspår har rensats ur läsartexten,
- kravliknande lärandemålsspråk har ersatts med mjukare handboksformuleringar,
- quiz- och kontrollfrågor har omvandlats till checklistor, riskkontroller och praktiska beslutsstöd,
- praktiska moment har rubriksatts som verifieringar, referensmönster, arbetsmönster eller felsökningsmönster,
- kapitelrubriker har normaliserats efter kapiteltyp,
- beslutsstöd, snabbval, riskkontroller, vanliga misstag och korsreferenser har förstärkts,
- slutblocket har gjorts mer verktygsorienterat,
- en intern redaktionell stilguide har skapats för framtida ändringar.


## PLAN4: komplettering av vanliga butikskomponenter

`[PLAN4]` är genomförd. Boken har kompletterats med fler vanliga elektronikbutiksmoduler och Arduino-kit-komponenter.

Genomförda tillägg:

- Kapitel 22: rotary encoder, joystick, keypad, kapacitiv touch och IR-fjärrkontroll som inmatning.
- Kapitel 23: jordfukt, vattennivå, regnsensorer och MQ-gassensorer.
- Kapitel 33: FSR, flexsensorer, vågceller och HX711.
- Kapitel 9 och 38: nRF24L01, 433 MHz RF, RS485, CAN och LoRa.
- Kapitel 20 och 31: PCA9685, ULN2003/28BYJ-48, L298N, A4988 och DRV8825.
- Kapitel 24: IR-fjärrkontroll och IR-mottagarmoduler som optisk inmatning.
- Kapitel 38: uppdaterad samlad snabbguide för de nya komponenterna.
- `docs/lookup-index.md` och `docs/canon-terminology.md`: uppdaterade med de nya komponenterna.

Se `docs/plan4-step-10-handbokstruktur-v3.md`.

## PLAN5: komplettering av kretsar, moduler och induktiva laster

`[PLAN5]` är genomförd. Boken har kompletterats med fler vanliga kretsar, drivmoduler, nivåomvandling, ljudmoduler, optiska moduler, I/O-expansion och induktiva laster.

Genomförda tillägg:

- Kapitel 21: elektromagneter, solenoider och andra spolar som induktiva laster.
- Kapitel 31 och 20: DRV8833 och L9110S som praktiska motor-/drivmoduler.
- Kapitel 33, 4 och 9: LM393/digitala tröskelmoduler och I2C logic level converter.
- Kapitel 27 och 19: KY-037 och LM386.
- Kapitel 24 och 22: APDS-9960/GY-9960 för färg, ljus, närhet och enkla gester.
- Kapitel 30: PCF8575 som 16-bitars I2C-I/O-expander.
- Kapitel 25: analoga Hall-sensorer och 49E-typ.
- Kapitel 38: uppdaterad samlad snabbguide för PLAN5-tilläggen.
- `docs/lookup-index.md`, `docs/canon-terminology.md` och `docs/book-specification.md`: uppdaterade med de nya begreppen.
- `build/book.md`, EPUB och PDF: kontrollerade och uppdaterade i PLAN5 steg 10.

Se `docs/project-version-handbokstruktur-v4.md`.

## Redaktionell målbild

Boken ska fungera som en praktisk Arduino-handbok och referens med tydlig kvalitet, progression och återanvändbara exempel. Den kan läsas från början till slut, men ska också fungera som uppslagsverk för kort, sensorer, komponenter, kretsar, felsökning och praktiska val.

Se `docs/editorial-target.md`, `docs/final-structure-rule.md` och `docs/reference-function-strengthening.md`.

## Genomförda plansteg

| Plan | Status |
|---|---|
| `[PLAN]` | Genomförd |
| `[PLAN2]` | Genomförd |
| `[PLAN3]` | Genomförd |
| `[PLAN4]` | Genomförd |
| `[PLAN5]` | Genomförd |

## Navigering och uppslagsfunktion

- `chapters/00-inledning.md` förklarar hur boken kan användas.
- `chapters/referens-snabbvalsguider-38.md` är den huvudsakliga snabbguiden i boken.
- `docs/lookup-index.md` fungerar som tematiskt redaktörsindex.

## Export

Projektet innehåller lokal exportpipeline:

```bash
python3 scripts/export-book.py validate
python3 scripts/export-book.py markdown
python3 scripts/export-book.py epub
python3 scripts/export-book.py pdf
```

Exportfiler finns i `exports/`.

## Viktiga kataloger

```text
chapters/  Manuskapitel
docs/      Specifikation, status, redaktionella styrdokument och granskningsloggar
build/     Sammanslagen markdown
exports/   Genererade EPUB/PDF-filer
scripts/   Lokal exportpipeline
styles/    EPUB/PDF-stilar
assets/    Omslag och bildresurser
```

## Senaste uppdatering

- `[PLAN4]` steg 10: projektet har versionssatts som `handbokstruktur-v3` och ny bas-zip har skapats.

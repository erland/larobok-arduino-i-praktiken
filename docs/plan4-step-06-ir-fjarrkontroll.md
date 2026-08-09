# [PLAN4] Steg 6: IR-fjärrkontroll

## Syfte

Komplettera boken med tydligare behandling av IR-fjärrkontroll och IR-mottagarmoduler som vanliga Arduino-/elektronikbutikskomponenter.

## Beslut om placering

IR-fjärrkontroll behandlas på två nivåer:

- **Kapitel 22** beskriver IR-fjärr som användargränssnitt och inmatning.
- **Kapitel 24** beskriver IR-mottagaren som optisk mottagarmodul och förklarar varför den skiljer sig från vanlig ljusmätning.

Det gör att läsaren hittar IR-fjärr både när frågan handlar om gränssnitt och när frågan handlar om optiska komponenter.

## Genomförda ändringar

### Kapitel 22

- Den befintliga sektionen om IR-fjärrkontroll kompletterades med hänvisning till kapitel 24.
- `Relaterat` uppdaterades med praktisk koppling till optisk mottagarmodul och alternativa kommunikationsval.

### Kapitel 24

- Snabb orientering och användningspunkter kompletterades med IR-mottagare för fjärrkontroll.
- Ny sektion lades till: `IR-fjärrkontroll och mottagarmoduler`.
- Valguide, snabbreferens, kontrollfrågor och `Relaterat` uppdaterades.

## Redaktionell princip

IR-fjärr ska inte beskrivas som en generell ljussensor. Den ska beskrivas som digital inmatning via modulerad infraröd signal.

## Viktiga varningar

- IR-fjärr kräver ofta fri sikt.
- Olika fjärrkontroller kan använda olika protokoll och knappkoder.
- Okända knappkoder bör ignoreras.
- IR-fjärr bör inte användas för säkerhetskritisk styrning.
- Vid längre räckvidd, kommunikation genom väggar eller dubbelriktad data bör läsaren välja radio, Wi-Fi, BLE eller kabelburen kommunikation.

## Uppdaterade stödfiler

- `docs/lookup-index.md`
- `docs/canon-terminology.md`
- `docs/book-specification.md`
- `docs/project-status.md`
- `docs/exportability-check.md`
- `README.md`
- `build/book.md`

## Status

Steg 6 enligt `[PLAN4]` är genomfört.

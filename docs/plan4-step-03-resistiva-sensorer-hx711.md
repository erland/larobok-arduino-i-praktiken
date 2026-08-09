# [PLAN4] Steg 3: Resistiva sensorer, FSR, flexsensorer, vågceller och HX711

Datum: 2026-07-01

## Syfte

Detta steg kompletterar kapitel 33 med vanliga butikskomponenter som ofta förekommer i Arduino- och makerprojekt men som kräver analog signalanpassning eller särskild mätmodul.

## Uppdaterade områden

- `chapters/analog-signalanpassning-33.md`
- `docs/lookup-index.md`
- `docs/canon-terminology.md`
- `docs/book-specification.md`
- `docs/project-status.md`
- `README.md`
- `build/book.md`
- EPUB/PDF-exporter

## Tillägg i kapitel 33

Följande har lagts till:

- **Resistiva sensorer: FSR, flexsensorer och enkla trycksensorer**
  - varför de ofta kopplas som spänningsdelare
  - hur man väljer fast motstånd
  - varför de ofta ger relativa snarare än exakta värden

- **Vågceller och HX711**
  - varför vågceller inte bör kopplas direkt till Arduino-ADC
  - bryggkoppling och små differenssignaler
  - HX711 som praktisk analog front-end
  - betydelsen av mekanisk montering och kalibrering

## Redaktionellt beslut

Tilläggen placerades i kapitel 33 eftersom de handlar mindre om “en viss sensorfamilj” och mer om hur svaga, resistiva eller differensiella signaler behöver anpassas innan de kan användas tillförlitligt.

## Validering

Efter ändringen byggdes `build/book.md` om och exportvalideringen kördes utan varningar.

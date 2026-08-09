# [PLAN4] Steg 2: Miljö- och kit-sensorer

## Syfte

Komplettera kapitel 23 med vanliga miljö- och kit-sensorer som ofta finns i Arduino-startkit och elektronikbutiker, men som behöver tydliga begränsningar för att inte framstå som exakta mätinstrument.

## Ändrade kapitel

- `chapters/miljosensorer-23.md`

## Tillägg i kapitel 23

Följande områden har lagts till eller förstärkts:

- jordfuktssensorer
- vattennivåsensorer
- regnsensorer
- MQ-gassensorer

## Redaktionell princip

Dessa komponenter behandlas som praktiska indikatorer och experimentmoduler, inte som precisa eller säkerhetskritiska instrument.

Särskilt betonas att:

- resistiva jordfuktsensorer kan korrodera om de står spänningssatta länge,
- kapacitiva jordfuktsensorer ofta är bättre för längre projekt men ändå kräver kalibrering,
- vattennivå- och regnsensorer påverkas av smuts, torktid, placering och ledningsförmåga,
- MQ-gassensorer kräver uppvärmning, drar relativt mycket ström och kan reagera på flera gaser,
- billiga hobbykomponenter inte ska användas som brand-, gas- eller säkerhetslarm.

## Uppdaterade stödfiler

- `docs/lookup-index.md`
- `docs/canon-terminology.md`
- `docs/book-specification.md`
- `docs/project-status.md`
- `README.md`
- `build/book.md`

## Resultat

Kapitel 23 täcker nu bättre de miljö- och kit-sensorer som många läsare sannolikt stöter på i elektronikbutiker, utan att göra boken mindre kritisk eller mindre praktiskt trovärdig.

## Nästa steg enligt [PLAN4]

Steg 3: komplettera kapitel 33 med resistiva sensorer, FSR, flexsensor, vågcell och HX711.

# [PLAN4] Steg 5: Vanliga motor- och drivmoduler

## Syfte

Detta steg kompletterar bokens motor- och drivkapitel med vanliga moduler som ofta förekommer i Arduino-kit, elektronikbutiker och makerprojekt.

## Uppdaterade kapitel

- `chapters/servon-motorer-20.md`
- `chapters/drivkretsar-31.md`

## Tillägg

### Kapitel 20

Kapitel 20 har kompletterats med:

- **PCA9685** för många servon
- **L298N** som vanlig men äldre H-bryggmodul
- **28BYJ-48 + ULN2003** som klassisk kit-stegmotor
- **A4988 och DRV8825** som vanliga STEP/DIR-drivare för bipolära stegmotorer

Tilläggen placerades i kapitel 20 eftersom de hjälper läsaren välja rätt lösning utifrån rörelsetyp: servo, DC-motor eller stegmotor.

### Kapitel 31

Kapitel 31 har kompletterats med samma modulnamn ur drivkretsperspektiv:

- ULN2003/ULN2803 som transistorarrays
- L298N som äldre H-brygga
- A4988/DRV8825 som strömreglerande stegmotordrivare
- PCA9685 som I2C-styrd PWM-/servosignalgenerator

Tilläggen placerades även i kapitel 31 eftersom läsaren där väljer drivkrets, inte bara motortyp.

## Redaktionella principer

Tilläggen ska inte framställa vanliga moduler som automatiskt bästa val. Särskilt:

- L298N beskrivs som vanlig och pedagogiskt användbar, men ofta ineffektiv.
- PCA9685 beskrivs som signaldriver, inte lösning på servomatning.
- A4988/DRV8825 beskrivs som kraftkomponenter som kräver strömbegränsning och kylning.
- ULN2003 + 28BYJ-48 beskrivs som enkel kitlösning för långsam rörelse, inte generell precisionsmotorlösning.

## Uppdaterade stödfiler

- `docs/lookup-index.md`
- `docs/canon-terminology.md`
- `docs/book-specification.md`
- `docs/project-status.md`
- `README.md`
- `build/book.md`
- `exports/arduino-i-praktiken.epub`
- `exports/arduino-i-praktiken.pdf`

## Status

Steg 5 är genomfört och exportvaliderat.

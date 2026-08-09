# [PLAN4] Steg 8: Uppdatera lookup-index och canon

## Syfte

Detta steg säkerställer att komponenterna och modulerna som lades till i `[PLAN4]` steg 1–7 är konsekvent sökbara och redaktionellt dokumenterade.

Fokus ligger på:

- `docs/lookup-index.md`
- `docs/canon-terminology.md`
- `docs/book-specification.md`
- `docs/project-status.md`
- `README.md`

## Genomgång

Följande komponent- och modulgrupper kontrollerades mot uppslagsindex och terminologi/canon:

| Område | Komponenter/moduler | Primär placering |
|---|---|---|
| Användargränssnitt | rotary encoder, joystick, keypad, kapacitiv touch, IR-fjärrkontroll | Kapitel 22 och 24 |
| Miljö- och kit-sensorer | jordfukt, vattennivå, regnsensor, MQ-gassensorer | Kapitel 23 |
| Resistiva sensorer och mätning | FSR, flexsensor, vågcell, HX711 | Kapitel 33 |
| Kommunikation | nRF24L01, 433 MHz RF, RS485, CAN, LoRa | Kapitel 9 och 38 |
| Motor- och drivmoduler | PCA9685, ULN2003/28BYJ-48, L298N, A4988, DRV8825 | Kapitel 20 och 31 |
| Snabbval | alla ovanstående som vanliga färdiga moduler | Kapitel 38 |

## Beslut

- `lookup-index.md` behålls som redaktionellt uppslagsindex på frågenivå, inte som fullständig kopia av kapitel 38.
- `canon-terminology.md` används för stabila begreppsdefinitioner och första kapitel där komponenten/modulen behandlas.
- Kapitel 38 fortsätter vara läsarens primära snabbguide i själva boken.
- Inledningen ska bara beskriva hur uppslagsläsning fungerar, inte lista alla komponenter.

## Kontrollresultat

| Kontroll | Resultat |
|---|---|
| PLAN4-komponenter finns i uppslagsindex | Godkänd |
| PLAN4-komponenter finns i terminologi/canon | Godkänd |
| Primär kapitelplacering är konsekvent | Godkänd |
| Kapitel 38 är fortfarande läsarens huvudsakliga snabbguide | Godkänd |
| Indexet duplicerar inte hela kapitel 38 | Godkänd |

## Samlad bedömning

`[PLAN4]` steg 8 är genomfört. De nya komponenterna är nu konsekvent sökbara via uppslagsindexet, definierade i canon/terminologi och dokumenterade i projektets status och specifikation.

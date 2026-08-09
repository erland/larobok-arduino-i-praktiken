# [PLAN4] Steg 10: Skapa ny projektversion

Datum: 2026-07-01

## Syfte

Steg 10 skapar en ny basversion efter att alla kompletteringar i `[PLAN4]` har genomförts och exportkontrollerats.

## Ny projektversion

```text
arduino-i-praktiken-projekt-handbokstruktur-v3.zip
```

## Versionssättning

Följande metadata har uppdaterats:

- `book.yaml`
- `docs/export-metadata.yaml`

Ny version:

```text
handbokstruktur-v3
```

Datum:

```text
2026-07-01
```

## Ingår i v3

`handbokstruktur-v3` innehåller hela v2-strukturen samt kompletteringarna för vanliga butikskomponenter:

- användargränssnitt och inmatning: rotary encoder, joystick, keypad, kapacitiv touch och IR-fjärr,
- miljö- och kit-sensorer: jordfukt, vattennivå, regn och MQ-gassensorer,
- analog mätning: FSR, flexsensor, vågcell och HX711,
- kommunikation: nRF24L01, 433 MHz RF, RS485, CAN och LoRa,
- motor- och drivmoduler: PCA9685, ULN2003/28BYJ-48, L298N, A4988 och DRV8825,
- uppdaterad samlad snabbguide i kapitel 38,
- uppdaterat `lookup-index` och `canon-terminology`.

## Efterkontroll

Efter versionssättningen kördes projektets exportpipeline på nytt:

```bash
python3 scripts/export-book.py validate
python3 scripts/export-book.py markdown
python3 scripts/export-book.py epub
python3 scripts/export-book.py pdf
```

Resultat: godkänd utan valideringsvarningar.

## Bedömning

`handbokstruktur-v3` är en stabil ny basversion för fortsatt arbete.

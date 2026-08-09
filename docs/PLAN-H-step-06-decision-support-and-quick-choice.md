# PLAN-H steg H6 – Beslutsstöd och snabbval

Datum: 2026-07-01  
Status: Genomförd  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-05.zip`

## Syfte

Steg H6 stärker bokens handboksnytta genom att göra befintliga val- och snabbvalsdelar mer direkt användbara. Målet har inte varit att lägga till nya komponenter, utan att lyfta fram beslut som redan stöds av kapiteltexten.

## Principer

- Inga nya kapitel har skapats.
- Inga tekniska huvudavsnitt har skrivits om i sak.
- Inga nya komponentkategorier har lagts till.
- Beslutsstödet har hållits kort och placerats nära redan befintliga valtabeller, snabbval eller jämförelser.
- Formuleringarna är skrivna som handboksstöd: `Välj ... när ...`, `Börja med ...`, `Snabb beslutsrad`.

## Ändrade kapitel

| Kapitel | Fil | Typ av förstärkning |
|---|---|---|
| 20 | `chapters/servon-motorer-20.md` | Kort beslutsstöd för servo, DC-motor, stegmotor och PCA9685. |
| 21 | `chapters/relaer-mosfetar-laster-21.md` | Snabb beslutsrad för relä, MOSFET, färdig drivmodul och när experiment bör undvikas. |
| 22 | `chapters/displayer-anvandargranssnitt-22.md` | Snabbt displayval för LCD, OLED, TFT, e-paper och seriell logg. |
| 23 | `chapters/miljosensorer-23.md` | Snabbt sensorval för BME/BMP, SHT/AHT, DS18B20, luftkvalitet och jordfukt. |
| 24 | `chapters/ljus-farg-optiska-sensorer-24.md` | Snabbt optiskt val för LDR, luxsensor, färgsensor, optisk brytare och APDS-9960. |
| 25 | `chapters/avstand-narvaro-25.md` | Snabbt närvaroval för ultraljud, ToF, PIR, reed/Hall och ljusbarriär. |
| 28 | `chapters/strom-spanning-energi-28.md` | Snabb beslutsrad för när spänning, ström, effekt över tid, extern modul eller multimeter passar. |
| 30 | `chapters/io-expansion-30.md` | Snabbt expansionsval för 74HC595, 74HC165, MCP23017, PCF8575 och CD74HC4067. |
| 31 | `chapters/drivkretsar-31.md` | Kort beslutsrad för GPIO, MOSFET, DRV8833, L298N och ULN2003/ULN2803. |
| 34 | `chapters/stromforsorjning-batteridrift-34.md` | Snabbt matningsval för USB, separat matning, buck, boost och laboratorieaggregat. |
| 35 | `chapters/felsokning-35.md` | Beslutsstöd för första felsökningsspår: matning/jord, pinout, buss, råvärden eller biblioteksexempel. |
| 38 | `chapters/referens-snabbvalsguider-38.md` | Direktval i praktiken, snabb beslutslinje för drivsteg samt sensorval efter beslutet koden ska kunna ta. |

## Redaktionsbedömning

Steget stärker boken som uppslags- och arbetsbok. I stället för att läsaren bara får tabeller får hen nu korta praktiska valrader som kan användas direkt i ett projekt.

De nya texterna är avsiktligt korta. De ska inte ersätta kapiteltexten, utan fungera som snabb orientering innan läsaren går vidare till detaljerna.

## Kontroll

- `build/book.md` har byggts om.
- Inga H4-rubriker har införts.
- Inga interna projektspår har införts i kapiteltext.
- Nya punktlistor har tomrad före och efter.
- Nya tabeller har inte införts i detta steg.

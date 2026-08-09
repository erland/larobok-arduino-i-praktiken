# [PLAN-H] steg H2 – Ersätt kravliknande lärandemål i Snabb orientering

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-01.zip`  
Status: Genomförd

## Syfte

Steg H2 minskar lärobokskänslan i boken genom att ersätta kravliknande formuleringar som `Efter kapitlet ska du kunna` med mer handboksnära formuleringar.

Målet är inte att ta bort orienteringen i början av kapitlen. Målet är att göra den mindre prestationsinriktad och mer användningsorienterad.

## Principer

- Tekniskt innehåll har inte ändrats.
- Punktlistornas sakliga innehåll har behållits.
- Ersättningarna har varierats mellan kapitel för att undvika mekanisk upprepning.
- Formuleringar har anpassats efter kapiteltyp: orientering, komponent, sensor, robusthet, mätning och systemstöd.
- `build/book.md` har byggts om efter kapiteländringarna.

## Genomförda ändringar

Följande typer av formuleringar har ersatts:

| Före | Efter, princip |
|---|---|
| `Efter kapitlet ska du kunna:` | `Kapitlet hjälper dig att...`, `Kapitlet ger dig stöd för att...`, `Kapitlet fungerar som stöd när du behöver...` |
| `Efter kapitlet ska du framför allt kunna skilja på:` | `Kapitlet hjälper dig framför allt att skilja på:` |
| `Efter experimentet ska du kunna:` | `Experimentet hjälper dig att:` |
| `ska du kunna säga...` | `bör det vara tydligt...` |
| `bör du kunna svara på:` | `kontrollera:` |
| `bör du kunna gå en nivå djupare:` | `är det bra att gå en nivå djupare:` |

## Berörda kapitel

- `chapters/ekosystem-01.md`
- `chapters/utvecklingsmiljo-bibliotek-03.md`
- `chapters/avbrott-watchdog-08.md`
- `chapters/kommunikation-bussar-09.md`
- `chapters/led-rgb-ljuseffekter-17.md`
- `chapters/adresserbara-led-18.md`
- `chapters/buzzers-ljudsignaler-19.md`
- `chapters/relaer-mosfetar-laster-21.md`
- `chapters/displayer-anvandargranssnitt-22.md`
- `chapters/miljosensorer-23.md`
- `chapters/ljus-farg-optiska-sensorer-24.md`
- `chapters/avstand-narvaro-25.md`
- `chapters/rorelse-orientering-26.md`
- `chapters/ljud-mikrofoner-27.md`
- `chapters/strom-spanning-energi-28.md`
- `chapters/position-tid-identitet-29.md`
- `chapters/io-expansion-30.md`
- `chapters/drivkretsar-31.md`
- `chapters/displaykretsar-minne-32.md`
- `chapters/analog-signalanpassning-33.md`
- `chapters/stromforsorjning-batteridrift-34.md`

## Kontroll

Efter ändringen har kapiteltexterna kontrollsökts efter följande kravliknande formuleringar:

- `Efter kapitlet ska`
- `Efter kapitlet bör`
- `ska du kunna`
- `ska läsaren kunna`
- `bör du kunna`

Resultat: inga kvarvarande förekomster i `chapters/`.

## Bedömning

Steg H2 har genomförts med låg risk. Ändringen påverkar främst ton och läsarupplevelse, inte bokens tekniska innehåll.

Boken behåller kapitelorienteringen, men den låter mindre som en kursplan och mer som en praktisk handbok.

# [PLAN-H] steg H5 – Kapiteltypsspecifik rubriknormalisering

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-04.zip`  
Status: Genomfört  
Manusändring: Ja, men endast redaktionell rubriknormalisering. Inga tekniska fakta, kopplingar, kodexempel eller komponentbeskrivningar har ändrats i sak.

## Syfte

Steg H5 genomfördes för att minska känslan av att alla kapitel följer samma yttre mall. Boken ska fortfarande vara konsekvent och lätt att skanna, men olika kapiteltyper behöver olika orienteringsrubriker.

I tidigare version använde nästan alla kapitel rubriken `Snabb orientering`. Den rubriken var inte fel, men den blev mekanisk när den återkom i nästan hela boken. I detta steg har den ersatts med kapiteltypsspecifika rubriker som bättre beskriver kapitlets funktion.

## Genomförd klassificering

| Kapiteltyp | Typiska kapitel | Ny rubrikfamilj |
|---|---|---|
| Orienterings- och beslutskapitel | 1–4 | `Snabb överblick`, `Beslutsöversikt`, `Arbetsmiljö i korthet`, `Begrepp i praktiken` |
| Grundfunktionskapitel | 5–9 | `Grundfunktion i praktiken`, `Mätfunktion i praktiken`, `Tidsstyrning i praktiken`, `Robust körning i praktiken`, `Kommunikationsval i praktiken` |
| Kort- och plattformskapitel | 10–16 | `Kortprofil i korthet` |
| Komponent- och sensorkapitel | 17–20, 22–27, 29–32 | `Komponentöversikt`, `Sensoröversikt`, `Modulöversikt`, `Expansionsöversikt`, `Drivsteg i praktiken` |
| Robusthets- och säkerhetskapitel | 21, 28, 33–35 | `Riskbild och styrprincip`, `Mät- och energibild`, `Signalanpassning i praktiken`, `Matningsöversikt och riskbild`, `Felsökningsöversikt` |
| Metod- och projektkapitel | 36–37 | `Arbetsmönster i korthet`, `Projektöversikt` |
| Referenskapitel | 38 | Befintlig referensstruktur behölls |

## Genomförda ändringar

- `## Snabb orientering` har ersatts i alla kapitel där rubriken fanns.
- Ersättningarna har valts utifrån kapiteltyp, inte genom en enda global sök/ersätt-regel.
- I metodkapitlen har kvarvarande `## Praktiskt arbetspass` ersatts med `## Arbetsmönster`, eftersom det bättre beskriver användningen som handbok.
- `build/book.md` har byggts om efter kapiteländringarna.
- `docs/chapter-templates-by-type.md` har skapats som intern redaktionell referens inför kommande ändringar.

## Berörda kapitel

Följande kapitel har fått rubriknormalisering:

- `chapters/ekosystem-01.md`
- `chapters/valja-ratt-kort-02.md`
- `chapters/utvecklingsmiljo-bibliotek-03.md`
- `chapters/elektriska-grunder-04.md`
- `chapters/digital-io-05.md`
- `chapters/analog-lasning-adc-06.md`
- `chapters/pwm-timers-07.md`
- `chapters/avbrott-watchdog-08.md`
- `chapters/kommunikation-bussar-09.md`
- `chapters/klassiska-arduino-kort-10.md`
- `chapters/kloner-lagkostnadskort-11.md`
- `chapters/moderna-arduino-kort-12.md`
- `chapters/esp8266-nodemcu-13.md`
- `chapters/esp32-familjen-14.md`
- `chapters/raspberry-pi-pico-15.md`
- `chapters/smakort-specialkort-16.md`
- `chapters/led-rgb-ljuseffekter-17.md`
- `chapters/adresserbara-led-18.md`
- `chapters/buzzers-ljudsignaler-19.md`
- `chapters/servon-motorer-20.md`
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
- `chapters/felsokning-35.md`
- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`

## Kontroll

Efter ändringen kontrollerades att:

- `## Snabb orientering` inte längre finns kvar i `chapters/`.
- `## Praktiskt arbetspass` inte längre finns kvar i `chapters/`.
- Inga H4-rubriker (`####`) har införts.
- Kapitelordningen i `build/book.md` följer fortfarande `book.yaml`.
- Ändringen är redaktionell och påverkar inte tekniskt sakmaterial.

## Rekommendation inför nästa steg

Steg H6 bör nu kunna fokusera på att stärka beslutsstöd och snabbval där innehållet redan finns. H5 har gjort rubriklagret mer kapitelanpassat, men har inte lagt till nya beslutsmatriser eller snabbval.

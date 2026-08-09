# [PLAN-H] steg H4 – Omklassificera praktiska sektioner

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-03.zip`  
Status: Genomfört  
Manusändring: Ja, men endast redaktionell rubrik- och sektionsklassificering. Inga tekniska fakta, kopplingar eller komponentbeskrivningar har ändrats i sak.

## Syfte

Steg H4 genomfördes för att minska kurs- och workshopkänslan i boken utan att ta bort den praktiska nyttan. Målet var att rubriker som `Praktiskt test`, `Prova själv` och `Prova vidare` skulle ersättas av handboksnära rubriker som bättre beskriver vad sektionen faktiskt hjälper läsaren med.

## Genomförda ändringar

Följande rubriktyper har omklassificerats:

- `Praktiskt test` har ersatts med mer precisa rubriker som `Referensmönster`, `Verifiera kopplingen`, `Minsta fungerande mätkontroll`, `Porteringstest`, `Riskkontroll`, `Säker koppling`, `Jämförelsemönster`, `Felsökningsmönster`, `Arbetsmall` eller motsvarande.
- `Prova själv` har ersatts med rubriker som `Egen kontroll i praktiken`, `Kortvalschecklista i praktiken`, `Riskkontroll i praktiken`, `Nästa praktiska steg` eller `Egen bussreferens och felsökningsfall`.
- `Prova vidare` har ersatts med rubriker som `Vanliga varianter`, `Nästa praktiska kontroll` eller `Valchecklista för nästa drivlösning`.
- Undersektioner med `### Test N:` har ersatts med `### Kontroll N:` för att minska prov- och kursassociationen.

## Klassificeringsprincip

Rubrikerna har valts utifrån kapiteltyp:

| Kapiteltyp | Typisk ersättning |
|---|---|
| Orienteringskapitel | Kartläggning, beslutsmönster, egen kontroll |
| Grundfunktionskapitel | Referensmönster, verifiering, minsta fungerande kontroll |
| Kort- och plattformskapitel | Kortprofil, porteringstest, praktisk kontroll |
| Komponentkapitel | Referensmönster, verifiera modul, vanliga varianter |
| Robusthets-/säkerhetskapitel | Säker koppling, riskkontroll, felsökningsmönster |
| Metod-/projektkapitel | Kontroll, arbetsmönster, integrationskontroll |
| Referenskapitel | Arbetsmall |

## Berörda kapitel

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
- `chapters/referens-snabbvalsguider-38.md`

## Kontroll

Efter ändringarna har följande kontrollsökningar gjorts i `chapters/`:

- `## Praktiskt test` – inga träffar
- `## Prova själv` – inga träffar
- `## Prova vidare` – inga träffar
- `### Test ` – inga träffar
- H4-rubriker (`####`) – inga träffar

`build/book.md` har byggts om efter kapiteländringarna.

## Redaktionell bedömning

Steg H4 gör att bokens praktiska moment nu framstår mer som handboksverktyg än som skoluppgifter. Innehållet behåller sin praktiska karaktär, men rubrikerna signalerar tydligare vad läsaren får ut av sektionen: verifiering, referensmönster, riskkontroll, felsökning, portering eller beslutsstöd.

Detta förbereder nästa steg, H5, där rubriknormalisering ska göras mer systematiskt utifrån kapiteltyp.

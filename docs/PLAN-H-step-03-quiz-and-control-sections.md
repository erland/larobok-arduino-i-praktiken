# [PLAN-H] steg H3 – Omvandla quiz- och kontrollfrågor

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-02.zip`  
Status: Genomfört

## Syfte

Steg H3 minskar prov- och kurskänslan i boken genom att ersätta återkommande quizrubriker och kontrollrubriker med handboksnära checklistor.

Målet är inte att ändra tekniskt innehåll, utan att ändra läsarens upplevelse från:

> "Har jag lärt mig kapitlet?"

till:

> "Vad bör jag kontrollera, känna igen eller ta ställning till när jag använder detta i ett projekt?"

## Genomförda ändringar

Följande rubriktyper har ersatts i kapiteltexterna:

| Tidigare rubrik | Ny typ av rubrik |
|---|---|
| `Kontrollera att du hänger med` | `Snabb kontroll i praktiken`, `Viktiga samband att känna igen` eller `Arbetskontroll` |
| `Kontrollera ditt val` | `Valchecklista`, `Riskkontroll` eller `Användningschecklista` |
| `Kontrollera arbetssättet` | `Arbetschecklista` |
| `Kontrollfrågor före inkoppling` | `Riskkontroll före inkoppling` |

Numrerade frågelistor i dessa sektioner har också gjorts om till punktlistor och fått en kort inledande användningsrad. Det gör dem mer lika checklistor än quiz.

## Principer som användes

- Begrepps- och teorikapitel fick mjukare rubriker som `Viktiga samband att känna igen` eller `Snabb kontroll i praktiken`.
- Kort- och komponentkapitel fick oftast `Valchecklista`.
- Kapitel om laster, mätning och strömförsörjning fick `Riskkontroll`.
- Felsöknings- och projektkapitel fick `Arbetschecklista`.
- Referenskapitlet fick `Användningschecklista`.
- Tekniska fakta och kapitelinnehåll har inte ändrats i sak.

## Berörda kapitel

- `chapters/ekosystem-01.md`
- `chapters/valja-ratt-kort-02.md`
- `chapters/utvecklingsmiljo-bibliotek-03.md`
- `chapters/elektriska-grunder-04.md`
- `chapters/digital-io-05.md`
- `chapters/analog-lasning-adc-06.md`
- `chapters/pwm-timers-07.md`
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
- `chapters/ljud-mikrofoner-27.md`
- `chapters/strom-spanning-energi-28.md`
- `chapters/position-tid-identitet-29.md`
- `chapters/io-expansion-30.md`
- `chapters/displaykretsar-minne-32.md`
- `chapters/analog-signalanpassning-33.md`
- `chapters/stromforsorjning-batteridrift-34.md`
- `chapters/felsokning-35.md`
- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`
- `chapters/referens-snabbvalsguider-38.md`

## Kontroll

Efter ändringarna gjordes kontrollsökning i `chapters/`.

Följande rubriker finns inte längre kvar:

- `## Kontrollera att du hänger med`
- `## Kontrollera ditt val`
- `## Kontrollera arbetssättet`
- `### Kontrollfrågor före inkoppling`

`build/book.md` har byggts om efter kapiteländringarna.

## Kommentar inför nästa steg

Steg H3 ändrar framför allt quiz- och kontrollramen. En del praktiska sektioner har fortfarande rubriker som `Praktiskt test`, `Prova själv` och `Prova vidare`. Dessa hanteras i steg H4.

# [PLAN3] Steg 1: Granskning av `Förutsättningar`

## Syfte

Det här steget minskar känslan av mekanisk kapitelmall genom att granska alla förekomster av `Förutsättningar`.

Målet är inte att ta bort praktiskt viktiga förkunskaper. Målet är att behålla sektionen där den hjälper läsaren, men ta bort eller omformulera den när den bara fungerar som en kvarvarande mallrubrik.

## Genomförda beslut

| Kapitelgrupp | Beslut |
|---|---|
| Kapitel 1–3 | `Förutsättningar` togs bort eftersom innehållet främst var orienterande och redan täcks av `Snabb orientering`. |
| Kapitel 4 | `Förutsättningar` behölls men kortades eftersom kapitlet behöver markera lågspänningsfokus och praktisk mätberedskap. |
| Kapitel 10–16 | `Förutsättningar` ersattes med `Bedöm kortet med detta i åtanke`, eftersom plattformskapitlen fungerar bättre som valguider än som beroende kurskapitel. |
| Kapitel 5–9 | `Förutsättningar` behölls eftersom grundfunktionerna bygger på konkreta tekniska begrepp. |
| Kapitel 17–34 | `Förutsättningar` behölls där de stödjer koppling, ström, signaler, bibliotek och felsökning. Ett fåtal längre avsnitt kortades. |
| Kapitel 35–37 | `Förutsättningar` behölls där de beskriver vilka tidigare byggblock som används i arbetsflöde och projekt. Ett par längre avsnitt kortades. |
| Kapitel 38 | Ingen ändring behövdes. |

## Filer med direkta manusändringar

- `chapters/ekosystem-01.md`
- `chapters/valja-ratt-kort-02.md`
- `chapters/utvecklingsmiljo-bibliotek-03.md`
- `chapters/elektriska-grunder-04.md`
- `chapters/klassiska-arduino-kort-10.md`
- `chapters/kloner-lagkostnadskort-11.md`
- `chapters/moderna-arduino-kort-12.md`
- `chapters/esp8266-nodemcu-13.md`
- `chapters/esp32-familjen-14.md`
- `chapters/raspberry-pi-pico-15.md`
- `chapters/smakort-specialkort-16.md`
- `chapters/analog-signalanpassning-33.md`
- `chapters/io-expansion-30.md`
- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`

## Resultat

Före granskningen fanns `Förutsättningar` i nästan alla kapitel. Efter granskningen är sektionen borttagen eller omformulerad där den främst signalerade kursboksmässig progression.

Aktuellt resultat:

- `Förutsättningar` finns kvar i 27 kapitel.
- Plattformskapitlen 10–16 använder i stället `Bedöm kortet med detta i åtanke`.
- De kvarvarande `Förutsättningar`-sektionerna är i huvudsak tekniskt motiverade.

## Redaktionell regel framåt

`Förutsättningar` ska inte användas som obligatorisk kapitelrubrik.

Använd den bara när läsaren verkligen behöver känna igen tidigare begrepp, praktiska verktyg, säkerhetsgränser eller elektriska samband innan kapitlet blir meningsfullt.

I valguidekapitel ska rubriker som `Bedöm ... med detta i åtanke` föredras framför `Förutsättningar`.

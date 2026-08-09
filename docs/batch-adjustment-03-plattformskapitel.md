# [PLAN] Batchjustering 3: kort- och plattformskapitel

## Omfattning

Plansteg 7, batch 3 omfattar kapitel 10–16:

| Kapitel | Fil | Status |
|---:|---|---|
| 10 | `chapters/klassiska-arduino-kort-10.md` | Batchjusterat |
| 11 | `chapters/kloner-lagkostnadskort-11.md` | Batchjusterat |
| 12 | `chapters/moderna-arduino-kort-12.md` | Batchjusterat |
| 13 | `chapters/esp8266-nodemcu-13.md` | Harmoniserat |
| 14 | `chapters/esp32-familjen-14.md` | Batchjusterat |
| 15 | `chapters/raspberry-pi-pico-15.md` | Batchjusterat |
| 16 | `chapters/smakort-specialkort-16.md` | Batchjusterat |

## Syfte

Batchen gör kort- och plattformskapitlen mer användbara som handbok och valguide. Läsaren ska snabbt kunna avgöra när en kortfamilj passar, när ett annat kort är bättre och vilka elektriska, praktiska och verktygsmässiga begränsningar som spelar roll.

## Genomförda strukturändringar

| Tidigare rubrik | Ny hantering |
|---|---|
| `Varför detta kapitel finns` | `Snabb orientering` |
| `Lärandemål` | `Det du kan använda kapitlet till` |
| `Innan vi börjar` | `Förutsättningar` |
| `Praktiskt experiment` | `Praktiskt test` |
| `Övningar` | `Prova vidare` |
| `Quiz/reflektionsfrågor` | `Kontrollera ditt val` |
| `Referenssammanfattning` | `Snabbreferens` |
| `Referensruta: snabbval` | `Snabbval` |
| `Nästa steg` | `Se också` |

## Redaktörsnoteringar

- Kapitel 13 var redan pilotjusterat och har därför harmoniserats snarare än skrivits om från grunden.
- Kapitel 10 och 15 hade både tabellbaserad referens och sammanfattning. Dessa har separerats som `Snabbreferens` och `Sammanfattande valbild` för att undvika dubbla identiska rubriker.
- Plattformskapitlen behåller sitt tekniska djup men får tydligare handboksmarkörer: snabb orientering, valguide, snabbreferens, snabbval och korsreferenser.

## Kontroll

Efter batchen kontrollerades att kapitel 10–16 inte längre använder de gamla kursrubrikerna som standardrubriker:

- `Varför detta kapitel finns`
- `Lärandemål`
- `Innan vi börjar`
- `Quiz/reflektionsfrågor`
- `Nästa steg`

`build/book.md` har byggts om från kapitelordningen i `book.yaml`.

# [PLAN] Batchjustering 5: sensor- och mätkapitel

Status: Genomfört 2026-06-30.

## Omfattning

Batch 5 omfattar kapitel 23–29:

| Kapitel | Fil | Kapiteltyp |
|---:|---|---|
| 23 | `chapters/miljosensorer-23.md` | Sensor- och mätkapitel |
| 24 | `chapters/ljus-farg-optiska-sensorer-24.md` | Sensor- och mätkapitel |
| 25 | `chapters/avstand-narvaro-25.md` | Sensor- och mätkapitel |
| 26 | `chapters/rorelse-orientering-26.md` | Sensor- och mätkapitel |
| 27 | `chapters/ljud-mikrofoner-27.md` | Sensor- och mätkapitel |
| 28 | `chapters/strom-spanning-energi-28.md` | Sensor- och mätkapitel |
| 29 | `chapters/position-tid-identitet-29.md` | Sensor- och mätkapitel |

## Redaktionell princip

Sensor- och mätkapitlen ska fungera som praktiska uppslagskapitel. Läsaren ska snabbt kunna förstå:

- vad sensortypen mäter,
- när den passar,
- vilka varianter som finns,
- hur den kopplas och läses,
- vilka elektriska krav som är viktiga,
- hur mätvärden filtreras eller tolkas,
- hur vanliga fel felsöks,
- vilka alternativ som bör övervägas.

## Genomförda strukturändringar

| Tidigare rubrik | Ny hantering |
|---|---|
| `Varför detta kapitel finns` | `Snabb orientering` |
| `Lärandemål` | `Det du kan använda kapitlet till` |
| `Innan vi börjar` | `Förutsättningar` |
| `Experiment` / `Praktiskt experiment` | `Praktiskt test` |
| `Experimentvariant` | `Testvariant` |
| `Övningar` | `Prova vidare` |
| `Övning N` | `Test N` |
| `Quiz/reflektionsfrågor` | `Kontrollera ditt val` |
| `Quiz och reflektionsfrågor` | `Kontrollera ditt val` |
| `Referenssammanfattning` | `Snabbreferens` |
| `Referensruta: snabbval` | `Snabbval` |
| `Snabb sammanfattning` | `Snabb överblick` |
| `Nästa steg` | `Se också` |

## Bedömning

Batchen gör sensor- och mätkapitlen mer handboksnära utan att ta bort deras förklarande värde. Kapitlen behåller praktiska exempel och kodmönster, men framstår mindre som kurslektioner och mer som stöd för läsare som vill välja, koppla, jämföra och felsöka sensorer.

## Kontroll

Efter batchen kontrollerades att de gamla kursrubrikerna inte längre förekommer som H2-rubriker i kapitel 23–29.

`build/book.md` har uppdaterats efter ändringarna.

## Nästa rekommenderade steg

Fortsätt med [PLAN] steg 7, batch 6: robusthets- och kretskapitel, kapitel 30–34.

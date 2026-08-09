# [PLAN] Pilotjustering av kapitelstruktur

Datum: 2026-06-30  
Plansteg: 4. Gör en pilotjustering på 3–5 kapitel  
Status: Genomförd som första manuspilot.

## Syfte

Detta dokument sammanfattar den första pilotjusteringen av kapitel enligt den redaktionella målbilden, kapiteltypologin och kapitelmallarna.

Målet med piloten är att testa om boken blir mer handboksnära och uppslagsverksvänlig utan att förlora pedagogisk tydlighet.

## Pilotkapitel

| Kapitel | Fil | Kapiteltyp | Justeringsfokus |
|---:|---|---|---|
| 2 | `chapters/valja-ratt-kort-02.md` | Orienteringskapitel | Ersatte formell kursinledning med snabb orientering och praktiska förutsättningar. |
| 8 | `chapters/avbrott-watchdog-08.md` | Grundfunktionskapitel | Gjorde inledningen mer problem- och användningsnära. |
| 13 | `chapters/esp8266-nodemcu-13.md` | Kort- och plattformskapitel | Tydliggjorde när ESP8266 passar, när det bör väljas bort och vilka fällor som är viktigast. |
| 20 | `chapters/servon-motorer-20.md` | Komponent- och aktuator-kapitel | Gjorde kapitlet mer praktiskt orienterat kring val, matning, styrning och felsökning. |
| 38 | `chapters/referens-snabbvalsguider-38.md` | Referenskapitel | Gjorde kapitlet tydligt till referens snarare än lektion. |

## Genomförda strukturändringar

I pilotkapitlen har följande principer testats:

- `Varför detta kapitel finns`, `Lärandemål` och `Innan vi börjar` har ersatts av `Snabb orientering` och, där det behövs, `Förutsättningar`.
- I referenskapitlet har de formella inledande rubrikerna ersatts av `Så använder du referensen`.
- `Övningar` har bytts till mer praktiska rubriker som `Prova själv`, `Praktiskt test` eller `Bygg din egen snabbguide`.
- `Quiz/reflektionsfrågor` har bytts till `Kontrollera ditt val` där frågorna fortfarande fungerar som självkontroll.
- `Nästa steg` har bytts till `Se också`.

## Redaktionell bedömning

Piloten visar en rekommenderad riktning för resten av boken:

1. Grund- och orienteringskapitel kan fortfarande ha en tydlig pedagogisk progression, men bör börja med praktisk nytta i stället för kursmål.
2. Kort-, komponent- och sensorkapitel bör hjälpa läsaren att snabbt avgöra om tekniken passar projektet.
3. Referenskapitlet bör inte låtsas vara ett vanligt kapitel. Det ska vara snabb åtkomst till beslutstabeller och felsökningsstöd.
4. Fristående läsning bör prioriteras. En läsare som hoppar direkt till ett kapitel ska snabbt förstå sammanhang, förutsättningar och risker.

## Rekommenderad utvärdering

Nästa plansteg bör vara att granska pilotkapitlen i faktisk läsning:

- Känns inledningen mindre skolaktig?
- Går det snabbare att förstå vad kapitlet hjälper läsaren med?
- Är `Förutsättningar` lagom kort?
- Är `Prova själv` och `Praktiskt test` bättre än `Övningar`?
- Bör `Kontrollera ditt val` behållas, kortas eller tas bort i fler kapitel?
- Är `Se också` mer användbart än `Nästa steg`?

## Rekommendation inför nästa steg

Gör inte batchjustering av alla kapitel förrän pilotkapitlen har godkänts. Använd dem som stilprov för att avgöra hur hårt resten av boken ska styras mot handbok/referens.

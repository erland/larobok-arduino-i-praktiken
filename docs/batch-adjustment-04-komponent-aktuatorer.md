# [PLAN] Batchjustering 4: komponent- och aktuator-kapitel

## Omfattning

Detta dokument sammanfattar [PLAN] steg 7, batch 4: justering av kapitel 17–22.

Batchen omfattar:

| Kapitel | Fil | Kapiteltyp | Status |
|---:|---|---|---|
| 17 | `chapters/led-rgb-ljuseffekter-17.md` | Komponent-/aktuator-kapitel | Batchjusterat |
| 18 | `chapters/adresserbara-led-18.md` | Komponent-/aktuator-kapitel | Batchjusterat |
| 19 | `chapters/buzzers-ljudsignaler-19.md` | Komponent-/aktuator-kapitel | Batchjusterat |
| 20 | `chapters/servon-motorer-20.md` | Komponent-/aktuator-kapitel | Harmoniserat efter tidigare pilotjustering |
| 21 | `chapters/relaer-mosfetar-laster-21.md` | Komponent-/aktuator-kapitel | Batchjusterat |
| 22 | `chapters/displayer-anvandargranssnitt-22.md` | Komponent-/aktuator-kapitel | Batchjusterat |

## Redaktionell riktning

Komponent- och aktuator-kapitlen ska fungera som praktiska handbokskapitel. Läsaren ska snabbt kunna förstå:

- när komponenten eller aktuatorn är relevant,
- vilka elektriska krav och begränsningar som finns,
- hur den kopplas och styrs,
- vilka bibliotek eller kodmönster som behövs,
- vanliga misstag och felsökningsvägar,
- hur kapitlet kopplar till andra delar av boken.

## Genomförda strukturändringar

| Tidigare rubriktyp | Ny rubriktyp |
|---|---|
| `Varför detta kapitel finns` | `Snabb orientering` |
| `Lärandemål` | `Det du kan använda kapitlet till` |
| `Innan vi börjar` | `Förutsättningar` |
| `Praktiskt experiment` / `Experiment` | `Praktiskt test` |
| `Övningar` | `Praktiskt test` |
| `Övning N` | `Test N` |
| `Quiz/reflektionsfrågor` / `Quiz och reflektionsfrågor` | `Kontrollera ditt val` |
| `Referenssammanfattning` | `Snabbreferens` |
| `Referensruta: snabbval` | `Snabbval` |
| `Nästa steg` | `Se också` |

## Bedömning

Batchen följer den slutliga strukturregeln i `docs/final-structure-rule.md`.

Resultatet gör kapitel 17–22 mer handboksnära utan att ta bort den pedagogiska förklaringen. Fokus har flyttats från kursmarkörer till praktisk nytta, felsökning, valhjälp och återanvändbara tester.

## Kontroll

Efter batchjusteringen har följande kontrollerats:

- de gamla kursrubrikerna finns inte kvar som H2-rubriker i kapitel 17–22,
- H4-rubriker har inte införts,
- befintliga kodblock har bevarats,
- `build/book.md` har byggts om från kapitelordningen,
- projektstatus och README har uppdaterats.

## Nästa rekommenderade steg

Fortsätt med [PLAN] steg 7, batch 5: sensor- och mätkapitlen 23–29.

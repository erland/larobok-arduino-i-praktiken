# [PLAN] 8. Normalisering av återkommande sektioner

Datum: 2026-06-30

## Syfte

Detta steg kontrollerar och normaliserar återkommande kapitelrubriker efter att batchjusteringarna i steg 7 har genomförts.

Målet är att boken konsekvent ska kännas som en praktisk Arduino-handbok med lärobokskvalitet, inte som en traditionell kursbok med samma pedagogiska markörer i varje kapitel.

## Normaliseringsregel

Följande princip gäller efter detta steg:

| Tidigare sektion | Normaliserad hantering |
|---|---|
| `Varför detta kapitel finns` | Ersätts av `Snabb orientering` eller bakas in i inledningen. |
| `Lärandemål` | Ersätts av `Det du kan använda kapitlet till` eller integreras i praktisk orientering. |
| `Innan vi börjar` | Ersätts av `Förutsättningar` endast där det behövs. |
| `Övningar` | Ersätts av `Praktiskt test`, `Prova själv`, `Prova vidare` eller `Praktiskt arbetspass`. |
| `Quiz/reflektionsfrågor` | Ersätts av `Kontrollera att du hänger med`, `Kontrollera ditt val` eller tas bort när det inte tillför värde. |
| `Nästa steg` | Ersätts av `Se också`, eller i inledningen av en mer naturlig läsanvisning. |
| `Praktiskt experiment` | Ersätts av `Praktiskt test`. |
| `Referenssammanfattning` och äldre referensrubriker | Ersätts av `Snabbreferens` eller `Snabbval`. |

## Genomförd kontroll

Efter batchjustering 1–7 fanns de flesta normaliseringar redan på plats. Detta steg gjorde en slutlig sökning i kapitelmanus efter kvarvarande rubriker från den gamla strukturen.

Följande kvarvarande avvikelser hittades och korrigerades:

| Fil | Korrigering |
|---|---|
| `chapters/00-inledning.md` | `Nästa steg` ändrades till `Börja här`. Texten om kapitelmönster ändrades från experiment/referenssammanfattning till praktiskt test/snabbreferens/korsreferenser. |
| `chapters/valja-ratt-kort-02.md` | `Praktiskt experiment: välj kort för tre projekt` ändrades till `Praktiskt test: välj kort för tre projekt`. |
| `chapters/utvecklingsmiljo-bibliotek-03.md` | `Referensruta` ändrades till `Snabbreferens`. |

## Saker som medvetet inte ändrades

Rubriken `Snabb sammanfattning` finns kvar i de kapitel där den fungerar som faktisk repetition och inte konkurrerar med en tydlig `Snabbreferens`. Den ska inte användas som obligatoriskt slutblock i framtida kapitel, men behöver inte tas bort där den hjälper läsaren.

Rubriker som innehåller ordet `Varför` i vanlig saklig mening, till exempel `Varför LED behöver strömbegränsning`, är inte gamla kursrubriker och ska därför behållas.

## Kontrollresultat

Efter normaliseringen hittades inga kvarvarande H2/H3-rubriker i kapitelmanus med följande gamla standardrubriker:

- `Varför detta kapitel finns`
- `Lärandemål`
- `Innan vi börjar`
- `Nästa steg`
- `Övningar`
- `Quiz/reflektionsfrågor`
- `Praktiskt experiment`
- `Referenssammanfattning`
- `Referensruta`

## Rekommendation för fortsatt arbete

Gå vidare till `[PLAN] 9. Stärk uppslagsverksfunktionen`.

Där bör fokus ligga på att förstärka:

- snabbval,
- valguider,
- felsökning,
- snabbreferenser,
- säkerhetsrutor,
- elektriska krav,
- korsreferenser mellan relaterade kapitel.

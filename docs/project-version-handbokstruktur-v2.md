# Projektversion: handbokstruktur-v2

Datum: 2026-07-01

## Syfte

Denna version är den nya basversionen efter att `[PLAN]`, `[PLAN2]` och `[PLAN3]` har genomförts.

Versionen markerar att boken har gått från en mer traditionell kapitelstruktur till en mer redaktionellt mogen praktisk handbok och uppslagsvänlig Arduino-referens.

## Genomförda arbetslinjer

| Plan | Status | Huvudresultat |
|---|---|---|
| `[PLAN]` | Genomförd | Boken fick redaktionell målbild, kapiteltypologi, kapitelmallar, batchjusterade kapitel, uppslagsverksfunktion, progressionskontroll och exportkontroll. |
| `[PLAN2]` | Genomförd | Mekaniska `Se också`-sektioner togs bort eller ersattes med selektiva, problemorienterade `Relaterat`-sektioner. |
| `[PLAN3]` | Genomförd | Finputsning av `Förutsättningar`, `Det du kan använda kapitlet till`, `Snabb sammanfattning`/`Snabbreferens`, `Relaterat`, navigering och exportbarhet. |

## Redaktionell status

Boken ska nu hanteras som:

> en praktisk Arduino-handbok med lärobokskvalitet, avsedd att fungera både för sammanhängande läsning och som uppslagsverk.

## Viktiga egenskaper i v2

- Inga obligatoriska `Se också`-sektioner.
- `Relaterat` används selektivt och problemorienterat.
- Kapiteltypsanpassade rubriker används i stället för en enhetlig kursmall.
- Kapitel 38 fungerar som huvudsaklig snabbguide i själva boken.
- `docs/lookup-index.md` fungerar som tematiskt redaktörsindex.
- Markdown- och exportkontroll har genomförts utan valideringsvarningar.

## Rekommenderad fil

```text
arduino-i-praktiken-projekt-handbokstruktur-v2.zip
```

## Nästa möjliga arbetssteg

Efter denna version bör arbetet främst handla om:

- språkgranskning,
- teknisk faktakontroll,
- eventuell uppdatering av kodexempel,
- slutlig exportgranskning av EPUB/PDF,
- omslags- eller metadatajusteringar inför publicering.

# [PLAN2] Batch 6: robusthets- och kretskapitel

Datum: 2026-07-01  
Omfattning: kapitel 30–34  
Status: Genomförd.

## Syfte

Batch 6 granskar `Se också` och andra korsreferenser i robusthets- och kretskapitlen.

Målet är att ta bort linjära övergångar till nästa kapitel och bara behålla hänvisningar som hjälper läsaren med:

- robusthet,
- elektriska risker,
- felsökning,
- strömförsörjning,
- signalproblem,
- konkreta kretsval.

## Beslut per kapitel

| Kapitel | Fil | Beslut |
|---:|---|---|
| 30 | `chapters/io-expansion-30.md` | `Korsreferens` gjordes om till `Relaterat` med fokus på I2C/SPI och digitala signaler. Linjärt `Se också` togs bort. |
| 31 | `chapters/drivkretsar-31.md` | `Korsreferens` gjordes om till `Relaterat` med fokus på motorer, MOSFET:ar, reläer och strömförsörjning. Linjärt `Se också` togs bort. |
| 32 | `chapters/displaykretsar-minne-32.md` | `Korsreferens` gjordes om till `Relaterat` med fokus på I2C/SPI och datalagring i större projekt. Linjärt `Se också` togs bort. |
| 33 | `chapters/analog-signalanpassning-33.md` | `Korsreferens` gjordes om till `Relaterat` med fokus på ADC, mätning, matningsbrus och jordning. Linjärt `Se också` togs bort. |
| 34 | `chapters/stromforsorjning-batteridrift-34.md` | `Se också` ersattes med `Relaterat` eftersom kopplingen till felsökning, laster och analoga störningar är praktiskt motiverad. |

## Redaktionell bedömning

Batch 6 bör inte ta bort alla korsreferenser. Robusthetskapitlen behandlar praktiska felkedjor där ämnena faktiskt hänger ihop: kommunikation, drivning, signalanpassning, laster, jordning och strömförsörjning.

Däremot ska de inte avslutas med framåtdrivande kapitelövergångar. Därför har `Se också` tagits bort som linjär slutsektion och ersatts av selektiva `Relaterat`-sektioner där kopplingen ger praktisk nytta.

## Kontroll

Efter batchen gäller:

- inga `Se också`-rubriker finns kvar i kapitel 30–34,
- inga `Korsreferens`-rubriker finns kvar i kapitel 30–34,
- kvarvarande hänvisningar ligger under `Relaterat`,
- hänvisningarna är problemorienterade snarare än sekventiella,
- `build/book.md` är uppdaterad,
- projektets markdownvalidering är körd utan varningar.

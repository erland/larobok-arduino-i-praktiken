# [PLAN2] Batch 1: Inledning och orienteringskapitel

Datum: 2026-07-01  
Status: Genomförd

## Omfattning

Batchen omfattar:

- `chapters/00-inledning.md`
- `chapters/ekosystem-01.md`
- `chapters/valja-ratt-kort-02.md`
- `chapters/utvecklingsmiljo-bibliotek-03.md`
- `chapters/elektriska-grunder-04.md`

## Bedömningsprincip

Varje `Se också` eller motsvarande korsreferens har bedömts utifrån tre frågor:

1. Hjälper hänvisningen läsaren att lösa ett konkret problem?
2. Pekar den på ett faktiskt tekniskt beroende eller ett närliggande val?
3. Tillför den något utöver nästa kapitels `Snabb orientering`?

Om svaret huvudsakligen var nej togs hänvisningen bort.

## Beslut per fil

| Fil | Beslut | Motivering |
|---|---|---|
| `00-inledning.md` | Justerad | `Börja här` ersattes med `Välj din väg`, så inledningen stödjer både linjär läsning och uppslagsläsning. |
| `ekosystem-01.md` | `Se också` borttaget | Avsnittet beskrev i praktiken nästa kapitel och tillförde inte en konkret uppslagsnytta. |
| `valja-ratt-kort-02.md` | `Se också` borttaget | Hänvisningen var en framåtdrivande kursövergång snarare än en nödvändig korsreferens. |
| `utvecklingsmiljo-bibliotek-03.md` | `Se också` borttaget | Texten upprepade nästa kapitels funktion och var inte nödvändig för uppslagsläsning. |
| `elektriska-grunder-04.md` | `Se också` borttaget | Övergången till digital I/O var pedagogiskt rimlig men inte nödvändig som stående slutsektion. |

## Resultat

Batch 1 stärker bokens uppslagsverkskaraktär genom att ta bort linjära slutövergångar i orienteringskapitlen.

Boken går fortfarande att läsa från början, men kapitel 1–4 känns mindre som en kurssekvens och mer som fristående orienteringskapitel.

## Rekommendation inför batch 2

I kapitel 5–9 bör vi vara mer selektiva än i batch 1. Grundfunktionskapitlen kan ibland behöva `Relaterat`, särskilt när ett begrepp är ett faktiskt beroende för senare kapitel, till exempel:

- digital I/O och knappar,
- ADC och sensorvärden,
- PWM och motor-/LED-styrning,
- avbrott och robusthet,
- I2C/SPI/UART och sensorer/displayer.

Men hänvisningar som bara säger “nästa kapitel handlar om...” bör tas bort.

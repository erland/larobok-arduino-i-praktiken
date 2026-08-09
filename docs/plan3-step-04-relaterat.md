# [PLAN3] Steg 4: Kvalitetsgranska `Relaterat`

Datum: 2026-07-01  
Status: Genomfört  
Utgångspunkt: `arduino-i-praktiken-projekt-plan3-steg-03-sammanfattning-snabbreferens.zip`

## Syfte

Detta steg granskar alla kvarvarande `Relaterat`-sektioner så att de inte blir en ny mekanisk slutsektion efter att `Se också` togs bort i `[PLAN2]`.

Målet är att varje hänvisning ska hjälpa läsaren att lösa ett konkret problem, göra ett bättre teknikval eller felsöka ett faktiskt samband mellan kapitel.

## Redaktionsregel efter granskningen

`Relaterat` får finnas kvar när det gör minst en av följande saker:

- pekar på ett tekniskt beroende, till exempel PWM, ADC, I2C, SPI, jordning eller strömbudget,
- hjälper läsaren felsöka ett vanligt problem,
- visar vart läsaren ska gå när ett praktiskt val behöver fördjupas,
- förklarar varför ett annat kapitel är relevant i situationen.

`Relaterat` ska inte användas för att bara lista närliggande eller efterföljande kapitel.

## Genomförda ändringar

Alla 24 kvarvarande `Relaterat`-sektioner har granskats och skrivits om till mer problemorienterade formuleringar.

| Kapitel | Beslut |
|---:|---|
| 5 | Behölls och skärptes mot snabba digitala händelser, bussmoduler och laster. |
| 6 | Behölls och skärptes mot sensormätning, energimätning och signalanpassning. |
| 7 | Behölls och skärptes mot LED, ljud, motorer, avbrott och watchdog. |
| 8 | Behölls och skärptes mot digitala händelser, icke-blockerande tid och felsökning. |
| 9 | Behölls och skärptes mot bussproblem, delade moduler och brus. |
| 17 | Behölls och skärptes mot PWM, laststyrning och strömbudget. |
| 18 | Behölls och skärptes mot icke-blockerande effekter, laststyrning och separat matning. |
| 19 | Behölls och skärptes mot timing, drivsteg och matningsproblem. |
| 20 | Behölls och skärptes mot styrsignal, drivning och separat matning. |
| 21 | Behölls och skärptes mot gemensam jord, induktiva laster och verklig strömförsörjning. |
| 22 | Behölls och skärptes mot displaykommunikation, större displayer och felsökning. |
| 23 | Behölls och skärptes mot I2C-felsökning, långa mätningar och sammansatta projekt. |
| 24 | Behölls och skärptes mot kalibrering, I2C/SPI och praktiska mätfel. |
| 25 | Behölls och skärptes mot digitala signaler, analog tröskling och seriella sensormoduler. |
| 26 | Behölls och skärptes mot avbrott, I2C/SPI och rörelsefel i integrerade projekt. |
| 27 | Behölls och skärptes mot analog ljudmätning, sampling och signalanpassning. |
| 28 | Behölls och skärptes mot ADC, signalanpassning och strömbudget/felsökning. |
| 29 | Behölls och skärptes mot kommunikation, loggning och praktiska tids-/ID-fel. |
| 30 | Behölls och skärptes mot bussadresser, digital I/O och systemfelsökning. |
| 31 | Behölls och skärptes mot motorer, induktiva laster och strömproblem. |
| 32 | Behölls och skärptes mot bussproblem, längre körning och större projekt. |
| 33 | Behölls och skärptes mot ADC, elektrisk mätning och matningsbrus. |
| 34 | Behölls och skärptes mot separat drivning, analog störning och systeminstabilitet. |
| 37 | Behölls och skärptes mot kortval, bussdelning, modulbyte och robust felsökning. |

## Resultat

- Inga `## Se också`-rubriker har återinförts.
- `Relaterat` finns kvar i 24 kapitel, men formuleringarna är nu mer problemorienterade.
- Inga `Relaterat`-sektioner används som rena linjära övergångar till nästa kapitel.
- Kapitel 38 och `docs/lookup-index.md` fortsätter bära den breda navigeringen.
- `build/book.md` är uppdaterad.
- Exportvalideringen är körd utan varningar.

## Nästa rekommenderade steg

Gå vidare till `[PLAN3]` steg 5: kontrollera inledning, kapitel 38 och lookup-index tillsammans.

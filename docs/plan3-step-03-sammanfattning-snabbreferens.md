# [PLAN3] Steg 3: Snabb sammanfattning och Snabbreferens

Datum: 2026-07-01  
Plansteg: 3. Slå ihop överlapp mellan `Snabb sammanfattning` och `Snabbreferens`  
Status: Genomfört.

## Syfte

Målet med detta steg var att undvika dubbla avslut i kapitel som både hade `Snabb sammanfattning` och `Snabbreferens`.

I en praktisk handbok bör avslutet inte kännas som en återkommande skolboksmall. Kapitel som är uppslagsnära bör i första hand avslutas med en användbar referens, medan mer förklarande kapitel kan behålla en sammanfattning.

## Beslutsregel

- `Snabb sammanfattning` används när kapitlet främst är förklarande eller undervisande.
- `Snabbreferens` används när kapitlet främst ska kunna användas som uppslag.
- Båda rubrikerna ska inte användas i samma kapitel om de överlappar.
- Om båda fanns och `Snabbreferens` redan gav konkret praktisk nytta togs `Snabb sammanfattning` bort.

## Kapitel som justerades

Följande kapitel hade både `Snabb sammanfattning` och `Snabbreferens`. I dessa kapitel togs `Snabb sammanfattning` bort och `Snabbreferens` behölls:

| Kapitel | Fil | Beslut |
|---:|---|---|
| 3 | `utvecklingsmiljo-bibliotek-03.md` | Behöll `Snabbreferens` eftersom kapitlet fungerar bättre som verktygs- och arbetsflödesreferens. |
| 5 | `digital-io-05.md` | Behöll `Snabbreferens` eftersom tabellen ger bättre praktiskt stöd än en punktvis sammanfattning. |
| 7 | `pwm-timers-07.md` | Behöll `Snabbreferens` eftersom begreppstabellen är mer användbar vid uppslag. |
| 8 | `avbrott-watchdog-08.md` | Behöll `Snabbreferens` eftersom kapitlet innehåller flera val mellan tekniker och robusthetsmönster. |
| 9 | `kommunikation-bussar-09.md` | Behöll `Snabbreferens` eftersom läsaren ofta behöver snabb hjälp att välja buss eller felsöka. |
| 17 | `led-rgb-ljuseffekter-17.md` | Behöll `Snabbreferens` eftersom den fungerar som praktisk snabbguide för LED-val och drivning. |
| 22 | `displayer-anvandargranssnitt-22.md` | Behöll `Snabbreferens` eftersom displayval lämpar sig väl för tabellformat. |
| 30 | `io-expansion-30.md` | Behöll `Snabbreferens` eftersom kapitlet handlar om komponentval och begränsningar. |
| 32 | `displaykretsar-minne-32.md` | Behöll `Snabbreferens` eftersom minne, display och loggning lämpar sig för valtabeller. |

## Resultat

Efter justeringen finns inga kapitel som både har `Snabb sammanfattning` och `Snabbreferens`.

`Snabb sammanfattning` finns kvar i kapitel där den gör pedagogisk nytta. `Snabbreferens` finns kvar i kapitel där läsaren sannolikt vill slå upp val, begränsningar eller praktiska rekommendationer.

## Efterkontroll

- Inga H4-rubriker hittades.
- Inga `## Se också`-rubriker finns i kapitelmanuset.
- `build/book.md` är uppdaterad.
- Exportvalidering är genomförd utan varningar.

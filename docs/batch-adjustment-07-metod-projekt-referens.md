# [PLAN] Batchjustering 7: metod-, projekt- och referenskapitel

## Omfattning

Detta dokument sammanfattar genomförd batchjustering enligt **[PLAN] 7. Batchjustera resten av kapitlen**, batch 7.

Batchen omfattar:

| Kapitel | Fil | Kapiteltyp |
|---:|---|---|
| 35 | `chapters/felsokning-35.md` | Metodkapitel |
| 36 | `chapters/breadboard-till-modul-36.md` | Metod-/projektkapitel |
| 37 | `chapters/modular-sensor-styrstation-37.md` | Projektkapitel |
| 38 | `chapters/referens-snabbvalsguider-38.md` | Referenskapitel |

## Redaktionell inriktning

Batchen följer den slutliga strukturregeln i `docs/final-structure-rule.md`.

Målet har varit att göra kapitlen mer användbara som praktisk handbok:

- tydligare snabb orientering i början,
- mindre kursbokskänsla,
- mer fokus på arbetssätt, checklistor och beslut,
- praktiska tester i stället för skolövningar,
- `Se också` i stället för framåtdrivande kursprogression,
- referenskapitlet som faktisk uppslagsdel snarare än avslutande lektion.

## Genomförda strukturändringar

| Gammal struktur | Ny struktur |
|---|---|
| `Varför detta kapitel finns` | `Snabb orientering` |
| `Lärandemål` | `Det du kan använda kapitlet till` |
| `Innan vi börjar` | `Förutsättningar` |
| `Praktiskt experiment` | `Praktiskt test` |
| `Övningar` | `Praktiskt arbetspass` |
| `Övning N` | `Test N` |
| `Snabb sammanfattning` | `Checklista` eller `Snabbreferens` |
| `Quiz/reflektionsfrågor` | `Kontrollera arbetssättet` eller `Kontrollera ditt val` |
| `Nästa steg` | `Se också` |

## Kapitelvisa kommentarer

### Kapitel 35: Felsökning med metod

Kapitlet har harmoniserats som metodkapitel. De tidigare kursmarkörerna har ersatts med en mer praktisk struktur som passar läsare som har fastnat i ett konkret fel och vill hitta ett systematiskt arbetssätt.

### Kapitel 36: Från breadboard till återanvändbar modul

Kapitlet har justerats mot projekt- och metodkapitlets struktur. Fokus ligger på övergången från experiment till modul, med praktiskt arbetspass och checklista snarare än övnings- och quizkänsla.

### Kapitel 37: Sammanhängande projekt

Kapitlet har harmoniserats som sammanbindande projektkapitel. Det ska fungera både som slutprojekt och som modell för hur tidigare delar kan kombineras.

### Kapitel 38: Referens

Kapitlet var redan pilotjusterat och har nu harmoniserats med batchens språkbruk. Referenskaraktären har bevarats.

## Kontroll efter batch

Följande kontroller har gjorts i batchens kapitel:

- gamla kursrubriker är borttagna utanför kodblock,
- inga H4-rubriker används,
- `build/book.md` är uppdaterad,
- kapitel 38 behåller sin roll som referens och snabbvalsguide.

## Nästa rekommenderade steg

Nästa steg enligt [PLAN] är **8. Normalisera återkommande sektioner**. Eftersom alla batchar nu är genomförda bör det steget göras som en helhetskontroll över hela boken, inte som kapitel-för-kapitel-redigering från början.

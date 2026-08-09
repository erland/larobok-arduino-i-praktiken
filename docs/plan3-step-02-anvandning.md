# [PLAN3] Steg 2: Granska `Det du kan använda kapitlet till`

Datum: 2026-07-01  
Status: Genomfört.

## Syfte

Detta steg granskar om rubriken `Det du kan använda kapitlet till` fortfarande tillför praktisk nytta efter att boken har justerats mot handbok och uppslagsverk.

Målet är att rubriken inte ska bli ett nytt namn på gamla formella lärandemål.

## Genomförd princip

Sektionen har behållits när den hjälper läsaren förstå vad kapitlet är praktiskt användbart till, särskilt i:

- grundfunktionskapitel,
- komponent- och aktuator-kapitel,
- sensor- och mätkapitel,
- robusthets- och kretskapitel.

Sektionen har tagits bort där `Snabb orientering`, `Snabbval`, `Valguide`, `Arbetssättet` eller kapiteltypen redan gör samma jobb.

## Ändrade kapitel

Följande kapitel fick sektionen borttagen eftersom den överlappade med befintlig orientering eller gjorde kapitlet mer kursbokslikt än nödvändigt:

| Kapitel | Beslut |
|---|---|
| 10. Klassiska Arduino-kort | Sektionen togs bort. Kortvalet bärs av `Snabb orientering`, `Bedöm kortet med detta i åtanke`, jämförelser och `Snabbval`. |
| 11. Kloner och lågkostnadskort | Sektionen togs bort. Bedömningen ligger tydligare i kapitlets risk- och valdelar. |
| 12. Moderna Arduino-kort | Sektionen togs bort. Kapitlet fungerar bättre som plattformsöversikt utan lärandemålsliknande punktlista. |
| 14. ESP32-familjen | Sektionen togs bort. Praktisk nytta framgår redan av plattformsbeskrivning, valguide och fallgropar. |
| 15. Raspberry Pi Pico | Sektionen togs bort. Val- och plattformsdelarna gör samma arbete bättre. |
| 16. Småkort och specialkort | Sektionen togs bort. Kapitlet ska kännas som kortvalsreferens. |
| 35. Felsökning med metod | Sektionen togs bort. Metoden blir tydligare när kapitlet går direkt från orientering till arbetssätt. |
| 36. Från breadboard till återanvändbar modul | Sektionen togs bort. Kapitlet fungerar bättre som praktiskt arbetskapitel. |
| 37. Modulär sensor- och styrstation | Sektionen togs bort. Projektkapitlet behöver inte en separat användningslista före arbetsflödet. |

Kapitel 13 saknade redan sektionen efter tidigare justering och behövde därför ingen ändring.

## Resultat

Före steget fanns `Det du kan använda kapitlet till` i 30 kapitel.

Efter steget finns rubriken kvar i 21 kapitel, där den bedöms ge praktisk nytta snarare än mekanisk kursstruktur.

## Redaktionell regel framåt

`Det du kan använda kapitlet till` får användas när den hjälper läsaren att snabbt avgöra kapitlets praktiska nytta. Den ska inte användas som obligatorisk ersättning för lärandemål.

Om `Snabb orientering` redan förklarar nyttan, eller om kapitlet har tydliga val-, metod- eller referensdelar, ska sektionen tas bort eller bakas in i den omgivande texten.

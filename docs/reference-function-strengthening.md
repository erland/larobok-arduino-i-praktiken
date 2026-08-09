# [PLAN] 9. Stärkt uppslagsverksfunktion

## Syfte

Det här steget stärker bokens funktion som praktiskt uppslagsverk. Efter batchjusteringarna har kapitlen redan fått mer handboksnära rubriker. Detta steg gör uppslagsfunktionen mer explicit och lättare att underhålla.

Målet är att läsaren snabbt ska kunna gå från en fråga till rätt kapitel, rätt kontrollpunkt och rätt typ av beslut.

## Princip

Boken ska stödja tre lässätt:

1. **Följ boken från början.** Läsaren bygger successivt förståelse för Arduino-ekosystem, kort, I/O, sensorer, aktuatorer och robusta kretsar.
2. **Hoppa direkt till ett område.** Läsaren kan gå direkt till ett kapitel om ett kort, en sensor, en motor, en display eller en kretskategori.
3. **Felsök ett konkret problem.** Läsaren kan använda snabbval, checklistor, korsreferenser och referenskapitlet för att hitta rimliga kontroller.

## Uppslagsfunktioner som ska prioriteras

| Funktion | Syfte |
|---|---|
| Snabb orientering | Gör det tydligt vad kapitlet hjälper läsaren att lösa. |
| När du använder detta | Hjälper läsaren avgöra om kapitlet är relevant. |
| När du bör välja något annat | Minskar risken för fel komponent, kort eller metod. |
| Valguide / Snabbval | Gör kapitlet användbart som beslutstöd. |
| Snabbreferens | Samlar praktiska fakta i kort form. |
| Felsökning | Hjälper läsaren när koppling, kod eller bibliotek inte fungerar. |
| Vanliga misstag | Förklarar typiska fel innan de uppstår. |
| Säkerhetsruta | Markerar elektriska eller praktiska risker. |
| Korsreferens / Se också | Binder samman boken som uppslagsverk. |

## Genomförda förstärkningar i steg 9

- Inledningen har fått en tydligare beskrivning av hur boken används som uppslagsverk.
- Referenskapitlet har fått ett snabbindex som pekar läsaren till rätt kapitel utifrån vanlig fråga.
- Ett separat uppslagsindex har lagts till i `docs/lookup-index.md`.
- Projektstatus och bokspecifikation har uppdaterats med att uppslagsfunktionen nu är ett uttryckligt redaktionellt krav.
- `build/book.md` har byggts om från uppdaterade kapitel.

## Redaktörsregel för kommande ändringar

När ett kapitel ändras framöver ska redaktören kontrollera om kapitlet behöver minst en av följande funktioner:

- snabbval eller snabbreferens,
- felsökning,
- vanliga misstag,
- säkerhetsruta,
- korsreferenser till närliggande kapitel.

Alla kapitel behöver inte alla funktioner, men komponent-, sensor-, plattforms- och robusthetskapitel bör normalt ha flera av dem.

## Resultatbedömning

Steg 9 bedöms som genomfört. Uppslagsfunktionen var delvis stärkt redan i batch 1–7 och normaliseringen i steg 8. I detta steg har den gjorts mer synlig, sökbar och styrande.

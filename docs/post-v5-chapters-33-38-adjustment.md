# Post-v5-justering: kapitel 33–38

## Utgångspunkt

Denna justering utgår från `arduino-i-praktiken-projekt-v5-kapitel-27-32-justering.zip`.

Syftet är att göra sista blocket mer konsekvent med de redaktionella justeringarna i kapitel 1–32: behålla konkret handboksnytta men ta bort dokumentations-, arbetsmalls- och övningskänsla där den inte behövs.

## Ändrade kapitel

- `chapters/analog-signalanpassning-33.md`
- `chapters/stromforsorjning-batteridrift-34.md`
- `chapters/felsokning-35.md`
- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`
- `chapters/referens-snabbvalsguider-38.md`

## Genomförda principer

- `Det du kan använda kapitlet till` har vävts in i kapitelöversikten i kapitel 33 och 34.
- Kurslika `Nästa praktiska kontroll`- och `Valchecklista`-avsnitt har tagits bort.
- Praktiska verifieringar som faktiskt hjälper läsaren felsöka, mäta eller bedöma kopplingar har behållits.
- Risk- och säkerhetsnära kontroller har behållits, men dokumentations- och frågeformat har tonats ned.
- Dokumentationsspråk har justerats där dokumentation inte är själva poängen.
- Kapitel 38 har renodlats som referens genom att arbetsmallar och egna referensmallar tagits bort.

## Kapitelvis sammanfattning

### Kapitel 33

- Nyttosektionen har vävts in i `Signalanpassning i praktiken`.
- `Nästa praktiska kontroll` har tagits bort.
- `Valchecklista` har tagits bort.
- Tröskel- och filtermönster har behållits, men språk som `I det här experimentet` och `Vad du ska observera` har gjorts mer handboksnära.

### Kapitel 34

- Nyttosektionen har vävts in i `Matningsöversikt och riskbild`.
- `Riskkontroll: gör en strömbudget och hitta svag matning` har kortats och gjorts om till en praktisk riskkontroll.
- `Nästa praktiska kontroll` har tagits bort.
- Den frågeformade slutsektionen `Riskkontroll` har tagits bort.
- Säkerhetsruta och praktiska riskkontroller har behållits.

### Kapitel 35

- `Felsökningsmönster: I2C-problem metodiskt` har behållits, men dokumentationsspråk har ändrats till kontrollspråk.
- `Checklista` och `Arbetschecklista` har slagits ihop till `Felsökningschecklista`.
- Rapport-/arbetsbladsformuleringar har tonats ned.

### Kapitel 36

- `Dokumentera pinout innan du glömmer` har ändrats till `Spara pinout medan kopplingen fungerar`.
- `Modulmapp i projektet` har ändrats till `Exempel: enkel modul-README`.
- `Modulmall i praktiken` har tagits bort eftersom den överlappade med kapitlets modulchecklista och gav arbetsövningskänsla.
- `Modulchecklista` har justerats till mer praktiskt modulunderhåll.

### Kapitel 37

- `Dokumentera slutprojektet` har ändrats till `Spara projektets viktiga beslut`.
- `Integrationsordning i praktiken` har ändrats till `Integrationsordning`.
- Kortvalsjämförelse och uppkopplingsfördjupning i integrationsordningen har kortats bort eller omvandlats till neutral versionsråd.
- `Projektkontroll före nästa version` har ändrats till `Kontroll före nästa version`.

### Kapitel 38

- `Snabbval: experimentnivå` har ändrats till `Snabbval: prototypnivå`.
- `Snabbval: dokumentation du bör skapa` har ändrats till `Snabbval: anteckningar som sparar felsökningstid`.
- `Arbetsmall: gör en egen valguide` har tagits bort.
- `Egen referensmall` har tagits bort.
- `Användningschecklista` har ändrats till `Så omsätter du tabellerna`.

## Kontroll

Efter justeringen har `build/book.md` byggts om.

Kontrollerade mönster i kapitel 33–38:

- inga `## Det du kan använda kapitlet till`
- inga `## Nästa praktiska kontroll`
- inga `## Valchecklista`
- ingen `## Arbetsmall: gör en egen valguide`
- ingen `## Egen referensmall`
- inga `I det här experimentet`-formuleringar
- inga `experimentlogg`-formuleringar
- inga H4-rubriker

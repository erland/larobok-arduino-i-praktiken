# Post-v5-justering: kapitel 17–21

Status: Genomfört 2026-07-02.

## Syfte

Fortsätta den redaktionella rensningen efter v5 så att kapitel 17–21 känns mer som praktiska handbokskapitel och mindre som läroboks- eller workshopkapitel.

Principen för detta steg var:

- behåll praktiska kontroller som verifierar konkret funktion, koppling, ström, färg, ljud, rörelse eller laststyrning,
- ta bort avslutande checklistor och frågebaserade kontrollavsnitt,
- väv in `Det du kan använda kapitlet till` i kapitlets första översikt där den sektionen förekom,
- tona ned ord och rubriker som `experiment`, `mål`, `syfte` och dokumentationsmallar när de gav kurskänsla,
- bevara säkerhetsnära kontroller i motor- och lastkapitel.

## Ändrade kapitel

### Kapitel 17

Fil: `chapters/led-rgb-ljuseffekter-17.md`

- Vävde in `Det du kan använda kapitlet till` i `Komponentöversikt`.
- Tog bort `Valchecklista`.
- Ersatte `Verifiera ljusfunktionen` med `Kontrollpunkter för LED-kod`.
- Gjorde referensmönstret för statusljus mindre experimentlikt.

Motiv: kapitlet behåller praktisk nytta kring LED, RGB, statusmönster och icke-blockerande kod, men tappar avslutande frågelista och uppgiftskänsla.

### Kapitel 18

Fil: `chapters/adresserbara-led-18.md`

- Vävde in `Det du kan använda kapitlet till` i `Komponentöversikt`.
- Tog bort `Valchecklista`.
- Ersatte `Verifiera LED-pixelkedjan` med `Kontrollpunkter vid uppstart`.
- Ändrade `Mål` till `Vad mönstret visar`.
- Ändrade observationsspråk till mer praktisk kontroll.

Motiv: färgordning, strömbudget, gemensam jord och nivåskiftning är verkliga handbokskontroller och bör vara kvar, men inte som övningsblock.

### Kapitel 19

Fil: `chapters/buzzers-ljudsignaler-19.md`

- Vävde in `Det du kan använda kapitlet till` i `Komponentöversikt`.
- Tog bort `Valchecklista`.
- Ersatte `Verifiera ljudkomponenten` med `Felsök ljudsignalen`.
- Gjorde referensmönstret för ljudstatus mindre experimentlikt.

Motiv: praktisk felsökning av aktiv/passiv buzzer, piezo, högtalare och timerkonflikter är mer relevant för handboken än dokumentationsövningar kring ljudkomponenter.

### Kapitel 20

Fil: `chapters/servon-motorer-20.md`

- Tog bort `Valchecklista`.
- Ersatte `Verifiera servostyrningen` med `Kontrollpunkter för rörelsekod och motorstart`.
- Ändrade `Syfte` i servoreferensmönstret till `Vad mönstret visar`.
- Tonade ned experimentformuleringar.

Motiv: motor- och servokapitel behöver behålla praktiska kontroller kring matning, gemensam jord, acceleration, startström och blockering, men inte avslutande valfrågor.

### Kapitel 21

Fil: `chapters/relaer-mosfetar-laster-21.md`

- Vävde in `Det du kan använda kapitlet till` i `Riskbild och styrprincip`.
- Tog bort `Valchecklista för laster`.
- Ändrade `Syfte` i MOSFET-referensmönstret till `Vad kopplingen visar`.
- Ersatte `Riskkontroll: relä med säker vilologik` med `Kontrollera relämodulens viloläge`.
- Tog bort dokumentationsmall för relämodul.
- Ersatte avslutande frågebaserad `Riskkontroll` med `Sista kontroll före inkoppling`.

Motiv: säkerhetsnära kontroller ska vara kvar, men som handlingsbara kontrollpunkter i stället för dokumentationsmallar eller quizliknande frågor.

## Kontroll

Efter ändringen har `build/book.md` byggts om.

Kontrollerat för kapitel 17–21:

- inga `## Det du kan använda kapitlet till`,
- inga `## Valchecklista`,
- ingen `## Valchecklista för laster`,
- inga `## Verifiera ljusfunktionen`,
- inga `## Verifiera LED-pixelkedjan`,
- inga `## Verifiera ljudkomponenten`,
- inga `## Verifiera servostyrningen`,
- inga `### Dokumentationsmall`,
- inga H4-rubriker.

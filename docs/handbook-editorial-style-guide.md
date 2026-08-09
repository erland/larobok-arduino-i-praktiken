# Intern redaktionell stilguide för handboken

Datum: 2026-07-01  
Tillhör: `[PLAN-H]` steg H10  
Status: Intern arbetsreferens  
Gäller för: framtida redigering av *Arduino i praktiken*

## Syfte

Den här stilguiden ska hindra att boken glider tillbaka mot lärobok, kursbok eller intern projektlogg när nya kapitel, komponenter eller korrigeringar läggs till.

Boken ska läsas som en praktisk handbok: ett arbetsverktyg för någon som bygger, väljer, kopplar, felsöker eller jämför Arduino-komponenter.

## Grundprinciper

- Skriv för en läsare som vill komma vidare i ett praktiskt projekt.
- Använd rubriker som beskriver nytta, val, verifiering, risk eller felsökning.
- Undvik formuleringar som låter som prov, kursmål eller lärandemål.
- Lägg inte interna projektspår i läsartexten.
- Ändra inte teknisk nivå utan skäl.
- Lägg hellre till ett kort beslutsstöd än en lång teoriförklaring.
- Bevara bokens vänliga och pedagogiska ton, men gör den mer handboksnära än skolboksmässig.

## Handbokston

### Föredra

Använd formuleringar som hjälper läsaren att agera:

- I det här kapitlet får du en praktisk överblick över...
- Kapitlet hjälper dig att känna igen...
- Använd detta när...
- Välj detta när...
- Kontrollera detta innan du kopplar in...
- Börja med minsta fungerande koppling.
- Jämför alternativen innan du väljer modul.
- Om det inte fungerar, börja med matning, jord och enkel testkod.

### Undvik

Undvik formuleringar som låter som krav eller prov:

- Efter kapitlet ska du kunna...
- Kontrollera att du hänger med
- Testa dina kunskaper
- Övning
- Laboration
- Fråga 1, fråga 2, fråga 3
- Läsaren ska...
- Studenten ska...
- I detta kursmoment...

Undvik också interna projektspår i läsartext:

- `PLAN5`
- `[PLAN-H]`
- `docs/lookup-index.md`
- `build/book.md`
- `canon`
- `project-status`
- filnamn, zipnamn eller interna arbetsdokument

## Ersättningsmönster

| Undvik | Använd hellre |
|---|---|
| Efter kapitlet ska du kunna... | Kapitlet hjälper dig att känna igen... |
| Kontrollera att du hänger med | Snabb kontroll i praktiken |
| Kontrollera ditt val | Valchecklista |
| Praktiskt test | Verifiera kopplingen / Referensmönster / Riskkontroll |
| Prova själv | Egen kontroll i praktiken / Nästa praktiska steg |
| Prova vidare | Vanliga varianter / Nästa praktiska kontroll |
| Test 1 | Kontroll 1 |
| Övning | Arbetsmönster / Praktisk kontroll / Referensmönster |
| Laboration | Minsta fungerande koppling / Verifiering |

## Kapiteltyper

### Inledning

Mål: hjälpa läsaren förstå vad boken är och hur den används.

Passande rubriker:

- Vad boken handlar om
- Vem boken är för
- Hur boken är upplagd
- Så använder du boken som uppslagsverk
- Säkerhet och rimliga gränser

Undvik:

- interna filreferenser,
- versionshistorik,
- projektlogg,
- tekniska arbetsfiler.

### Orienterings- och beslutskapitel

Exempel: ekosystem, kortval, utvecklingsmiljö och elektriska grunder.

Passande rubriker:

- Snabb överblick
- Beslutsöversikt
- Arbetsmiljö i korthet
- Begrepp i praktiken
- Viktiga samband att känna igen
- Vanliga missförstånd
- Snabb sammanfattning

Praktiska moment ska bara finnas när de hjälper läsaren att verifiera något konkret. Teoriexperiment ska normalt kortas, tas bort eller omvandlas till ett exempel.

### Grundfunktionskapitel

Exempel: digital I/O, analog läsning, PWM, avbrott och kommunikationsbussar.

Passande rubriker:

- Grundfunktion i praktiken
- Mätfunktion i praktiken
- Tidsstyrning i praktiken
- Robust körning i praktiken
- Kommunikationsval i praktiken
- Referensmönster
- Snabb kontroll i praktiken
- Vanliga fel

Praktiska moment bör visa minsta fungerande kod eller minsta fungerande koppling.

### Kort- och plattformskapitel

Exempel: UNO, Nano, Mega, kloner, moderna Arduino-kort, ESP8266, ESP32, Pico och småkort.

Passande rubriker:

- Kortprofil i korthet
- Bedöm kortet med detta i åtanke
- Kortfamiljen i praktiken
- Plattformen i praktiken
- När kortet passar
- När du bör välja något annat
- Porteringstest
- Valguide

Fokusera på val, begränsningar, kompatibilitet och praktiska konsekvenser.

### Komponent- och sensorkapitel

Exempel: LED, buzzers, motorer, displayer, sensorer, I/O-expansion, drivkretsar och minne.

Passande rubriker:

- Komponentöversikt
- Sensoröversikt
- Modulöversikt
- Expansionsöversikt
- Drivsteg i praktiken
- Vad komponenten gör
- När den passar
- Koppling i praktiken
- Referensmönster
- Verifiera modulen
- Vanliga problem
- Valchecklista

Fokusera på vad komponenten gör, när den passar, hur den kopplas och hur läsaren ser att den fungerar.

### Robusthets- och säkerhetskapitel

Exempel: laster, strömmätning, signalanpassning, strömförsörjning och felsökning.

Passande rubriker:

- Riskbild och styrprincip
- Mät- och energibild
- Signalanpassning i praktiken
- Matningsöversikt och riskbild
- Felsökningsöversikt
- Riskkontroll
- Säker koppling
- Felsökningsordning
- Vanliga misstag

Här är checklistor och riskkontroller viktigare än kodexempel.

### Metod- och projektkapitel

Exempel: från breadboard till modul och modulär sensor-/styrstation.

Passande rubriker:

- Arbetsmönster i korthet
- Projektöversikt
- Arbetsmönster
- Stegvis integration
- Modulchecklista
- Testordning
- Felsökningsstrategi
- Arbetschecklista

Fokusera på ordning, återanvändbarhet, dokumentation och testbarhet.

### Referenskapitel

Exempel: snabbvalsguider och jämförelsetabeller.

Passande rubriker:

- Så använder du referensen
- Snabbindex
- Snabbval
- Jämförelsetabell
- Valchecklista
- Referensmall
- När du väljer mellan alternativen

Undvik:

- övningar,
- quiz,
- kapitelmål,
- långa förklarande sidospår.

## Praktiska moment

Praktiska moment ska finnas när de hjälper läsaren att verifiera eller använda något.

### Bra praktiska moment

- minsta fungerande koppling,
- minsta fungerande kod,
- kontroll av matning och jord,
- verifiering av I2C-adress,
- kontroll av sensorvärde,
- jämförelse av två moduler,
- stegvis felsökning.

### Svagare praktiska moment

- rena teoriexperiment,
- frågor där läsaren bara återger text,
- övningar som inte leder till ett praktiskt beslut,
- experiment som kräver utrustning utan att tydligt hjälpa projektet.

## Beslutsstöd

När ett kapitel beskriver flera alternativ bör det normalt innehålla ett kort beslutsstöd.

Exempel:

- Välj MOSFET när lasten är DC och ska styras snabbt.
- Välj relä när du behöver galvanisk separation eller bara av/på.
- Välj DRV8833 för små DC-motorer och lägre spänning.
- Välj PCA9685 när du behöver många servokanaler.
- Välj I2C när du vill ansluta flera moduler med få pinnar.

Beslutsstöd ska vara kort, praktiskt och kopplat till verkliga val.

## Riskkontroll

Riskkontroll ska användas när fel kan ge trasiga komponenter, felaktiga mätvärden eller svår felsökning.

Vanliga riskområden:

- motorer,
- reläer,
- solenoider,
- MOSFETar,
- strömförsörjning,
- batteridrift,
- nivåskiftning,
- analog signalanpassning,
- strömmätning,
- externa moduler.

Riskkontroller ska vara konkreta:

- Kontrollera gemensam jord.
- Kontrollera att lasten har egen matning om den kräver mer ström än kortet kan ge.
- Kontrollera flybackdiod eller modulens inbyggda skydd.
- Kontrollera logiknivå innan 3,3 V-kort kopplas till 5 V-moduler.
- Kontrollera polaritet innan spänning ansluts.

## Korsreferenser

Korsreferenser ska hjälpa läsaren hitta nästa relevanta problemområde.

### Föredra

- Vid I2C-problem, se kapitlet om kommunikationsbussar.
- Vid brusiga mätvärden, se kapitlet om analog signalanpassning.
- Vid motorproblem, kontrollera även strömförsörjningen och drivkretsen.
- Vid många moduler, se I/O-expansion och bussval.

### Undvik

- långa mekaniska listor,
- interna filreferenser,
- “se även” utan förklaring,
- hänvisningar till planer eller arbetsdokument.

## Markdownregler

Följ projektets etablerade markdownstandard:

- använd endast H1–H3 i kapitel,
- använd exakt en H1 per kapitel,
- använd tomrad före och efter listor, tabeller och kodblock,
- använd två mellanslag för nästlade listor,
- använd kodspråk i kodblock där det är relevant,
- undvik rå HTML i bokmanus,
- bygg om `build/book.md` efter kapiteländringar.

## Kontroll före ny projektversion

Innan en ny versionszip skapas bör följande kontrolleras:

- Inga interna projektspår finns i `chapters/`.
- Inga kvarvarande kursrubriker som `Praktiskt test`, `Prova själv`, `Prova vidare`, `Kontrollera att du hänger med` eller `Snabb orientering` finns kvar.
- Inga H4-rubriker finns i kapitel.
- Kapitelrubriker följer kapiteltypens funktion.
- Beslutsstöd finns där läsaren behöver välja mellan alternativ.
- Riskkontroller finns där felkoppling kan skada komponenter eller ge missvisande resultat.
- `build/book.md` är uppdaterad.
- Exportmetadata är synkroniserad inför EPUB/PDF.

## Relation till andra interna dokument

Denna fil är den övergripande redaktionella stilguiden. Den kompletterar:

- `docs/chapter-templates-by-type.md` för rubrikfamiljer,
- `docs/PLAN-H.md` för genomförandestegen,
- `docs/plan-h-implementation-log.md` för vad som redan har gjorts,
- `docs/canon-terminology.md` för tekniska termer och konsekvent terminologi.

Vid konflikt bör bokmanusets etablerade teknik och canon behållas, men rubrik- och tonval följa denna stilguide.

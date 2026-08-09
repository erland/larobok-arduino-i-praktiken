# [PLAN-H] – Redaktionell handboksplan

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–12 genomförda  
Status: Förslag till genomförandeplan  
Planens typ: Redaktionell handboksplan  
Viktig regel: `[PLAN-H]` är en arbetsplan. Själva bokmanuset ändras först när planen genomförs steg för steg.

## Syfte

`[PLAN-H]` ska göra *Arduino i praktiken* tydligare som praktisk handbok. Planen ska inte lägga till fler komponenter eller bygga om bokens kapitelordning. Den ska i stället rensa bort läroboksspår, interna projektspår och kursliknande avslut, samt ersätta dem med handboksnära rubriker, checklistor, verifieringsmönster, riskkontroller och felsökningsstöd.

Analysen visar att boken redan är stark innehållsmässigt. Den återkommande svagheten ligger främst i det redaktionella lagret: vissa formuleringar låter som lärandemål, vissa praktiska moment presenteras som övningar, och flera kapitel använder samma mall även när kapiteltypen egentligen kräver en annan struktur.

## Grundprinciper för genomförandet

- Ändra inte tekniskt innehåll i onödan.
- Lägg inte till nya komponenter.
- Skapa inte nya kapitel om det inte blir absolut nödvändigt.
- Bevara bokens praktiska täckning från v4.
- Gör varje kapitel mer handboksnära utan att göra det torrare.
- Ersätt kurs- och provkänsla med användningsnytta.
- Anpassa rubriker efter kapiteltyp.
- Uppdatera `build/book.md` först när faktiska kapiteländringar har gjorts.
- Uppdatera `docs/project-status.md` efter varje genomfört steg.
- Packa ny projekt-zip efter varje genomfört steg.

## Definition av önskad handbokston

Boken ska kännas som ett arbetsverktyg för någon som bygger, felsöker eller väljer Arduino-komponenter.

### Föredra

- Här får du en praktisk överblick över...
- Använd kapitlet när du behöver...
- Kapitlet hjälper dig att känna igen...
- Välj detta när...
- Kontrollera detta innan du kopplar in...
- Vanliga misstag
- Snabb kontroll i praktiken
- Felsökningsordning
- Referensmönster
- Minsta fungerande koppling
- Riskkontroll

### Undvik

- Efter kapitlet ska du kunna...
- Kontrollera att du hänger med
- Testa dina kunskaper
- Övning, om det egentligen är ett handgrepp eller en verifiering
- Interna plan- eller filnamn i läsartexten, till exempel `PLAN5`, `docs/lookup-index.md`, `canon`, `build/book.md` eller projektstatus

## Kapiteltyper och rekommenderade rubrikfamiljer

### Inledning

Rekommenderad struktur:

- Vad boken hjälper dig med
- Vem boken är för
- Hur du använder boken
- Hur kapitlen är upplagda
- Referenskapitlet i slutet av boken

Undvik interna filreferenser.

### Orienteringskapitel

Exempel: tidiga kapitel om Arduino, arbetssätt och begreppsramar.

Rekommenderade rubriker:

- Snabb överblick
- Vad du behöver känna igen
- Vanliga missförstånd
- När detta spelar roll i praktiken
- Sammanfattning

Praktiska moment ska bara finnas om de är tydligt motiverade. Teoriexperiment bör normalt tas bort eller skrivas om till korta exempel.

### Grundfunktionskapitel

Exempel: digital I/O, analog läsning, PWM, avbrott och kommunikation.

Rekommenderade rubriker:

- Grundidé
- När du använder detta
- Minsta fungerande exempel
- Vanliga fel
- Snabb kontroll i praktiken

Praktik bör behållas när den verifierar en funktion, men inte presenteras som kursövning.

### Kort- och plattformskapitel

Exempel: klassiska Arduino-kort, kloner, ESP8266, ESP32, Raspberry Pi Pico och småkort.

Rekommenderade rubriker:

- Kortprofil
- När kortet passar
- Begränsningar
- Porteringstest
- Kontrollera valet

### Komponentkapitel

Exempel: LED, displayer, sensorer, motorer, drivkretsar, I/O-expansion.

Rekommenderade rubriker:

- Vad komponenten gör
- När den passar
- Koppling i praktiken
- Referensmönster
- Verifiera modulen
- Vanliga problem
- Relaterat

### Robusthets- och säkerhetskapitel

Exempel: reläer, laster, strömmätning, strömförsörjning, felsökning.

Rekommenderade rubriker:

- Riskbild
- Säker koppling
- Riskkontroll
- Felsökningsordning
- Vanliga misstag
- Rekommenderat arbetssätt

### Metod- och projektkapitel

Exempel: från breadboard till modul och sensor-/styrstation.

Rekommenderade rubriker:

- Arbetsmönster
- Stegvis integration
- Modulchecklista
- Testordning
- Felsökningsstrategi

### Referenskapitel

Exempel: snabbvalsguider och slutreferens.

Rekommenderade rubriker:

- Snabbval
- Välj efter behov
- Jämförelsetabell
- Checklista
- Felsökningshjälp
- Mall

Ingen quiz- eller övningsstruktur.

## Genomförandesteg

### Steg H1 – Rensa interna projektspår i läsartext

**Syfte:** Göra boken fristående för läsaren.

**Berörda filer:**

- `chapters/00-inledning.md`
- `chapters/referens-snabbvalsguider-38.md`
- eventuellt andra kapitel om sökningen hittar interna fil-/plannamn

**Åtgärder:**

- Ta bort eller skriv om referensen till `docs/lookup-index.md` i inledningen.
- Ersätt `PLAN5` i kapitel 38 med läsarcentrerade formuleringar.
- Sök efter och rensa interna termer som `docs/`, `build/`, `canon`, `project-status`, `PLAN` och liknande om de förekommer i kapiteltext.
- Behåll interna hänvisningar i `docs/`, men inte i `chapters/`.

**Förväntad effekt:** Boken känns färdig och professionell.

**Risk:** Låg.

---

### Steg H2 – Ersätt kravliknande lärandemål i `Snabb orientering`

**Syfte:** Minska lärobokskänslan utan att ta bort orienteringen.

**Berörda filer:** Alla kapitel där formuleringar som `Efter kapitlet ska du...` eller liknande finns.

**Åtgärder:**

- Sök efter `Efter kapitlet ska`, `Efter kapitlet bör`, `ska du kunna` och närliggande formuleringar.
- Ersätt med kapitelanpassade handboksformuleringar.
- Använd inte samma ersättningsfras överallt.
- Behåll informationen om vad kapitlet hjälper läsaren med.

**Exempel på omskrivning:**

| Före | Efter |
|---|---|
| Efter kapitlet ska du framför allt kunna skilja på... | Här får du en praktisk överblick över skillnaden mellan... |
| Efter kapitlet ska du kunna välja... | Kapitlet hjälper dig att välja... |
| Efter kapitlet ska du känna till... | Här ser du vad som är viktigt att känna igen i praktiken... |

**Förväntad effekt:** Lägre prestationskänsla och tydligare handbokston.

**Risk:** Låg.

---

### Steg H3 – Omvandla quiz- och kontrollfrågor

**Syfte:** Ersätta provkänsla med handboksverktyg.

**Berörda filer:** Särskilt kapitel 1, 3, 4, 5 och senare kapitel med `Kontrollera ditt val`, `Kontrollera arbetssättet` eller liknande.

**Åtgärder:**

- Sök efter rubriker som börjar med `Kontrollera`.
- Bedöm varje förekomst efter funktion:
  - begreppskontroll,
  - valkontroll,
  - riskkontroll,
  - felsökning,
  - arbetskontroll.
- Ersätt quizformat med:
  - `Vanliga missförstånd`,
  - `Snabb kontroll i praktiken`,
  - `Valchecklista`,
  - `Riskkontroll`,
  - `Felsökningsordning`,
  - `Arbetschecklista`.

**Förväntad effekt:** Boken blir mer användbar som uppslags- och arbetsbok.

**Risk:** Låg–medel. Innehåll kan behöva skrivas om, inte bara byta rubrik.

---

### Steg H4 – Omklassificera `Praktiskt test`, `Prova själv` och `Prova vidare`

**Syfte:** Behålla praktisk nytta men minska kurs-/workshopkänsla.

**Berörda filer:** Nästan hela boken, men särskilt kapitel 1–10 och komponentkapitlen.

**Åtgärder:**

- Inventera varje `Praktiskt test`, `Prova själv` och `Prova vidare`.
- Dela in dem i följande kategorier:
  - bör tas bort,
  - bör slås ihop,
  - bör bli verifiering,
  - bör bli referensmönster,
  - bör bli felsökning,
  - bör bli arbetsmönster,
  - bör behållas med ny rubrik.
- Ta särskilt bort eller korta ned teoriexperiment i rent teoretiska kapitel.
- Undvik överlapp där `Praktiskt test` och `Prova själv` säger ungefär samma sak.

**Rekommenderade ersättningsrubriker:**

| Nuvarande rubrik | Möjlig handboksrubrik |
|---|---|
| Praktiskt test | Minsta fungerande test |
| Praktiskt test | Verifiera kopplingen |
| Praktiskt test | Referensmönster |
| Prova själv | Snabb kontroll i praktiken |
| Prova vidare | Vanliga varianter |
| Prova vidare | Nästa praktiska steg |

**Förväntad effekt:** Praktiken känns mer som ett stöd i arbetet än som en skoluppgift.

**Risk:** Medel. Detta är den mest omfattande redaktionella förändringen.

---

### Steg H5 – Inför kapiteltypsspecifik rubriknormalisering

**Syfte:** Sluta använda samma yttre mall mekaniskt i alla kapitel.

**Berörda filer:** Alla kapitel.

**Åtgärder:**

- Klassificera varje kapitel enligt kapiteltyperna i denna plan.
- Anpassa rubrikerna efter kapiteltyp.
- Bevara konsekvens där den hjälper, men tillåt variation där kapiteltypen kräver det.
- Säkerställ att varje kapitel fortfarande är lätt att skanna.

**Förväntad effekt:** Boken blir mindre monoton och mer professionellt redigerad.

**Risk:** Medel.

---

### Steg H6 – Stärk beslutsstöd och snabbval där innehållet redan finns

**Syfte:** Öka handboksnyttan utan att lägga till nya komponenter.

**Berörda filer:**

- `chapters/referens-snabbvalsguider-38.md`
- relevanta komponentkapitel
- robusthets- och felsökningskapitel

**Åtgärder:**

- Lyft fram befintliga valtabeller och checklistor.
- Gör vissa stycken mer direkt användbara som beslutshjälp.
- Lägg bara till korta sammanfattande valrader där det saknas och där befintligt innehåll redan stödjer slutsatsen.
- Undvik stora nya avsnitt.

**Exempel:**

- `Välj DRV8833 när...`
- `Välj MOSFET när...`
- `Undvik att mata motorer direkt från Arduino-kortet...`

**Förväntad effekt:** Läsaren hittar snabbare rätt lösning.

**Risk:** Låg–medel.

---

### Steg H7 – Förstärk riskkontroller och vanliga misstag

**Syfte:** Göra boken ännu mer praktisk och trygg att använda.

**Berörda filer:** Framför allt kapitel om ström, laster, motorer, drivkretsar, mätning, strömförsörjning och felsökning.

**Åtgärder:**

- Omvandla relevanta kontrollfrågor till riskkontroller.
- Lyft fram vanliga misstag där materialet redan finns.
- Gör säkerhetsrelaterade råd mer skannbara.
- Undvik att skapa skrämmande eller överdrivna säkerhetsvarningar.

**Förväntad effekt:** Boken blir starkare för praktiska byggsituationer.

**Risk:** Låg.

---

### Steg H8 – Gör slutblocket mer verktygsorienterat

**Syfte:** Stärka kapitel 36–38 som bokens avslutande arbets- och referensdel.

**Berörda filer:**

- `chapters/breadboard-till-modul-36.md`
- `chapters/modular-sensor-styrstation-37.md`
- `chapters/referens-snabbvalsguider-38.md`

**Åtgärder:**

- Gör kapitel 36 till tydligare modul- och arbetschecklista.
- Gör kapitel 37 till tydligare integrationsordning/projektmall.
- Gör kapitel 38 till renare referenskapitel utan intern planterminologi.
- Omvandla `Bygg din egen snabbguide` och liknande till mallar/verktyg snarare än övningar.

**Förväntad effekt:** Boken får ett starkare praktiskt avslut.

**Risk:** Låg–medel.

---

### Steg H9 – Uppdatera läsarvänliga korsreferenser

**Syfte:** Förbättra navigationen utan att återinföra mekaniska `Se också`-listor.

**Berörda filer:** Särskilt kapitel där nya PLAN5-tillägg och relaterade funktioner hör ihop.

**Åtgärder:**

- Ersätt interna hänvisningar med naturliga läsarhänvisningar.
- Lägg till korta hänvisningar där det tydligt hjälper läsaren.
- Undvik för långa listor i slutet av varje kapitel.
- Håll korsreferenser problembaserade.

**Exempel:**

- `Om lasten drar mer ström än Arduino-kortet tål, se kapitlet om reläer, MOSFET:ar och laster.`
- `Om sensorn använder I²C, jämför med kapitlet om kommunikation och bussar.`

**Förväntad effekt:** Boken blir lättare att använda som uppslagsverk.

**Risk:** Låg.

---

### Steg H10 – Skapa intern redaktionell stilguide för framtida ändringar

**Syfte:** Förhindra att samma problem återkommer i senare planer.

**Berörda filer:**

- Ny fil: `docs/handbook-editorial-style-guide.md`
- Eventuellt uppdatering av `docs/canon-terminology.md` eller motsvarande canonfil om projektet använder den för stil/terminologi

**Åtgärder:**

- Dokumentera godkända rubrikfamiljer.
- Dokumentera fraser att undvika.
- Dokumentera ersättningsmönster.
- Dokumentera kapiteltyper och rekommenderad struktur.
- Dokumentera hur praktiska moment ska namnges.

**Förväntad effekt:** Framtida utveckling blir mer konsekvent.

**Risk:** Låg.

---

### Steg H11 – Bygg om `build/book.md` och kontrollera markdown

**Syfte:** Säkerställa att den redigerade boken fortfarande exporterar korrekt.

**Berörda filer:**

- `build/book.md`
- eventuellt `docs/project-status.md`
- eventuellt exports om export körs i detta steg

**Åtgärder:**

- Bygg om samlad markdown efter kapiteländringar.
- Kontrollera rubriknivåer.
- Kontrollera listor och tabeller.
- Kontrollera att inga interna filreferenser läckt in i läsartext.
- Kontrollera att inga `####`-rubriker eller rå markdownproblem införts.

**Förväntad effekt:** Projektet är tekniskt redo för export.

**Risk:** Låg.

---

### Steg H12 – Exportkontroll och ny projektversion

**Syfte:** Avsluta redaktionsrundan som ny stabil basversion.

**Berörda filer:**

- `exports/`
- `README.md`
- `book.yaml`
- `docs/export-metadata.yaml`
- `docs/book-specification.md`
- `docs/project-status.md`
- ny versionsfil, exempelvis `docs/project-version-handbokstruktur-v5.md`

**Åtgärder:**

- Kör exportkontroll.
- Skapa EPUB/PDF om exportmiljön är tillgänglig.
- Uppdatera version från v4 till v5 eller motsvarande.
- Dokumentera att `[PLAN-H]` är genomförd.
- Skapa slutlig projekt-zip, exempelvis `arduino-i-praktiken-projekt-handbokstruktur-v5.zip`.

**Förväntad effekt:** En ny stabil handboksbas efter redaktionell genomgång.

**Risk:** Låg–medel beroende på exportmiljö.

## Rekommenderad arbetsordning

1. H1 – Rensa interna projektspår.
2. H2 – Ersätt lärandemålsspråk.
3. H3 – Omvandla quiz/kontrollfrågor.
4. H4 – Omklassificera praktiska moment.
5. H5 – Rubriknormalisering efter kapiteltyp.
6. H6 – Stärk beslutsstöd och snabbval.
7. H7 – Förstärk riskkontroller och vanliga misstag.
8. H8 – Gör slutblocket mer verktygsorienterat.
9. H9 – Uppdatera läsarvänliga korsreferenser.
10. H10 – Skapa redaktionell stilguide.
11. H11 – Bygg om och markdownkontrollera.
12. H12 – Exportkontroll och ny projektversion.

## Rekommenderad zip-namngivning

Under genomförandet:

```text
arduino-i-praktiken-projekt-PLAN-H-steg-01.zip
arduino-i-praktiken-projekt-PLAN-H-steg-02.zip
...
arduino-i-praktiken-projekt-PLAN-H-steg-12.zip
```

Slutversion:

```text
arduino-i-praktiken-projekt-handbokstruktur-v5.zip
```

## Kontrollista för varje genomförandesteg

Innan varje steg markeras som klart:

- Berörda kapitel eller dokument har faktiskt lästs.
- Endast planerade filer har ändrats.
- Inga oavsiktliga kapiteländringar har gjorts.
- `docs/project-status.md` är uppdaterad.
- Om steglogg används är den uppdaterad.
- Ny projekt-zip har skapats.
- Ändrade filer listas i chattsvaret.

## Förväntad slutbild

När `[PLAN-H]` är genomförd bör boken fortfarande innehålla samma tekniska bredd som v4, men kännas mer som en färdig professionell handbok:

- färre kurslika formuleringar,
- inga interna projektspår i läsartext,
- tydligare handboksrubriker,
- bättre praktiska checklistor,
- bättre risk- och felsökningsstöd,
- mer varierad struktur mellan olika kapiteltyper,
- starkare avslutande referensdel.

## Relation till tidigare planer

`PLAN1`–`PLAN5` utvecklade bokens innehåll, struktur och komponenttäckning. `[PLAN-H]` ska inte fortsätta lägga till innehåll på samma sätt. Den ska konsolidera boken redaktionellt och göra `handbokstruktur-v4` till en mer sammanhållen handboksbas.

## Beslutspunkt innan genomförande

Innan `[PLAN-H]` börjar genomföras bör användaren godkänna planen eller justera:

- om alla H-steg ska genomföras,
- om steg H4 ska vara strikt eller varsamt,
- om slutversionen ska heta `handbokstruktur-v5`,
- om EPUB/PDF ska byggas först i H12 eller även under mellanliggande steg.

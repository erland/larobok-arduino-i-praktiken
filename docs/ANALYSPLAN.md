# [ANALYSPLAN]

## Syfte

Denna analysplan startar från projektversion `handbokstruktur-v4` och ska steg för steg leda fram till en separat redaktionell arbetsplan: `[PLAN-H]`.

Målet är inte att ändra bokmanuset i analysfasen. Målet är att förstå hur boken fungerar som praktisk handbok, vilka kapitel som fortfarande bär spår av lärobok/kursbok, vilka återkommande sektioner som bör normaliseras och vilka konkreta redaktionella åtgärder som bör ingå i `[PLAN-H]`.

## Grundprinciper

- Analysfasen får inte ändra kapiteltexten.
- Varje analyssteg ska läsa berörda kapitel i faktiskt projektinnehåll, inte bara markera steget som klart.
- Varje analyssteg ska dokumenteras i en egen fil i `docs/`.
- Varje analyssteg ska uppdatera `docs/plan-h-analysis-log.md`.
- `[PLAN-H]` skapas först när alla analyssteg är genomförda.
- `[PLAN-H]` ska vara en arbetsplan för senare redigering, inte själva redigeringen.

## Analysfrågor som återkommer i varje kapitelblock

Varje kapitelblock ska bedömas utifrån följande frågor:

1. **Handboksidentitet**  
   Känns kapitlet som en praktisk handbok, en lärobok, en workshop eller ett uppslagsverk?

2. **Läsartilltal**  
   Finns formuleringar som låter kravställande, skolmässiga eller provorienterade, till exempel "Efter kapitlet ska du kunna"?

3. **Rubrikstruktur**  
   Är rubrikerna relevanta för kapitlets typ, eller återanvänds samma mall mekaniskt?

4. **Snabb orientering**  
   Hjälper avsnittet läsaren att navigera, eller låter det som lärandemål?

5. **Praktiskt test och Prova själv**  
   Är praktiska moment motiverade av kapitlets innehåll, eller skapas teoriexperiment som gör boken mer lärobokslik?

6. **Quiz och kontrollfrågor**  
   Finns avsnitt som "Kontrollera att du hänger med" eller liknande, och bör de ersättas med handboksformat som "Vanliga missförstånd", "Tänk på" eller "Snabb kontroll i praktiken"?

7. **Interna projektartefakter**  
   Finns referenser till filer som `docs/lookup-index.md`, `canon`, `build/book.md`, projektstatus eller andra interna arbetsdokument som inte hör hemma i läsartexten?

8. **Överlapp och repetition**  
   Överlappar sektioner varandra, till exempel "Praktiskt test" och "Prova själv"?

9. **Kapiteltyp**  
   Vilken kapiteltyp bör kapitlet tillhöra: orientering, teori/begrepp, praktisk komponent, robusthet/säkerhet, metod/projekt eller referens?

10. **Förslag till PLAN-H-regel**  
   Vilka generella regler bör härledas från observationerna?

## Bedömningsskala

Varje kapitelblock ska avslutas med en sammanfattande bedömning:

- **Handbokskänsla:** 1–5
- **Läroboksspår:** låg / medel / hög
- **Behov av redaktionell åtgärd:** låg / medel / hög
- **Risk vid ändring:** låg / medel / hög

## Steg 1 – Start och metodkalibrering

**Omfattning:** Projektets övergripande dokument och kapitelstruktur.

**Analys:**

- Läs `README.md`, `book.yaml`, `docs/book-specification.md`, `docs/project-version-handbokstruktur-v4.md`, `docs/chapter-typology.md` om den finns, och kapitelöversikten.
- Fastställ vad v4 säger att boken är.
- Identifiera vilka kapiteltyper som redan finns i projektet.
- Formulera analysens definition av "praktisk handbok" för detta projekt.
- Skapa en lista över formuleringar och sektionstyper som särskilt ska spåras i kommande steg.

**Resultatfil:** `docs/plan-h-analysis-step-01-method-and-identity.md`

## Steg 2 – Kapitel 00–05

**Omfattning:**

- `chapters/00-inledning.md`
- kapitel 1–5 enligt projektets kapitelordning.

**Fokus:**

- Inledningens roll och eventuella interna filreferenser.
- Tidiga teori- och orienteringskapitel.
- "Snabb orientering" och kravliknande formuleringar.
- Eventuella quiz/kontrollfrågor.
- Om praktiska moment är motiverade eller bör tas bort.

**Resultatfil:** `docs/plan-h-analysis-step-02-chapters-00-05.md`

## Steg 3 – Kapitel 06–10

**Omfattning:** Kapitel 6–10 enligt projektets kapitelordning.

**Fokus:**

- Grundfunktioner, signaler och kommunikation.
- Skillnaden mellan förklaring, test, exempel och övning.
- Om teoretiska kapitel bör få en renare handboksstruktur.
- Formuleringar som bör ersättas med mjukare handboksspråk.

**Resultatfil:** `docs/plan-h-analysis-step-03-chapters-06-10.md`

## Steg 4 – Kapitel 11–15

**Omfattning:** Kapitel 11–15 enligt projektets kapitelordning.

**Fokus:**

- Plattform, utvecklingsmiljö och användning.
- Om kapitel fungerar som guide, referens eller lärobok.
- Onödigt utbildningsspråk.
- Rubriker som bör bli mer handboksnära.

**Resultatfil:** `docs/plan-h-analysis-step-04-chapters-11-15.md`

## Steg 5 – Kapitel 16–20

**Omfattning:** Kapitel 16–20 enligt projektets kapitelordning.

**Fokus:**

- Komponent- och aktuatorrelaterade kapitel.
- Om "Praktiskt test" och "Prova själv" båda behövs.
- Om praktiska avsnitt bör omformas till "Exempel", "Snabb kontroll" eller "Vanliga fel".
- Om kapitlen har bra beslutsstöd.

**Resultatfil:** `docs/plan-h-analysis-step-05-chapters-16-20.md`

## Steg 6 – Kapitel 21–25

**Omfattning:** Kapitel 21–25 enligt projektets kapitelordning.

**Fokus:**

- Laster, displayer, ljus, optik, närvaro och sensorliknande kapitel.
- Hur senare komponentkapitel använder praktiska tester.
- Om referenser mellan kapitel hjälper eller stör.
- Om det finns överlapp mellan förklaring, test och självständiga moment.

**Resultatfil:** `docs/plan-h-analysis-step-06-chapters-21-25.md`

## Steg 7 – Kapitel 26–30

**Omfattning:** Kapitel 26–30 enligt projektets kapitelordning.

**Fokus:**

- Sensorer, robusthet och I/O-expansion.
- Om kapitel bör innehålla felsökning hellre än quiz.
- Om avsnitten stöder snabb problemlösning.
- Identifiera handboksformat som bör återanvändas i PLAN-H.

**Resultatfil:** `docs/plan-h-analysis-step-07-chapters-26-30.md`

## Steg 8 – Kapitel 31–35

**Omfattning:** Kapitel 31–35 enligt projektets kapitelordning.

**Fokus:**

- Drivkretsar, signalanpassning, strömförsörjning och robusta kretsar.
- Säkerhet, felrisker och praktiska rekommendationer.
- Om kapitlen bör ha mer "När väljer du vad?" och mindre övningsspråk.
- Om PLAN5-tillägg sitter naturligt i kapitlen.

**Resultatfil:** `docs/plan-h-analysis-step-08-chapters-31-35.md`

## Steg 9 – Kapitel 36–38

**Omfattning:** Kapitel 36–38 enligt projektets kapitelordning.

**Fokus:**

- Övergång från byggpraktik till referens.
- Referenskapitlets användbarhet.
- Snabbvalsguider, uppslagsstruktur och navigation.
- Om kapitel 38 bör stärkas ytterligare med beslutstabeller, felsökning eller korsreferenser.
- Om interna indexdokument nämns i läsartexten.

**Resultatfil:** `docs/plan-h-analysis-step-09-chapters-36-38.md`

## Steg 10 – Tväranalys av hela boken

**Omfattning:** Samtliga tidigare analysrapporter.

**Analys:**

- Sammanställ återkommande problem.
- Sammanställ formuleringar som bör ersättas.
- Identifiera sektioner som bör tas bort, slås ihop eller byta namn.
- Definiera rekommenderade kapitelmallar per kapiteltyp.
- Identifiera vilka kapitel som kräver redigering och vilken typ av redigering.

**Resultatfil:** `docs/plan-h-analysis-step-10-cross-analysis.md`

## Steg 11 – Prioritering och åtgärdskarta

**Omfattning:** Samtliga identifierade åtgärder.

**Analys:**

Dela in åtgärder i tre nivåer:

- **Kritiska:** bör åtgärdas för att boken tydligt ska kännas som handbok.
- **Rekommenderade:** höjer kvalitet och läsupplevelse.
- **Valfria:** förbättringar som kan göras senare utan att störa helheten.

För varje åtgärd anges:

- berörda kapitel,
- berörda dokument,
- typ av ändring,
- risknivå,
- uppskattad effekt.

**Resultatfil:** `docs/plan-h-analysis-step-11-prioritization.md`

## Steg 12 – Skapa [PLAN-H]

**Omfattning:** Slutlig redaktionell plan.

**PLAN-H ska innehålla:**

- syfte,
- arbetsprinciper,
- stegvis genomförande,
- berörda filer per steg,
- tydliga regler för kapiteltyper,
- regler för att ersätta läroboksspråk,
- regler för när praktiska moment ska behållas,
- regler för att ta bort interna projektartefakter från läsartext,
- kvalitetssäkring och exportkontroll,
- versionssättning efter genomförd PLAN-H.

**Resultatfil:** `docs/PLAN-H.md`

## Slutregel

När `[ANALYSPLAN]` är genomförd ska projektet fortfarande vara innehållsmässigt oförändrat jämfört med v4, förutom analysdokument och projektstatus. Först efter att `[PLAN-H]` godkänts börjar redigering av kapitel och boktext.


## Slutstatus

`[ANALYSPLAN]` är genomförd till och med steg 12.

Resultatet är:

- `docs/PLAN-H.md`

Bokmanuset har inte ändrats under analysfasen.

# [ANALYSPLAN] steg 11 – Prioritering och åtgärdskarta

Datum: 2026-07-01  
Basversion: `handbokstruktur-v4` med `[ANALYSPLAN]` steg 1–10 genomförda  
Status: Genomförd  
Resultattyp: Prioritering och åtgärdskarta. Inga kapitel eller bokmanus har ändrats.

## Syfte

Detta steg väger samman analysresultaten från steg 1–10 och prioriterar vilka redaktionella åtgärder som bör ingå i kommande `[PLAN-H]`.

Målet är att skapa en arbetsbar åtgärdskarta, inte att redigera boken direkt. Prioriteringen ska göra det lättare att utforma `[PLAN-H]` i rätt ordning, med tydliga risknivåer och förväntad effekt.

## Underlag

Prioriteringen bygger på:

- `docs/plan-h-analysis-step-01-method-and-identity.md`
- `docs/plan-h-analysis-step-02-chapters-00-05.md`
- `docs/plan-h-analysis-step-03-chapters-06-10.md`
- `docs/plan-h-analysis-step-04-chapters-11-15.md`
- `docs/plan-h-analysis-step-05-chapters-16-20.md`
- `docs/plan-h-analysis-step-06-chapters-21-25.md`
- `docs/plan-h-analysis-step-07-chapters-26-30.md`
- `docs/plan-h-analysis-step-08-chapters-31-35.md`
- `docs/plan-h-analysis-step-09-chapters-36-38.md`
- `docs/plan-h-analysis-step-10-cross-analysis.md`

## Prioriteringsprinciper

Åtgärderna delas in i tre nivåer:

- **Kritiska:** bör genomföras för att v5 tydligt ska kännas som en praktisk handbok och inte som kursbok/lärobok.
- **Rekommenderade:** höjer läsupplevelse, konsekvens och professionell känsla, men är inte lika identitetskritiska.
- **Valfria:** kan genomföras senare eller endast där tid och omfattning tillåter.

Varje åtgärd bedöms med:

- berörda kapitel,
- berörda dokument,
- typ av ändring,
- risknivå,
- uppskattad effekt,
- rekommenderad hantering i `[PLAN-H]`.

## Kritiska åtgärder

### K1. Ta bort interna projektartefakter ur läsartext

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Särskilt `00-inledning.md` och kapitel 38 |
| Berörda dokument | Kapiteltext, eventuellt `build/book.md` vid senare export |
| Typ av ändring | Redaktionell rensning |
| Risknivå | Låg |
| Effekt | Hög |

#### Observation

Analysen har identifierat interna projektspår som inte hör hemma i läsartext. Det tydligaste exemplet är referens till `docs/lookup-index.md` i inledningen och intern planterminologi som `PLAN5` i kapitel 38.

#### Rekommenderad PLAN-H-regel

Läsartexten får inte referera till projektfiler, interna plansteg, `docs/`, `build/`, canon, projektstatus eller arbetsdokument. Sådant ska endast finnas i projektets dokumentation.

#### Förväntad effekt

Boken känns mer färdig, professionell och fristående för läsaren.

---

### K2. Ersätt lärandemålsspråk med användningsnytta

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Många kapitel, särskilt tidiga kapitel och flera komponent-/grundfunktionskapitel |
| Berörda dokument | Kapiteltext |
| Typ av ändring | Ton- och formuleringnormalisering |
| Risknivå | Låg |
| Effekt | Hög |

#### Observation

Formuleringar som `Efter kapitlet ska du kunna`, `Efter kapitlet ska du framför allt kunna skilja på` och liknande gör boken mer prov- och lärobokslik än handboksnära.

#### Rekommenderad PLAN-H-regel

Byt kravformuleringar mot användningsnytta. Exempel:

| Nuvarande typ | Rekommenderad handboksform |
|---|---|
| Efter kapitlet ska du kunna skilja på... | Här får du en praktisk överblick över skillnaden mellan... |
| Efter kapitlet ska du framför allt kunna... | Kapitlet hjälper dig att känna igen när... |
| Kontrollera att du hänger med | Vanliga missförstånd / Snabb kontroll i praktiken / Tänk på |

#### Förväntad effekt

Läsaren får lägre prestationskänsla och boken får tydligare handboksidentitet.

---

### K3. Omvandla quiz- och kontrollfrågor till handboksverktyg

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Särskilt kapitel 1, 3, 4, 5 samt flera senare kapitel med `Kontrollera ditt val` |
| Berörda dokument | Kapiteltext |
| Typ av ändring | Struktur- och rubriknormalisering |
| Risknivå | Låg–medel |
| Effekt | Hög |

#### Observation

Avsnitt som `Kontrollera att du hänger med`, `Kontrollera ditt val` och liknande kan ge kurs-/quizkänsla. Vissa innehåller värdefullt beslutsstöd, men formen bör ändras.

#### Rekommenderad PLAN-H-regel

Quizliknande avsnitt ska inte tas bort automatiskt. De ska omklassificeras:

| Innehållstyp | Ny rubrik/funktion |
|---|---|
| Begreppsfrågor | Vanliga missförstånd |
| Valfrågor | Valchecklista |
| Riskfrågor | Riskkontroll |
| Felsökningsfrågor | Felsökningsordning |
| Avslutande självtest | Snabb kontroll i praktiken |

#### Förväntad effekt

Boken behåller pedagogisk tydlighet men känns mindre som skolmaterial.

---

### K4. Omklassificera `Praktiskt test`, `Prova själv` och `Prova vidare`

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Nästan hela boken, men med olika behov beroende på kapiteltyp |
| Berörda dokument | Kapiteltext |
| Typ av ändring | Kapiteltypsbaserad strukturredigering |
| Risknivå | Medel |
| Effekt | Mycket hög |

#### Observation

`Praktiskt test` används i v4 för flera olika saker: introduktionsexempel, verifiering, huvudövning, felsökning, beslutsstöd, arbetsmönster och fördjupning. I vissa teorikapitel skapar detta teoriexperiment som gör boken mer lärobokslik. I komponent- och robusthetskapitel är praktiken däremot ofta central.

#### Rekommenderad PLAN-H-regel

Praktiska moment ska inte tas bort generellt. De ska namnges efter funktion:

| Faktisk funktion | Rekommenderad rubrik |
|---|---|
| Visa minsta fungerande koppling | Minsta fungerande koppling |
| Kontrollera att komponenten fungerar | Verifiera modulen |
| Visa återanvändbar lösning | Referensmönster |
| Kontrollera risk före byggande | Riskkontroll |
| Felsöka ett symptom | Felsökningsmönster |
| Visa arbetsgång | Arbetsmönster |
| Visa projektintegration | Integrationsordning |
| Skapa egen referens | Mall |

#### Förväntad effekt

Boken får mer professionell struktur utan att tappa praktisk användbarhet.

---

### K5. Inför kapiteltypsspecifika rubrikfamiljer

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Alla kapitel |
| Berörda dokument | Kapiteltext, eventuellt `docs/chapter-templates-by-type.md` |
| Typ av ändring | Strukturprincip |
| Risknivå | Medel |
| Effekt | Mycket hög |

#### Observation

En återkommande orsak till lärobokskänsla är att samma yttre mall syns i många olika kapiteltyper. Orienteringskapitel, komponentkapitel, robusthetskapitel och referenskapitel behöver olika struktur.

#### Rekommenderad PLAN-H-regel

`[PLAN-H]` bör definiera rubrikfamiljer för:

1. Inledning
2. Orienterings- och begreppskapitel
3. Grundfunktionskapitel
4. Kort- och plattformskapitel
5. Komponent- och sensorkapitel
6. Robusthets- och säkerhetskapitel
7. Metod- och projektkapitel
8. Referenskapitel

#### Förväntad effekt

Boken känns mindre mekanisk och mer redaktionellt mogen.

---

## Rekommenderade åtgärder

### R1. Bevara och stärka snabbvalsguiderna

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Särskilt kapitel 38, men även snabbvalsrutor i många kapitel |
| Typ av ändring | Förstärkning, inte rensning |
| Risknivå | Låg |
| Effekt | Hög |

Snabbvalsguiderna är en av bokens största styrkor. De bör inte kortas ned i en redaktionell rensning. Däremot bör de få renare handboksram och konsekventa rubriker.

### R2. Gör `Snabb orientering` mer varierad och kapitelanpassad

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Många kapitel |
| Typ av ändring | Rubrik- och formuleringnormalisering |
| Risknivå | Låg |
| Effekt | Medel–hög |

`Snabb orientering` fungerar bra när den hjälper läsaren att navigera, men sämre när den låter som lärandemål. I `[PLAN-H]` bör den ibland ersättas av:

- `När du använder detta`
- `Vad du behöver veta först`
- `Snabb överblick`
- `När detta passar`
- `Typiska användningsfall`
- `Begränsningar att känna till`

### R3. Lyft positiva stilmodeller

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Kapitel 2, 5, 14, 15, 24, 35, 38 |
| Typ av ändring | Intern stilmodell |
| Risknivå | Låg |
| Effekt | Medel–hög |

Flera kapitel visar redan en stark handbokston. `[PLAN-H]` bör använda dem som stilreferenser:

- Kapitel 2: beslutsstöd.
- Kapitel 5: praktisk grundfunktion.
- Kapitel 14–15: kort- och plattformshandbok.
- Kapitel 24: komponentpresentation med exempel/variation.
- Kapitel 35: felsökningsmetodik.
- Kapitel 38: referensnav och snabbval.

### R4. Stärk risk- och säkerhetsrutor

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Särskilt 19–21, 23–25, 28, 31, 33–34 |
| Typ av ändring | Bevarande och tydligare placering |
| Risknivå | Låg |
| Effekt | Hög |

Varningar om ström, extern matning, gemensam jord, nivåskiftning, motorstörningar, flybackdioder, batterier och mätning ska bevaras och gärna göras mer konsekventa.

### R5. Stärk läsarvänliga korsreferenser

| Fält | Bedömning |
|---|---|
| Berörda kapitel | Många kapitel, särskilt drivning, signalanpassning, strömförsörjning och felsökning |
| Typ av ändring | Navigationsförbättring |
| Risknivå | Låg |
| Effekt | Medel |

Korsreferenser bör stärkas mellan närliggande ämnen, men utan interna dokumentreferenser. Exempel:

- motorer → drivkretsar → strömförsörjning → felsökning
- sensorer → signalanpassning → kommunikation → felsökning
- plattformskort → nivåskiftning → bussar

### R6. Gör kapitel 36–38 till tydligare slutverktyg

| Fält | Bedömning |
|---|---|
| Berörda kapitel | 36–38 |
| Typ av ändring | Slutblocksförstärkning |
| Risknivå | Låg–medel |
| Effekt | Hög |

Slutblocket bör rama in bokens användning efter första läsning:

- Kapitel 36: modulchecklista och arbetsmönster.
- Kapitel 37: integrationsordning och projektmall.
- Kapitel 38: ren referens, snabbval och mallar.

## Valfria åtgärder

### V1. Skapa en kort redaktionell stilguide för v5

| Fält | Bedömning |
|---|---|
| Berörda dokument | Nytt dokument i `docs/` |
| Typ av ändring | Stöd för framtida redigering |
| Risknivå | Låg |
| Effekt | Medel |

En stilguide kan innehålla exempel på önskat handboksspråk, rubrikfamiljer och förbjudna interna projektspår.

### V2. Skapa en checklista för framtida kapitel

| Fält | Bedömning |
|---|---|
| Berörda dokument | `docs/quality-checklist.md` eller nytt dokument |
| Typ av ändring | Kvalitetssäkring |
| Risknivå | Låg |
| Effekt | Medel |

Checklistan kan användas vid framtida PLAN6/PLAN-H-liknande arbete.

### V3. Skapa separat lista över positiva exempel

| Fält | Bedömning |
|---|---|
| Berörda dokument | Nytt dokument i `docs/` |
| Typ av ändring | Redaktionsstöd |
| Risknivå | Låg |
| Effekt | Låg–medel |

Det kan vara användbart att ha exempel på bra före/efter-formuleringar, men detta är inte nödvändigt för att skriva `[PLAN-H]`.

## Rekommenderad arbetsordning för [PLAN-H]

Steg 11 rekommenderar att `[PLAN-H]` inte börjar med kapitel 1 och arbetar linjärt. Den bör i stället genomföras i denna ordning:

1. **Global rensning av interna projektspår**  
   Låg risk och hög effekt.

2. **Global ersättning av lärandemålsspråk**  
   Låg risk och hög synlig effekt.

3. **Definition av kapiteltypsspecifika rubrikfamiljer**  
   Måste göras innan praktiska sektioner redigeras.

4. **Omklassificering av praktiska moment per kapiteltyp**  
   Största kvalitetslyftet, men kräver noggrannhet.

5. **Omvandling av quiz/kontrollfrågor till handboksverktyg**  
   Genomförs efter att rubrikfamiljerna är fastställda.

6. **Stärkning av referens, snabbval, riskrutor och korsreferenser**  
   Slutlig förbättringsrunda.

7. **Markdown- och exportkontroll**  
   Säkerställer att redigeringen inte skadar EPUB/PDF.

8. **Versionssättning av ny handboksbas**  
   Förslagsvis `handbokstruktur-v5` eller annan namnstandard som användaren väljer.

## Kapitelgrupper med störst åtgärdsbehov

| Kapitelgrupp | Åtgärdsbehov | Kommentar |
|---|---|---|
| Kapitel 00–05 | Hög | Tydliga interna referenser, tidiga läroboksspår och quiz-/testkänsla. |
| Kapitel 06–10 | Medel | Starka grundfunktioner, men praktiken bör ramas om som verifiering/validering. |
| Kapitel 11–15 | Medel | Bra plattformskapitel, men slutsektioner bör bli kortprofil, porteringstest och beslutschecklistor. |
| Kapitel 16–20 | Medel | Praktiskt starkt block; flera praktiska sektioner behöver funktionsmärkas. |
| Kapitel 21–25 | Medel | Sensor- och komponentinnehåll bör bevaras men få tydligare verifierings-/riskformat. |
| Kapitel 26–30 | Medel | Starkt handboksblock; rubriker och kontrollsektioner bör normaliseras. |
| Kapitel 31–35 | Låg–medel | Mycket starkt block; främst rubrik- och ramjustering. |
| Kapitel 36–38 | Medel | Slutblocket är starkt men behöver renare mall-/referensram och borttagning av internt planspråk. |

## Riskbedömning inför PLAN-H

### Låg risk

- Ta bort interna filreferenser.
- Byta `Efter kapitlet ska du kunna` till mjukare formuleringar.
- Byta `Kontrollera att du hänger med` till `Vanliga missförstånd` eller `Snabb kontroll i praktiken`.
- Byta `PLAN5-tillägg` till läsarvänlig rubrik.

### Medel risk

- Slå ihop eller ta bort överlappande `Praktiskt test` och `Prova själv`.
- Omforma praktiska moment i teorikapitel.
- Ändra rubrikstruktur i många kapitel samtidigt.

### Högre risk

- Ta bort praktiska moment i komponent-, sensor- och robusthetskapitel.
- Korta snabbvalsguider.
- Minska varningar, riskrutor eller felsökningsdelar.

Dessa högre riskåtgärder bör undvikas eller göras mycket försiktigt.

## Slutsats

Steg 11 visar att `[PLAN-H]` bör vara en koncentrerad redaktionell plan, inte en ny innehållsplan.

De mest värdefulla åtgärderna är:

1. rensa bort interna projektspår,
2. ersätta läroboksspråk,
3. göra praktiska moment funktionsmärkta,
4. omvandla quiz/kontrollfrågor till checklistor och handboksverktyg,
5. införa kapiteltypsspecifika rubrikfamiljer,
6. bevara bokens starka praktiska innehåll.

Med denna prioritering kan `[PLAN-H]` ge ett stort kvalitetslyft utan att ändra bokens ämnesmässiga omfattning.

# [PLAN-H] steg H10 – Intern redaktionell stilguide

Datum: 2026-07-01  
Status: Genomfört  
Steg: H10  
Syfte: Skapa en intern stilguide som förhindrar att boken glider tillbaka mot lärobok, kursbok eller intern projektlogg vid framtida ändringar.

## Sammanfattning

Steg H10 har genomförts utan ändringar i bokmanuset. Arbetet har i stället skapat och kopplat in interna redaktionella stöd så att kommande ändringar kan göras konsekvent.

Den viktigaste nya filen är:

- `docs/handbook-editorial-style-guide.md`

Den kompletterar den tidigare rubrikreferensen:

- `docs/chapter-templates-by-type.md`

## Gjorda ändringar

- Skapade en intern redaktionell stilguide för handbokston.
- Dokumenterade fraser som bör undvikas.
- Dokumenterade rekommenderade ersättningsmönster.
- Dokumenterade kapiteltyper och deras redaktionella funktion.
- Dokumenterade hur praktiska moment ska namnges.
- Dokumenterade riktlinjer för beslutsstöd, riskkontroll och korsreferenser.
- Kopplade `docs/chapter-templates-by-type.md` till den nya stilguiden.

## Vad stilguiden styr

Stilguiden styr inte tekniska fakta. Den styr hur innehållet bör ramas in redaktionellt.

Den ska användas vid framtida arbete med:

- rubriker,
- kapitelstruktur,
- praktiska moment,
- snabbval,
- riskkontroller,
- kontrollfrågor,
- korsreferenser,
- ton och läsartilltal.

## Viktiga principer som dokumenterats

- Boken ska vara en praktisk handbok, inte en kursbok.
- Praktiska moment ska vara verifieringar, referensmönster, riskkontroller eller arbetsmönster.
- Kontrollfrågor ska i normalfallet vara checklistor eller användningskontroller.
- Beslutsstöd ska ligga nära de val läsaren faktiskt behöver göra.
- Interna projektspår ska aldrig förekomma i läsartext.
- Nya kapitel ska först klassificeras efter kapiteltyp innan rubriker bestäms.

## Berörda filer

- `docs/handbook-editorial-style-guide.md`
- `docs/chapter-templates-by-type.md`
- `docs/PLAN-H-step-10-editorial-style-guide.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

## Kontroll

- Inga kapitel i `chapters/` har ändrats.
- `build/book.md` har inte byggts om, eftersom bokmanuset inte ändrats.
- Inga nya H4-rubriker har införts i bokmanus.
- Inga interna projektspår har införts i bokmanus.

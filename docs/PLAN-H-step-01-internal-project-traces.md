# [PLAN-H] steg H1 – Rensa interna projektspår i läsartext

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-ANALYSPLAN-steg-12.zip`  
Status: Genomförd

## Syfte

Göra läsartexten fristående från projektets interna arbetsfiler och tidigare utvecklingsplaner.

Steget ändrar inte bokens tekniska innehåll. Det rensar endast formuleringar som hör hemma i projektets arbetsmaterial snarare än i den publicerade boken.

## Genomförda ändringar

### Inledning

Filen `chapters/00-inledning.md` innehöll en direkt hänvisning till `docs/lookup-index.md`.

Den har ersatts med en läsarvänlig formulering om sakregister och snabbguider i slutet av boken.

### Kapitel 38

Filen `chapters/referens-snabbvalsguider-38.md` innehöll rubriken `Snabbguide: PLAN5-tillägg i praktiken` och en brödtext som nämnde `PLAN5`.

Det har skrivits om till en neutral läsarformulering:

- rubriken handlar nu om vanliga kompletterande moduler och kretsar,
- brödtexten beskriver praktiska behov i växande projekt utan att nämna intern planhistorik.

### Kapitel 28

Filen `chapters/strom-spanning-energi-28.md` innehöll en hänvisning till projektets `canon` och `README`.

Den har skrivits om till en läsarvänlig rekommendation om att dokumentera metoden i projektets egna anteckningar.

## Kontroll

Efter ändringen har kapiteltexterna sökts igenom efter interna projektspår:

- `docs/`
- `build/`
- `canon`
- `project-status`
- `PLAN5`
- `[PLAN...]`

Inga sådana interna projektspår finns kvar i `chapters/`.

## Berörda filer

- `chapters/00-inledning.md`
- `chapters/referens-snabbvalsguider-38.md`
- `chapters/strom-spanning-energi-28.md`
- `build/book.md`
- `docs/PLAN-H-step-01-internal-project-traces.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

## Rekommendation inför nästa steg

Nästa steg enligt `[PLAN-H]` är H2: ersätt kravliknande lärandemål i `Snabb orientering`.

Det bör göras kapitelvis eller i tydliga kapitelblock eftersom formuleringarna varierar något mellan kapitlen.

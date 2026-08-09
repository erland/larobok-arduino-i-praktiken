# [PLAN-H] steg H11 – Markdownbygge och kontroll

Datum: 2026-07-01  
Bas: `arduino-i-praktiken-projekt-PLAN-H-steg-10.zip`  
Status: Genomfört

## Syfte

Steg H11 säkerställer att den redigerade handboken efter steg H1–H10 fortfarande har ett konsekvent samlat manus och att kapiteltexterna är tekniskt redo inför exportkontroll och ny version i H12.

## Genomförda kontroller

- `build/book.md` har byggts om från kapitelordningen i `docs/export-metadata.yaml`.
- Projektets lokala validering har körts med `scripts/export-book.py validate`.
- Kapitelordningen i metadata har kontrollerats mot faktiska kapitel.
- Varje kapitel har kontrollerats för exakt en H1-rubrik utanför kodblock.
- H4-rubriker eller djupare rubriker har kontrollerats.
- Kodblock har kontrollerats för balanserade kodstängsel.
- Kapiteltexterna har sökts igenom efter interna projektspår och gamla kurs-/mallrubriker.

## Resultat

Valideringen gav inga projektvarningar:

```text
Validering klar utan varningar.
```

Kontrollresultat:

| Kontroll | Resultat |
|---|---|
| Saknade kapitel i metadataordning | 0 |
| Extra kapitel utanför metadataordning | 0 |
| Kapitel med fel H1-antal utanför kodblock | 0 |
| H4-rubriker eller djupare | 0 |
| Obalanserade kodblock | 0 |
| Kvarvarande interna projektspår i kapiteltext | 0 |
| Kvarvarande gamla kurs-/mallrubriker | 0 |

## Mindre korrigering

En kvarvarande läsarformulering i `chapters/00-inledning.md` nämnde den tidigare rubriken `Snabb orientering`. Den har ersatts med en mer generell formulering om kapitlens överblickar, snabbval, snabbreferenser, vanliga misstag och felsökningsavsnitt.

Detta är en redaktionell konsekvensjustering efter H5 och ändrar inte bokens tekniska innehåll.

## Berörda filer

- `chapters/00-inledning.md`
- `build/book.md`
- `docs/PLAN-H-step-11-markdown-build-check.md`
- `docs/plan-h-implementation-log.md`
- `docs/project-status.md`

## Slutsats

Projektet är tekniskt redo för steg H12: exportkontroll och ny projektversion.

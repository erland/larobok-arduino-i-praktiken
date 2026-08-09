# FINAL-PUTS efter PLAN-E

Datum: 2026-07-02  
Version: `plan-e-final-puts`

## Syfte

Detta steg gör en sista konsekvensputs av bokprojektet efter PLAN-E. Fokus är inte att lägga till nya exempel, utan att säkra att den senaste versionen uppträder som en sammanhållen praktisk handbok och referens.

## Genomförda ändringar

- `book.yaml` och `docs/export-metadata.yaml` har uppdaterats till `plan-e-final-puts`.
- `README.md` och `docs/project-status.md` har uppdaterats från äldre `handbokstruktur-v5`-status till aktuell PLAN-E-slutputs.
- `chapters/00-inledning.md` har justerats så boken beskrivs som praktisk handbok och referens.
- Kvarvarande `lärobok`-formuleringar i kapitelmanus har ersatts med mer passande handboksformuleringar.
- `experiment`-språk har putsats selektivt där det gav labb-/kurskänsla, särskilt i inledningen, kapitel 3, 23, 31, 33 och 36.
- Tekniskt rimliga användningar av ord som `experiment`, `experimentera` och `experimentell` kan finnas kvar när de beskriver prototypande, utforskande test eller komponenternas karaktär.

## Kontroller

- Inga `lärobok`-träffar kvar i kapitelmanus.
- Inga `experimentlogg`-träffar kvar i kapitelmanus.
- Inga gamla rubriker som `### Mål`, `### Syfte`, `### Material` eller `### Reflektion` i kapitelmanus.
- Inga H4-rubriker.
- Kodblock är balanserade.
- `build/book.md` har byggts om.
- EPUB-export har skapats enligt projektets standard.

## Resultat

Denna version bör betraktas som en mogen releasekandidat efter PLAN-E.

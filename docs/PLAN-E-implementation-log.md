# PLAN-E – implementation logg

## 2026-07-02 – E1, kapitel 1–8

Utgångspunkt: `arduino-i-praktiken-projekt-v5-post-finputs-epub-export.zip`.

Genomförda ändringar:

- Kapitel 2: ändrade `Robot eller mekaniskt experiment` till `Robot eller mekaniskt projekt`.
- Kapitel 3: förstärkte I2C-scanner-mönstret genom att koppla det tydligare till senare kapitel om displayer, miljösensorer, I/O-expansion och felsökning.
- Kapitel 4: omformade befintlig mätkontroll till `Referensmönster: minsta säkra koppling med LED, knapp och analog signal`.
- Kapitel 5: omformade knappmönstret till `Referensmönster: robust knappmodul utan delay`, bytte labbliknande underrubriker och ersatte fler-kort-tabellen med praktiska kontrollpunkter.
- Kapitel 6: gjorde potentiometerexemplet mer handboksnära och lade till `Från potentiometer till sensor`.
- Kapitel 7: gjorde den analoga LED-fade-varianten helt tidsstyrd med `millis()` i stället för `delay(20)`.
- Kapitel 8: lade till `Referensmönster: timeout och säkert standardläge` som generiskt robusthetsmönster före plattformsspecifik watchdog-kod.
- `build/book.md` byggdes om.

Kontroll:

- Inga H4-rubriker i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- De nya och omformade E1-avsnitten använder handbokston: referensmönster, kontrollpunkter, förväntat beteende och praktiska användningsråd.
## 2026-07-02 – E2, kapitel 9–16

Utgångspunkt: `arduino-i-praktiken-projekt-plan-e-steg-01-kapitel-01-08.zip`.

Genomförda ändringar:

- Kapitel 9: lade till ett kort SPI-mönster för delad buss och separata chip select-pinnar.
- Kapitel 10: omformade porteringstestet till `Referensmönster: samma lilla projekt på UNO, Nano och Mega`.
- Kapitel 11: lade till praktisk kortidentifiering innan kodfelsökning.
- Kapitel 12: lade till moderna korts praktiska vinster och omformade porteringskontrollen till referensmönster.
- Kapitel 13: bytte kvarvarande `Variationer` i referensmönstret till `Anpassningar`.
- Kapitel 14: lade till `ESP32-specifik variant: deep sleep för batterinod`.
- Kapitel 15: lade till `Picos unika styrka: stabil timing och PIO`.
- Kapitel 16: omformade specialkortskontrollen till `Referensmönster: kortprofil innan specialkortet byggs in`.
- `build/book.md` byggdes om.

Kontroll:

- Inga H4-rubriker i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- Kapitel 9–16 innehåller inte längre gamla E2-relevanta labbmarkörer som `### Syfte`, `### Mål`, `### Material`, `I det här experimentet`, `experimentlogg` eller `Kontroll 1`.

## 2026-07-02 – E3, kapitel 17–26

Utgångspunkt: `arduino-i-praktiken-projekt-plan-e-steg-02-kapitel-09-16.zip`.

Genomförda ändringar:

- Kapitel 18: lade till `Praktisk tumregel: räkna ström innan du ökar antalet pixlar`.
- Kapitel 19: omformade ljudstatusavsnittet till `Typiska ljudkoder i ett projekt`.
- Kapitel 23: lade till `Placering är en del av mätningen`.
- Kapitel 24: lade till `Typiskt mönster: ljuströskel med hysteresis`.
- Kapitel 26: lade till `Vanliga användningar av samma rörelsemönster`.
- Kapitel 17–26: gjorde konsekvensputs av kvarvarande `### Material`-rubriker och några närliggande experimentformuleringar.
- `build/book.md` byggdes om.

Kontroll:

- Inga H4-rubriker i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- Kapitel 17–26 innehåller inte längre `### Material`.
- De nya E3-tilläggen är korta handboksrutor och användningsmönster, inte övningsblock.

## 2026-07-02 – E4, kapitel 27–34

Utgångspunkt: `arduino-i-praktiken-projekt-plan-e-steg-03-kapitel-17-26.zip`.

Genomförda ändringar:

- Kapitel 27: lade till `Typiska ljudmönster` för klappdetektering, bullernivå, digital trigger, statusindikator och mer avancerad ljudanalys.
- Kapitel 28: gjorde en mindre konsekvensputs av batteri-/lastmonitorns exempelrubrik och ersatte kvarvarande experimentformulering i säkerhetsvarningen.
- Kapitel 29: rensade kvarvarande experimentformulering, rättade händelsestrukturens verbform och lade till `Typisk händelserad`.
- Kapitel 30: förtydligade att 74HC595 ger fler logiska utgångar men inte mer lastström, samt gjorde exempelrubrikerna konsekventa.
- Kapitel 31: gjorde jämförelsemönstrets exempelrubrik konsekvent och ändrade dokumentationsspråk till mer praktiskt sparspråk.
- Kapitel 32: lade till `Typisk loggrad med statusfält` och justerade dataloggerexemplet så loggformatet inkluderar status och fel.
- Kapitel 33: bytte verifieringsrubrikerna till återanvändbara referensmönster för analog tröskel med hysteres och lågpassfiltrering.
- Kapitel 34: tonade ned kvarvarande experimentformuleringar i matnings- och snabbvalstext.
- `build/book.md` byggdes om.

Kontroll:

- Inga H4-rubriker i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- Kapitel 27–34 innehåller inte längre `### Material`, `### Syfte`, `### Mål`, `Det här experimentet`, `I det här experimentet`, `experimentlogg`, `## Verifiera` eller `Experimentet tränar`.
- E4-tilläggen är avgränsade handboksrutor och referensmönster, inte nya övningsblock.

## 2026-07-02 – E5, kapitel 35–38

Utgångspunkt: `arduino-i-praktiken-projekt-plan-e-steg-04-kapitel-27-34.zip`.

Genomförda ändringar:

- Kapitel 35: lade till `Typiska minimisketcher för felsökning` som kopplar vanliga symptom till rätt minimisketch.
- Kapitel 36: lade till `Före och efter: från lös sketch till modul` och ändrade modul-README-exemplets `Syfte` till `Vad modulen gör`.
- Kapitel 37: lade till `Så hänger projektet ihop med tidigare mönster` för att knyta slutprojektet till bokens tidigare referensmönster.
- Kapitel 38: justerade snabbguidens avslutande dokumentationsformulering till praktiskt sparspråk.
- `build/book.md` byggdes om.

Kontroll:

- Inga H4-rubriker i ändrade kapitel.
- Kodblocken i ändrade kapitel är balanserade.
- E5-tilläggen är metodmönster och referensstöd, inte nya komponentexperiment.


## 2026-07-02 – Steg E6: slutkontroll och export

- Skapade `docs/example-coverage-review.md`.
- Granskade kvarvarande läroboksmarkörer i kapitelmanus.
- Gjorde två små språkjusteringar i kapitel 13 och 37.
- Byggde om `build/book.md` och exporterade EPUB enligt projektstandard.
- Skapade final projekt-zip för PLAN-E.

## 2026-07-02 – RUBRIKPUTS efter PLAN-E-final

- Genomförde riktad rubrik- och ordningsputs i kapitel 23, 27, 28, 36 och 37.
- Bytte slutnära `Snabb överblick` till `Snabb sammanfattning` där innehållet var sammanfattande text.
- Tydliggjorde skillnaden mellan tidig modulchecklista och avslutande slutkontroll i kapitel 36.
- Flyttade `Kontroll före nästa version` före `Snabbreferens` i kapitel 37.
- Uppdaterade metadata till `plan-e-final-rubrikputs`.


## Efter PLAN-E: GitHub Actions-publicering

Datum: 2026-08-10  
Version: `plan-e-final-rubrikputs-github-actions`

Genomfört:

- Infört `.github/workflows/01-validate.yml`.
- Infört `.github/workflows/02-build-preview.yml`.
- Infört `.github/workflows/03-release.yml`.
- Lagt till `scripts/validate_project.py` som deterministisk CI-validerare för projektets faktiska struktur.
- Lagt till `scripts/build_book.py` som CI-lager ovanpå `scripts/export-book.py`.
- Lagt till `docs/github-actions-publishing.md`.
- Uppdaterat metadata, README och projektstatus.

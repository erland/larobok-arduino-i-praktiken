# Post-v5-justering: kapitel 22–26

Datum: 2026-07-02

## Syfte

Fortsätta den redaktionella efterbearbetningen efter handbokstruktur-v5 med samma princip som i kapitel 1–21:

- behåll praktiska moment som verifierar, mäter eller felsöker något konkret,
- ta bort moment som främst känns som dokumentationsövningar, kontrollfrågor eller läroboksuppgifter,
- väv in användningsmål i kapitelöversikter i stället för att ha dem som separata målavsnitt,
- tona ned språk som `experiment`, `Syfte`, `Mål` och dokumentationsmallar när de inte behövs.

## Ändrade kapitel

- `chapters/displayer-anvandargranssnitt-22.md`
- `chapters/miljosensorer-23.md`
- `chapters/ljus-farg-optiska-sensorer-24.md`
- `chapters/avstand-narvaro-25.md`
- `chapters/rorelse-orientering-26.md`

## Genomförda ändringar

### Kapitel 22

- Vävde in `Det du kan använda kapitlet till` i `Komponentöversikt`.
- Justerade inledningen till referensmönstret så att det inte presenteras som ett experiment.
- Tog bort `Verifiera display och gränssnitt`.
- Tog bort `Valchecklista`.

### Kapitel 23

- Vävde in `Det du kan använda kapitlet till` i `Sensoröversikt`.
- Justerade `Referensmönster: miljölogger med jämförelse`.
- Bytte `Syfte` till `Vad mönstret visar`.
- Tog bort `Vanliga varianter`.
- Tog bort `Valchecklista`.

### Kapitel 24

- Vävde in `Det du kan använda kapitlet till` i `Sensoröversikt`.
- Justerade `Exempel: sensorstyrd RGB-status` från experimentform till mönsterform.
- Tog bort `Dokumentera en optisk sensorprofil`.
- Tog bort `Vanliga varianter`.
- Tog bort `Valchecklista`.

### Kapitel 25

- Vävde in `Det du kan använda kapitlet till` i `Sensoröversikt`.
- Justerade `Jämförelsemönster: två närvarotekniker`.
- Bytte `Syfte` till `Vad mönstret visar`.
- Ersatte dokumentationsuppmaning i kopplingsavsnittet med praktiska kontrollpunkter.
- Tog bort `Dokumentera en avstånds- eller närvarosensorprofil`.
- Tog bort `Vanliga varianter`.
- Tog bort `Valchecklista`.

### Kapitel 26

- Vävde in `Det du kan använda kapitlet till` i `Sensoröversikt`.
- Justerade `Referensmönster: lutnings- och skakindikator`.
- Bytte `Syfte` till `Vad mönstret visar`.
- Bytte `Genomförande` till `Arbetsgång`.
- Tog bort `Vanliga varianter`.

## Kontroll

- `build/book.md` har byggts om.
- Inga H4-rubriker har införts.
- De berörda kapitlen innehåller inte längre:
  - `## Det du kan använda kapitlet till`
  - `## Valchecklista`
  - `## Vanliga varianter`
  - `## Verifiera display och gränssnitt`
  - `## Dokumentera en optisk sensorprofil`
  - `## Dokumentera en avstånds- eller närvarosensorprofil`
- Praktiska referensmönster som mäter, verifierar eller demonstrerar konkret funktion har behållits.

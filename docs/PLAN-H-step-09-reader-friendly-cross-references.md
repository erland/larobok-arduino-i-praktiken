# PLAN-H steg H9: Läsarvänliga korsreferenser

Datum: 2026-07-01

## Syfte

Steg H9 uppdaterar bokens korsreferenser så att de fungerar som praktisk navigation för läsaren, inte som interna projektspår eller mekaniska listor.

Målet är att läsaren snabbare ska kunna gå från ett problem till rätt kapitel:

- när en modul inte svarar,
- när en last kräver mer ström,
- när mätvärden är brusiga,
- när flera moduler delar buss,
- när projektet växer från enkel koppling till system.

## Genomförda ändringar

### Förkortade och förtydligade befintliga `Relaterat`-avsnitt

Flera befintliga relaterat-avsnitt har skrivits om till mer problembaserade hänvisningar. Särskilt långa listor har kortats ned och gjorts mer skannbara.

Berörda kapitel:

- kapitel 9 – kommunikation och bussar
- kapitel 20 – servon och motorer
- kapitel 21 – reläer, MOSFET:ar, solenoider och laster
- kapitel 22 – displayer och användargränssnitt
- kapitel 23 – miljösensorer
- kapitel 24 – ljus, färg och optiska sensorer
- kapitel 25 – avstånd och närvaro
- kapitel 27 – ljud och mikrofoner
- kapitel 28 – ström, spänning och energi
- kapitel 30 – I/O-expansion
- kapitel 31 – drivkretsar
- kapitel 32 – displaykretsar och minne
- kapitel 33 – analog signalanpassning
- kapitel 34 – strömförsörjning
- kapitel 37 – modulär sensor- och styrstation

### Lade till korta korsreferenser där kapitel tidigare saknade läsarväg vidare

Nya `Relaterat`-avsnitt har lagts till där det tydligt hjälper läsaren att navigera mellan översikt, kortval, plattformar, felsökning, modulbygge och referensdel.

Berörda kapitel:

- kapitel 1 – Arduino-kompatibla system som ekosystem
- kapitel 2 – välja rätt kort
- kapitel 3 – utvecklingsmiljö och bibliotek
- kapitel 4 – elektriska grunder
- kapitel 10–16 – kortprofiler och plattformsval
- kapitel 35 – felsökning
- kapitel 36 – från breadboard till modul
- kapitel 38 – referens och snabbvalsguider

### Rensade kvarvarande läsartext kring referensnavigation

I kapitel 38 har en formulering justerats så att den inte markerar rubriken `Relaterat` som kodliknande projekttext. Hänvisningen är nu läsarvänlig och fungerar som vanlig boknavigation.

## Redaktionsprinciper som användes

Korsreferenserna ska:

- vara problembaserade,
- hålla sig korta,
- peka till kapitel, inte interna filer,
- förklara varför läsaren ska gå vidare,
- undvika långa slutlistor,
- inte bli en mekanisk katalog efter varje kapitel.

## Kontroll

Följande kontroller har gjorts i `chapters/`:

- Inga H4-rubriker (`####`) finns.
- Inga interna projektspår som `docs/`, `build/`, `canon`, `project-status` eller `PLAN5` finns i kapiteltexterna.
- Gamla rubriker som `## Praktiskt test`, `## Prova själv`, `## Prova vidare` och `## Snabb orientering` har inte återinförts.
- `build/book.md` har byggts om efter ändringarna.

## Resultat

Boken har nu tydligare läsarvänliga korsreferenser. Navigationen är mer handboksnära: läsaren får veta vilket kapitel som hjälper vid ett visst problem, val eller nästa praktiska beslut.

# [PLAN2] Batch 4: komponenter och aktuatorer – korsreferenser

Datum: 2026-07-01  
Plansteg: [PLAN2] batch 4  
Kapitel: 17–22  
Status: Genomförd

## Syfte

Batch 4 granskar `Se också`, `Korsreferens` och liknande hänvisningar i komponent- och aktuator-kapitlen.

Målet är att boken inte ska binda ihop kapitel mekaniskt som en kursbok. Hänvisningar ska bara finnas där de hjälper läsaren med ett konkret praktiskt problem, till exempel:

- PWM och timing,
- strömförsörjning,
- drivning av laster,
- säkerhet,
- felsökning,
- relevanta alternativ.

## Beslut per kapitel

| Kapitel | Fil | Beslut |
|---:|---|---|
| 17 | `led-rgb-ljuseffekter-17.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på PWM, laststyrning och strömförsörjning. |
| 18 | `adresserbara-led-18.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på timing, laststyrning och strömbudget. |
| 19 | `buzzers-ljudsignaler-19.md` | `Se också` ersattes med `Relaterat` med fokus på timers, icke-blockerande signaler, laststyrning och strömförsörjning. |
| 20 | `servon-motorer-20.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på PWM, drivning, separat matning och störningar. |
| 21 | `relaer-mosfetar-laster-21.md` | Linjärt `Se också` togs bort. Tidigare `Korsreferens` omformulerades till `Relaterat` med fokus på gemensam jord, induktiva laster och strömförsörjning. |
| 22 | `displayer-anvandargranssnitt-22.md` | `Se också` ersattes med `Relaterat` med fokus på I2C/SPI, strömförsörjning och felsökning. |

## Redaktionell bedömning

Batch 4 bör inte ta bort alla kopplingar, eftersom komponent- och aktuator-kapitlen ofta behöver praktiska hänvisningar till grundfunktioner och robust elektronik.

Däremot ska hänvisningarna inte fungera som övergångar till nästa kapitel. De ska fungera som uppslagsstöd när läsaren behöver förstå en teknisk koppling.

## Resultat

- Mekaniska `Se också`-avsnitt är borttagna ur kapitel 17–22.
- Praktiskt motiverade hänvisningar finns kvar som `Relaterat`.
- `Relaterat` används inte som en ny obligatorisk slutrubrik, utan bara där kopplingen är praktiskt användbar.
- Hänvisningarna fokuserar på problemområden snarare än kapitelordning.

## Kontroll

Efter batchen ska projektet valideras med exportscriptet och `build/book.md` byggas om.

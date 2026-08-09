# [PLAN4] Steg 1: Komplettera kapitel 22

Datum: 2026-07-01  
Status: Genomfört

## Syfte

Detta steg kompletterar kapitel 22 med vanliga inmatningsmoduler som ofta finns i Arduino-kit och elektronikbutiker men som tidigare var svagt behandlade.

## Ändrade manusdelar

Följande tillägg har gjorts i `chapters/displayer-anvandargranssnitt-22.md`:

- tydligare jämförelsetabell för inmatning,
- egen sektion om rotary encoder,
- egen sektion om joystick-modul,
- egen sektion om keypad/knappsats,
- egen sektion om kapacitiv touch,
- kort sektion om IR-fjärrkontroll som enkel inmatning,
- kompletterat praktiskt test för att välja rätt inmatning,
- uppdaterad snabbreferens,
- uppdaterade kontrollfrågor,
- uppdaterad `Relaterat`-sektion.

## Redaktionellt beslut

Rotary encoder, joystick, keypad och touch behandlas i kapitel 22 eftersom de i första hand är användargränssnitt och inmatning. De kopplas samtidigt till tidigare kapitel:

- kapitel 5 för digitala signaler, knappar och debounce,
- kapitel 6 för analoga värden och joystickens dödzon,
- kapitel 8 för interrupt när rotary encoder kräver snabb respons,
- kapitel 30 för keypad eller många knappar via I/O-expansion.

IR-fjärrkontroll finns med som kort inmatningsalternativ i kapitel 22, men kan fortfarande fördjupas i kapitel 24 om optiska/IR-signaler senare kompletteras enligt `[PLAN4]`.

## Uppdaterade stödokument

- `docs/lookup-index.md` har fått fler ingångar för rotary encoder, joystick, keypad, touch och IR-fjärr.
- `docs/book-specification.md`, `docs/project-status.md` och `README.md` har uppdaterats med att `[PLAN4]` har påbörjats.

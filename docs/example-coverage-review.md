# Exempeltäckningsgranskning efter PLAN-E

**Datum:** 2026-07-02  
**Status:** Slutkontroll efter PLAN-E E1–E5.

Den här interna granskningen sammanfattar hur varje kapitel täcker typisk användning, viktiga val eller återanvändbara metodmönster efter PLAN-E.

| Kapitel | Exempelstatus | PLAN-E-åtgärd | Bedömning |
|---|---|---|---|
| 1 | Arduino-kompatibla system som ekosystem | Befintligt ekosystemexempel med portabilitet/LED_BUILTIN räcker. | Starkt – lämnat orört |
| 2 | Att välja rätt kort för rätt projekt | Beslutsfall fanns redan; mindre justering av projekt-/kortvalsspråk. | Stärkt med kort språkputs |
| 3 | Utvecklingsmiljö, bibliotek och projektstruktur | Testprojekt, README och I2C-scanner fungerar som arbetsmetodsexempel. | Starkt – lämnat i sak, kopplat tydligare |
| 4 | Elektriska grunder för programmerare | Minsta säkra koppling med LED, knapp och analog signal stärkt som grundmönster. | Omformad till referensmönster |
| 5 | Digital I/O, knappar och logiska signaler | Robust knappmodul utan delay omformad till handboksnära mönster. | Omformad till referensmönster |
| 6 | Analog läsning, ADC och mätosäkerhet | Ny bro från potentiometer till verklig sensor. | Stärkt med kort ruta |
| 7 | PWM, timers och tidsstyrning | Analog PWM-variant gjord icke-blockerande och tidsmönstren hålls återanvändbara. | Stärkt med kodjustering |
| 8 | Avbrott, watchdog och robust körning | Timeout och säkert standardläge tillagt för robust körning. | Nytt kort mönster |
| 9 | Kommunikation: UART, I2C, SPI och 1-Wire | SPI-mönster för delad buss och chip select tillagt; I2C/UART-mönster fanns redan. | Stärkt med kort ruta |
| 10 | Klassiska Arduino-kort: UNO, Nano och Mega | UNO/Nano/Mega-portering gjord till praktiskt referensmönster. | Omformad till referensmönster |
| 11 | Kloner, lågkostnadskort och tredjepartsvarianter | Kortidentifiering före kodfelsökning tillagd. | Stärkt med kort ruta |
| 12 | Moderna Arduino-kort | Moderna korts särdrag och porteringskontroll tydligare. | Omformad och förstärkt |
| 13 | ESP8266 och NodeMCU | ESP8266 Wi-Fi-sensorindikator fanns redan; anpassningar och språk putsade. | Starkt – mindre konsekvensputs |
| 14 | ESP32-familjen i Arduino-världen | ESP32 deep sleep för batterinod tillagt för plattformens särart. | Nytt kort mönster |
| 15 | Raspberry Pi Pico, RP2040 och RP2350 i Arduino-miljö | Pico/PIO och stabil timing förklaras som särskild styrka. | Stärkt med kort ruta |
| 16 | Småkort, specialkort och avancerade utvecklingskort | Specialkortskontroll gjord till kortprofil före integration. | Omformad till referensmönster |
| 17 | LED, RGB-LED och ljuseffekter | Statusljusmönstret täcker normal LED-användning. | Starkt – lämnat i sak |
| 18 | Adresserbara LED: NeoPixel, WS2812 och liknande | Ström/matning för adresserbara LED förtydligad. | Stärkt med kort ruta |
| 19 | Buzzers, ljudsignaler och enkla ljudutgångar | Typiska ljudkoder i projekt tillagda. | Stärkt med kort tabell |
| 20 | Servon, DC-motorer och stegmotorer | Servo som fysisk sensorindikator räcker som praktiskt motor-/rörelsemönster. | Starkt – lämnat orört |
| 21 | Reläer, MOSFET:ar, solenoider och andra laster | MOSFET/relä/riskmönster behållna; säkerhetsnytta prioriterad. | Starkt – mindre konsekvensputs |
| 22 | Displayer och enkla användargränssnitt | OLED + knapp fungerar som typiskt UI-mönster. | Starkt – lämnat i sak |
| 23 | Temperatur, fukt, tryck och miljösensorer | Sensorplacering som del av mätningen tillagd. | Stärkt med kort ruta |
| 24 | Ljus, färg, UV och optiska sensorer | Ljuströskel med hysteresis tillagd som normal optisk användning. | Stärkt med kort mönster |
| 25 | Avstånd, närvaro och objektupptäckt | Jämförelse mellan närvarotekniker fungerar väl. | Starkt – lämnat i sak |
| 26 | Rörelse, orientering och vibration | Vanliga användningar av rörelsemönstret tillagda. | Stärkt med kort ruta |
| 27 | Ljud, mikrofoner och enkla signalmätningar | Typiska ljudmönster tillagda. | Stärkt med kort tabell |
| 28 | Ström, spänning, energi och batterimätning | Batteri-/lastmonitor och INA219-mönster behållna. | Starkt – mindre konsekvensputs |
| 29 | Position, tid och identitet | Typisk händelserad tillagd och kvarvarande experimentspråk rensat. | Stärkt med kort exempel |
| 30 | I/O-expansion, shift registers och multiplexers | 74HC595 som logisk utgångsexpansion, inte lastdrivning, förtydligad. | Stärkt med kort förtydligande |
| 31 | Drivkretsar för LED, motorer och laster | Jämförelsemönster för drivlösningar behållet. | Starkt – mindre konsekvensputs |
| 32 | Displaykretsar, minne och datalagring | Typisk loggrad med status/fel tillagd; dataloggerexempel stärkt. | Stärkt med kort exempel |
| 33 | Analog signalanpassning, op-förstärkare och komparatorer | Analog tröskel och lågpassfilter fått tydligare mönsteridentitet. | Omformad till referensmönster |
| 34 | Strömförsörjning, batteridrift och robust konstruktion | Riskkontroll/strömförsörjning behållna. | Starkt – mindre konsekvensputs |
| 35 | Felsökning med metod | Typiska minimisketcher för felsökning tillagda. | Stärkt med kort tabell |
| 36 | Från breadboard till återanvändbar modul | Före/efter från lös sketch till modul tillagt. | Stärkt med kort exempel |
| 37 | Sammanhängande projekt: modulär sensor- och styrstation | Slutprojektet kopplat till tidigare referensmönster. | Stärkt med helhetstabell |
| 38 | Referens: snabbvalsguider och jämförelsetabeller | Referenskapitel behållet; snabbguide putsad. | Starkt – mindre språkputs |

## Slutbedömning

PLAN-E har stärkt exempelbalansen utan att göra boken till en samling övningar. Grundkapitlen har tydligare referensmönster, plattformskapitlen visar särarter bättre, komponentkapitlen har kompletterats med korta praktiska rutor och metodkapitlen binder ihop felsökning, modulering och slutprojekt.

Inga större nya experiment har lagts till. Förbättringarna är främst korta mönster, praktiska tabeller, rubrikidentitet och konkreta standardexempel.

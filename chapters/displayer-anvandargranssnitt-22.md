# 22. Displayer och enkla användargränssnitt

## Komponentöversikt
Hittills har boken rört sig från kortval och elektriska grunder till signaler, kommunikationsbussar, ljus, ljud, motorer och laststyrning. Det är fullt möjligt att bygga många Arduino-projekt med bara seriell monitor som återkoppling, men så fort projektet ska användas utan dator behövs ofta ett lokalt användargränssnitt.

Ett användargränssnitt behöver inte vara stort eller avancerat. I många inbyggda system räcker det med en LED, en knapp och kanske en liten display. Men valet av display och inmatning påverkar både hårdvara, strömförbrukning, minnesanvändning, kodstruktur och felsökning. En enkel 16x2 LCD kan vara mer robust än en färgdisplay. En liten OLED kan vara perfekt på skrivbordet men olämplig i stark sol eller i ett batteridrivet projekt som ska visa samma bild i månader. En rotary encoder kan ge ett bättre användarflöde än fem knappar, men kräver mer genomtänkt kod.

Det här kapitlet handlar om den praktiska nivån där Arduino-projekt börjar kännas som färdiga instrument:

- en display visar mätvärden, status och menyer
- knappar låter användaren byta läge
- en rotary encoder ger snabb navigering
- en enkel menystruktur gör projektet begripligt utan dator
- koden skiljer mellan mätlogik, styrlogik och presentation

Kapitlet är inte en komplett bok om grafiska gränssnitt. Det fungerar som praktiskt stöd när du behöver välja mellan LCD, OLED, TFT, e-paper, sifferdisplay och LED-matris, koppla displayen säkert, hantera enkel inmatning och hålla mätning, tillstånd och presentation isär i koden. Målet är att ge dig ett fungerande sätt att välja displaytyp och förstå när ett enklare gränssnitt är bättre än ett mer imponerande.

## Förutsättningar

Det här kapitlet bygger på flera tidigare delar:

- kapitel 4 om spänning, ström, gemensam jord och 3,3 V kontra 5 V
- kapitel 5 om knappar, aktiv LOW-logik och debouncing
- kapitel 7 om `millis()` och icke-blockerande uppdatering
- kapitel 9 om I2C och SPI
- kapitel 17 och 18 om LED som enkel statusåterkoppling

Vi kommer att tänka på displayen som en utenhet, men den beter sig annorlunda än en LED eller motor. En display är ofta en liten datoriserad modul med egen styrkrets, eget minne, eget kommunikationsprotokoll och ibland ganska höga krav på biblioteket. Det gör att två displayer som ser lika stora ut kan vara mycket olika ur Arduino-perspektiv.

En bra startregel är:

> Visa bara det användaren behöver veta just nu, och uppdatera bara när informationen faktiskt har förändrats.

Det gör både hårdvara och kod enklare.

## Vad ett enkelt användargränssnitt består av

Ett enkelt Arduino-gränssnitt brukar ha tre lager.

Det första lagret är **presentation**. Det kan vara en LED, en display, en buzzer eller en kombination. Presentationen svarar på frågan: vad vill systemet säga till användaren?

Det andra lagret är **inmatning**. Det kan vara knappar, brytare, touch, potentiometer, rotary encoder, RFID eller data från en seriell terminal. Inmatningen svarar på frågan: vad vill användaren göra?

Det tredje lagret är **tillstånd**. Det är systemets aktuella läge: vilken vy visas, vilket värde redigeras, om larm är aktivt, om systemet loggar data eller om en meny är öppen.

I små tester blandas dessa lager ofta ihop. Koden läser en sensor, skriver direkt till displayen, väntar med `delay()`, läser en knapp och ändrar en global variabel. Det fungerar en stund, men blir snabbt svårt att bygga vidare på.

En bättre grundstruktur är:

- läs inmatning
- uppdatera systemets tillstånd
- läs eller beräkna mätvärden vid rätt intervall
- uppdatera displayen när något behöver visas om
- låt programmet fortsätta loopa utan långa blockeringar

Det är samma princip som tidigare kapitel har använt för knappar, LED-effekter, buzzers och motorer.

## Displaytyper i praktiken

Det finns många displaytyper, men i Arduino-projekt återkommer några grupper oftare än andra.

| Displaytyp | Typisk användning | Vanligt gränssnitt | Styrkor | Svagheter |
|---|---|---|---|---|
| 16x2 eller 20x4 LCD | Enkel text | Parallell eller I2C-backpack | Robust, billig, lättläst | Begränsad grafik, ofta stor |
| OLED 0,96 tum | Kompakt text/grafik | I2C eller SPI | Skarp bild, enkel koppling | Kan vara liten, inbränning vid statisk bild |
| TFT | Färg och grafik | SPI eller parallell | Färg, grafik, pekskärm på vissa moduler | Mer kod, mer minne, mer ström |
| E-paper | Statisk information | SPI | Mycket låg ström vid stillbild, läsbar i ljus | Långsam uppdatering |
| 7-segmentsdisplay | Talvärden | Direkt, shift register eller drivkrets | Tydlig för siffror | Dålig för text |
| LED-matris | Status, symboler, enkel grafik | SPI/I2C/drivkrets | Visuell och robust | Begränsad upplösning |
| Seriell terminal | Utveckling och debug | USB/UART | Ingen extra hårdvara | Kräver dator eller terminal |

Tabellen visar inte vilken display som är bäst. Den visar att displayval alltid är ett projektval.

För en datalogger som bara visar temperatur och batterinivå kan en liten OLED eller 16x2 LCD räcka. För en portabel mätare som ska kunna visa flera sidor med värden kan OLED med rotary encoder vara lagom. För en väggmonterad informationspanel kan TFT eller e-paper passa bättre. För en batteridriven etikett som uppdateras sällan kan e-paper vara överlägset.

Snabbt displayval:

- Välj **16x2 LCD** när texten ska vara robust och enkel.
- Välj **OLED** när projektet behöver kompakt statusinformation med lite grafik.
- Välj **TFT** när färg, många vyer eller enkel grafik är viktigare än låg komplexitet.
- Välj **e-paper** när bilden ändras sällan och läsbarhet eller batteritid väger tungt.
- Välj **seriell logg** i stället för display när informationen bara behövs under utveckling.

## LCD: robust textdisplay

Den klassiska tecken-LCD:n, ofta 16x2 eller 20x4 tecken, är fortfarande användbar. Den är inte modernast, men den är tydlig, billig och relativt lätt att förstå. Ursprungligen kopplas sådana displayer ofta parallellt med flera GPIO-pinnar, men många moduler har ett I2C-backpack som gör att displayen bara kräver SDA, SCL, matning och jord.

Välj LCD när:

- du vill visa kort text och enkla värden
- du vill ha något robust och välkänt
- projektet inte behöver grafik
- några rader text räcker
- stor fysisk läsbarhet är viktigare än hög upplösning

Välj något annat när:

- du behöver grafik, ikoner eller många värden
- du har mycket begränsat utrymme
- du behöver modern visuell känsla
- du vill ha mycket låg strömförbrukning vid statisk visning

En LCD har ofta kontrastjustering. Om displayen tänds men ingen text syns är kontrast nästan alltid en av de första sakerna att kontrollera. På I2C-backpack sitter ofta en liten potentiometer för detta.

Tänk också på matningsspänning. Många klassiska LCD-moduler är gjorda för 5 V. Vissa fungerar med 3,3 V-logik, andra gör det inte pålitligt. En 5 V-I2C-backpack kan ha pull-up-motstånd till 5 V, vilket kan vara olämpligt för 3,3 V-kort. Läs modulens dokumentation eller mät pull-up-nivån om du är osäker.

## OLED: liten men informationsrik display

Små OLED-displayer, ofta 128x64 eller 128x32 pixlar, är mycket vanliga i Arduino-projekt. De är skarpa, kompakta och fungerar bra för text, symboler, grafer och enkla menyer. Många använder styrkretsar som SSD1306 eller SH1106, ofta via I2C.

Välj OLED när:

- projektet behöver kompakt display
- du vill visa både text och enkel grafik
- du vill ha ett snyggt instrumentliknande uttryck
- I2C-koppling med få ledningar är praktiskt
- du kan acceptera begränsad fysisk storlek

Välj något annat när:

- displayen ska läsas på långt avstånd
- informationen är statisk under mycket lång tid
- maximal batteritid är viktig och displayen måste vara synlig hela tiden
- inbränning eller åldrande kan bli ett problem

OLED är ofta enkel att koppla, men biblioteket kan använda en framebuffer i RAM. En 128x64 monokrom display kräver typiskt 1024 byte bara för bildbufferten. Det är inget problem på många moderna kort, men på en klassisk ATmega328P-baserad UNO eller Nano är 1024 byte en stor del av SRAM. Därför är OLED ett bra exempel på hur en display kan påverka kortvalet.

På ESP32, RP2040, moderna Arduino-kort och många specialkort är detta sällan ett problem. På små AVR-kort bör du däremot vara mer sparsam med textsträngar, buffertar och grafikbibliotek.

## TFT: färg, grafik och mer komplexitet

TFT-displayer ger färg och grafik. De finns i många storlekar och kan ibland ha pekskärm. I Arduino-sammanhang ansluts de ofta via SPI, men vissa större eller snabbare moduler använder parallella gränssnitt.

Välj TFT när:

- du behöver färg
- du vill visa grafer, ikoner eller flera informationspaneler
- projektet har tillräckligt med minne och CPU
- strömförbrukning inte är den största begränsningen
- du accepterar mer komplex UI-kod

Välj enklare display när:

- du bara visar några mätvärden
- batteridrift är viktig
- kortet har lite RAM eller långsam SPI
- felsökning och robusthet är viktigare än visuell effekt

TFT kan snabbt flytta fokus från elektronikexperiment till grafisk programmering. Det kan vara rätt i ett instrumentprojekt, men fel i ett kapitel där sensorn eller styrningen egentligen är huvudpoängen. En bra kompromiss är att börja med enkla textvyer och bara lägga till grafik när det hjälper användaren förstå systemet.

För snabbare TFT-projekt är SPI-hastighet, val av bibliotek, displaycontroller och kortets prestanda viktiga. På ESP32 och RP2040 kan TFT vara mycket praktiskt. På klassiska AVR-kort fungerar små TFT-displayer, men gränsen för vad som känns smidigt kommer snabbare.

## E-paper: läsbart och strömsnålt när bilden ändras sällan

E-paper, eller elektroniskt papper, är annorlunda än LCD, OLED och TFT. Bilden ligger kvar utan kontinuerlig uppdatering, och displayen kan vara mycket läsbar i starkt ljus. Det gör e-paper intressant för batteridrivna projekt, etiketter, mätvärden som ändras sällan och informationsskyltar.

Välj e-paper när:

- informationen ändras sällan
- låg viloström är viktig
- läsbarhet i omgivningsljus är viktig
- lång batteritid är viktigare än snabb uppdatering

Välj något annat när:

- värden ändras flera gånger per sekund
- du behöver animation
- uppdateringslatens stör användarupplevelsen
- displayen måste vara bakgrundsbelyst i mörker

E-paper kräver ofta mer tålamod i kod och testning. Uppdateringen kan vara långsam, vissa displayer behöver särskilda resetsekvenser, och partiell uppdatering fungerar olika bra på olika modeller. E-paper är därför ett bra val först när projektets informationsmönster verkligen passar tekniken.

## 7-segmentsdisplayer och enkla numeriska gränssnitt

Om projektet bara ska visa ett tal kan en 7-segmentsdisplay vara bättre än en grafisk display. Den är tydlig, billig och kan läsas på avstånd. Nackdelen är att den är specialiserad. Den visar siffror bra, men text dåligt.

Välj 7-segmentsdisplay när:

- ett eller några numeriska värden är huvudinnehållet
- avläsning på avstånd är viktig
- displayen ska vara robust och direkt
- användaren inte behöver menyer eller längre text

Vanliga sätt att styra sådana displayer är:

- direkt GPIO för mycket enkla tester
- shift register
- drivkrets som MAX7219 eller TM1637-liknande modul
- färdig I2C/SPI-modul

Om du använder direkt GPIO går många pinnar åt. Det är pedagogiskt men sällan bäst i ett större projekt. En drivkrets eller färdig modul frigör GPIO och gör koden enklare.

## LED-matris och symbolbaserad återkoppling

En LED-matris ligger mellan LED-indikator och riktig display. Den kan visa siffror, symboler, små ikoner, statusmönster och enklare animationer. Den är ofta mer synlig än en liten OLED men mindre informationsrik än en TFT.

Välj LED-matris när:

- projektet behöver tydlig visuell status
- symboler eller enkla tal räcker
- ljus och rörelse i presentationen är önskvärt
- användaren ska förstå läget på avstånd

Välj OLED, LCD eller TFT när:

- textinformation är viktig
- menyer behövs
- många mätvärden ska visas samtidigt

LED-matriser är särskilt användbara i installationsprojekt, spel, enkla kontrollpaneler och varningssystem.

## Inmatning: knappar, brytare och encoder

En display utan inmatning är en informationsyta. En display med inmatning blir ett gränssnitt.

De enklaste inmatningarna är knappar och brytare. De är robusta och lätta att förstå, men många knappar kräver fler pinnar och tydligare användarflöde. En rotary encoder kan ersätta flera knappar genom att ge rotation plus ofta ett tryck. Det passar bra för menyer, val av värde och bläddring mellan vyer.

| Inmatning | Passar för | Styrkor | Svagheter |
|---|---|---|---|
| En knapp | Växla vy, bekräfta, starta | Enkel, robust | Begränsad interaktion |
| Flera knappar | Meny, upp/ned, start/stopp | Lätt att märka upp | Fler pinnar, mer debounce |
| Rotary encoder | Menyer, värdejustering | Kompakt och effektiv | Kräver bra kod och ibland interrupt |
| Joystick-modul | Två axlar, val, små robotar, enkla spel | Två analoga värden plus ofta knapp | Kräver kalibrering och dödzon |
| Keypad eller knappsats | PIN-kod, menyval, enkel panel | Många knappar med få pinnar | Kräver rad/kolumn-skanning och debounce |
| Kapacitiv touch | Paneler, beröringsknappar, tät front | Inga rörliga delar | Kan vara störkänsligt och miljöberoende |
| IR-fjärrkontroll | Enkel fjärrstyrning utan extra knappar på lådan | Billig, trådlös, lätt att prova | Kräver fri sikt och avkodningsbibliotek |
| APDS-9960/GY-9960 | Enkel gest- eller närhetsinmatning utan mekanisk knapp | Beröringsfri och kan även mäta ljus/färg | Känslig för avstånd, ljus och placering |
| Potentiometer | Analog inställning | Intuitiv | Mindre exakt, analogt brus |
| DIP-switch | Fast konfiguration | Stabilt och tydligt | Inte dynamiskt |

För den här boken är en knapp, en rotary encoder och en liten display de mest återanvändbara grunderna för ett lokalt gränssnitt. Joystick, keypad, touch, IR-fjärr och APDS-9960-baserade gestmoduler är vanliga butikskomponenter som passar när projektet behöver mer specialiserad inmatning. Knappar anknyter till kapitel 5. Joystick och potentiometer anknyter till kapitel 6. Rotary encoder anknyter till digital I/O, debouncing, ibland interrupt och UI-tillstånd.

## Rotary encoder: ratt med steg, riktning och knapp

En rotary encoder ser ofta ut som en potentiometer, men den fungerar annorlunda. En vanlig potentiometer ger ett analogt värde inom ett begränsat område. En rotary encoder ger i stället pulser när den vrids. Många moduler har dessutom en inbyggd tryckknapp.

Det gör encodern särskilt användbar för små menyer:

- vrid åt höger för nästa alternativ
- vrid åt vänster för föregående alternativ
- tryck för att bekräfta
- håll inne för att gå tillbaka eller öppna inställningar

En enkel mekanisk encoder har ofta två digitala signaler, vanligen kallade A och B. När encodern vrids ändras signalerna i en viss ordning. Genom att jämföra ordningen kan programmet avgöra riktningen.

I små projekt räcker det ofta att läsa encodern regelbundet i `loop()`. Det fungerar bäst när programmet inte blockerar med långa `delay()`-anrop. Om encodern ska reagera snabbt, eller om programmet gör mycket annat, kan interrupt vara bättre. Då gäller samma varning som i kapitel 8: gör interrupt-koden kort och flytta den egentliga logiken till huvudloopen.

Var särskilt uppmärksam på studs. Mekaniska encoders kan ge flera snabba signalväxlingar vid varje steg. Använd bibliotek eller en tydlig debounce-strategi i stället för att anta att varje flank är ett rent steg.

## Joystick-modul: två analoga axlar och en knapp

Den vanliga joystickmodulen i Arduino-kit består oftast av två potentiometrar och en tryckknapp. Den ena axeln kopplas till en analog ingång för X, den andra till en analog ingång för Y, och knappen kopplas som en vanlig digital knapp.

Den passar bra när användaren ska styra riktning, välja bland alternativ eller ändra två värden:

- liten robot eller pan/tilt-fäste
- meny där vänster/höger byter vy och upp/ned ändrar värde
- enkel spelkontroll
- manuell styrning av servon eller motorer

Joystickmoduler behöver nästan alltid en dödzon runt mitten. Mittenvärdet är sällan exakt samma varje gång, och analoga värden kan brusas lite. I praktisk kod bör du därför tolka ett intervall runt mitten som nollrörelse.

En bra tumregel är:

> Läs joystickens mittläge vid start eller använd en tydlig dödzon innan du låter värdet styra något mekaniskt.

## Keypad och knappsatser

En keypad, till exempel en 3x4- eller 4x4-knappsats, är i praktiken en knappmatris. I stället för att varje knapp får en egen pinne delas knapparna upp i rader och kolumner. Programmet aktiverar en rad i taget och läser kolumnerna för att se vilken knapp som trycks.

Det gör keypad användbart för:

- PIN-koder
- menyer med siffror och specialknappar
- enkel kontrollpanel
- projekt där många knappar behövs men antalet pinnar är begränsat

Nackdelen är att koden blir lite mer komplex än för en enskild knapp. Du behöver tänka på scanning, debounce och ibland så kallad ghosting om flera knappar kan tryckas samtidigt. För vanliga meny- och kodprojekt räcker ofta ett etablerat keypad-bibliotek.

Om projektet redan använder många pinnar kan en I/O-expander i kapitel 30 vara ett bättre val än att koppla hela knappsatsen direkt till mikrokontrollern.

## Kapacitiv touch: knapp utan mekanisk rörelse

Kapacitiva touchmoduler, till exempel enkla TTP223-liknande moduler, fungerar ofta som digitala knappar: de ger HIGH eller LOW när användaren rör vid ytan. Mer avancerade touchkontroller, till exempel flerkanaliga moduler, kan läsa många touchytor via I2C. Vissa kort, särskilt inom ESP32-familjen, har också inbyggt stöd för kapacitiv touch på vissa pinnar.

Touch passar bra när du vill ha:

- en slät frontpanel
- få rörliga delar
- enkel vädertåligare eller kapslad inmatning
- diskret kontroll utan tydliga mekaniska knappar

Men touch är mer miljökänsligt än en mekanisk knapp. Fukt, långa ledningar, jordning, kapsling och brus från strömförsörjningen kan påverka känsligheten. Testa därför touch i den kapsling och med den strömförsörjning som projektet faktiskt ska använda.

## IR-fjärrkontroll som enkel inmatning

En IR-mottagarmodul av TSOP- eller VS1838B-typ kan göra en vanlig fjärrkontroll till inmatning för ett Arduino-projekt. Det är ett enkelt sätt att styra läge, meny eller start/stopp utan att borra hål för knappar i lådan.

IR-fjärr passar när:

- projektet står synligt i rummet
- fri sikt mellan fjärr och mottagare är rimlig
- inmatningen inte är säkerhetskritisk
- du vill återanvända en billig fjärrkontroll

Begränsningen är att IR kräver fri sikt och att olika fjärrkontroller kan använda olika protokoll. Använd ett etablerat IR-bibliotek och bygg koden så att okända knappkoder ignoreras. Om projektet ska fungera genom väggar eller över längre avstånd är radio, Wi-Fi, BLE eller kabelburen kommunikation bättre.

Kapitel 24 behandlar IR-mottagaren som optisk modul och förklarar varför den ska ses som modulerad inmatning, inte som vanlig ljusmätning.

APDS-9960/GY-9960 kan på liknande sätt användas som beröringsfri inmatning med enkla gester eller närhet. Då är kapitel 24 rätt plats för sensorns optiska begränsningar, medan detta kapitel hjälper dig tänka på gesten som ett UI-val: nästa vy, föregående vy, bekräfta eller avbryt.

## Ett enkelt UI-tillstånd

Många Arduino-menyer kan börja med en enum:

```cpp
enum class Screen {
  Overview,
  Details,
  Settings
};
```

Sedan har programmet ett aktuellt läge:

```cpp
Screen currentScreen = Screen::Overview;
```

När användaren trycker på en knapp eller vrider encodern ändras tillståndet. Displaykoden visar olika innehåll beroende på tillståndet.

Det viktiga är att displayen inte ska vara den del av programmet som bestämmer allt. Displayen ska visa systemets tillstånd. Inmatningen ska föreslå förändringar. Huvudlogiken ska avgöra vad som är tillåtet.

Ett praktiskt mönster är:

```cpp
void loop() {
  unsigned long now = millis();

  readInputs(now);
  updateMeasurements(now);
  updateState(now);
  updateDisplay(now);
}
```

Det här är inte mycket kod, men det är en stor skillnad i tänkesätt. Det gör att sensorer, motorer, buzzers och display kan fungera tillsammans utan att en del blockerar alla andra.

## Uppdatera displayen lagom ofta

En vanlig nybörjarfälla är att skriva om hela displayen varje varv i `loop()`. Det kan ge flimmer, långsam kod, onödiga I2C/SPI-transaktioner och svår felsökning.

Bättre strategier är:

- uppdatera displayen med fast intervall, till exempel 5 gånger per sekund
- uppdatera direkt när användaren byter vy
- uppdatera när ett visat värde faktiskt har ändrats tillräckligt mycket
- separera snabb intern mätning från långsammare presentation
- undvik att rensa hela skärmen om bara ett litet fält ändras

För små OLED- och LCD-projekt räcker ofta en enkel tidsstyrd uppdatering:

```cpp
const unsigned long DISPLAY_INTERVAL_MS = 250;
unsigned long lastDisplayUpdateMs = 0;

void updateDisplay(unsigned long now) {
  if (now - lastDisplayUpdateMs < DISPLAY_INTERVAL_MS) {
    return;
  }

  lastDisplayUpdateMs = now;

  // Skriv aktuell vy till displayen här.
}
```

När projektet växer kan du lägga till en flagga som säger att displayen är smutsig, ofta kallad `dirty` i UI-sammanhang. Då uppdateras displayen när något har ändrats eller när ett intervall har passerat.

## Referensmönster: liten mätpanel med OLED och knapp

Det här referensmönstret visar en enkel mätpanel med I2C-OLED, knapp och analogt värde. Mönstret är avsiktligt enkelt men visar flera viktiga principer:

- displayen uppdateras med intervall
- knappen hanteras med debounce
- aktuell vy sparas som tillstånd
- sensordata och presentation hålls isär
- koden kan senare byggas ut med fler sensorer, rotary encoder, joystick eller keypad

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- en I2C-OLED, till exempel 128x64 med SSD1306-liknande styrkrets
- en knapp
- en potentiometer eller annan enkel analog signalkälla
- kopplingskablar
- breadboard
- eventuellt nivåskiftning om displaymodulen och kortet kräver olika logiknivå

Exemplet använder generiska pinnamn. Anpassa dem efter ditt kort.

### Koppling

Koppla OLED-displayen enligt modulens märkning:

| OLED-pin | Anslutning |
|---|---|
| VCC | 3,3 V eller 5 V enligt modulens specifikation |
| GND | GND |
| SDA | Kortets SDA |
| SCL | Kortets SCL |

Koppla knappen mellan en digital pinne och GND. I koden används intern pull-up.

Koppla potentiometern så här:

| Potentiometer | Anslutning |
|---|---|
| Ena ytterbenet | GND |
| Andra ytterbenet | 3,3 V eller 5 V enligt kortets ADC-ingång |
| Mittenbenet | Analog ingång |

Kontrollera särskilt att den analoga ingången inte får högre spänning än kortet tål. På många 3,3 V-kort ska potentiometern matas från 3,3 V, inte 5 V.

### Kod

Kodexemplet använder ett typiskt SSD1306-biblioteksmönster. Biblioteksnamn och konstruktor kan skilja mellan installationer och displaymoduler, så se detta som ett robust mönster snarare än en exakt garanti för varje modul.

```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

constexpr int SCREEN_WIDTH = 128;
constexpr int SCREEN_HEIGHT = 64;
constexpr int OLED_RESET_PIN = -1;
constexpr int OLED_ADDRESS = 0x3C;

constexpr int BUTTON_PIN = 2;
constexpr int SENSOR_PIN = A0;

constexpr unsigned long DEBOUNCE_MS = 30;
constexpr unsigned long MEASURE_INTERVAL_MS = 100;
constexpr unsigned long DISPLAY_INTERVAL_MS = 250;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET_PIN);

enum class Screen {
  Overview,
  RawValue,
  BarGraph
};

Screen currentScreen = Screen::Overview;

bool lastRawButtonState = HIGH;
bool stableButtonState = HIGH;
unsigned long lastButtonChangeMs = 0;

unsigned long lastMeasureMs = 0;
unsigned long lastDisplayMs = 0;

int rawValue = 0;
int percentValue = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Serial.begin(115200);
  delay(200);

  Wire.begin();

  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS)) {
    Serial.println("OLED init failed. Check address, wiring and power.");
    while (true) {
      delay(1000);
    }
  }

  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("Arduino UI");
  display.println("Starting...");
  display.display();
}

void loop() {
  unsigned long now = millis();

  readButton(now);
  updateMeasurement(now);
  updateDisplay(now);
}

void readButton(unsigned long now) {
  bool rawState = digitalRead(BUTTON_PIN);

  if (rawState != lastRawButtonState) {
    lastRawButtonState = rawState;
    lastButtonChangeMs = now;
  }

  if (now - lastButtonChangeMs >= DEBOUNCE_MS && rawState != stableButtonState) {
    stableButtonState = rawState;

    if (stableButtonState == LOW) {
      nextScreen();
    }
  }
}

void nextScreen() {
  if (currentScreen == Screen::Overview) {
    currentScreen = Screen::RawValue;
  } else if (currentScreen == Screen::RawValue) {
    currentScreen = Screen::BarGraph;
  } else {
    currentScreen = Screen::Overview;
  }

  lastDisplayMs = 0;
}

void updateMeasurement(unsigned long now) {
  if (now - lastMeasureMs < MEASURE_INTERVAL_MS) {
    return;
  }

  lastMeasureMs = now;

  rawValue = analogRead(SENSOR_PIN);
  percentValue = map(rawValue, 0, 1023, 0, 100);
  percentValue = constrain(percentValue, 0, 100);
}

void updateDisplay(unsigned long now) {
  if (lastDisplayMs != 0 && now - lastDisplayMs < DISPLAY_INTERVAL_MS) {
    return;
  }

  lastDisplayMs = now;

  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);

  if (currentScreen == Screen::Overview) {
    drawOverview();
  } else if (currentScreen == Screen::RawValue) {
    drawRawValue();
  } else {
    drawBarGraph();
  }

  display.display();
}

void drawOverview() {
  display.println("Overview");
  display.println();
  display.print("Value: ");
  display.print(percentValue);
  display.println(" %");
  display.println();
  display.println("Press: next view");
}

void drawRawValue() {
  display.println("Raw ADC");
  display.println();
  display.setTextSize(2);
  display.print(rawValue);
}

void drawBarGraph() {
  display.println("Bar graph");

  int barX = 0;
  int barY = 24;
  int barW = 120;
  int barH = 12;
  int fillW = map(percentValue, 0, 100, 0, barW);

  display.drawRect(barX, barY, barW, barH, SSD1306_WHITE);
  display.fillRect(barX, barY, fillW, barH, SSD1306_WHITE);

  display.setCursor(0, 44);
  display.print(percentValue);
  display.println(" %");
}
```

### Vad du bör se

Displayen startar med en enkel hälsning och visar sedan en översiktsvy. När du vrider potentiometern ändras värdet. När du trycker på knappen byter displayen mellan tre vyer:

- översikt
- rått ADC-värde
- enkel stapelgraf

Det här är ett litet exempel, men strukturen är användbar. Du kan byta ut potentiometern mot en sensor, lägga till fler vyer, visa batterinivå, komplettera med buzzer eller använda LED från tidigare kapitel som statusindikator.

## Anpassning för olika kort

Kodexemplet använder `A0` och antar 10-bitars analogt värde mellan 0 och 1023. Det passar klassisk Arduino-stil, men alla kort beter sig inte likadant.

På ESP32 kan ADC-upplösning, linjäritet och tillåtna pinnar skilja sig. På RP2040-baserade kort finns andra ADC-pinnar och ofta 3,3 V som maximal analog ingång. På moderna Arduino-kort kan upplösningen vara annan eller kunna konfigureras.

Därför bör du göra tre saker när du flyttar experimentet:

- kontrollera vilken pinne som verkligen är analog ingång
- kontrollera maximal tillåten spänning på ADC-ingången
- justera `map()` efter verklig upplösning eller använd en kalibreringsfunktion

Ett mer portabelt mönster är att definiera en konstant:

```cpp
constexpr int ADC_MAX_VALUE = 1023;
```

och sedan använda den i konverteringen:

```cpp
percentValue = map(rawValue, 0, ADC_MAX_VALUE, 0, 100);
```

På ett kort där du använder 12-bitars ADC kan du ändra konstanten till 4095 om upplösningen faktiskt är inställd så.

## I2C-adresser och bussdelning

Många små OLED- och LCD-moduler använder I2C. Det är bekvämt, men det betyder också att displayen delar buss med andra sensorer. Det kan skapa problem om adresser krockar, pull-up-motstånd blir för starka eller kabeldragningen blir lång.

Vanliga symptom är:

- displayen hittas inte
- displayen fungerar ensam men inte tillsammans med sensorn
- I2C-scanner visar fel antal enheter
- projektet låser sig när displayen uppdateras
- vissa värden blir korrupta när kablarna flyttas

Felsök i den här ordningen:

1. Testa displayen ensam med ett minimalt exempel.
2. Kör I2C-scanner och dokumentera adressen.
3. Testa sensorn ensam.
4. Koppla display och sensor tillsammans.
5. Kontrollera att alla moduler delar GND.
6. Kontrollera pull-up-nivåer och matningsspänning.
7. Korta kablarna och sänk I2C-hastigheten om det behövs.

I2C är utmärkt för små interna kopplingar. Det är däremot inte magiskt. Långa kablar, blandade spänningsnivåer och många moduler kan göra en enkel display till ett bussproblem.

## SPI-displayer och pinnkonflikter

Många TFT- och e-paper-displayer använder SPI. Det ger högre hastighet än I2C, men kräver fler signaler: SCK, MOSI, ofta MISO, chip select, data/command och reset.

SPI kan delas mellan flera enheter, men varje enhet behöver normalt egen chip select. Problem uppstår ofta när:

- två moduler använder samma CS-pinne
- en displaymodul inte släpper MISO korrekt
- SD-kort och TFT delar buss men bibliotek antar olika inställningar
- kortets standard-SPI-pinnar skiljer sig från modulens exempel
- 5 V-kort kopplas direkt till 3,3 V-display utan nivåskiftning

När du använder SPI-display bör du dokumentera alla signaler i en pinout-kommentar i koden, inte bara skriva “koppla enligt exempel”. Exempel:

```cpp
// Display wiring:
// VCC -> 3V3
// GND -> GND
// SCK -> board SCK
// MOSI -> board MOSI
// CS  -> D10
// DC  -> D9
// RST -> D8
```

Detta gör experimentet mycket lättare att flytta mellan UNO, ESP32, Pico och andra kort.

## Minnesfrågan: text, grafik och buffertar

Displayer är ofta den första komponenten som gör minne synligt för Arduino-programmeraren. En sensor returnerar kanske några byte. En display kan behöva en hel bildbuffert, flera fonter och många textsträngar.

På små AVR-kort bör du tänka på:

- SRAM är begränsat
- stora displaybuffertar kan ge instabila fel
- långa textsträngar i RAM kan bli ett problem
- stora fonter och bitmappar tar flash
- bibliotek kan dra in mer kod än du först tror

På modernare kort är minnesläget bättre, men principen kvarstår: ett gränssnitt ska vara så enkelt som projektet tillåter. En liten textdisplay kan vara mer robust än en grafisk display med avancerade fonter.

## Menydesign för små system

En liten display tvingar fram prioriteringar. Du kan inte visa allt. Det är bra.

En enkel meny kan byggas kring några fasta vyer:

- **Översikt:** viktigaste värdena
- **Detaljer:** mer tekniska mätvärden
- **Status:** fel, varningar, anslutning och batteri
- **Inställningar:** tröskelvärden eller lägen
- **Om:** kort, firmwareversion och sensorstatus

För många projekt räcker tre vyer:

- översikt
- detaljer
- inställning

Det viktiga är att varje vy har en tydlig uppgift. Undvik att skapa en menystruktur som kräver manual bara för att ändra ett värde.

En praktisk princip:

> En knapp kan byta vy. En lång knapptryckning kan bekräfta. En rotary encoder kan ändra värde.

Men var försiktig med långtryck, dubbeltryck och dolda funktioner. De är praktiska för byggaren men ofta otydliga för användaren.

## När display inte är rätt lösning

Det är lätt att sätta display på allt. Det är inte alltid rätt.

En display kan vara fel val när:

- projektet ska vara mycket strömsnålt
- användaren ändå tittar i en app eller webbsida
- systemet bara behöver visa drift/fel
- miljön är fuktig, ljus, varm eller mekaniskt hård
- kostnad och kapsling är viktigare än lokal information

I sådana fall kan andra gränssnitt vara bättre:

- LED för status
- buzzer för larm
- seriell logg för utveckling
- webbsida på ESP32/ESP8266
- MQTT eller annan extern visualisering
- SD-loggning för senare analys

Det här är särskilt viktigt i sensorprojekt. En display är bra när den hjälper användaren på plats. Den är mindre bra om den bara upprepar data som ändå ska skickas vidare.

## Vanliga misstag

- **Misstag: Att välja TFT när textdisplay hade räckt.**
  - Varför det händer: Färgdisplay känns mer imponerande.
  - Hur man undviker det: Börja med informationsbehovet. Om projektet bara visar tre värden är OLED, LCD eller 7-segment ofta bättre.

- **Misstag: Att skriva om displayen varje varv i `loop()`.**
  - Varför det händer: Det är det enklaste sättet att få något att synas.
  - Hur man undviker det: Uppdatera displayen med intervall eller bara när värden ändras.

- **Misstag: Att glömma RAM-kostnaden för OLED-buffertar.**
  - Varför det händer: Displayen ser liten ut, men biblioteket behöver minne.
  - Hur man undviker det: Kontrollera minnesanvändning efter kompilering och välj enklare bibliotek eller annat kort vid behov.

- **Misstag: Att anta att I2C-displayens adress är 0x3C.**
  - Varför det händer: Många exempel använder 0x3C.
  - Hur man undviker det: Kör I2C-scanner och dokumentera adressen i koden.

- **Misstag: Att blanda 5 V och 3,3 V utan att kontrollera pull-ups.**
  - Varför det händer: I2C-moduler har ofta dolda pull-up-motstånd på breakoutkortet.
  - Hur man undviker det: Kontrollera modulens schema eller mät bussens vilonivå.

- **Misstag: Att bygga menyer med `delay()`.**
  - Varför det händer: Det fungerar i ett isolerat displaytest.
  - Hur man undviker det: Använd `millis()` och låt inmatning, mätning och display uppdateras oberoende.

- **Misstag: Att använda displayen som felsökningsverktyg för allt.**
  - Varför det händer: Displayen är synlig och praktisk.
  - Hur man undviker det: Behåll seriell loggning under utveckling. Displayen ska visa användarinformation, inte ersätta all debug.

- **Misstag: Att inte planera kapsling och montering.**
  - Varför det händer: Displayen fungerar på breadboard.
  - Hur man undviker det: Kontrollera redan tidigt hur display, knappar och kablar ska sitta fysiskt.

## Snabbreferens

| Val | Passar när | Var försiktig med |
|---|---|---|
| 16x2 LCD | Enkel text, robust panel | Kontrast, 5 V/I2C-pullups, begränsad grafik |
| OLED | Kompakt text och enkel grafik | RAM-buffert, liten läsbar yta, statisk bild |
| TFT | Färg, grafer, rikare UI | Mer kod, mer ström, mer minne, SPI-detaljer |
| E-paper | Statisk information och låg ström | Långsam uppdatering, bibliotek, resetsekvenser |
| 7-segment | Tydliga tal | Dåligt för text, kräver drivning |
| LED-matris | Status, ikoner, enkla effekter | Begränsad upplösning, ström |
| En knapp | Växla vy eller start/stopp | Begränsat användarflöde |
| Rotary encoder | Menyer och värdeval | Debounce, riktning, ibland interrupt |
| Joystick | Tvådimensionell styrning eller val | Död zon, brus, kalibrering |
| Keypad | PIN-kod och många knappar | Rad/kolumn-skanning, debounce |
| Kapacitiv touch | Slät panel eller få rörliga delar | Fukt, brus, kapsling |
| IR-fjärr | Enkel fjärrstyrning | Fri sikt, protokoll, knappkoder |

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | 3,3 V eller 5 V beroende på modul |
| Typiskt gränssnitt | I2C, SPI, parallell eller digital I/O |
| Välj när | projektet behöver lokal information eller meny |
| Välj inte när | seriell logg räcker under utveckling |
| Vanliga fel | fel adress, kontrast, bibliotek, för många displayuppdateringar |
| Alternativ att överväga | seriell monitor, LED, webbsida, IR-fjärr, APDS-9960-gest, keypad |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När en display inte svarar, börja med kapitel 9 om bussar innan du byter bibliotek.
- När många knappar, keypad eller flera inmatningar tar slut på pinnar, gå vidare till kapitel 30 om I/O-expansion.
- När IR-fjärr, gestsensor eller optisk inmatning är en del av gränssnittet, jämför med kapitel 24.
- När skärmen flimrar, blir tom eller kräver mer ström än väntat, använd kapitel 34 och felsökningsordningen i kapitel 35.


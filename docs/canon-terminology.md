# Canon: Terminologi

Denna fil ska uppdateras när boken växer. Syftet är att hålla begrepp, svenska termer och engelska standardbegrepp konsekventa.

## Grundprinciper

- Brödtext skrivs på svenska.
- Vedertagna engelska begrepp får användas där de är standard eller där svensk term blir otydlig.
- Första gången ett centralt begrepp används bör svensk term och engelsk term anges tillsammans, till exempel: nivåskiftning (level shifting).

## Centrala begrepp

| Begrepp | Engelsk term | Första kapitel | Kort definition |
|---|---|---|---|
| Arduino-kompatibelt kort | Arduino-compatible board | 1 | Ett utvecklingskort som kan programmeras med Arduino-liknande verktyg eller API. |
| Kortfamilj | board family | 2 | Grupp av kort som delar mikrokontroller, kärna, pinout eller ekosystem. |
| Logiknivå | logic level | 2 | Den spänning som representerar digitalt HIGH och LOW. |
| Gemensam jord | common ground | 4 | Delad referenspunkt mellan kretsar som ska kommunicera elektriskt. |
| Arduino core | Arduino core | 1 | Implementering av Arduino-programmeringsmodellen för en viss mikrokontrollerfamilj. |
| Board package | board package | 1 | Paket med kortdefinitioner, kompilatorinställningar och uppladdningsstöd för en kortfamilj. |
| Bibliotek | library | 1 | Återanvändbar kod som ger stöd för sensorer, displayer, protokoll eller moduler. |
| Shield | shield | 1 | Tilläggskort som ofta monteras ovanpå ett Arduino-kort i kompatibel formfaktor. |
| Breakout board | breakout board | 1 | Litet kort som gör en komponent enklare att koppla, ofta genom 2,54 mm-stift och stödkomponenter. |
| Modul | module | 1 | Färdig funktionell enhet med en eller flera komponenter och ofta regulator, nivåskiftning eller terminaler. |
| Pinout | pinout | 1 | Beskrivning av vilka funktioner kortets fysiska pinnar har. |
| Kortvalsprofil | board selection profile | 2 | Kort dokumentation av projektkrav, valt kort, alternativ och risker. |
| Användbar pinne | usable pin | 2 | En fysisk GPIO som faktiskt kan användas säkert för projektets funktion utan konflikt med boot, inbyggd hårdvara eller reserverade funktioner. |
| Boot-relaterad pinne | boot-related pin | 2 | Pinne vars nivå vid uppstart kan påverka om kortet startar normalt eller hamnar i programmerings-/bootläge. |
| Strömbudget | power budget | 2 | Uppskattning av hur mycket ström kort, sensorer, moduler och laster drar i olika driftlägen. |
| Formfaktor | form factor | 2 | Kortets fysiska storlek, pinplacering och anslutningssätt. |
| GPIO | GPIO | 2 | General Purpose Input/Output; programmerbar pinne som kan användas som digital ingång eller utgång när kortets begränsningar tillåter det. |
| ADC | analog-to-digital converter | 2 | Krets eller funktion som omvandlar analog spänning till digitalt mätvärde. |
| PWM | pulse-width modulation | 2 | Teknik där en digital signal snabbt slås av och på med varierande duty cycle för att styra exempelvis ljusnivå eller motorhastighet. |
| Sketch | sketch | 3 | Arduino-program eller experimentmapp som innehåller källkoden som kompileras och laddas upp. |
| Board Manager | Board Manager | 3 | Funktion i Arduino-miljön för att installera stöd för olika kortfamiljer. |
| Library Manager | Library Manager | 3 | Funktion i Arduino-miljön för att söka, installera och uppdatera bibliotek. |
| FQBN | fully qualified board name | 3 | Entydig teknisk identifierare för kortval i Arduino CLI. |
| Seriell monitor | Serial Monitor | 3 | Verktyg som visar seriell textutskrift från kortet och används som enkel loggkanal. |
| Seriell plotter | Serial Plotter | 3 | Verktyg som visualiserar seriella mätvärden över tid. |
| Minimal testsketch | minimal test sketch | 3 | Litet fristående program som testar en sensor, modul eller krets innan integration. |
| Pinout-kommentar | pinout comment | 3 | Kommentar i koden som dokumenterar kort, spänningsnivå och kopplingar. |
| Spänning | voltage | 4 | Elektrisk potentialskillnad mellan två punkter; i Arduino-kopplingar normalt mätt mot GND. |
| Ström | current | 4 | Elektriskt flöde som avgör hur mycket en komponent eller last belastar kretsen. |
| Resistans | resistance | 4 | Motstånd mot strömflöde, används bland annat för strömbegränsning, pullups och spänningsdelare. |
| Effekt | power | 4 | Energiomvandling per tidsenhet; viktig när regulatorer, motstånd och laster blir varma. |
| Ohms lag | Ohm's law | 4 | Sambandet mellan spänning, ström och resistans: U = R * I. |
| Pull-up | pull-up | 4 | Motstånd eller intern funktion som ger en signal ett definierat HIGH-läge när inget annat driver den. |
| Pull-down | pull-down | 4 | Motstånd som ger en signal ett definierat LOW-läge när inget annat driver den. |
| Nivåskiftning | level shifting | 4 | Anpassning av digital signal mellan olika logiknivåer, exempelvis 5 V och 3,3 V. |
| Spänningsdelare | voltage divider | 4 | Koppling med två motstånd som skapar en lägre spänning från en högre spänning. |
| Avkopplingskondensator | decoupling capacitor | 4 | Kondensator nära en komponent som stabiliserar matningen vid snabba strömvariationer. |
| Flyback-diod | flyback diode | 4 | Skyddsdiod som ger induktiv last en säker strömväg när styrningen bryts. |
| Flytande ingång | floating input | 4 | Digital ingång utan definierad nivå som kan läsa slumpmässigt HIGH eller LOW. |
| I2C logic level converter | I2C logic level converter | 4 | Färdig nivåomvandlarmodul som låter 5 V- och 3,3 V-I2C-enheter dela buss med rätt låg- och högsida. |
| Induktiv last | inductive load | 4 | Last som lagrar energi i magnetfält, exempelvis reläspole, elektromagnet, solenoid eller motor. |
| Digital I/O | digital I/O | 5 | Användning av GPIO som digital ingång eller utgång med logiska nivåer LOW och HIGH. |
| Högimpedant läge | high-impedance mode | 5 | Tillstånd där en ingång påverkar kretsen mycket lite men därför behöver en definierad extern eller intern signalnivå. |
| Aktiv HIGH | active high | 5 | Signal där den aktiva betydelsen representeras av HIGH. |
| Aktiv LOW | active low | 5 | Signal där den aktiva betydelsen representeras av LOW. |
| Kontaktstuds | contact bounce | 5 | Snabba oönskade växlingar när en mekanisk knapp eller brytare ändrar läge. |
| Debouncing | debouncing | 5 | Teknik för att filtrera kontaktstuds och skapa stabila knapphändelser. |
| Open drain | open drain | 5 | Utgångsprincip där signalen aktivt kan dras LOW men behöver pull-up för HIGH. |
| Händelse | event | 5 | Programlogisk representation av att något just inträffade, exempelvis att en knapp blev tryckt. |
| Analog signal | analog signal | 6 | Signal där spänningen kan variera kontinuerligt inom ett mätområde. |
| Referensspänning | reference voltage | 6 | Spänning som ADC:n jämför ingångsspänningen med när råvärdet beräknas. |
| ADC-upplösning | ADC resolution | 6 | Antal digitala steg som ADC:n delar in mätområdet i, ofta angivet i bitar. |
| Råvärde | raw value | 6 | Det obearbetade heltal som `analogRead()` eller motsvarande ADC-läsning returnerar. |
| Kvantisering | quantization | 6 | Omvandling av ett kontinuerligt analogt värde till ett begränsat antal digitala steg. |
| Mätosäkerhet | measurement uncertainty | 6 | Samlad osäkerhet från brus, referens, komponenter, koppling och metod. |
| Kalibrering | calibration | 6 | Anpassning av råvärden till uppmätta gränser eller kända referenser. |
| Filtrering | filtering | 6 | Bearbetning som minskar brus eller snabba variationer i mätvärden. |
| Hysteresis | hysteresis | 6 | Beslutsmönster med separata till- och frånslagströsklar för att undvika pendling. |
| Exponentiellt glidande medelvärde | exponential moving average | 6 | Enkel lågpassfiltrering där nya mätvärden vägs in gradvis. |

| PWM | pulse-width modulation | 7 | Digital pulssignal där duty cycle används för att styra upplevd eller genomsnittlig nivå. |
| Duty cycle | duty cycle | 7 | Andel av en PWM-period där signalen är HIGH. |
| PWM-frekvens | PWM frequency | 7 | Antal PWM-perioder per sekund; påverkar bland annat flimmer, ljud och drivkretsars beteende. |
| PWM-upplösning | PWM resolution | 7 | Antal möjliga steg för duty cycle, ofta uttryckt i bitar. |
| Timer | timer | 7 | Hårdvaruresurs som räknar tid och används av bland annat PWM, `millis()`, servo- och ljudfunktioner. |
| Icke-blockerande kod | non-blocking code | 7 | Kod som låter `loop()` fortsätta köra och använder tidkontroller i stället för blockerande väntan. |
| `millis()` | `millis()` | 7 | Funktion som returnerar antal millisekunder sedan programstart och används för tidsstyrning. |
| Rollover | rollover | 7 | Tillfälle när en räknare når sitt maxvärde och börjar om; hanteras robust med subtraktion av tidsvärden. |
| Avbrott | interrupt | 8 | Mekanism där mikrokontrollern tillfälligt stoppar huvudprogrammet och kör en särskild hanteringsfunktion. |
| ISR | interrupt service routine | 8 | Kort funktion som körs när ett avbrott triggas. |
| `volatile` | `volatile` | 8 | Nyckelord som talar om att en variabel kan ändras utanför den vanliga programordningen. |
| Kritisk sektion | critical section | 8 | Kort koddel där avbrott tillfälligt stoppas för att kopiera eller ändra delad data säkert. |
| Watchdog | watchdog timer | 8 | Timer som kan återställa systemet om programmet fastnar eller slutar visa att det kör korrekt. |
| Timeout | timeout | 8 | Tidsgräns som hindrar kod från att vänta för alltid på sensor, modul eller tillstånd. |
| Säkert läge | safe mode | 8 | Fördefinierat tillstånd där systemet minimerar risk eller skada när fel upptäcks. |
| Brownout | brownout | 8 | Spänningsfall som gör att mikrokontrollern kan starta om eller bete sig instabilt. |

| UART | Universal Asynchronous Receiver/Transmitter | 9 | Seriellt gränssnitt där två enheter skickar data utan separat klockledning, normalt med TX, RX och GND. |
| I2C | Inter-Integrated Circuit | 9 | Tvåtrådsbuss med SDA och SCL där flera enheter kan dela samma buss genom adresser. |
| SPI | Serial Peripheral Interface | 9 | Synkron buss med klocka, data och chip select som ofta används för snabb kommunikation med displayer, minne och kretsar. |
| 1-Wire | 1-Wire | 9 | Specialiserad buss där data kan skickas över en dataledning, ofta använd för DS18B20-temperatursensorer. |
| SDA | serial data | 9 | I2C-signal för data. |
| SCL | serial clock | 9 | I2C-signal för klocka. |
| MOSI | main/controller out, peripheral in | 9 | SPI-signal där controllern skickar data till en peripheral. |
| MISO | main/controller in, peripheral out | 9 | SPI-signal där en peripheral skickar data tillbaka till controllern. |
| SCK | serial clock | 9 | SPI-signal för klocka. |
| Chip select | chip select | 9 | SPI-signal som väljer vilken peripheral som är aktiv på bussen. |
| I2C-adress | I2C address | 9 | Adress som identifierar en peripheral på en I2C-buss. |
| Adresskonflikt | address conflict | 9 | Situation där två I2C-enheter på samma buss använder samma adress. |
| Baud rate | baud rate | 9 | Symbolhastighet för seriell kommunikation, ofta använd som praktisk hastighetsinställning för UART. |
| Pull-up-motstånd | pull-up resistor | 9 | Motstånd som drar en buss eller signal till HIGH när ingen enhet aktivt drar den LOW. |
| Controller | controller | 9 | Enhet som initierar och styr kommunikation på en buss. |
| Peripheral | peripheral | 9 | Enhet som svarar eller kontrolleras av en controller på en buss. |
| Logikanalysator | logic analyzer | 9 | Mätverktyg som visar digitala signaler över tid och hjälper till att felsöka busskommunikation. |
| AVR | AVR | 10 | Mikrokontrollerfamilj som används i många klassiska Arduino-kort. |
| ATmega328P | ATmega328P | 10 | Vanlig 8-bitars mikrokontroller i klassiska UNO- och Nano-liknande kort. |
| ATmega2560 | ATmega2560 | 10 | 8-bitars mikrokontroller i Mega-liknande kort med fler pinnar och mer minne än ATmega328P. |
| 5 V-logik | 5 V logic | 10 | Digital logik där HIGH normalt ligger nära 5 V. Praktiskt med äldre moduler men riskabelt för 3,3 V-kretsar. |
| Pin mapping | pin mapping | 10 | Samlad koppling mellan projektets funktionsnamn och kortets pinnummer eller fysiska pinnar. |
| Shield-kompatibilitet | shield compatibility | 10 | Hur väl ett korts formfaktor och pinout fungerar med Arduino-shields. |


| Tredjepartsvariant | third-party variant | 11 | Arduino-kompatibelt kort från annan tillverkare än Arduino, ofta med egen formfaktor, USB-lösning eller pinout. |
| Klon | clone | 11 | Kort som försöker efterlikna ett välkänt Arduino-kort i formfaktor, pinout eller användningssätt. |
| Lågkostnadskort | low-cost board | 11 | Billigt utvecklingskort där pris och experimentvänlighet ofta är viktigare än dokumentation och långsiktig reproducerbarhet. |
| USB-seriechip | USB-to-serial chip | 11 | Krets som översätter USB från datorn till seriell kommunikation mot mikrokontrollern. |
| CH340 | CH340 | 11 | Vanligt USB-seriechip på många lågkostnadsbaserade Arduino- och ESP-kort. |
| CP210x | CP210x | 11 | Familj av USB-seriechip som förekommer på flera utvecklingskort. |
| Bootloader | bootloader | 11 | Litet program i mikrokontrollern som gör det möjligt att ladda upp ny kod, ofta via seriell kommunikation. |
| Kortidentitet | board identity | 11 | Dokumenterad sammanställning av kortets familj, mikrokontroller, USB-chip, logiknivå, boardval, pinout och särskilda risker. |
| Silkscreen | silkscreen | 11 | Tryckt text och märkning på kretskortet, exempelvis pinnamn och modellbeteckning. |
| NodeMCU | NodeMCU | 11 | Vanlig ESP8266-baserad utvecklingskortfamilj som kan programmeras i Arduino-kompatibel miljö. |
| D1 mini | D1 mini | 11 | Kompakt ESP8266-baserat utvecklingskort, ofta använt i små Wi-Fi-projekt. |

| Modernt Arduino-kort | modern Arduino board | 12 | Arduino-kompatibelt kort med modernare mikrokontroller, mer minne, uppkoppling, ny formfaktor eller andra funktioner utöver klassiska AVR-baserade kort. |
| UNO R4 | UNO R4 | 12 | Modern UNO-generation med 32-bitars mikrokontroller och bekant UNO-formfaktor. |
| UNO R4 WiFi | UNO R4 WiFi | 12 | UNO R4-variant med trådlös kommunikation via separat ESP32-S3-baserad radiomodul. |
| Nano ESP32 | Nano ESP32 | 12 | Kompakt Nano-format där ESP32-S3 är huvudplattform för Arduino-sketch och uppkopplade projekt. |
| MKR-serien | MKR family | 12 | Arduino-kortfamilj med kompakt formfaktor och inriktning mot uppkopplade eller projektnära lösningar. |
| Portenta | Portenta | 12 | Avancerad Arduino-kortfamilj för mer professionella, industriella eller beräkningsintensiva tillämpningar. |
| Native USB | native USB | 12 | USB-funktion där mikrokontrollern själv hanterar USB, vilket kan påverka seriell monitor, reset och uppstart. |
| Kortprofil | board profile | 12 | Dokumenterad sammanställning av pinnar, logiknivå, ADC-skala, bussar och kortspecifika antaganden för ett projekt. |

| ESP8266 | ESP8266 | 13 | Wi-Fi-mikrokontroller som kan programmeras i Arduino-kompatibel miljö och köra användarkoden direkt. |
| ESP8266-modul | ESP8266 module | 13 | Modul, exempelvis ESP-12E/ESP-12F, som innehåller ESP8266 och ofta används på utvecklingskort. |
| Boot-relaterad pinne | boot-related pin | 13 | GPIO vars nivå vid uppstart påverkar mikrokontrollerns bootläge. |
| Deep sleep | deep sleep | 13 | Strömsparläge där mikrokontrollern stängs ned nästan helt och vaknar senare, ofta via reset eller timer. |
| Wi-Fi-station | Wi-Fi station mode | 13 | Läge där ESP8266 ansluter som klient till ett befintligt Wi-Fi-nätverk. |
| I2C-scanner | I2C scanner | 13 | Minimal testsketch som söker efter adresserade I2C-enheter på bussen innan sensorbibliotek används. |
| ESP32-familjen | ESP32 family | 14 | Samling av Espressif-baserade mikrokontroller, moduler och utvecklingskort som kan användas i Arduino-kompatibel miljö. |
| ESP32-chip | ESP32 chip | 14 | Själva mikrokontrollern eller SoC:en i ESP32-familjen, skild från modul och utvecklingskort. |
| ESP32-modul | ESP32 module | 14 | Färdig radiomodul med ESP32-chip, flash, antenn och stödkomponenter. |
| ESP32-utvecklingskort | ESP32 development board | 14 | Kort med ESP32-modul samt USB, regulator, knappar och stift för experiment. |
| Native USB | native USB | 14 | USB-funktion där mikrokontrollern själv hanterar USB, vilket kan påverka uppladdning, seriell monitor och reset. |
| BLE | Bluetooth Low Energy | 14 | Strömsnål Bluetooth-teknik för lokal konfiguration, närvaro och mindre datamängder. |
| LEDC | LED PWM Controller | 14 | ESP32-periferienhet som ofta används för PWM i Arduino-ESP32-miljö. |
| Lokalt reservläge | local fallback mode | 14 | Driftläge där projektet fortsätter fungera lokalt när nätverk eller annan extern tjänst saknas. |
| RP2040 | RP2040 | 15 | Raspberry Pi:s ursprungliga mikrokontrollerfamilj för Pico-liknande kort. |
| RP2350 | RP2350 | 15 | Nyare Raspberry Pi-mikrokontrollerfamilj för Pico 2-liknande kort. |
| PIO | Programmable I/O | 15 | Programmerbara I/O-state machines för tidskritiska signaler på RP2040/RP2350. |
| Pico W | Pico W | 15 | Pico-variant med trådlöst stöd; Arduino-stöd och bibliotek måste kontrolleras för valt projekt. |
| Bootloader-läge | bootloader mode | 15 | Läge där kortet kan ta emot ny firmware eller visas som uppladdningsenhet. |

| Specialkort | specialized board | 16 | Arduino-kompatibelt kort där en tydlig specialisering, till exempel formfaktor, radio, kamera, batteristöd eller prestanda, motiverar kortvalet. |
| Småkort | compact board | 16 | Mycket kompakt utvecklingskort där liten fysisk storlek är en huvudfördel men där pinnar och intern hårdvara måste kontrolleras extra noggrant. |
| Feather-format | Feather form factor | 16 | Adafruit-formfaktor och ekosystem med många kort och tillägg, ofta lämpat för batteridrivna prototyper. |
| Teensy | Teensy | 16 | Arduino-kompatibel kortfamilj från PJRC som ofta används när prestanda, timing, ljud eller USB-funktioner är viktiga. |
| ESP32-CAM | ESP32-CAM | 16 | ESP32-baserad kameraplattform med Wi-Fi och kamera, men ofta med få fria pinnar och mer krävande uppladdning och strömförsörjning. |
| Kortprofil | board profile | 16 | Samlad dokumentation av exakt kortmodell, mikrokontroller, logiknivå, pinout, board-val, intern hårdvara och risker. |
| TinyML | TinyML | 16 | Maskininlärning på små mikrokontroller- eller edge-enheter där minne, energi och beräkningskapacitet är starkt begränsade. |


| LED | light-emitting diode | 17 | Lysdiod som används som indikator, statusutgång, ljuseffekt eller del av ett enkelt användargränssnitt. |
| Seriemotstånd | series resistor | 17 | Motstånd i serie med LED som begränsar strömmen och skyddar både LED och mikrokontrollerpinne. |
| RGB-LED | RGB LED | 17 | LED med separata röda, gröna och blå kanaler som kan blandas till olika färger. |
| Common anode | common anode | 17 | LED- eller RGB-LED-koppling där flera kanaler delar positiv anslutning och ofta styrs med inverterad logik. |
| Common cathode | common cathode | 17 | LED- eller RGB-LED-koppling där flera kanaler delar jordanslutning och styrs med vanlig positiv logik. |
| PWM-dimning | PWM dimming | 17 | Styrning av upplevd ljusstyrka genom att snabbt växla LED mellan av och på med olika duty cycle. |
| Statusmönster | status pattern | 17 | Konsekvent blink-, färg- eller ljusmönster som visar systemets tillstånd. |

| Adresserbar LED | addressable LED | 18 | LED med inbyggd styrkrets som gör att varje pixel kan få ett eget färgvärde via en digital dataström. |
| NeoPixel | NeoPixel | 18 | Adafruits produktnamn och ett vanligt vardagsnamn för WS2812/SK6812-liknande adresserbara LED-produkter. |
| WS2812B | WS2812B | 18 | Vanlig adresserbar 5 V RGB-pixel med en dataledning och timingkänsligt protokoll. |
| SK6812 | SK6812 | 18 | WS2812-liknande adresserbar LED-familj som ofta förekommer i RGB- och RGBW-varianter. |
| APA102 | APA102 | 18 | Adresserbar LED-typ med separat data- och clock-signal, ofta använd när timing eller uppdatering behöver vara mer flexibel. |
| DotStar | DotStar | 18 | Adafruits namn för APA102-liknande adresserbara LED-produkter. |
| RGBW | RGBW | 18 | Färgformat där varje pixel har röd, grön, blå och separat vit kanal. |
| Färgordning | color order | 18 | Den ordning som färgkanaler skickas i till LED-pixeln, exempelvis RGB eller GRB. |
| Global ljusstyrka | global brightness | 18 | Övergripande ljusstyrkebegränsning som påverkar alla pixlar och kan minska strömförbrukningen. |

| Aktiv buzzer | active buzzer | 19 | Ljudkomponent med inbyggd oscillator som normalt piper när den får matning eller en aktiv digital signal. |
| Passiv buzzer | passive buzzer | 19 | Ljudkomponent utan egen oscillator som behöver en växlande signal för att skapa ton. |
| Piezoelement | piezo element | 19 | Tunn komponent som kan omvandla elektrisk påverkan till vibration och ljud, ofta med låg strömförbrukning. |
| `tone()` | `tone()` | 19 | Arduino-funktion som genererar en fyrkantsvåg med vald frekvens på en digital pinne. |
| `noTone()` | `noTone()` | 19 | Arduino-funktion som stoppar en tidigare startad ton på en pinne. |
| Ljudmönster | sound pattern | 19 | Konsekvent sekvens av pip, toner och pauser som visar systemstatus eller händelsetyp. |
| Drivsteg | driver stage | 19 | Transistor-, MOSFET- eller förstärkarlösning som gör att en mikrokontrollerpinne kan styra en last utan att själv leverera lastströmmen. |
| Fyrkantsvåg | square wave | 19 | Digital växlande signal som ofta används för att driva passiva buzzers och skapa enkla toner. |
| Servo | servo | 20 | Motorenhet med motor, växellåda, positionsåterkoppling och intern styrning som kan placera axeln ungefärligt efter en styrsignal. |
| Kontinuerlig servo | continuous rotation servo | 20 | Servo-liknande motorenhet där styrsignalen påverkar rotationsriktning och hastighet snarare än position. |
| DC-motor | DC motor | 20 | Motor som roterar när den får likspänning och där riktning och hastighet ofta styrs med drivare och PWM. |
| H-brygga | H-bridge | 20 | Motordrivarkrets eller modul som kan byta strömriktning genom en DC-motor och därmed styra rotationsriktning. |
| Stallström | stall current | 20 | Strömmen en motor kan dra när den är blockerad eller startar från stillastående, ofta mycket högre än normal driftström. |
| Stegmotor | stepper motor | 20 | Motor som flyttas i diskreta steg och ofta används när repeterbar rörelse eller positionering behövs. |
| STEP/DIR | step/direction | 20 | Vanligt gränssnitt för stegmotordrivare där en puls på STEP ger rörelse och DIR anger riktning. |
| Acceleration | acceleration | 20 | Kontrollerad ökning av motorhastighet som minskar risken för tappade steg eller mekaniska ryck. |
| Relä | relay | 21 | Styrd brytare som kan slå av eller på en last via en separat styrsignal. |
| COM/NO/NC | common/normally open/normally closed | 21 | Vanliga reläkontakter där COM är gemensam, NO är öppen i viloläge och NC är sluten i viloläge. |
| MOSFET | MOSFET | 21 | Transistor som ofta används som elektronisk brytare för lågspända DC-laster. |
| Low-side switch | low-side switch | 21 | Koppling där drivsteget bryter lastens anslutning mot jord. |
| Logic-level MOSFET | logic-level MOSFET | 21 | MOSFET som kan slås på tillräckligt väl med mikrokontrollerns logikspänning. |
| `Rds(on)` | on-resistance | 21 | Resistansen genom en påslagen MOSFET, viktig för värme och spänningsfall. |
| `Vgs(th)` | gate threshold voltage | 21 | Gate-spänning där MOSFET:en precis börjar leda en liten testström, inte full påslagning. |
| Flyback-diod | flyback diode | 21 | Diod som skyddar drivsteget mot spänningsspikar från induktiva laster. |
| Solenoid | solenoid | 21 | Spole som skapar mekanisk rörelse när den aktiveras, till exempel i en ventil eller slagaktuator. |
| Elektromagnet | electromagnet | 21 | Spole som skapar magnetkraft utan att nödvändigtvis ha en definierad slaglängd. |
| Spole som last | coil load | 21 | Samlingsbegrepp för reläspole, solenoid, elektromagnet och liknande induktiva laster. |
| Aktiv låg | active low | 21 | Logik där LOW aktiverar funktionen och HIGH avaktiverar den. |
| Säker startlogik | safe startup logic | 21 | Konstruktion och kod som gör att lasten hamnar i säkert läge vid reset och uppstart. |


| Display | display | 22 | Utenhet som visar text, siffror, symboler eller grafik för användaren. |
| Användargränssnitt | user interface | 22 | Kombination av presentation, inmatning och tillstånd som gör att användaren kan förstå och påverka systemet. |
| Presentation | presentation | 22 | Den del av gränssnittet som visar information, exempelvis display, LED eller ljudsignal. |
| Inmatning | input | 22 | Den del av gränssnittet där användaren påverkar systemet, exempelvis knapp, brytare eller rotary encoder. |
| UI-tillstånd | UI state | 22 | Variabel eller datastruktur som beskriver vilken vy, meny eller inställning som är aktiv. |
| Framebuffer | framebuffer | 22 | Minnesbuffert som innehåller bildens pixlar innan de skickas till displayen. |
| Rotary encoder | rotary encoder | 22 | Vridgivare som används för menyval eller värdejustering, ofta med inbyggt tryck. |
| E-paper | e-paper | 22 | Displayteknik som behåller bilden utan kontinuerlig uppdatering och passar information som ändras sällan. |
| Miljösensor | environmental sensor | 23 | Sensor som mäter omgivningens egenskaper, exempelvis temperatur, luftfuktighet, lufttryck eller luftkvalitet. |
| Relativ luftfuktighet | relative humidity | 23 | Andel vattenånga i luften jämfört med vad luften kan bära vid aktuell temperatur. |
| Lufttryck | air pressure | 23 | Tryck från omgivande luft, ofta mätt i hPa i väderstationsprojekt. |
| 1-Wire | 1-Wire | 23 | Digital buss där flera sensorer kan dela en datapinne och identifieras med unika adresser. |
| Sensorprofil | sensor profile | 23 | Kort dokumentation av sensor, gränssnitt, matning, placering, mätintervall och felkällor. |
| Självuppvärmning | self-heating | 23 | När sensor eller närliggande elektronik värmer mätpunkten och påverkar mätvärdet. |
| Kalibrering | calibration | 23 | Jämförelse eller justering mot referens för att förstå eller minska mätavvikelse. |
| Hysteresis | hysteresis | 23 | Separata gränser för aktivering och avaktivering så att styrning inte växlar snabbt runt ett tröskelvärde. |


| LDR | light-dependent resistor | 24 | Ljuskänsligt motstånd som ofta används i en spänningsdelare för relativ ljusmätning. |
| Fototransistor | phototransistor | 24 | Ljuskänslig transistor som kan användas för snabbare optisk detektion än en LDR. |
| Lux | lux | 24 | Enhet för belysningsstyrka, alltså ljusflöde per yta viktat ungefär mot mänskligt seende. |
| Spektral känslighet | spectral sensitivity | 24 | Beskriver vilka våglängder en sensor reagerar mest på. |
| Färgsensor | color sensor | 24 | Sensor som mäter ljus i flera kanaler, ofta röd, grön, blå och clear. |
| Clear-kanal | clear channel | 24 | Ofiltrerad eller bredare ljuskanal i vissa färgsensorer som används som referens för total ljusnivå. |
| UV-sensor | UV sensor | 24 | Sensor som reagerar på ultraviolett ljus, ofta UVA och/eller UVB. |
| IR-reflektionssensor | IR reflective sensor | 24 | Sensor som skickar ut infrarött ljus och mäter reflekterat ljus från ett objekt eller en yta. |
| Optisk brytare | optical interrupter | 24 | Sensor där en ljusstråle mellan sändare och mottagare bryts av ett passerande objekt. |
| Optisk sensorprofil | optical sensor profile | 24 | Dokumentation av sensor, placering, ljuskälla, geometri, gränssnitt, filtrering och begränsningar. |

| Avståndsmätning | distance measurement | 25 | Mätning av hur långt bort ett objekt är från sensorn. |
| Närvarodetektion | presence detection | 25 | Tolkning av om person eller objekt finns i ett område, ofta utan exakt avstånd. |
| Objektupptäckt | object detection | 25 | Detektion av att ett objekt finns nära, passerar en punkt eller bryter en signal. |
| Ultraljudssensor | ultrasonic sensor | 25 | Sensor som skickar ljudpuls och mäter ekotid för att uppskatta avstånd. |
| Time-of-Flight | Time-of-Flight | 25 | Optisk avståndsteknik där flygtid eller relaterade ljusegenskaper används för mätning. |
| PIR | passive infrared | 25 | Sensor som reagerar på förändringar i infraröd värmestrålning, ofta från människor eller djur i rörelse. |
| mmWave | millimeter wave radar | 25 | Radarbaserad sensorteknik som kan upptäcka närvaro och ibland zoner eller avstånd. |
| Reed switch | reed switch | 25 | Magnetpåverkad brytare som ofta används för dörrar, luckor och ändlägen. |
| Hallgivare | Hall sensor | 25 | Elektronisk sensor som reagerar på magnetfält. |
| Analog Hall-sensor | analog Hall sensor | 25 | Hallgivare som ger en varierande analog spänning beroende på magnetfältet. |
| 49E-typ | 49E-type Hall sensor | 25 | Vanlig typbeteckning för enkla analoga Hall-sensorer i Arduino- och makerprojekt. |
| Ljusbarriär | light barrier | 25 | Sändare och mottagare där ett objekt detekteras genom att bryta en ljusstråle. |
| Närvarohållning | presence hold | 25 | Tidslogik där systemet fortsätter betrakta ett område som upptaget efter senaste rörelse. |
| Sensorprofil | sensor profile | 25 | Dokumentation av sensor, mätområde, gränssnitt, felkällor och praktiska begränsningar. |
| Tilt-sensor | tilt sensor | 26 | Sensor eller brytare som ändrar signal när den lutas över ett ungefärligt läge. |
| Vibrationssensor | vibration sensor | 26 | Sensor som reagerar på skakning, slag eller mekanisk vibration, ofta som händelsesignal. |
| Accelerometer | accelerometer | 26 | Sensor som mäter acceleration längs en eller flera axlar, inklusive tyngdkraftens acceleration. |
| Gyroskop | gyroscope | 26 | Sensor som mäter rotationshastighet runt en eller flera axlar. |
| IMU | inertial measurement unit | 26 | Modul som ofta kombinerar accelerometer och gyroskop, ibland även magnetometer. |
| Magnetometer | magnetometer | 26 | Sensor som mäter magnetfält och kan användas för kompassriktning med rätt kalibrering. |
| Sensoraxel | sensor axis | 26 | Definierad mätriktning, exempelvis X, Y eller Z, som måste dokumenteras mot faktisk montering. |
| Drift | drift | 26 | Långsam avvikelse över tid, särskilt viktig för gyroskopbaserad vinkeluppskattning. |
| Sensorfusion | sensor fusion | 26 | Metod där data från flera sensorer kombineras för stabilare orienterings- eller rörelseuppskattning. |

| Ljudsensor | sound sensor | 27 | Modul eller krets som används för att upptäcka ljudhändelser eller ge en enkel ljudrelaterad signal. |
| Mikrofonmodul | microphone module | 27 | Modul med mikrofon och ofta förstärkning eller komparator som gör ljudsignalen lättare att läsa. |
| Ljudtrigger | sound trigger | 27 | Digital händelsesignal som visar att ljudnivån passerat en tröskel. |
| Mittnivå | bias level | 27 | Analog vilonivå som ljudsignalen svänger runt, ofta ungefär halva matningsspänningen. |
| Peak-to-peak | peak-to-peak | 27 | Skillnad mellan högsta och lägsta signalvärde under ett tidsfönster. |
| Samplingsfönster | sample window | 27 | Kort tidsperiod där flera mätvärden samlas för att ge ett mer stabilt ljudmått. |
| I2S | I2S | 27 | Digitalt ljudgränssnitt för strömmad ljuddata mellan mikrofon, ljudkrets och mikrokontroller. |
| Ljudaktivitet | sound activity | 27 | Tolkad systemstatus som visar att ljudnivån varit tillräckligt hög enligt vald tröskel och tidslogik. |
| Relativ ljudnivå | relative sound level | 27 | Jämförbart ljudmått inom samma projekt, men inte kalibrerad ljudtrycksnivå i decibel. |

| Spänningsdelare | voltage divider | 28 | Två eller flera motstånd som delar ned en spänning till en lägre mätbar nivå. |
| Shuntmotstånd | shunt resistor | 28 | Litet känt motstånd som används för att mäta ström genom spänningsfallet över motståndet. |
| High-side-mätning | high-side measurement | 28 | Strömmätning där shunten eller sensorn placeras mellan matningsspänning och last. |
| Low-side-mätning | low-side measurement | 28 | Strömmätning där shunten placeras mellan last och jord. |
| Hall-effektsensor | Hall effect sensor | 28 | Sensor som kan mäta ström indirekt genom magnetfältet runt en ledare. |
| Effekt | power | 28 | Hur snabbt energi används eller levereras, ofta beräknad som spänning multiplicerat med ström. |
| Energi | energy | 28 | Ackumulerad effekt över tid, exempelvis wattimmar i batteri- och loggningssammanhang. |
| Batteristatus | battery state | 28 | Tolkad nivå som beskriver om batteriet är OK, lågt eller kritiskt snarare än exakt procent. |
| Strömbudget | power budget | 28 | Uppskattning av hur mycket ström olika delar av systemet använder i olika lägen. |

| GNSS | GNSS | 29 | Samlingsnamn för satellitbaserade positioneringssystem som används för position och ofta exakt tid. |
| Fix | fix | 29 | Tillstånd där en GNSS-modul har tillräcklig satellitinformation för att ge användbar position. |
| RTC | real-time clock | 29 | Klockkrets som håller kalender- och klocktid även när mikrokontrollern startar om. |
| UTC | Coordinated Universal Time | 29 | Standardiserad tidsreferens som ofta är lämplig att lagra i loggfiler. |
| NTP | Network Time Protocol | 29 | Metod för att hämta tid via nätverk. |
| RFID | RFID | 29 | Radiofrekvensidentifiering som används för att läsa ID från taggar eller kort på kort avstånd. |
| NFC | NFC | 29 | Närfältskommunikation, en kortdistansvariant som ofta används för kort och taggar. |
| UID | unique identifier | 29 | Identifierande kod som kan läsas från många taggar eller enheter, men som inte i sig är stark autentisering. |
| Nod-ID | node ID | 29 | Identifierare för en specifik enhet eller mätpunkt i ett system. |
| Tidsstämplad händelse | timestamped event | 29 | Loggpost som kombinerar tid, nod, händelsetyp, värde och status. |

| I/O-expansion | I/O expansion | 30 | Användning av externa kretsar för att ge mikrokontrollern fler digitala eller analoga anslutningsmöjligheter. |
| Shift register | shift register | 30 | Krets som flyttar bitar seriellt och kan användas för att skapa flera parallella utgångar eller läsa flera parallella ingångar. |
| I/O-expander | I/O expander | 30 | Krets som ger extra digitala in- och utgångar, ofta via I2C. |
| PCF8575 | PCF8575 I/O expander | 30 | Enkel 16-bitars I2C-I/O-expander för knappar, LED och långsamma digitala styrsignaler; ersätter inte PWM-driver, högströmsdrivare eller snabb sampling. |
| Multiplexer | multiplexer | 30 | Krets som väljer en av flera signaler och kopplar den till en gemensam signalväg. |
| Bitmask | bitmask | 30 | Tal där enskilda bitar representerar olika tillstånd eller funktioner. |
| Drivkrets | driver circuit | 31 | Krets eller modul som omvandlar en mikrokontrollers styrsignal till lämplig laststyrning. |
| Lågsidestyrning | low-side switching | 31 | Styrning där drivkomponenten sitter mellan lasten och jord. |
| Högsidestyrning | high-side switching | 31 | Styrning där drivkomponenten sitter mellan plusmatningen och lasten. |
| Konstantströmsdrivare | constant-current driver | 31 | Drivare som reglerar strömmen genom en last, ofta högeffekts-LED. |

| Icke-flyktigt minne | non-volatile memory | 32 | Minne som behåller data efter omstart eller strömavbrott. |
| EEPROM | EEPROM | 32 | Icke-flyktigt minne för små datamängder som ändras sällan, exempelvis konfiguration. |
| Extern EEPROM | external EEPROM | 32 | Separat EEPROM-krets, ofta via I2C eller SPI, som används när intern EEPROM saknas eller inte räcker. |
| FRAM | FRAM | 32 | Icke-flyktigt minne med hög skrivtålighet som passar för ofta ändrat tillstånd och små händelseloggar. |
| Flashlagring | flash storage | 32 | Flashbaserad lagring för program, filer eller inställningar beroende på plattform. |
| SD-kort | SD card | 32 | Flyttbart flashbaserat lagringsmedium som ofta används för större loggfiler. |
| CSV | CSV | 32 | Textbaserat tabellformat där värden separeras med kommatecken och enkelt kan analyseras i efterhand. |
| Framebuffer | framebuffer | 32 | RAM-buffert där hela eller delar av en displaybild byggs upp före visning. |
| Displaykontroller | display controller | 32 | Krets som styr en displaypanel och erbjuder ett gränssnitt mot mikrokontrollern. |
| Displaydrivare | display driver | 32 | Hårdvara eller mjukvara som förenklar styrning av display eller LED-visning. |
| Analog signalanpassning | analog signal conditioning | 33 | Anpassning av en analog signal så att den blir säker, stabil och mätbar för mikrokontrollern. |
| Spänningsdelare | voltage divider | 33 | Två resistorer som skalar ned en spänning till ett lägre mätområde. |
| RC-filter | RC filter | 33 | Filter byggt med resistor och kondensator, ofta för att dämpa snabba störningar. |
| Op-förstärkare | operational amplifier / op-amp | 33 | Analog förstärkarkrets som kan förstärka, buffra eller filtrera signaler. |
| Buffert | buffer / voltage follower | 33 | Koppling som avlastar signalkällan och ger lägre utgångsimpedans utan att ändra signalnivån nämnvärt. |
| Komparator | comparator | 33 | Krets som jämför två analoga nivåer och ger en digital utgång. |
| Hysteres | hysteresis | 33 | Separata på- och avtrösklar som gör ett tröskelbeslut stabilare. |
| Instrumentförstärkare | instrumentation amplifier | 33 | Förstärkare för små differenssignaler där gemensam störning behöver undertryckas. |



| Kapacitiv jordfuktssensor | capacitive soil moisture sensor | 23 | Sensor som uppskattar markfukt via kapacitiv påverkan snarare än direkt ström genom jord. |
| Resistiv jordfuktssensor | resistive soil moisture sensor | 23 | Enkel fuktsensor som mäter ledningsförmåga men kan korrodera om den står spänningssatt länge. |
| Vattennivåsensor | water level sensor | 23 | Modul eller givare som används för att indikera vattennärvaro eller ungefärlig nivå. |
| Regnsensor | rain sensor | 23 | Modul som reagerar på vatten på en exponerad yta och ofta används som enkel nederbördsindikator. |
| MQ-gassensor | MQ gas sensor | 23 | Vanlig uppvärmd gasindikator för experiment; bör inte användas som säkerhetskritisk gasdetektor. |
## Kapitel 35: Felsökning med metod

- **Minimal reproduktion:** Minsta möjliga koppling och kod som fortfarande visar felet eller bevisar funktionen.
- **Diagnostisk sketch:** Liten testsketch som isolerar en komponent, buss, pinne eller strömförsörjningssituation.
- **I2C-scanner:** Sketch som testar vilka I2C-adresser som svarar på bussen.
- **Heartbeat:** Periodisk logg eller signal som visar att programmet fortfarande kör.
- **Logikanalysator:** Verktyg för att observera digitala signaler, timing och protokoll.
- **Oscilloskop:** Verktyg för att observera spänning över tid, särskilt brus, dippar, flanker och analoga signaler.
- **Metodregel:** Ändra en sak åt gången och dokumentera resultatet.

| FSR | force-sensitive resistor | 33 | Resistiv sensor som ändrar resistans när den belastas och ofta läses via spänningsdelare. |
| Flexsensor | flex sensor | 33 | Resistiv böjsensor som ändrar resistans när den böjs och används främst för relativa mätvärden. |
| Vågcell | load cell | 33 | Kraft- eller viktsensor med bryggkoppling som ger mycket små differenssignaler. |
| HX711 | HX711 load cell amplifier/ADC | 33 | Vanlig modul för att läsa vågceller med förstärkning och högupplöst digital avläsning. |

## Kapitel 36: Från breadboard till återanvändbar modul

- **Pin mapping:** Samlad koppling mellan logiska funktioner och faktiska mikrokontrollerpinnar.
- **Hårdvarukonfiguration:** Projektfil eller kodavsnitt där pinnummer, I2C-adresser, tidsintervall och kortspecifika val samlas.
- **Modulgränssnitt:** Den praktiska beskrivningen av vad en modul behöver, vad den gör, hur den konfigureras och hur den testas.
- **Wrapper-klass:** Tunt kodlager runt ett bibliotek eller en komponent som ger projektet ett stabilt och tydligt gränssnitt.
- **Diagnostisk testsketch:** Fristående testprogram som verifierar en modul innan den integreras i ett större system.
- **Mekanisk stabilitet:** Hur väl kablar, kontakter, lödningar och montering tål hantering utan intermittenta fel.
- **Modulregel:** Dokumentera pinout, spänning, gränssnitt, bibliotek och testmetod innan en fungerande breadboard-koppling plockas isär.


| Sensor- och styrstation | sensor and control station | 37 | Sammanhängande Arduino-projekt som kombinerar mätning, presentation, styrning och diagnostik. |
| Mätflöde | measurement flow | 37 | Kedjan från sensorläsning till validerade mätvärden som resten av systemet kan använda. |
| Beslutsflöde | decision flow | 37 | Koddel som tolkar mätvärden och bestämmer systemstatus. |
| Systemstatus | system state | 37 | Namngivet läge, exempelvis normal, varning, alarm eller sensorfel, som används av flera utgångar. |
| Stubbe | stub | 37 | Enkel ersättningsfunktion eller testimplementation som används innan en verklig komponent kopplas in. |
| Hysteresis | hysteresis | 37 | Skillnad mellan gräns för aktivering och avaktivering som minskar pendling och fladdrig styrning. |
| Integrationsplan | integration plan | 37 | Stegvis ordning för att testa och koppla ihop moduler i ett större projekt. |

| Snabbvalsguide | quick selection guide | 38 | Kort beslutsstöd som hjälper läsaren välja mellan vanliga teknikalternativ. |
| Beslutsfråga | decision question | 38 | Fråga som gör ett teknikval tydligare genom att koppla valet till ett projektkrav. |
| Risklista | risk list | 38 | Samlad lista över möjliga problem som bör kontrolleras innan integration. |
| Komponentmall | component template | 38 | Återanvändbar struktur för att dokumentera modulnamn, chip, matning, signalnivå, gränssnitt och bibliotek. |
| Joystick-modul | joystick module | 22 | Inmatningsmodul med två analoga axlar och ofta en digital tryckknapp. |
| Keypad / knappsats | keypad / matrix keypad | 22 | Knappmatris där rader och kolumner skannas för att läsa många knappar med färre pinnar. |
| Kapacitiv touch | capacitive touch | 22 | Beröringsinmatning som reagerar på ändrad kapacitans i stället för mekanisk rörelse. |
| IR-fjärrkontroll | IR remote control | 22 | Fjärrinmatning via infrarött ljus och mottagarmodul, vanligt för enkla meny- eller lägesval. |
| IR-mottagarmodul | IR receiver module | 24 | Optisk mottagare för modulerad IR-signal från fjärrkontroll; används som digital inmatning, inte som allmän ljussensor. |

| nRF24L01 | nRF24L01 | 9 | Billig 2,4 GHz-radiomodul för korta datapaket mellan små noder, känslig för stabil 3,3 V-matning. |
| 433 MHz RF | 433 MHz RF | 9 | Enkel radiolänk för fjärrsignaler eller små datamängder, ofta billig men störningskänslig. |
| RS485 | RS485 | 9 | Elektriskt gränssnitt för robust seriell kommunikation över längre kabel med transceivermoduler. |
| CAN | CAN bus | 9 | Robust meddelandebuss för flera noder, vanlig i fordon, robotar och mer krävande system. |
| LoRa | LoRa | 9 | Radioteknik för små datamängder över lång räckvidd med låg datahastighet. |
| PCA9685 | PCA9685 PWM driver | 20 | I2C-styrd PWM-driver som ofta används för många servon eller flera PWM-kanaler. |
| L298N | L298N motor driver | 20 | Vanlig äldre H-bryggmodul för DC-motorer; pedagogiskt användbar men ofta ineffektiv och varm jämfört med modernare drivers. |
| DRV8833 | DRV8833 motor driver | 20 | Liten modern dubbel H-brygga som ofta passar små DC-motorer och batteridrivna projekt bättre än L298N, förutsatt att motorström, kylning och matning är rätt dimensionerade. |
| L9110S | L9110S motor driver | 20 | Enkel lågkostnadsdrivare för små DC-motorer i kit- och robotprojekt; olämplig för tyngre laster och motorer med hög stallström. |
| ULN2003 | ULN2003 transistor array | 20 | Transistorarray som ofta används med 28BYJ-48-stegmotor eller flera små lågside-laster. |
| A4988 | A4988 stepper driver | 20 | Vanlig STEP/DIR-drivare för bipolära stegmotorer med strömbegränsning och microstepping. |
| DRV8825 | DRV8825 stepper driver | 20 | STEP/DIR-drivare för bipolära stegmotorer, liknande A4988 men med egna ström-, kyl- och microstepping-egenskaper. |

## PLAN4-kompletteringar

Följande komponentgrupper har lagts till eller förstärkts efter `handbokstruktur-v2` och ska hanteras konsekvent i boken:

- Använd `rotary encoder` för vridgivare med A/B-signaler; kalla den inte potentiometer.
- Använd `joystick-modul` för tvåaxlad analog inmatning med eventuell knapp.
- Använd `keypad` eller `knappsats` för knappmatris.
- Beskriv billiga jordfukt-, vattennivå-, regn- och MQ-moduler som indikatorer eller hobbygivare, inte som exakta eller säkerhetskritiska mätinstrument.
- Beskriv FSR och flexsensorer som relativa resistiva sensorer.
- Beskriv vågcell + HX711 som en mätkedja som kräver mekanisk montering och kalibrering.
- Beskriv L298N som vanlig men äldre och ofta ineffektiv drivmodul.
- Beskriv A4988/DRV8825 som STEP/DIR-drivare som kräver strömbegränsning och kylning.

| LM393 | LM393 comparator | 33 | Vanlig komparator på billiga sensormoduler, ofta kopplad till potentiometer och digital tröskelutgång. |
| Digital tröskelmodul | digital threshold module | 33 | Sensormodul som ger en digital ja/nej-signal utifrån en inställd tröskel, inte ett exakt mätvärde. |
| KY-037 | KY-037 sound sensor module | 27 | Vanlig ljudsensormodul med mikrofon och ofta både analog utgång och digital tröskelutgång; passar enkla ljudhändelser, inte seriös ljudanalys. |
| LM386 | LM386 audio amplifier | 19 | Enkel ljudförstärkarkrets eller modul för små högtalare; skiljs från aktiv/passiv buzzer och kräver hänsyn till brus, matning och volym. |
| APDS-9960/GY-9960 | APDS-9960 gesture/color/proximity sensor | 24 | I2C-baserad optisk sensormodul för färg, ljus, närhet och enkla handgester; kräver ofta bibliotek och stabil placering. |


## PLAN5-kompletteringar

Följande komponenter och begrepp har lagts till eller förstärkts efter `handbokstruktur-v3` och ska hanteras konsekvent i boken:

- Beskriv elektromagneter, solenoider och andra spolar som induktiva laster som kräver drivsteg, separat matning vid behov och flyback-skydd.
- Beskriv DRV8833 som en liten modern dubbel H-brygga för små motorer, ofta lämpligare än L298N i batteridrivna projekt.
- Beskriv L9110S som en enkel lågkostnadsdrivare för små DC-motorer, inte som lösning för tyngre laster.
- Beskriv LM393-moduler som digitala tröskelmoduler, inte som exakta mätinstrument.
- Beskriv I2C logic level converter som praktisk nivåskiftning mellan 5 V-kort och 3,3 V-I2C-moduler.
- Beskriv KY-037 som enkel ljudsensor för ljudhändelser och relativ nivå, inte som inspelningsmikrofon.
- Beskriv LM386 som enkel ljudförstärkare för små högtalare, inte som buzzer.
- Beskriv APDS-9960/GY-9960 som I2C-baserad optisk sensor för färg, ljus, närhet och enkla gester, inte som kamera eller robust industriell gestdetektor.
- Beskriv PCF8575 som 16-bitars I2C-I/O-expander för enkla digitala signaler, inte som ersättning för PWM-driver, högströmsdrivare eller snabb sampling.
- Beskriv analog Hall-sensor och 49E-typ som varierande analog magnetfältssensor, inte som lika enkel av/på-kontakt som reedkontakt eller digital Hall-sensor.
- Använd begreppet induktiv last konsekvent för laster som lagrar energi i magnetfält, inklusive reläspolar, elektromagneter, solenoider och motorer.

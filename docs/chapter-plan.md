# Kapitelplan
## Övergripande upplägg
Boken är en stor modulär lärobok, handbok och referens om Arduino-kompatibla system. Den börjar med ekosystem, kortval och praktiska elektronikgrunder, fortsätter med gemensamma funktioner och kommunikationsbussar, går vidare till kortfamiljer, aktuatorer, sensorer och IC-kretsar, och avslutas med robust systembygge, felsökning och snabbvalsguider.
Varje teknikdel bör innehålla:
- vad tekniken, kortet, sensorn eller kretsen gör
- typiska varianter
- när den är ett bra val
- när något annat passar bättre
- elektriska krav och begränsningar
- vanliga bibliotek och kodmönster
- praktiskt experiment
- felsökning
- referenssammanfattning

## Del 1: Orientering och grundplattform
### Kapitel 0: Inledning — Så använder du boken
- **Syfte:** Förklarar bokens målgrupp, upplägg och hur den kan användas både som lärobok och referens.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 1: Arduino-kompatibla system som ekosystem
- **Syfte:** Ger en karta över Arduino-världen: officiella kort, kompatibla kort, kloner, tredjepartskärnor, shields, moduler, breakout boards och bibliotek.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 2: Att välja rätt kort för rätt projekt
- **Syfte:** Introducerar ett beslutsramverk för kortval baserat på I/O, minne, CPU, spänningsnivå, nätverk, formfaktor, pris och bibliotek.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 3: Utvecklingsmiljö, bibliotek och projektstruktur
- **Syfte:** Går igenom Arduino IDE, board managers, library managers, exempelprojekt, seriell monitor och återanvändbar experimentstruktur.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 4: Elektriska grunder för programmerare
- **Syfte:** Ger en praktisk elektronikintroduktion för programmerare: spänning, ström, resistans, effekt, jord, pull-up, pull-down, kondensatorer och nivåskiftning.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Del 2: Gemensamma funktioner i Arduino-kompatibla kort
### Kapitel 5: Digital I/O, knappar och logiska signaler
- **Syfte:** Fördjupar digitala ingångar och utgångar, knappar, flytande ingångar, interna pullups och debouncing.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 6: Analog läsning, ADC och mätosäkerhet
- **Syfte:** Förklarar analogRead, ADC-upplösning, referensspänning, brus, sampling, filtrering och kalibrering.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 7: PWM, timers och tidsstyrning
- **Syfte:** Visar PWM, duty cycle, frekvens, timers, millis, micros och icke-blockerande kod.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 8: Avbrott, watchdog och robust körning
- **Syfte:** Behandlar interrupt, watchdog, felåterhämtning och hur man undviker vanliga avbrottsproblem.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 9: Kommunikation: UART, I2C, SPI och 1-Wire
- **Syfte:** Jämför UART, I2C, SPI och 1-Wire med fokus på val, koppling, adressering och felsökning.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Del 3: Kortfamiljer och kompatibla varianter
### Kapitel 10: Klassiska Arduino-kort: UNO, Nano och Mega
- **Syfte:** Går igenom klassiska AVR-baserade Arduino-kort som UNO, Nano och Mega.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 11: Kloner, lågkostnadskort och tredjepartsvarianter
- **Syfte:** Behandlar ATmega328P-baserade kloner, CH340/CP210x, NodeMCU, Wemos/Lolin D1 mini, ESP8266 och ESP32 DevKit-varianter.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 12: Moderna Arduino-kort
- **Syfte:** Behandlar modernare officiella Arduino-kort, mer minne, USB-förbättringar, trådlös kommunikation och nyare mikrokontrollers.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 13: ESP8266 och NodeMCU
- **Syfte:** Ger ESP8266 och NodeMCU egen plats med fokus på Wi-Fi, 3,3 V, boot pins och enkla IoT-projekt.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 14: ESP32-familjen i Arduino-världen
- **Syfte:** Behandlar ESP32-familjen med Wi-Fi, BLE, ADC-begränsningar, deep sleep, pinout och bibliotek.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 15: Raspberry Pi Pico, RP2040 och RP2350 i Arduino-miljö
- **Syfte:** Visar hur Pico, RP2040 och RP2350 passar i Arduino-världen.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 16: Småkort, specialkort och avancerade utvecklingskort
- **Syfte:** Samlar småkort, specialkort och avancerade utvecklingskort som XIAO, Feather, Teensy, ESP32-CAM och Portenta-liknande kort.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Del 4: Utenheter, aktuatorer och användargränssnitt
### Kapitel 17: LED, RGB-LED och ljuseffekter
- **Syfte:** Går igenom vanliga LED, seriemotstånd, RGB-LED, transistorstyrning, LED-matriser och ljuseffekter.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 18: Adresserbara LED: NeoPixel, WS2812 och liknande
- **Syfte:** Behandlar NeoPixel, WS2812 och andra adresserbara LED med timing, nivåskiftning och strömförsörjning.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 19: Buzzers, ljudsignaler och enkla ljudutgångar
- **Syfte:** Jämför aktiva och passiva buzzers, piezoelement, tone och enkla ljudmönster.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 20: Servon, DC-motorer och stegmotorer
- **Syfte:** Behandlar servon, DC-motorer, H-bryggor, ESC, stegmotorer, strömtoppar och separat matning.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 21: Reläer, MOSFET:ar, solenoider och andra laster
- **Syfte:** Visar relämoduler, MOSFET:ar, ULN2803, flyback-dioder, optokoppling och säkra lastgränser.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 22: Displayer och enkla användargränssnitt
- **Syfte:** Jämför LCD, OLED, TFT, e-paper, sifferdisplayer, knappar, keypads, rotary encoders och menyer.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Del 5: Sensorer som kategorier
### Kapitel 23: Temperatur, fukt, tryck och miljösensorer
- **Syfte:** Jämför DHT, DS18B20, BMP280, BME280, SHT-serier och miljömätning i praktiken.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 24: Ljus, färg, UV och optiska sensorer
- **Syfte:** Behandlar LDR, fototransistor, digitala ljussensorer, färgsensorer, UV-sensorer, IR-reflektion och optiska brytare.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 25: Avstånd, närvaro och objektupptäckt
- **Syfte:** Jämför ultraljud, IR-avstånd, ToF, PIR, radar/mmWave, reed switches och brytare.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 26: Rörelse, orientering och vibration
- **Syfte:** Går igenom accelerometer, gyro, IMU, magnetometer, tilt, vibration och grundläggande filtrering.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 27: Ljud, mikrofoner och enkla signalmätningar
- **Syfte:** Jämför ljudnivåmoduler, analoga mikrofoner, I2S-mikrofoner och ljudtriggerkretsar.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 28: Ström, spänning, energi och batterimätning
- **Syfte:** Behandlar spänningsdelare, INA219/INA226, Hall-sensorer, shuntmotstånd, batterimätning och energilogging.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 29: Position, tid och identitet
- **Syfte:** Går igenom GPS/GNSS, RTC, RFID/NFC och enkla identitetslösningar.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Del 6: Vanliga IC-kretsar och moduler
### Kapitel 30: I/O-expansion, shift registers och multiplexers
- **Syfte:** Behandlar 74HC595, 74HC165, MCP23017, PCF8574, analoga multiplexers och I/O-expansion.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 31: Drivkretsar för LED, motorer och laster
- **Syfte:** Fördjupar drivkretsar för LED, motorer och laster: ULN2803, MOSFET, H-brygga, stegmotordrivare och konstantströmsdrivare.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 32: Displaykretsar, minne och datalagring
- **Syfte:** Behandlar EEPROM, FRAM, SD-kort, displaydrivare, buffring och datalagring.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 33: Analog signalanpassning, op-förstärkare och komparatorer
- **Syfte:** Introducerar op-förstärkare, komparatorer, filtrering, offset, skydd och analog front-end.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Del 7: Systembygge, robusthet och referens
### Kapitel 34: Strömförsörjning, batteridrift och robust konstruktion
- **Syfte:** Samlar strömförsörjning, batteridrift, regulatorer, buck/boost, sleep, kapsling, kablar och störningar.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 35: Felsökning med metod
- **Syfte:** Visar systematisk felsökning med seriell loggning, minimal testsketch, multimeter, I2C-scanner, logikanalysator och oscilloskop.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 36: Från breadboard till återanvändbar modul
- **Syfte:** Tar experiment från breadboard till mer hållbara moduler med pinout, lödbar prototyp, wrapper-klasser och konfiguration.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 37: Sammanhängande projekt: modulär sensor- och styrstation
- **Syfte:** Knyter ihop kortval, sensorer, aktuatorer, kommunikation, strömförsörjning och felsökning i ett större projekt.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.
### Kapitel 38: Referens: snabbvalsguider och jämförelsetabeller
- **Syfte:** Samlar snabbvalsguider och jämförelsetabeller för kort, bussar, sensorer, aktuatorer, matning och vanliga fel.
- **Läsarens förkunskaper:** Tidigare kapitel och praktisk programmeringsvana.
- **Nya huvudbegrepp:** Definieras i kapitlet och registreras i canon-filerna när kapitlet skrivs.
- **Praktiskt exempel/scenario:** Ett avgränsat experiment som kan byggas vidare eller jämföras med andra kapitel.
- **Övning:** Dokumentera val, koppling, kod och felsökningsobservationer.
- **Svårighetsgrad:** Erfaren, med praktiskt stöd där elektronikmomenten kräver det.
- **Bygger vidare på:** Föregående delars begrepp och praktiska experiment.

## Progressionskontroll

- Begrepp introduceras först i ekosystem-, kortvals- och elektronikgrundkapitlen.
- Sensorer och aktuatorer kommer efter I/O, analog läsning, PWM och bussar.
- Kortfamiljer placeras före komponentkategorier så att läsaren kan förstå plattformsskillnader.
- IC-kretsar och analog signalanpassning kommer efter att läsaren mött konkreta sensorer och utenheter.
- Slutprojektet binder ihop kortval, sensorer, aktuatorer, strömförsörjning och felsökning.

# 38. Referens: snabbvalsguider och jämförelsetabeller

## Så använder du referensen

Det här kapitlet är inte tänkt som en vanlig lektion. Det är bokens snabbaste väg från fråga till beslut. Använd det när du står med en projektidé, ett okänt kort, en sensorpåse, en modul eller ett felsymptom och vill veta vilken riktning som är rimlig att börja med.

Snabbvalsguiderna ersätter inte datablad, pinout-diagram eller bibliotekens dokumentation. De hjälper dig i stället att ställa rätt frågor innan du kopplar, beställer komponenter eller skriver mycket kod.

Använd tabellerna som första sortering:

- välj kort efter projektkrav
- välj buss efter avstånd, hastighet, antal enheter och felsökningsbarhet
- välj sensor efter vad som faktiskt ska mätas
- välj aktuator, drivkrets och matning utan att överbelasta mikrokontrollern
- identifiera risker innan de blir felsökningsproblem

När ett val verkar rimligt gör du fortfarande grundkontrollerna: spänning, ström, logiknivå, pinout, gränssnitt, bibliotek, fysisk miljö och felsökningsmöjlighet.

> Jag väljer den här lösningen eftersom projektet kräver X, och den här komponenten löser X bättre än alternativen med acceptabla begränsningar.

## Snabbindex: börja i rätt kapitel

| Om frågan gäller | Börja i | Gå vidare till |
|---|---:|---|
| Kortval och plattform | 2 | 10–16 |
| Digitala signaler, knappar och pinnar | 5 | 9, 30 |
| Analog mätning | 6 | 23, 28, 33 |
| PWM, dimring och styrsignaler | 7 | 17, 18, 20 |
| Avbrott, timing och robusthet | 8 | 35 |
| Kommunikation och bussar | 9 | 22, 23–29, 32 |
| Användargränssnitt och inmatning | 22 | 5, 6, 8, 24 |
| LED, ljud, motorer och laster | 17–22 | 31, 34 |
| Vanliga kit- och butikssensorer | 23, 24, 33 | 6, 35 |
| Sensorer och mätning | 23–29 | 33, 34 |
| I/O-expansion, drivning och minne | 30–32 | 9, 34 |
| Analog signalanpassning och strömförsörjning | 33–34 | 35 |
| Felsökning och projektmognad | 35–37 | 38 |

Använd snabbindexet som första navigering. När du har hittat rätt område använder du kapitlets översikt, snabbval, snabbreferens, vanliga misstag, felsökning och eventuella relaterat-hänvisningar för att ringa in nästa praktiska steg.

## Snabbguide: vanliga kompletterande moduler och kretsar

Följande moduler och kretsprinciper dyker ofta upp när ett projekt växer från enkel prototyp till något som ska driva last, läsa en billig sensormodul, hantera fler pinnar eller koppla ihop 5 V- och 3,3 V-delar. Använd tabellen som vägvisare till rätt kapitel och kontrollpunkt.

| När du står med detta behov | Börja med | Se upp med | Förklaras praktiskt i |
|---|---|---|---|
| Styra ventil, lås, solenoid, elektromagnet eller annan spole | MOSFET/transistor eller drivmodul | Induktiv last, separat matning, flyback-skydd och värme | Kapitel 21 |
| Driva små DC-motorer effektivt i batteriprojekt | DRV8833 | Motorström, stallström, kylning och rätt matningsspänning | Kapitel 31 |
| Få en enkel liten robotmotor att snurra med lågkostnadsmodul | L9110S | Endast små laster, värme och begränsad strömtålighet | Kapitel 31 |
| Förstå varför en billig sensor bara ger digital ja/nej-signal | LM393-baserad tröskelmodul | Potentiometertröskel, aktiv nivå och att signalen inte är exakt mätning | Kapitel 33 |
| Koppla 5 V-Arduino till 3,3 V-I2C-modul | I2C logic level converter | LV/HV-sida, gemensam jord, pullups och bussens spänning | Kapitel 9 och 33 |
| Upptäcka klapp eller enkel ljudhändelse | KY-037 eller liknande ljudsensormodul | Brus, känslighet, tröskel och att modulen inte är en ljudinspelare | Kapitel 27 |
| Göra en liten högtalare hörbar från analog signal eller enkel ljudutgång | LM386-modul | Brus, volym, högtalarimpedans och matningsstörningar | Kapitel 19 och 27 |
| Mäta färg, ljus, närhet eller enkla handgester med en I2C-modul | APDS-9960/GY-9960 | Kort avstånd, ljusmiljö, bibliotek och mekanisk placering | Kapitel 24 |
| Få 16 extra enkla digitala I/O via I2C | PCF8575 | Inte PWM, inte hög ström, kvasi-bidirektionellt beteende och adressval | Kapitel 30 |
| Mäta magnetfält ungefärligt eller följa magnetisk rörelse | Analog Hall-sensor, till exempel 49E/OH49E-typ | Kalibrering, brus, magnetplacering och att värdet är analogt snarare än bara av/på | Kapitel 25 |

Tumregeln är att modellnamnet sällan är hela svaret. Börja med funktionen: mäta, driva, förstärka, nivåskifta eller expandera. Kontrollera sedan spänning, ström, logiknivå, gränssnitt och miljö innan du kopplar in modulen.

Direktval i praktiken:

- Välj **DRV8833** före L298N när projektet är litet, batteridrivet eller behöver bättre verkningsgrad.
- Välj **L9110S** när det är ett enkelt kitprojekt med små motorer och låga krav.
- Välj **MOSFET** när lasten är lågspänd DC och behöver mer ström än en pinne klarar.
- Välj **logic level converter** när 3,3 V- och 5 V-I2C-moduler blandas och pullup-nivån annars blir osäker.
- Välj **LM393-modul** när du behöver en enkel digital tröskelsignal, inte ett exakt mätvärde.

## Snabbguide: från projektidé till första test

När du startar ett nytt Arduino-projekt kan du använda följande ordning.

1. Beskriv vad systemet ska göra utan att nämna komponenter.
2. Lista indata: sensorer, knappar, brytare, kommunikation och användarval.
3. Lista utdata: LED, display, ljud, motorer, reläer, nätverk och loggning.
4. Bestäm fysisk miljö: skrivbord, utomhus, fordon, batteri, verkstad eller kapsling.
5. Välj ungefärlig kortfamilj.
6. Välj sensorer och aktuatorer.
7. Kontrollera spänning och ström.
8. Kontrollera gränssnitt och antal pinnar.
9. Kontrollera bibliotek och exempel.
10. Bygg minsta test för varje komponent.
11. Integrera en komponent i taget.
12. Spara pin mapping, adresser och matning när första testet fungerar.

Det här låter långsamt, men det sparar tid. De flesta svåra Arduino-fel kommer från för snabba antaganden: fel pinne, fel logiknivå, för svag matning, fel bibliotek, fel adress eller för mycket integration på en gång.

## Snabbval: vilket kort ska jag börja med?

| Projektbehov | Bra förstaval | Varför | Se upp med |
|---|---|---|---|
| Enkla tester med LED, knappar och sensorer | UNO, Nano eller kompatibel ATmega328P-variant | Enkel modell, mycket dokumentation, 5 V-logik | Lite minne, ingen inbyggd nätverksteknik |
| Många pinnar och klassisk Arduino-känsla | Mega 2560 eller liknande | Många I/O, enkel portering från UNO | Stor formfaktor, äldre arkitektur |
| Wi-Fi till låg kostnad | ESP8266/NodeMCU eller ESP32 | Bra för enkla IoT-projekt | 3,3 V-logik, boot pins, strömspikar |
| Wi-Fi, BLE och mer prestanda | ESP32-familjen | Kraftfullt, många varianter, stort ekosystem | Pinout- och variantdetaljer spelar stor roll |
| Många GPIO och bra timingexperiment | Raspberry Pi Pico/RP2040/RP2350 | Bra pris/prestanda, många pinnar, intressant I/O | Trådlöst kräver särskild variant eller extern modul |
| Liten fysisk produkt | Seeed XIAO, Adafruit Feather, Pro Mini eller liknande | Liten formfaktor, ofta batterivänligt | Mindre felsökningsvänligt, tät pinout |
| Avancerad styrning, snabb I/O eller ljud/LED med höga krav | Teensy eller snabbare specialkort | Hög prestanda och bra periferiutbud | Mer plattformsspecifik kod |
| Industriell prototyp eller avancerad gateway | Portenta-liknande kort eller robust specialkort | Mer resurser, robustare målmiljö | Dyrare och mer komplext |
| Undervisning med reproducerbara labbar | Officiellt Arduino-kort eller väldokumenterad variant | Färre okända faktorer | Högre pris |
| Snabba billiga experiment | Lågkostnadsklon | Billigt och lätt att ha flera av | Varierande kvalitet, USB-drivrutin och pinout |

### Enkel beslutsfråga

Börja med att fråga:

> Behöver projektet nätverk?

Om svaret är ja är ESP32 ofta ett bättre förstaval än klassisk UNO. Om svaret är nej och projektet är enkelt är UNO/Nano-liknande kort fortfarande mycket användbara. Om projektet kräver många pinnar eller speciell timing kan Mega, Pico eller specialkort vara bättre.

## Snabbval: när ska jag välja ett annat kort?

| Symptom i projektet | Trolig orsak | Byt eller ändra till |
|---|---|---|
| Minnet tar slut på UNO/Nano | För mycket bibliotek, displaykod eller text | ESP32, Pico, Mega eller modern Arduino |
| Wi-Fi-modul gör projektet krångligt | Nätverk är centralt men kortet saknar det | ESP32 eller Nano ESP32 |
| Motorn stör sensorerna | Matning och jordning är för svag | Separat matning, bättre avkoppling, robustare kortval |
| ADC-värden är instabila | Brus, referensproblem eller dålig analogdel | Bättre analog design, extern ADC eller annan sensor |
| Pinnar tar slut | För många I/O direkt på kortet | I/O-expander, shift register, multiplexer eller större kort |
| Batteriet tar slut snabbt | Kortet eller kringkomponenter drar för mycket | Low-power-kort, sleep, effektiv regulator |
| Biblioteket fungerar bara ibland | Fel core, fel variant eller föråldrat bibliotek | Annat kort, annan biblioteksversion eller enklare komponent |
| Tidskritisk signal fungerar inte | För mycket avbrott, långsam kod eller fel plattform | Pico/PIO, Teensy eller dedikerad drivkrets |
| Kopplingen blir svår att felsöka | För många komponenter samtidigt | Modulär uppdelning och testsketcher |

## Snabbval: kommunikationsbuss

| Gränssnitt | Passar bäst för | Styrkor | Begränsningar | Vanliga exempel |
|---|---|---|---|---|
| Digital I/O | Knappar, brytare, enklare moduler | Enkelt, tydligt, lätt att felsöka | Kräver en pinne per signal | Knapp, PIR, reed switch |
| Analog ingång | Enkla varierande signaler | Billigt och direkt | Brus, kalibrering, ADC-skillnader | LDR, potentiometer, analog sensor |
| UART | Punkt-till-punkt-kommunikation | Enkelt, robust, bra för moduler | Ofta en enhet per port | GPS, seriell modul, debug |
| I2C | Flera sensorer på samma buss | Få pinnar, adresserbar buss | Pullups, adresskrockar, nivåskiftning, korta avstånd | BME280, OLED, RTC |
| SPI | Snabb dataöverföring | Snabbt, tydligt master/slave-mönster | Fler pinnar, chip select per enhet | SD-kort, TFT, snabb ADC |
| 1-Wire | Enkla distribuerade sensorer | Få ledare, flera sensorer möjligt | Timingkänsligt, särskilda komponenter | DS18B20 |
| PWM | Styrning av effektliknande nivå | Enkelt för LED och motorhastighet | Inte riktig analog spänning | LED-dimning, fläkt, motorstyrning |
| I2S | Digitalt ljud | Bättre för ljuddata | Kräver kraftigare kort och bibliotek | Digital mikrofon, ljudutgång |
| USB | Datoranslutning, HID, seriell | Kraftfullt där kortet stöder det | Kortspecifikt | Seriell port, tangentbordsmakro | 
| nRF24L01 | Små trådlösa noder och fjärrkontroller | Billig, snabb för korta paket | Känslig 3,3 V-matning, kräver bibliotek | Sensornod, handkontroll |
| 433 MHz RF | Enkel fjärrsignal eller envägsdata | Billigt, enkelt, ofta lång räckvidd inomhus | Störningskänsligt, begränsad återkoppling | Fjärrknapp, väderstationsmodul |
| RS485 | Robust seriell kommunikation över kabel | Längre kablar, flera noder möjligt | Kräver transceiver, terminering och protokoll | Sensorbuss, verkstad, installation |
| CAN | Robust kommunikation mellan noder | Felhantering, prioriterade meddelanden, tåligt | Kräver CAN-stöd och transceiver | Fordon, robot, distribuerat system |
| LoRa | Små datamängder över lång räckvidd | Lång räckvidd och låg energiförbrukning | Låg bandbredd, regelverk, längre sändtid | Utomhussensor, fjärrmätning |

### Tumregler för bussval

Välj I2C när du har flera långsamma sensorer nära kortet.

Välj SPI när du behöver hastighet, särskilt för displayer eller SD-kort.

Välj UART när modulen redan talar seriellt eller när kommunikationen är punkt-till-punkt.

Välj analog ingång bara när du accepterar brus, kalibrering och variation mellan kort.

Välj digital I/O när informationen verkligen är av/på.

Välj färdig digital sensor när noggrannhet och stabilitet är viktigare än lägsta pris.

Välj nRF24L01 när flera små noder ska skicka korta datapaket och du kan ge modulen stabil 3,3 V.

Välj 433 MHz när signalen är enkel och du kan acceptera begränsad robusthet.

Välj RS485 när kommunikationen behöver gå längre över kabel än vad UART, I2C eller SPI klarar på ett pålitligt sätt.

Välj CAN när flera noder behöver dela meddelanden robust i fordon, robotar eller mer krävande miljöer.

Välj LoRa när räckvidd och låg energiförbrukning är viktigare än hög datahastighet.

## Snabbval: sensor efter mätuppgift

| Jag vill mäta eller upptäcka | Börja med | Välj hellre något annat när |
|---|---|---|
| Temperatur inomhus | BME280, SHT-serie eller DS18B20 | DHT om pris är viktigare än kvalitet |
| Temperatur utomhus eller i vätska | DS18B20 i kapslad variant | BME/SHT om du även behöver luftdata |
| Luftfuktighet | SHT-serie eller BME280 | Undvik om miljön kondenserar utan rätt kapsling |
| Lufttryck | BMP280 eller BME280 | Välj annan sensor om absolut noggrannhet krävs |
| Enkel ljusnivå | LDR eller digital ljussensor | Digital sensor om värden ska jämföras över tid |
| Färg | Färgsensor eller APDS-9960/GY-9960 | Kamera om scenen är komplex |
| Enkel gest eller optisk närhet | APDS-9960/GY-9960 | Knappar, touch eller ToF om gestläget blir instabilt |
| UV | UV-sensormodul | Professionell mätare om värdet är säkerhetskritiskt |
| Avstånd nära objekt | ToF-sensor | Ultraljud om objektet är större och avståndet längre |
| Billig avståndsmätning | Ultraljud | ToF om precision nära objekt är viktig |
| Mänsklig rörelse | PIR | Radar/mmWave om närvaro utan rörelse behövs |
| Närvaro vid dörr/fönster | Reed switch eller hall-sensor | PIR om du vill se rörelse i rummet |
| Ungefärlig magnetposition eller magnetisk rörelse | Analog Hall-sensor, till exempel 49E-typ | Reedkontakt eller digital Hall-sensor om du bara behöver av/på-status |
| Lutning eller slag | Accelerometer | IMU om orientering behövs |
| Rotation/orientering | IMU | Encoder om du mäter mekanisk axel |
| Vibration | Vibrationssensor eller accelerometer | Accelerometer om du behöver amplitud eller mönster |
| Ljudhändelse | Enkel ljudsensor | Mikrofon/I2S om du behöver analysera ljud |
| Klapp eller enkel ljudhändelse | KY-037 eller liknande ljudsensormodul | I2S-mikrofon om du behöver ljuddata eller analys |
| Digital tröskel från enkel sensor | LM393-baserad modul | Analog mätning om du behöver veta hur mycket signalen varierar |
| Strömförbrukning | INA219/INA226-liknande sensor | Shunt och förstärkare om du behöver egen mätkedja |
| Batterispänning | Spänningsdelare till ADC | Batteriövervakningskrets om systemet ska vara robust |
| Position utomhus | GPS/GNSS | Annan teknik om du är inomhus |
| Tid utan nätverk | RTC-modul | NTP om systemet ändå alltid har nätverk |
| Identitet | RFID/NFC | QR/kamera eller BLE om användarflödet kräver det |

## Snabbval: aktuatorer och utenheter

| Jag vill göra detta | Börja med | Viktig kontroll |
|---|---|---|
| Visa enkel status | Vanlig LED | Seriemotstånd och pinström |
| Visa flera statuslägen | RGB-LED | Gemensam anod/katod och ström |
| Skapa ljuseffekter | Adresserbara LED | Extern matning, nivåskiftning och kondensator |
| Ge enkelt pip | Aktiv buzzer | Spänning och ström |
| Spela tonmönster | Passiv buzzer | Timer/PWM-konflikter |
| Driva liten högtalare | LM386-modul eller annan liten förstärkare | Brus, matning, volym och högtalarimpedans |
| Visa text | I2C-OLED eller LCD | Adress, bibliotek och läsbarhet |
| Visa grafik | TFT | SPI-hastighet, minne och bibliotek |
| Visa statisk information med låg ström | E-paper | Uppdateringshastighet och bibliotek |
| Flytta något till viss vinkel | Servo | Separat matning och strömtoppar |
| Snurra motor enkelt | DC-motor med drivkrets | H-brygga/MOSFET, motorström och flyback |
| Styra position stegvis | Stegmotor med driver | Strömbegränsning och kylning |
| Slå av/på last | Relämodul eller MOSFET | Lasttyp, ström, spänning och isolering |
| Styra ventil, solenoid eller elektromagnet | MOSFET och flyback-skydd | Induktiv last, separat matning, värme och mekanik |
| Läsa användarval | Knapp, rotary encoder eller keypad | Debouncing, pullups och antal pinnar |
| Styra meny eller markör | Rotary encoder eller joystick | Studs, avläsningstakt och analog mittpunkt |
| Läsa många knappar | Keypad eller I/O-expander | Rad/kolumn-koppling och debounce |
| Göra beröringsknapp | Kapacitiv touchmodul | Fukt, jordning och falska tryck |
| Ta emot fjärrkontroll | IR-mottagarmodul | Fri sikt, protokoll och okända knappkoder |

## Snabbval: drivkrets eller direkt pinne?

En Arduino-pinne är en styrsignal, inte en strömkälla för laster. Använd direkt pinne bara för små, enkla signaler.

| Last eller modul | Direkt pinne? | Rekommendation |
|---|---|---|
| En LED med seriemotstånd | Ofta ja | Håll strömmen låg |
| Flera LED | Sällan | Använd transistor, drivkrets eller LED-driver |
| RGB-LED | Ibland | Kontrollera total ström |
| Adresserbar LED-strip | Nej för matning | Data från pinne, extern matning för LED |
| Aktiv buzzer | Ibland | Kontrollera ström och använd transistor vid behov |
| Passiv buzzer | Ibland | Kontrollera timerkonflikter |
| Liten högtalare | Nej | Använd förstärkare, till exempel LM386-modul, om ljudet ska bli hörbart |
| Litet servo | Nej för matning | Signalen från pinne, separat matning |
| DC-motor | Nej | H-brygga eller MOSFET-driver, till exempel DRV8833 för små motorer eller L9110S för enkla kitprojekt |
| Stegmotor | Nej | Stegmotordrivare, till exempel ULN2003 för 28BYJ-48 eller A4988/DRV8825 för bipolär motor |
| Reläspole | Nej | Relämodul eller transistor med skydd |
| Solenoid, elektromagnet eller annan spole | Nej | MOSFET/transistor eller drivmodul, separat matning och flyback-skydd |
| Sensor med digital utgång | Ja, för signal | Kontrollera logiknivå |
| I2C-sensor | Ja, för signal | Kontrollera pullups och spänning |

Snabb beslutslinje:

- Om lasten gör mekaniskt arbete, lyser starkt, värmer, klickar eller rör sig: använd normalt drivsteg.
- Om pinnen bara skickar information till en modul: kontrollera främst logiknivå och buss.
- Om du är osäker: börja med separat matning, gemensam jord och ett drivsteg som tål mer än den uppmätta lasten.

## Snabbval: vanliga färdiga moduler

| Modul | Passar bäst för | Viktig kontroll |
|---|---|---|
| Rotary encoder | Meny, volym, inställningsratt | Debounce, A/B-riktning och eventuell knapp |
| Joystick-modul | Tvåaxlig styrning och enkla kontroller | Analog mittpunkt, dödzon och knappsignal |
| Keypad | PIN-kod, menyval och många knappar | Rad/kolumn-matris, debounce och pinbehov |
| TTP223/MPR121 touch | Beröringsknappar och paneler | Fukt, jordning och oavsiktliga tryck |
| IR-mottagare | Enkel fjärrstyrning | Fri sikt, störljus och protokoll |
| LM393-baserad tröskelmodul | Enkel ja/nej-detektering från ljus, ljud, regn eller vibration | Potentiometertröskel, aktiv nivå och att digital utgång inte är exakt mätning |
| KY-037 ljudsensormodul | Klappdetektering, enkel ljudnivå och ljudhändelser | Inte seriös ljudinspelning eller exakt ljudanalys |
| LM386-förstärkarmodul | Liten högtalare och enkel analog ljudutgång | Brus, matning, volym och högtalarimpedans |
| APDS-9960/GY-9960 | Färg, ljus, närhet och enkla handgester via I2C | Bibliotek, avstånd, ljusmiljö och mekanisk placering |
| Jordfukt/vatten/regn | Enkla indikatorer i växt- och väderprojekt | Korrosion, smuts och att värdena ofta är relativa |
| MQ-gassensor | Grov gas-/rökindikation i experiment | Uppvärmning, strömförbrukning och kalibrering |
| FSR/flexsensor | Tryck, böjning och kreativa gränssnitt | Spänningsdelare, kalibrering och icke-linjär respons |
| Vågcell + HX711 | Vikt och kraft | Mekanisk montering, kalibrering och stabil matning |
| PCA9685 | Många servosignaler | Löser signaler, inte servoström |
| ULN2003 + 28BYJ-48 | Enkel kit-stegmotor | Långsam rörelse, moment och matning |
| L298N | Äldre DC-/stegmotordrivning | Värme, spänningsfall och låg effektivitet |
| DRV8833 | Små DC-motorer och vissa små stegmotorer | Motorström, kylning, batteridrift och rätt matning |
| L9110S | Enkla små DC-motorer i kit- och robotprojekt | Endast lätta laster, värme och stallström |
| A4988/DRV8825 | Bipolära stegmotorer | Strömbegränsning, kylning och acceleration |
| I2C logic level converter | 5 V-kort till 3,3 V-I2C-moduler | Rätt låg-/högsida, gemensam jord och pullups |

## Snabbval: modul eller lös IC-krets?

| Välj färdig modul när | Välj lös IC-krets när |
|---|---|
| Du vill experimentera snabbt | Du designar egen krets eller PCB |
| Databladet kräver stödkomponenter du inte vill dimensionera nu | Du vill kontrollera varje detalj |
| Komponenten har mycket små ben | Du har rätt lödutrustning och layout |
| Modulen har regulator, pullups eller nivåskiftning som hjälper dig | Modulens extrafunktioner stör projektet |
| Du undervisar eller prototypar | Du optimerar kostnad, storlek eller ström |
| Du vill felsöka på breadboard | Du bygger produktnära hårdvara |
| Biblioteksexempel utgår från modulen | Du kan läsa datablad och anpassa drivrutin |

### Viktig varning om moduler

Moduler är bekväma, men de kan dölja viktiga detaljer. En modul kan ha egna pullups, regulator, nivåskiftare, lysdioder, skyddsmotstånd eller filter. Det är ofta bra, men kan också ge oväntad strömförbrukning, fel logiknivå eller konflikter när flera moduler kopplas ihop.

Dokumentera därför alltid inte bara komponenten utan modulen:

- modulens namn
- chip på modulen
- matningsspänning
- signalnivå
- gränssnitt
- adress eller chip select
- extra komponenter på modulen
- vald biblioteksversion

## Snabbval: nivåskiftning och spänningsnivåer

| Situation | Risk | Rekommenderad åtgärd |
|---|---|---|
| 5 V Arduino till 3,3 V sensor | Sensorns ingång kan skadas | Nivåskifta signaler eller använd 3,3 V-kort |
| 3,3 V kort till 5 V modul | Modulen kanske inte tolkar HIGH | Kontrollera datablad, använd nivåskiftare vid behov |
| I2C med blandade spänningar | Pullups kan dra bussen till fel nivå | Placera pullups till rätt spänning eller använd I2C-nivåskiftare |
| 5 V-kort till 3,3 V-I2C-sensor | 5 V på SDA/SCL kan skada modulen | Använd I2C logic level converter med LV till 3,3 V och HV till 5 V |
| SPI till SD-kortmodul | Kortet kan vara 3,3 V även om modulen tar 5 V matning | Kontrollera signalnivå, inte bara VCC |
| Adresserbara LED med 3,3 V data och 5 V matning | För låg HIGH-nivå kan ge flimmer | Använd nivåskiftare eller kortare ledning om det fungerar stabilt |
| UART mellan olika kort | Fel nivå eller korsad TX/RX | Kontrollera nivå, gemensam jord och TX/RX-korsning |
| Extern modul med egen matning | Signal saknar referens | Koppla gemensam jord om inte isolering används |

## Snabbval: strömförsörjning

| Projekt | Bra startpunkt | Se upp med |
|---|---|---|
| Enkel breadboard med sensorer | USB från dator | Datorns USB-port är inte lastkälla för motorer |
| LED-strip | Separat 5 V-nätaggregat | Gemensam jord och tillräcklig ström |
| Servo eller flera servon | Separat 5–6 V matning | Strömtoppar, jord och spänningsdippar |
| Batteridriven sensor | LiPo eller AA med effektiv regulator | Sleep current och regulatorns viloström |
| ESP32 med Wi-Fi | Stabil 3,3 V-reglering via kortets regulator eller bra matning | Strömspikar vid radioaktivitet |
| Motorprojekt | Separat motormatning | Störningar, back-EMF och jorddragning |
| Lång kabel till sensor | Lokal avkoppling och robust gränssnitt | Brus, spänningsfall och jordloopar |
| Utomhusprojekt | Skyddad regulator och kapsling | Fukt, kondens och temperatur |

### Enkel strömbudget

Gör alltid en enkel strömbudget före integration:

| Del | Uppskattad ström | Kommentar |
|---|---:|---|
| Mikrokontrollerkort | 50–250 mA | Beror starkt på kort och radio |
| Sensorer | 1–50 mA | Vissa kan sova mellan mätningar |
| Display | 5–200 mA | OLED/TFT/backspegel skiljer mycket |
| LED/indikatorer | 2–20 mA per LED | Adresserbara LED kan dra mycket |
| Servo/motor | 100 mA till flera A | Dimensionera för toppar |
| Radio/Wi-Fi | Kortvariga toppar | Viktigt för ESP-baserade kort |

Det exakta värdet ska mätas i ditt projekt. Tabellen är bara en påminnelse om vilka delar som brukar dominera.

## Snabbval: felsökning efter symptom

| Symptom | Kontrollera först | Trolig kategori |
|---|---|---|
| Inget händer alls | Matning, USB-kabel, rätt port, blink-sketch | Grundläggande kortkontakt |
| Upload misslyckas | Board-val, port, bootläge, USB-drivrutin | Utvecklingsmiljö |
| Seriell monitor visar skräp | Baudrate | UART/monitorinställning |
| Sensor hittas inte på I2C | SDA/SCL, adress, pullups, spänning | Buss/koppling |
| I2C fungerar ensam men inte med flera moduler | Adresskrock eller för starka/för svaga pullups | Bussintegration |
| SPI-display visar bara vitt/svart | CS/DC/RST, bibliotekskonfiguration | Pin mapping |
| ADC-värden hoppar | Brus, jord, referens, kabel, filter | Analog mätning |
| Servo rycker eller nollställer kortet | För svag matning | Strömförsörjning |
| ESP32 startar om när Wi-Fi används | Matningen klarar inte strömspikar | Strömförsörjning |
| Motor stör sensorer | Gemensam matning, jorddragning, avkoppling | Störningar |
| Kod fungerar tills display läggs till | Minne, SPI/I2C-konflikt eller timerkonflikt | Resurskonflikt |
| Buzzer påverkar PWM eller servo | Timerkonflikt | Intern periferi |
| Värden verkar rimliga men långsamt fel | Kalibrering, uppvärmning, placering | Mätmetodik |
| Projekt fungerar på bordet men inte i kapsling | Värme, kablar, matning, åtkomst | Mekanik/system |

## Snabbval: vilken metod ska jag felsöka med?

| Fråga | Verktyg eller metod |
|---|---|
| Lever kortet? | Blink-sketch och seriell utskrift |
| Får modulen matning? | Multimeter mellan VCC och GND |
| Är jord gemensam? | Kontinuitetsmätning och visuell kontroll |
| Finns I2C-enheten? | I2C-scanner |
| Kommer digital signal fram? | LED-test, multimeter eller logikanalysator |
| Är PWM ungefär rätt? | LED, multimeter eller oscilloskop |
| Är UART rätt kopplad? | Kontroll av TX/RX, baudrate och gemensam jord |
| Är spänningen stabil? | Multimeter, helst oscilloskop vid snabba dippar |
| Stämmer biblioteksexemplet? | Kör originalexempel oförändrat |
| Är felet integrationen? | Testa komponenten ensam med minimal sketch |
| Är antagandet fel? | Läs datablad/pinout och dokumentera skillnaden |

## Snabbval: kortfamiljer och typiska risker

| Kortfamilj | Typiska styrkor | Typiska risker |
|---|---|---|
| UNO/Nano ATmega328P | Enkelhet, 5 V, mycket exempel | Lite minne, begränsad prestanda |
| Mega 2560 | Många pinnar, klassisk Arduino | Stor, äldre, inte särskilt snabb |
| UNO R4-liknande moderna kort | Modernare resurser, Arduino-känsla | Skillnader mot klassisk UNO kan överraska |
| ESP8266 | Billig Wi-Fi, stort community | Boot pins, få resurser jämfört med ESP32 |
| ESP32 | Wi-Fi/BLE, prestanda, många varianter | 3,3 V, ADC-detaljer, pinout och variantval |
| RP2040/Pico | Många GPIO, pris, timingmöjligheter | Trådlöst beror på kortvariant |
| XIAO/Feather/småkort | Litet, produktnära, ofta praktiskt | Färre pinnar åtkomliga, tätare felsökning |
| Teensy | Hög prestanda och avancerad I/O | Mer specialiserat ekosystem |
| Portenta/avancerade kort | Professionella möjligheter | Pris och komplexitet |
| Lågkostnadsklon | Billigt och experimentvänligt | Dokumentation, kvalitet och USB-chip varierar |

## Snabbval: vanliga sensorer och gränssnitt

| Sensorkategori | Vanligt gränssnitt | Exempel på komponenter | Typisk fallgrop |
|---|---|---|---|
| Temperatur/fukt/tryck | I2C, 1-Wire, digital enkeltråd | BME280, BMP280, SHT, DS18B20, DHT | Fel adress, långsam uppdatering, placering |
| Ljus | Analog, I2C | LDR, BH1750, TSL-varianter | Kalibrering och omgivningsljus |
| Färg | I2C | TCS-varianter, APDS-9960/GY-9960 | Avstånd och belysning påverkar starkt |
| Avstånd | Digital, I2C, UART | HC-SR04, VL53L0X/VL53L1X | Objektets yta och vinkel |
| Närvaro | Digital, UART, I2C | PIR, mmWave-modul, APDS-9960/GY-9960 nära objekt | Falska positiva och placering |
| Rörelse/orientering | I2C, SPI | MPU/ICM/BNO-varianter | Kalibrering och filter |
| Ljud | Analog, digital, I2S | KY-037, mikrofonmoduler, I2S-mikrofon | Ljudanalys kräver mer än ljuddetektion |
| Ström/spänning | Analog, I2C | INA219/INA226, shunt, Hall | Fel mätområde eller osäker mätning |
| Tid | I2C | DS3231, PCF8523 | Batteri och tidszon/logik |
| GPS/GNSS | UART, I2C | NEO/M10-liknande moduler | Antenn, uppstartstid och inomhusproblem |
| RFID/NFC | SPI, I2C, UART | MFRC522, PN532 | Spänning, antenn och bibliotek |
| Jord/vatten/regn | Analog, digital | jordfukt, vattennivå, regnsensor | Korrosion, smuts och relativa värden |
| Gas/rök | Analog, digital tröskel | MQ-2, MQ-7, MQ-135 | Uppvärmning, kalibrering och falsk precision |
| Tryck/böjning | Analog | FSR, flexsensor | Icke-linjär respons och mekanisk montering |
| Vikt/kraft | Digital mätmodul | vågcell + HX711 | Kalibrering, montering och störningar |
| IR-fjärr | Digital, modulerad signal | TSOP/VS1838B-liknande mottagare | Fri sikt, störljus och protokoll |

Välj sensor efter beslutet du vill kunna ta i koden:

- Behöver du bara **ja/nej** räcker ofta digital tröskel, brytare, PIR, reed switch eller LM393-baserad modul.
- Behöver du **riktning eller trend** är analog signal, luxsensor, ToF, IMU eller ström-/spänningsmodul ofta bättre.
- Behöver du **jämförbara mätvärden** bör du prioritera digital sensor, dokumenterad placering och kalibrering framför lägsta pris.

## Snabbval: när ska jag använda extern ADC, DAC eller expander?

| Problem | Extern krets kan hjälpa | Kommentar |
|---|---|---|
| För få digitala pinnar | MCP23017, PCF8574, PCF8575, shift register | Välj efter hastighet, riktning och antal I/O |
| För få analoga ingångar | Analog multiplexer eller extern ADC | Multiplexer delar ADC, extern ADC kan ge bättre mätning |
| För låg analog upplösning | Extern ADC | Särskilt vid långsamma noggranna mätningar |
| Behöver riktig analog utgång | DAC | PWM räcker inte alltid |
| Många LED | LED-driver eller shift register | Undvik att belasta mikrokontrollerpinnar |
| Många knappar | I/O-expander, keypad-matris | Kräver debouncing och tydlig scanning |
| 16 enkla I2C-I/O | PCF8575 | För knappar, LED och långsamma styrsignaler, inte PWM eller hög ström |
| Flera identiska I2C-sensorer med samma adress | Multiplexer eller adressval | I2C-multiplexer kan lösa adresskrock |
| Många servon | Servodriver | Frigör timing och pinnar |

## Snabbval: bibliotek

| Situation | Rekommendation |
|---|---|
| Du testar en ny modul | Börja med bibliotekets minsta exempel |
| Det finns flera bibliotek | Välj aktivt underhållet bibliotek med tydliga exempel |
| Biblioteket kräver specifikt kort | Kontrollera core och arkitektur |
| Kodexemplet använder gamla pin-namn | Översätt till ditt korts faktiska pin mapping |
| Biblioteket blockerar länge | Mät loop-tid och överväg asynkron eller enklare användning |
| Biblioteket fungerar på UNO men inte ESP32 | Kontrollera arkitekturstöd och timer/I/O-antaganden |
| Biblioteket tar mycket minne | Byt kort, byt bibliotek eller minska funktioner |
| Biblioteket döljer för mycket | Skriv tunn wrapper och dokumentera antaganden |

## Snabbval: prototypnivå

Alla prototyper behöver inte vara lika ambitiösa. Välj nivå efter vad du behöver veta just nu.

| Syfte | Prototypnivå |
|---|---|
| Kontrollera att kortet fungerar | Blink och seriell utskrift |
| Kontrollera en sensor | Minimal läsning och råvärden |
| Förstå mätkvalitet | Råvärde, filtrering, kalibrering och störtest |
| Jämföra två komponenter | Samma testmiljö och samma kodstruktur |
| Bygga prototyp | Sensor, statusutgång, enkel felhantering |
| Bygga återanvändbar modul | Wrapper, konfiguration, diagnostik och exempel |
| Förbereda fältbruk | Strömbudget, kapsling, felåterhämtning och loggning |

## Snabbval: anteckningar som sparar felsökningstid

Minsta anteckningar som brukar spara felsökningstid:

- kortmodell
- board-val i utvecklingsmiljön
- matningsspänning
- kopplade komponenter
- pin mapping
- I2C-adresser eller SPI chip select
- bibliotek och versioner
- vad testsketchen kontrollerar
- förväntat resultat
- observerat resultat
- felsökningsnoteringar

För ett projekt som ska leva längre än första prototypen är även detta användbart:

- strömbudget
- risklista
- alternativ komponent
- kapslings- och kabelantaganden
- versionshistorik
- kända begränsningar
- beslut om varför kortet valdes

## Vanliga misstag

- **Misstag:** Att välja kort efter vad som råkar ligga närmast.
  - **Varför det händer:** Arduino-projekt börjar ofta spontant.
  - **Hur man undviker det:** Skriv först projektets krav och välj kort efter dem.

- **Misstag:** Att välja sensor efter modulnamn i stället för mätuppgift.
  - **Varför det händer:** Moduler marknadsförs ofta med breda namn som låter mer exakta än de är.
  - **Hur man undviker det:** Fråga vad som ska mätas, i vilken miljö och med vilken noggrannhet.

- **Misstag:** Att underskatta strömförsörjningen.
  - **Varför det händer:** Logiksignaler fungerar med små strömmar, men motorer, servon, LED-strippar och radio gör inte det.
  - **Hur man undviker det:** Gör strömbudget och använd separat matning för laster.

- **Misstag:** Att blanda 5 V och 3,3 V utan nivåkontroll.
  - **Varför det händer:** Moduler har ofta VCC-pinnar som verkar toleranta, men signalpinnarna kan vara känsligare.
  - **Hur man undviker det:** Kontrollera signalnivåer, inte bara matningsspänning.

- **Misstag:** Att använda I2C som om det vore en obegränsad kabelstandard.
  - **Varför det händer:** I2C är enkelt på breadboard och många sensorer använder det.
  - **Hur man undviker det:** Håll kablar korta, kontrollera pullups och byt metod vid längre avstånd.

- **Misstag:** Att integrera allt innan varje del fungerar ensam.
  - **Varför det händer:** Det känns effektivt att bygga slutprojektet direkt.
  - **Hur man undviker det:** Skapa minsta test för varje komponent och behåll testsketcherna.

- **Misstag:** Att tro att alla kompatibla kort beter sig likadant.
  - **Varför det händer:** Arduino-API:t ger en gemensam yta.
  - **Hur man undviker det:** Dokumentera core, pinout, logiknivå, ADC-egenskaper och timers.

- **Misstag:** Att hoppa över dokumentation för små tester.
  - **Varför det händer:** Experimentet känns för enkelt för att dokumenteras.
  - **Hur man undviker det:** Skriv åtminstone kort, pin mapping, bibliotek och resultat.

## Snabbreferens

- Välj kort efter projektkrav, inte efter vana.
- Välj sensor efter mätuppgift, miljö och noggrannhetskrav.
- Välj buss efter avstånd, hastighet, antal enheter och felsökningsbarhet.
- Använd externa drivkretsar för laster; mikrokontrollerpinnar är styrsignaler.
- Kontrollera alltid spänning, ström, logiknivå, pinout, bibliotek och matning.
- Vanliga kitmoduler är bra startpunkter, men kontrollera alltid deras begränsningar: korrosion, kalibrering, värme, strömtoppar, störningar och bibliotek.
- Färdiga moduler är utmärkta för experiment, men dokumentera vad som faktiskt sitter på modulen.
- Testa varje komponent ensam innan integration.
- Behåll testsketcher, pin mapping och beslutstexter.
- Snabbvalstabeller är startpunkter, inte datablad.

## Så omsätter du tabellerna

Använd punkterna när du går från uppslagstabell till faktisk koppling eller första prototyp.

- Börja med projektkrav innan du låser kort, sensor eller bibliotek.
- Välj I2C när enkel koppling och flera korta moduler väger tyngre än hög hastighet.
- Välj SPI när hastighet, displayprestanda eller tydligare enhetsval är viktigare än få ledningar.
- Kontrollera signalnivåer även om modulen kan matas med 5 V.
- Mata servon, motorer och andra laster separat när strömmen kan bli hög eller ryckig.
- Skilj mellan att upptäcka ljudnivå och att analysera ljudinnehåll.
- Välj färdig modul när du vill komma igång snabbt; välj lös IC när du behöver kontroll över kretsen.
- Spara alltid kortmodell, pin mapping och minimal testsketch när kopplingen fungerar.
- Behåll minimala testsketcher även när huvudprojektet fungerar.

## Relaterat

- När snabbguiden visar vilket område du behöver, gå tillbaka till det kapitel som förklarar komponenten eller principen.
- När flera alternativ verkar rimliga, använd valchecklistorna i respektive kapitel innan du kopplar upp.
- När projektet redan består av flera moduler, kombinera snabbguiden med integrationsordningen i kapitel 37.

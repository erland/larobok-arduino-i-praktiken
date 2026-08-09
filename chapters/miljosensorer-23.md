# 23. Temperatur, fukt, tryck och miljösensorer

## Sensoröversikt
Många Arduino-projekt börjar med en enkel mätning: temperatur i ett rum, luftfuktighet i ett växthus, lufttryck i en väderstation eller temperaturen på ett rör, ett batteripack eller ett chassi. Miljösensorer är därför en bra brygga mellan ren elektronik och praktiska system.

Samtidigt är miljösensorer lätta att underskatta. De flesta moduler har bara tre eller fyra pinnar, många bibliotek har färdiga exempel, och det går ofta att få ett värde på seriell monitor efter några minuter. Men ett värde är inte samma sak som en bra mätning. Sensorn kan vara felplacerad, värmas av kortet, påverkas av luftflöde, ligga för nära en regulator, ha för långsam uppdatering, ha fel adress på I2C-bussen eller ge en precision som inte passar projektets syfte.

Det här kapitlet visar hur du väljer och använder vanliga miljösensorer på ett sätt som är både praktiskt och rimligt robust. Fokus ligger på sensorer som ofta används med Arduino-kompatibla kort:

- enkla temperatur- och fuktsensorer som DHT11, DHT22 och AM2302
- digitala temperatursensorer som DS18B20
- tryck- och kombisensorer som BMP280 och BME280
- bättre fuktsensorer i SHT- och AHT-familjer
- miljömoduler för luftkvalitet, CO2 eller partiklar på översiktsnivå
- vanliga kit-sensorer för jordfukt, vattennivå och regn
- MQ-gassensorer som exempel på vanliga men ofta övertolkade hobbykomponenter

Kapitlet är inte en komplett metrologikurs. Det fungerar som praktiskt stöd när du behöver välja mellan temperatur-, fukt-, tryck- och kombisensorer, förstå vanliga felkällor som placering, självuppvärmning, kabelproblem och mätintervall, och bygga en enkel mätning som går att lita på i sitt sammanhang. Målet är att du ska kunna välja rätt typ av sensor och veta när du bör byta till en annan sensor eller annan mätmetod.

## Förutsättningar

Det här kapitlet bygger på flera tidigare delar av boken:

- kapitel 4 om spänning, ström, gemensam jord och nivåskiftning
- kapitel 6 om analog läsning, filtrering och mätosäkerhet
- kapitel 7 om `millis()` och icke-blockerande uppdatering
- kapitel 9 om I2C och 1-Wire
- kapitel 22 om att visa mätvärden i ett enkelt användargränssnitt

Miljösensorer är bra exempel på varför hårdvara, kod och fysisk placering måste ses som ett system. Du kan skriva perfekt kod och ändå få dåliga värden om sensorn sitter nära en varm spänningsregulator. Du kan också ha en dyr sensor men få sämre resultat än med en billigare sensor om luftflödet är dåligt eller om mätintervallet är olämpligt.

En bra startregel är:

> Miljömätning handlar lika mycket om placering och tolkning som om att läsa ett digitalt värde.

## Placering är en del av mätningen

En miljösensor mäter inte bara rummet, växthuset eller kapslingen. Den mäter den plats där modulen faktiskt sitter. Därför kan samma sensor ge olika resultat beroende på montering, luftflöde och värmekällor i närheten.

Kontrollera särskilt:

- avstånd till regulatorer, processorer och andra varma komponenter,
- om sensorn sitter i stillastående luft eller luftflöde,
- om kapslingen bromsar temperatur- eller fuktförändringar,
- om direkt solljus, drag eller fukt kan påverka värdet,
- hur lång tid sensorn behöver för att stabilisera sig efter start.

Ett bra sensorvärde börjar alltså ofta med en bra placering. Kodfiltrering kan jämna ut brus, men den kan inte rädda en sensor som sitter på fel plats.

## Vad menas med miljösensor?

I Arduino-sammanhang används ordet miljösensor ofta ganska brett. Det kan betyda en sensor för temperatur, luftfuktighet, lufttryck, ljus, gas, partiklar, koldioxid eller andra egenskaper i omgivningen. I det här kapitlet fokuserar vi på temperatur, fukt och tryck, men vi tar också upp när bredare luftkvalitetssensorer blir relevanta.

Det är viktigt att skilja mellan vad sensorn faktiskt mäter och vad projektet egentligen vill veta.

En temperatursensor mäter temperaturen där sensorn befinner sig. Den mäter inte nödvändigtvis rummets representativa temperatur. En fuktsensor mäter relativ luftfuktighet nära sensorn. Den säger inte automatiskt hur torr en växts jord är. En trycksensor mäter lufttryck vid sensorn. Den kan användas för vädertrend eller höjdskillnad, men bara om du förstår begränsningarna.

Miljösensorer används ofta i projekt som:

- väderstationer
- växthusövervakning
- dataloggers
- batteridrivna sensornoder
- smarta hem-prototyper
- kyl- och värmeövervakning
- akvarium och vattenrelaterad temperaturmätning
- ventilation och inomhusklimat
- undervisningsprojekt
- fältmätningar

I en snabb komponentgenomgång är det lockande att visa sensorn och koden först. I praktiska projekt bör du börja med frågan: vad ska beslutet baseras på?

Om projektet bara ska visa "ungefär varmt eller kallt" räcker en enkel sensor. Om projektet ska styra ventilation, larma för frost eller logga långsiktiga trender behöver du tänka mer på noggrannhet, stabilitet, placering och felhantering.

## Huvudkategorier

Miljösensorer kan grupperas på flera sätt. För praktiska Arduino-projekt är följande uppdelning användbar.

| Kategori | Exempel | Typiskt gränssnitt | Styrka | Begränsning |
|---|---|---|---|---|
| Enkel temperatur/fukt | DHT11, DHT22, AM2302 | Eget digitalt protokoll | Billigt och lätt att testa | Långsam, begränsad noggrannhet |
| Digital temperatur | DS18B20 | 1-Wire | Flera sensorer på samma buss, finns kapslad | Kräver pull-up och särskilt bibliotek |
| Tryck/temperatur | BMP280 | I2C eller SPI | Stabil tryckmätning, kompakt | Ingen luftfuktighet |
| Temperatur/fukt/tryck | BME280 | I2C eller SPI | Bra väderstationssensor | Kan påverkas av värme och placering |
| Bättre temperatur/fukt | SHT3x, SHT4x, AHT20 | I2C | Ofta bättre fuktmätning än DHT | Kostar mer än enklare moduler |
| Luftkvalitet | SCD4x, SGP40, CCS811, PMS-moduler | I2C eller UART | Mäter CO2, VOC eller partiklar | Kräver mer tolkning och kalibrering |

Tabellen är inte en absolut ranking. Det viktiga är att matcha sensor med användningsfall. En DS18B20 kan vara bättre än en BME280 om du ska mäta temperatur i en vätska. En BME280 kan vara bättre än en DHT22 om du vill logga väderdata. En SHT40 kan vara bättre än en BME280 om fuktmätningen är viktigare än lufttrycket.

## DHT11, DHT22 och AM2302

DHT-sensorer är vanliga eftersom de är billiga, enkla att köpa och har många färdiga Arduino-exempel. De mäter temperatur och relativ luftfuktighet med ett enkelt digitalt protokoll via en datapinne.

DHT11 är den enklare varianten. Den är ofta billig men har begränsat mätområde, lägre upplösning och sämre noggrannhet. DHT22 och AM2302 är bättre alternativ i samma praktiska familj, med större mätområde och ofta bättre fuktmätning.

DHT-sensorer passar bra när:

- du vill göra ett snabbt inomhusexperiment
- låg kostnad är viktigare än noggrannhet
- uppdatering varje sekund eller långsammare räcker
- du vill introducera temperatur och luftfuktighet utan I2C
- du accepterar att mätvärdena är ungefärliga

DHT-sensorer passar sämre när:

- du behöver snabb uppdatering
- mätvärdena ska användas för styrning med små marginaler
- sensorn ska sitta i svår miljö
- fuktmätningen måste vara stabil över tid
- du behöver flera sensorer med enkel adressering
- du vill ha robust busskommunikation

Ett vanligt misstag är att använda DHT22 som om den vore en precisionssensor. Den kan vara fullt tillräcklig för inspiration och enkla projekt, men om du jämför flera DHT-sensorer bredvid varandra kommer du ofta att se skillnader. Det betyder inte nödvändigtvis att något är trasigt. Det betyder att sensorn och modulen har begränsningar.

### Praktiskt kopplingsmönster

En DHT-modul har ofta tre pinnar:

- VCC
- DATA
- GND

En lös komponent kan däremot kräva extern pull-up mellan DATA och VCC. Många färdiga moduler har redan detta motstånd.

Typisk koppling:

| DHT-modul | Arduino-kompatibelt kort |
|---|---|
| VCC | 3,3 V eller 5 V enligt modulens krav |
| GND | GND |
| DATA | Valfri digital GPIO, exempelvis D2 |

Kontrollera alltid modulens märkning. Vissa moduler fungerar med 3,3 V, andra förväntar sig 5 V, och vissa har otydlig dokumentation. Om du använder ESP8266, ESP32 eller Pico-liknande kort är 3,3 V-logik normalfallet.

## DS18B20 och 1-Wire-temperatur

DS18B20 är en digital temperatursensor som ofta används när man bara behöver temperatur men vill ha en mer flexibel eller robust lösning än en enkel DHT-sensor. Den finns som lös komponent i TO-92-kapsel och som vattentät kapslad prob med kabel.

DS18B20 använder 1-Wire. Det betyder att flera sensorer kan dela samma datapinne, eftersom varje sensor har en unik adress. Det är mycket användbart när du vill mäta flera punkter, till exempel:

- inomhus och utomhus
- tillopp och retur på en värmekrets
- flera nivåer i ett växthus
- batteripack, chassi och omgivning
- vatten, luft och elektronikbox

DS18B20 passar bra när:

- du behöver flera temperatursensorer på samma buss
- sensorn ska sitta en bit från kortet
- du vill använda kapslad temperaturprob
- du bara behöver temperatur, inte luftfuktighet
- du vill ha en digital sensor med tydligt adresserbara enheter

DS18B20 passar sämre när:

- du behöver mäta luftfuktighet eller tryck
- du vill ha mycket snabb temperaturrespons
- du vill undvika extra biblioteks- och adresshantering
- kabeldragningen är lång och elektriskt stökig utan korrekt uppbyggnad

### Pull-up och kablar

1-Wire kräver normalt en pull-up-resistor mellan data och VCC. Ett vanligt värde är 4,7 kΩ, men långa kablar, många sensorer och störig miljö kan kräva mer omsorg. I små breadboardtest fungerar standardkopplingen ofta direkt. I mer robusta installationer behöver du tänka på kabeltyp, jordning, kontaktkvalitet och uppdateringsintervall.

Typisk koppling:

| DS18B20 | Arduino-kompatibelt kort |
|---|---|
| VDD | 3,3 V eller 5 V enligt valt system |
| GND | GND |
| DQ | Digital GPIO med pull-up till VDD |

DS18B20 kan även användas i parasitmatningsläge, men för bokens referensmönster är separat VDD normalt bättre. Det blir enklare att förstå, enklare att felsöka och mer robust.

## BMP280 och BME280

BMP280 och BME280 är vanliga små sensorer från Bosch-familjen. De sitter ofta på breakout boards och kommunicerar via I2C eller SPI. BMP280 mäter temperatur och lufttryck. BME280 mäter temperatur, lufttryck och relativ luftfuktighet.

I många Arduino-projekt används BME280 som en kompakt väderstationssensor. Den ger flera mätvärden via samma modul och fungerar bra med I2C. BMP280 är ett alternativ när luftfuktighet inte behövs.

BMP280 passar bra när:

- lufttryck är viktigt
- du vill uppskatta höjdskillnad eller trycktrend
- du inte behöver fuktmätning
- du vill ha en kompakt digital sensor

BME280 passar bra när:

- du vill mäta temperatur, luftfuktighet och tryck i samma modul
- du bygger väderstation, inomhusklimatlogger eller teststation
- du vill använda I2C med färdiga bibliotek
- du vill ha bättre praktisk sensorupplevelse än med DHT

BME280 passar sämre när:

- fuktmätningen är absolut viktig och bör optimeras separat
- sensorn sitter nära varm elektronik
- modulen är monterad i en tät låda utan luftflöde
- du behöver mäta temperatur på en specifik yta eller i vätska

En viktig detalj är att BME280:s temperaturvärde ofta främst används internt för att kompensera andra mätningar. Det kan ändå användas som omgivningstemperatur, men om modulen sitter nära en regulator, ESP32 eller display kan värdet bli för högt. Det är därför inte ovanligt att en BME280 i en liten kapsling visar "rätt sensorvärde" men "fel rumstemperatur".

### BME280 eller BMP280?

Det finns många moduler som säljs med liknande utseende. Vissa är BME280, andra BMP280. Ibland är produktbeskrivningar otydliga eller felaktiga. Ett praktiskt test är att läsa chip-id via biblioteket eller se vilka mätvärden biblioteket faktiskt kan hämta.

| Val | Välj när | Undvik när |
|---|---|---|
| BMP280 | Du vill mäta tryck och temperatur billigt | Du behöver luftfuktighet |
| BME280 | Du vill ha temperatur, fukt och tryck i samma modul | Fuktmätningen är kritisk och bör optimeras separat |
| SHT3x/SHT4x plus BMP280 | Du vill ha bättre fuktmätning och separat tryck | Du vill ha lägsta kostnad och minst antal moduler |

## SHT3x, SHT4x och AHT20

SHT- och AHT-sensorer är vanliga alternativ när temperatur och luftfuktighet är i fokus. SHT3x och SHT4x används ofta i bättre moduler. AHT20 är också vanligt på prisvärda I2C-breakouts.

Dessa sensorer passar bra när:

- luftfuktighet är viktigare än lufttryck
- du vill undvika DHT-familjens begränsningar
- du vill använda I2C
- du vill ha stabilare mätvärden i inomhusprojekt
- du vill jämföra flera fuktsensorer

De passar sämre när:

- du även behöver lufttryck och bara vill ha en modul
- låg kostnad är viktigare än mätkvalitet
- miljön är mycket fuktig, smutsig eller kondenserande utan skydd
- du behöver certifierad eller spårbar mätning

Fuktsensorer är särskilt känsliga för placering och miljö. De kan påverkas av kondens, damm, kemikalier, fingeravtryck, självuppvärmning och dåligt luftflöde. Om du vill mäta fukt i ett växthus, badrum eller utomhusmiljö bör sensorn skyddas så att luft kan passera men vatten inte direkt träffar sensorelementet.

## Luftkvalitet, CO2 och partiklar

Temperatur, fukt och tryck är ofta början. I mer avancerade projekt vill man ibland mäta luftkvalitet. Här behöver du vara extra försiktig med tolkningen.

Vanliga kategorier är:

- VOC-sensorer som uppskattar flyktiga organiska ämnen
- CO2-sensorer, ofta NDIR-baserade eller fotoakustiska beroende på modell
- partikelsensorer för PM1.0, PM2.5 och PM10
- gasmoduler som reagerar på flera gaser men inte ger selektiv laboratoriemätning

Dessa sensorer är användbara men kräver mer förståelse än en vanlig temperaturgivare. En VOC-sensor mäter inte "luftkvalitet" i allmän mening, utan reagerar på vissa ämnen och algoritmer. En CO2-sensor kan behöva kalibreringsstrategi. En partikelsensor har fläkt, optisk kammare och underhållsfrågor. En billig gasmodul kan ge inspirerande experiment men bör inte användas som säkerhetskritisk detektor.

I den här boken behandlas luftkvalitet främst som inspirations- och systembyggnadsområde. När ett projekt rör hälsa, säkerhet, brand, gasläckage eller myndighetskrav ska du inte förlita dig på hobbykomponenter utan separat verifiering.


## Jordfukt, vattennivå och regnsensorer

Många Arduino-kit innehåller enkla moduler för jordfukt, vattennivå eller regn. De är lockande eftersom de ofta bara har tre pinnar och ger ett analogt värde direkt. De passar bra för experiment, växtprojekt, demonstrationsbyggen och enkla larm där du själv kan tolka resultatet.

De ska däremot inte behandlas som noggranna miljömätare. Flera billiga moduler mäter egentligen elektrisk ledningsförmåga mellan metallytor. Det gör att värdet påverkas av vatten, salter, smuts, korrosion, kontakttryck, temperatur och hur sensorn sitter fysiskt.

Vanliga varianter är:

| Modul | Typisk signal | Passar för | Viktig begränsning |
|---|---|---|---|
| Resistiv jordfukt | Analog spänning | Enkla växtprojekt och demonstrationer | Korroderar lätt och påverkas av jordens sammansättning |
| Kapacitiv jordfukt | Analog spänning | Mer långvariga växtprojekt | Behöver kalibreras mot den jord och placering du använder |
| Vattennivåmodul | Analog spänning eller digital tröskel | Enkel närvarodetektering av vatten | Är ofta mer indikator än exakt nivåmätare |
| Regnsensor | Analog spänning eller digital tröskel | Demonstration av regn/nederbörd | Smuts, torktid och korrosion påverkar resultatet |

En praktisk tumregel är:

> Använd billiga fukt- och vattenmoduler som indikatorer, inte som exakta instrument.

För resistiva jordfuktsensorer bör du undvika att låta ström gå genom sensorn hela tiden. Mata sensorn bara när du mäter, eller använd en kapacitiv jordfuktsensor om projektet ska sitta inkopplat länge. I odlingsprojekt är det ofta bättre att kalibrera mot tre praktiska lägen än att försöka få ett absolut procentvärde:

- torrt nog att vattna
- lagom fuktigt
- tydligt blött

För vattennivå- och regnsensorer är fysisk placering lika viktig som kod. En regnsensor kan visa "regn" långt efter en skur om den inte torkar. En vattennivåsensor kan påverkas av smuts, bubblor, lutning och hur vätskan leder ström.

## MQ-gassensorer: vanliga men lätta att misstolka

MQ-sensorer, till exempel MQ-2, MQ-3, MQ-7 och MQ-135, är vanliga i elektronikbutiker och Arduino-kit. De används ofta i tester om rök, alkoholånga, kolmonoxid eller "luftkvalitet". De är intressanta att prova, men de är också några av de sensorer som lättast misstolkas.

En MQ-modul består normalt av ett uppvärmt sensorelement och en analog utgång. Många moduler har också en justerbar digital utgång via komparator. Den digitala utgången betyder inte att sensorn säkert har identifierat en viss gas. Den betyder bara att signalen passerat en inställd tröskel.

Viktiga begränsningar:

- sensorn behöver uppvärmningstid innan värdet är meningsfullt
- många MQ-sensorer drar relativt mycket ström
- olika gaser kan påverka samma sensor
- temperatur och luftfuktighet kan påverka mätningen
- absolut koncentration kräver kalibrering, modellförståelse och referens
- billiga moduler bör inte användas som säkerhetskritiska gaslarm

Det praktiska värdet i hobbyprojekt är ofta relativ indikering:

- "värdet ändras när något händer"
- "luften ser annorlunda ut än basnivån"
- "vi kan logga trend över tid i ett test"

Skriv därför hellre "gasindikator" eller "luftkvalitetsindikator" än "gasdetektor" när du bygger med MQ-moduler. Om projektet handlar om brand, gasläckage, arbetsmiljö eller människors säkerhet ska du använda certifierad utrustning och inte en hobbykoppling.



## Valguide för vanliga miljösensorer

Ett praktiskt sätt att välja sensor är att börja med vad du faktiskt behöver mäta.

| Behov | Rimligt förstaval | Alternativ | Kommentar |
|---|---|---|---|
| Enkel inomhustemperatur och fukt | DHT22 eller AHT20 | SHT3x/SHT4x | DHT är enkelt, AHT/SHT ofta trevligare med I2C |
| Bättre fuktmätning | SHT3x eller SHT4x | AHT20 | Placering är avgörande |
| Temperatur i vatten eller på kabel | DS18B20-prob | Termistor, PT100-modul | DS18B20 är praktisk och adresserbar |
| Väderstation | BME280 | BMP280 plus SHT-sensor | Skydda mot sol, regn och egen värme |
| Trycktrend | BMP280 eller BME280 | Annan barometersensor | Absolutvärde kräver kalibrering mot referens |
| Många temperaturpunkter | DS18B20 | I2C-sensorer med multiplexing | 1-Wire gör flera sensorer smidiga |
| Batteridriven nod | Sensor med låg viloström | BME280/SHT med styrd matning | Mät intervallvis och sov mellan mätningar |
| Inomhusluft och ventilation | CO2-sensor plus temperatur/fukt | VOC-sensor som komplement | Tolka luftkvalitet försiktigt |
| Damm/partiklar | Partikelsensor via UART/I2C | Färdig luftkvalitetsmodul | Kräver luftflöde och underhåll |
| Jordfukt i växtprojekt | Kapacitiv jordfuktsensor | Resistiv jordfukt för korta experiment | Kalibrera mot din jord och undvik ständig ström genom resistiva sensorer |
| Enkel vattennärvaro | Vattennivåmodul eller flottör | Kapacitiv eller optisk nivågivare | Billiga moduler är indikatorer, inte exakta nivåmätare |
| Regnindikering | Regnsensor som enkel indikator | Vädertålig nederbördssensor | Smuts, torktid och korrosion påverkar mätningen |
| Gasexperiment | MQ-modul som relativ indikator | Mer specifik gas- eller CO2-sensor | Använd inte som säkerhetskritisk detektor |

Snabbt sensorval:

- Välj **BME280/BMP280** när tryck eller vädertrend ingår i projektet.
- Välj **SHT3x/SHT4x eller AHT20** när fuktmätningen är viktigare än lägsta pris.
- Välj **DS18B20** när temperaturen ska mätas på kabel, i vattennära miljö eller på flera punkter.
- Välj **CO2- eller partikelsensor** när luftkvalitet är huvudfrågan, och behandla enklare VOC/MQ-moduler som indikatorer.
- Välj **kapacitiv jordfuktsensor** hellre än resistiv när sensorn ska sitta kvar under längre tid.

Välj inte sensor enbart efter upplösning i databladet. För Arduino-projekt är dessa frågor ofta viktigare:

- Kan sensorn matas med kortets spänningsnivå?
- Har modulen nivåskiftning eller inte?
- Är gränssnittet I2C, SPI, 1-Wire, UART eller något eget?
- Finns ett stabilt bibliotek för den kortfamilj du använder?
- Hur ofta behöver du mäta?
- Var ska sensorn fysiskt placeras?
- Vad gör systemet om sensorn inte svarar?
- Behöver du kalibrera mot en referens?
- Behöver du jämföra flera sensorer över tid?

## Placering och fysisk design

Miljösensorer mäter sin omgivning, inte din avsikt. Placeringen är därför en del av konstruktionen.

För temperatur bör du tänka på värmekällor. Ett ESP32-kort, en linjär regulator, en display, en laddkrets eller en LED-strip kan värma luften runt sensorn. Om sensorn sitter i samma lilla kapsling som elektroniken kan värdet bli högre än rummets temperatur. Lösningen kan vara att placera sensorn utanför kapslingen, skapa ventilation, mäta mer sällan, stänga av värmealstrande delar eller kalibrera med försiktighet.

För luftfuktighet behöver sensorn kontakt med luften. En tät låda ger långsam respons eller fel värde. En sensor nära en vägg, nära jord, nära vatten eller nära en varm komponent kan visa något annat än den omgivning du tror att du mäter. Kondens kan dessutom påverka sensorn under lång tid.

För lufttryck är placeringen mindre känslig för små lokala variationer, men kapsling och lufttätning kan ändå påverka responsen. Om trycksensorn sitter i en helt tät låda kan den reagera långsamt eller inte alls på omgivande tryckförändring.

För utomhusmätning bör du skydda sensorn mot:

- direkt solinstrålning
- regn och snö
- kondens
- insekter och smuts
- vind som ger extrema korttidsvariationer
- värme från vägg, tak, asfalt eller kapsling

En enkel väderskyddad placering kan ge större förbättring än att byta till en dyrare sensor.

## Uppdateringsintervall och tidsbeteende

Alla miljösensorer ska inte läsas så snabbt som möjligt. Temperatur och luftfuktighet förändras ofta långsamt, och vissa sensorer har intern mätcykel som gör snabba läsningar meningslösa eller störande.

En bra strategi är att välja mätintervall utifrån systemets behov:

| Användning | Typiskt intervall | Kommentar |
|---|---|---|
| Seriellt experiment på skrivbordet | 1 till 2 sekunder | Bra för felsökning och observation |
| Inomhusklimatlogger | 10 till 60 sekunder | Minskar brus och onödig loggning |
| Väderstation | 10 till 60 sekunder | Medelvärde kan vara bättre än råvärde |
| Batteridriven nod | 1 till 15 minuter | Läs, logga/skicka och sov |
| Temperatur på rör eller massa | 5 till 60 sekunder | Responsen begränsas ofta av fysisk kontakt |

Snabbare läsning ger inte automatiskt bättre data. Det kan ge mer brus, mer strömförbrukning, mer egenvärme och större loggfiler.

## Kodstruktur för miljömätning

När ett experiment växer är det frestande att lägga allt i `loop()`:

- läs sensor
- skriv till seriell monitor
- visa på display
- styra LED eller relä
- vänta med `delay()`
- upprepa

Det fungerar för första testet, men blir snabbt svår felsökt. En bättre struktur är att skilja mellan fyra delar.

Den första delen är **sensorläsning**. Den hämtar råa eller biblioteksgivna värden och markerar om läsningen lyckades.

Den andra delen är **rimlighetskontroll**. Den avgör om värdet är inom rimligt område, om sensorn svarar och om data ska användas.

Den tredje delen är **bearbetning**. Den kan göra medelvärde, avrundning, trendberäkning eller hysteresis.

Den fjärde delen är **presentation och åtgärd**. Den skriver till seriell monitor, display, loggfil, nätverk eller styr en utenhet.

Det gör att du kan byta sensor utan att skriva om hela programmet.

## Referensmönster: miljölogger med jämförelse

Det här referensmönstret visar hur en I2C-baserad miljösensor kan läsas med fast mätintervall, rimlighetskontroll och tydlig utskrift till seriell monitor. Om du har flera sensorer kan samma struktur användas för att jämföra dem bredvid varandra.

### Vad mönstret visar

Mönstret visar hur du:

- kopplar en I2C-baserad miljösensor
- läser temperatur, fukt och eventuellt tryck
- använder `millis()` i stället för `delay()`
- skiljer mellan lyckad och misslyckad sensorläsning
- håller sensorplacering och mätintervall tydliga
- jämför flera sensorer när jämförelsen faktiskt behövs

### Det här används i exemplet

Du behöver:

- ett Arduino-kompatibelt kort
- en I2C-baserad miljösensor, till exempel BME280, SHT31, SHT40 eller AHT20
- breadboard eller kopplingskablar
- dator med seriell monitor
- gärna en andra sensor för jämförelse

För ett första försök är BME280 praktisk eftersom den kan ge temperatur, luftfuktighet och tryck i samma modul. Om du främst vill jämföra luftfuktighet är SHT- eller AHT-sensorer också bra.

### Koppling

För en typisk I2C-modul gäller:

| Sensormodul | Arduino UNO/Nano | ESP32-exempel | Pico-exempel |
|---|---|---|---|
| VCC | 5 V eller 3,3 V enligt modul | 3,3 V | 3,3 V |
| GND | GND | GND | GND |
| SDA | A4 | GPIO 21, eller vald SDA | Vald SDA enligt core |
| SCL | A5 | GPIO 22, eller vald SCL | Vald SCL enligt core |

Kontrollera alltid din modul. Vissa BME280-moduler har regulator och nivåskiftning. Andra är rena 3,3 V-moduler. Om du använder ett 5 V-kort med en ren 3,3 V-sensor behöver du nivåskiftning på I2C-bussen.

### Kodexempel med BME280

Det här exemplet visar kodstrukturen. Biblioteksnamn och API kan variera beroende på vilket BME280-bibliotek du använder. Anpassa `#include` och initiering efter ditt valda bibliotek.

```cpp
#include <Wire.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme;

const unsigned long sampleIntervalMs = 5000;
unsigned long lastSampleMs = 0;

struct EnvironmentReading {
  float temperatureC;
  float humidityPercent;
  float pressureHpa;
  bool ok;
};

EnvironmentReading readEnvironment() {
  EnvironmentReading reading;

  reading.temperatureC = bme.readTemperature();
  reading.humidityPercent = bme.readHumidity();
  reading.pressureHpa = bme.readPressure() / 100.0F;

  reading.ok = !isnan(reading.temperatureC)
    && !isnan(reading.humidityPercent)
    && !isnan(reading.pressureHpa);

  return reading;
}

bool isReasonable(const EnvironmentReading& reading) {
  if (!reading.ok) {
    return false;
  }

  if (reading.temperatureC < -40.0 || reading.temperatureC > 85.0) {
    return false;
  }

  if (reading.humidityPercent < 0.0 || reading.humidityPercent > 100.0) {
    return false;
  }

  if (reading.pressureHpa < 800.0 || reading.pressureHpa > 1100.0) {
    return false;
  }

  return true;
}

void printReading(const EnvironmentReading& reading) {
  Serial.print("temperature_c=");
  Serial.print(reading.temperatureC, 2);

  Serial.print(", humidity_percent=");
  Serial.print(reading.humidityPercent, 1);

  Serial.print(", pressure_hpa=");
  Serial.println(reading.pressureHpa, 1);
}

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // Useful on boards with native USB.
  }

  Wire.begin();

  bool sensorFound = bme.begin(0x76);
  if (!sensorFound) {
    Serial.println("BME280 not found at address 0x76.");
    Serial.println("Try address 0x77, check wiring, power and I2C pullups.");
    while (true) {
      delay(1000);
    }
  }

  Serial.println("Environment logger started.");
}

void loop() {
  const unsigned long now = millis();

  if (now - lastSampleMs >= sampleIntervalMs) {
    lastSampleMs = now;

    EnvironmentReading reading = readEnvironment();

    if (isReasonable(reading)) {
      printReading(reading);
    } else {
      Serial.println("Invalid or unreasonable sensor reading.");
    }
  }
}
```

Det viktiga i exemplet är inte bara biblioteket. Det viktiga är strukturen:

- mätintervallet ligger i en konstant
- sensorläsningen är en egen funktion
- rimlighetskontrollen är separat
- utskriften är separat
- `loop()` är kort och lätt att följa

När projektet växer kan du byta `printReading()` mot display, SD-kort, MQTT eller annan presentation utan att ändra sensorlogiken i onödan.

### Om du använder annan sensor

För SHT31, SHT40 eller AHT20 ändras bibliotek och läsfunktioner, men strukturen kan vara densamma. Målet är att skapa ett gemensamt format för mätvärden.

```cpp
struct EnvironmentReading {
  float temperatureC;
  float humidityPercent;
  float pressureHpa;
  bool hasPressure;
  bool ok;
};
```

Med en sådan struktur kan du skriva kod som fungerar även när vissa sensorer saknar tryckmätning.

### Jämförelse mellan två sensorer

Om du har två sensorer, placera dem bredvid varandra men inte direkt mot varma komponenter. Låt dem stabilisera sig några minuter. Logga sedan värden med samma intervall.

Dokumentera:

- sensor A och sensor B
- kort och matningsspänning
- I2C-adresser
- fysisk placering
- ungefärlig rumssituation
- mätintervall
- tid innan jämförelse startade
- observerad skillnad

Det här är ofta mer lärorikt än att bara läsa datablad. Du ser hur praktisk mätning beter sig i din miljö.

## Testvariant: DS18B20 med flera mätpunkter

Om du vill fokusera på temperatur kan du i stället bygga ett experiment med två eller flera DS18B20-sensorer på samma 1-Wire-buss.

Möjliga mätpunkter:

- rumsluft
- utsida av elektronikbox
- nära spänningsregulator
- nära batteri
- vattenbehållare
- utomhusprob

Målet är att upptäcka att "temperaturen" inte är en enda sak. Temperaturen beror på var och hur du mäter.

Kodmässigt bör experimentet:

- hitta sensorerna på bussen
- skriva ut deras adresser
- namnge varje sensor i en konfigurationslista
- läsa med rimligt intervall
- visa fel om en sensor kopplas bort

I ett senare system kan samma mönster användas för värmeövervakning, kylning, batterisäkerhet eller processmätning.

## Felsökning

Miljösensorer kan misslyckas på flera sätt. En robust sketch bör inte anta att varje mätning lyckas.

Vanliga fel är:

- sensorn hittas inte vid start
- I2C-adressen är fel
- SDA och SCL är omkastade
- VCC och GND är felkopplade
- modulen kräver 3,3 V men har kopplats till 5 V
- pull-ups saknas eller är olämpliga
- kabeln är för lång
- biblioteket stöder inte sensorns exakta variant
- sensorn ger `NaN`, nollvärden eller orimliga värden
- sensorn fungerar på USB men inte på batteridrift
- sensorn värms av kortet eller kapslingen

Ett bra felmeddelande bör säga vad användaren ska kontrollera. Skriv inte bara "error". Skriv hellre:

```cpp
Serial.println("BME280 not found. Check address 0x76/0x77, SDA/SCL, power and GND.");
```

När projektet saknar dator kan samma fel visas med LED-mönster, buzzer eller display.

## Filtrering och presentation

Miljövärden kan presenteras på flera sätt:

- råvärde
- avrundat värde
- medelvärde över tid
- trend
- min/max sedan start
- statusklass, exempelvis kallt, normalt, varmt
- larm med hysteresis

Råvärden är bäst under felsökning. Avrundade värden är ofta bäst för användare. För temperatur i ett rum är två decimaler sällan meningsfullt. En display som visar `21.6 °C` kan vara mer ärlig än `21.637 °C`.

Använd medelvärde när du vill minska brus, men var försiktig så att du inte döljer verkliga förändringar. Använd hysteresis när ett mätvärde styr något som kan slå av och på.

Exempel:

```cpp
const float fanOnC = 30.0;
const float fanOffC = 28.0;

bool fanEnabled = false;

void updateFan(float temperatureC) {
  if (!fanEnabled && temperatureC >= fanOnC) {
    fanEnabled = true;
  }

  if (fanEnabled && temperatureC <= fanOffC) {
    fanEnabled = false;
  }

  digitalWrite(FAN_CONTROL_PIN, fanEnabled ? HIGH : LOW);
}
```

Det här hindrar fläkten från att växla snabbt om temperaturen ligger nära 30 grader.

## Kalibrering och jämförelse

Kalibrering betyder inte alltid att du gör sensorn "sann". I hobbyprojekt betyder det ofta att du jämför med en referens och dokumenterar avvikelsen.

Praktiska kalibreringsnivåer:

| Nivå | Vad du gör | Passar för |
|---|---|---|
| Ingen kalibrering | Använder sensorns värde direkt | Snabba tester |
| Offset | Lägger till eller drar ifrån en konstant | Enkel temperaturkorrigering |
| Jämförelse | Loggar mot referenssensor | Långsiktiga projekt |
| Flampunkts-/fuktpunktstest | Testar mot kontrollerad miljö | Mer seriös fuktmätning |
| Certifierad kalibrering | Spårbar kalibrering mot standard | Professionella mätningar |

För bokens experiment räcker ofta jämförelse och dokumenterad offset. Det viktiga är att du inte blandar ihop upplösning med noggrannhet. En sensor kan visa många decimaler utan att vara exakt på motsvarande nivå.

## När du bör välja en annan sensor

Byt sensor eller mätmetod när kraven ändras.

Välj annan sensor om:

- DHT-sensorn ger för långsam eller ojämn fuktmätning
- temperatur ska mätas i vätska eller på långt avstånd
- en BME280 sitter för varmt och inte kan placeras bättre
- du behöver luftkvalitet snarare än temperatur/fukt/tryck
- du behöver flera mätpunkter
- I2C-bussen redan är full eller kabeln är lång
- projektet är säkerhetskritiskt
- du behöver känd noggrannhet över tid

Det är också rimligt att kombinera sensorer. En väderstation kan använda BME280 för tryck och SHT40 för fukt. En styrbox kan använda DS18B20 för intern temperatur och BME280 för omgivande luft. En inomhusklimatstation kan kombinera CO2-sensor med temperatur och fukt för bättre tolkning.

## Vanliga misstag

- **Misstag: Att placera sensorn direkt ovanför en varm mikrokontroller.**
  - **Varför det händer:** Det är praktiskt att montera allt tätt på samma breadboard eller i samma kapsling.
  - **Hur man undviker det:** Placera miljösensorn en bit från värmekällor och dokumentera placeringen.

- **Misstag: Att tro att fler decimaler betyder högre noggrannhet.**
  - **Varför det händer:** Bibliotek kan skriva ut flyttal med många decimaler.
  - **Hur man undviker det:** Läs datablad, jämför med referens och visa bara meningsfull precision.

- **Misstag: Att välja DHT11 för projekt där fuktmätningen faktiskt spelar roll.**
  - **Varför det händer:** DHT11 är billig och finns i många startkit.
  - **Hur man undviker det:** Använd DHT11 för demonstration, men välj DHT22, AHT20, SHT3x eller SHT4x när fuktdata är viktigare.

- **Misstag: Att koppla en 3,3 V-sensormodul direkt till 5 V-I2C utan att kontrollera modulen.**
  - **Varför det händer:** Breakout boards ser lika ut och säljtexter kan vara otydliga.
  - **Hur man undviker det:** Kontrollera VCC-krav, nivåskiftning och pull-ups innan koppling.

- **Misstag: Att läsa sensorn för ofta.**
  - **Varför det händer:** `loop()` kör snabbt och det känns naturligt att läsa varje varv.
  - **Hur man undviker det:** Använd `millis()` och välj ett mätintervall som passar sensorn och projektet.

- **Misstag: Att använda luftfuktighetssensor i miljö med kondens utan skydd.**
  - **Varför det händer:** Sensorn uppfattas som en "vädersensor" bara för att den mäter fukt.
  - **Hur man undviker det:** Skydda sensorn mot direkt vatten, ge luftflöde och planera för långsam återhämtning efter hög fukt.

- **Misstag: Att inte dokumentera vilken sensorvariant som används.**
  - **Varför det händer:** Moduler kan säljas med liknande namn och utseende.
  - **Hur man undviker det:** Spara sensor, modul, I2C-adress, bibliotek och kort tillsammans med projektet.

## Snabb sammanfattning

- Miljösensorer är enkla att börja med men kräver genomtänkt placering för bra mätvärden.
- DHT-sensorer är praktiska för enkla tester men bör inte behandlas som precisionssensorer.
- DS18B20 är ett starkt val för flera temperaturpunkter, kapslade prober och 1-Wire-baserad temperaturmätning.
- BMP280 mäter tryck och temperatur, medan BME280 även mäter luftfuktighet.
- SHT3x, SHT4x och AHT20 är bra alternativ när temperatur och luftfuktighet är viktigare än tryck.
- Luftkvalitetssensorer kräver mer tolkning än temperatur- och fuktsensorer.
- Jordfukt-, vattennivå- och regnsensorer är praktiska indikatorer men behöver kalibrering och rimliga förväntningar.
- MQ-gassensorer är vanliga i kit, men ska behandlas som praktiska indikatorer och inte som säkerhetslarm.
- Uppdateringsintervall bör väljas utifrån sensorn och projektet, inte utifrån hur snabbt `loop()` kan köras.
- Separera sensorläsning, rimlighetskontroll, bearbetning och presentation i koden.
- Visa inte fler decimaler än mätningen motiverar.
- Dokumentera sensor, bibliotek, placering, mätintervall och kända felkällor.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Ofta 3,3 V eller 5 V via modul |
| Typiskt gränssnitt | I2C, 1-Wire, digital puls eller analogt |
| Välj när | temperatur, fukt, tryck eller miljödata behövs |
| Välj inte när | du behöver certifierade mätningar utan kalibrering |
| Vanliga fel | självuppvärmning, dålig placering, långsam sensor, fel pullup |
| Alternativ att överväga | BME/SHT, DS18B20, enklare DHT, kapacitiv jordfukt, MQ som indikator |
| Var extra försiktig med | MQ-gasmoduler, resistiv jordfukt, regnsensorer och billiga vattennivåmoduler |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När sensorn inte hittas, börja med kapitel 9 om bussar och adresser.
- När modulen ger analog fukt-, vatten- eller gassignal, använd kapitel 6 och kapitel 33 för tolkning och filtrering.
- När lång mätning påverkas av värme, matning eller batteridrift, gå vidare till kapitel 34.
- När ett enkelt test fungerar men projektet ger orimliga värden, felsök enligt kapitel 35.


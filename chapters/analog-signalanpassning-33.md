# 33. Analog signalanpassning, op-förstärkare och komparatorer

## Signalanpassning i praktiken
I många Arduino-projekt kan en sensor kopplas direkt till en digital ingång, en analog ingång eller en kommunikationsbuss. Det är bekvämt, och det är ofta rätt väg när du arbetar med färdiga breakout boards. Men förr eller senare möter du signaler som inte passar mikrokontrollern direkt.

Signalen kan vara för svag. Den kan ligga på fel spänningsnivå. Den kan vara brusig. Den kan behöva filtreras. Den kan vara negativ i förhållande till GND. Den kan komma från en sensor med hög impedans. Den kan behöva jämföras mot en tröskel snarare än mätas exakt. Den kan till och med vara farlig för mikrokontrollern om den kopplas in utan skydd.

Det är här analog signalanpassning kommer in.

Signal­anpassning betyder att du bygger ett litet analogt mellanled mellan sensorn och Arduino-kortet. Mellanledet gör signalen mer användbar, mer mätbar eller säkrare. I enkla projekt kan det vara en spänningsdelare eller ett RC-filter. I mer avancerade projekt kan det vara en op-förstärkare, en komparator, en instrumentförstärkare eller en skyddskrets.

Det här kapitlet är inte tänkt att göra dig till analog konstruktör. Målet är mer praktiskt: du ska kunna känna igen när en signal inte bör kopplas direkt, välja en rimlig anpassning och veta när det är bättre att använda en färdig modul än att designa allt själv.

Kapitlet knyter ihop flera tidigare delar av boken:

- Från kapitel 4: spänning, ström, jord, resistans, kondensatorer och nivåskiftning.
- Från kapitel 6: analog läsning, ADC, referensspänning, brus och kalibrering.
- Från kapitel 28: ström- och spänningsmätning.
- Från kapitel 31: drivkretsar och skydd mellan mikrokontroller och omvärld.

Nu använder vi samma tänkande på små analoga signaler.

## Förutsättningar

Du bör känna igen analog läsning, referensspänning, gemensam jord, spänningsdelare och enkel filtrering. Det viktigaste är att komma ihåg att en analog ingång inte kan mäta “vad som helst”: signalen måste ligga inom kortets tillåtna spänningsområde och ha en rimlig källa, nivå och störmiljö.

## Vad menas med analog signalanpassning?

Analog signalanpassning är alla åtgärder du gör för att en fysisk signal ska passa den krets som ska läsa den.

Det kan handla om att:

- skala ned spänningen
- skala upp en svag signal
- flytta signalens offset
- filtrera bort brus
- skydda ingången mot för hög spänning
- minska källimpedansen
- jämföra signalen med en tröskel
- isolera eller buffra sensorn från lasten
- göra signalen mer linjär eller mer stabil
- omvandla ström till spänning
- omvandla resistans till spänning

En praktisk tumregel är att du bör ställa fyra frågor innan du kopplar en analog signal till ett Arduino-kort:

1. Vilket spänningsområde kan signalen få i verkligheten?
2. Vilket spänningsområde tål ingången?
3. Hur snabbt ändras signalen?
4. Behöver jag mäta ett värde eller bara veta om en gräns passerats?

De fyra frågorna löser inte allt, men de avslöjar de flesta risker tidigt.

## Direktkoppling, enkel anpassning eller analog front-end?

Alla signaler kräver inte op-förstärkare. Ofta räcker en enklare lösning. Det svåra är att välja rätt ambitionsnivå.

| Situation | Typisk lösning | Kommentar |
|---|---|---|
| Potentiometer mellan VCC och GND | Direkt till analog ingång | Fungerar bra om matningen matchar ADC-referensen. |
| Batterispänning över ADC-området | Spänningsdelare | Lägg till skydd och tänk på viloström. |
| Långsam brusig sensorsignal | RC-filter och medelvärde i kod | Bra för temperatur, ljus och långsamma mätningar. |
| Svag analog signal | Op-förstärkare | Kräver rätt komponentval och matning. |
| Sensor med hög impedans | Buffert med op-förstärkare | Hindrar ADC:n från att belasta sensorn. |
| Tröskelbeslut, till exempel “för mörkt” | Komparator eller tröskel i kod | Komparator ger snabb och ren digital signal. |
| Mycket liten differenssignal | Instrumentförstärkare eller färdig modul | Undvik egen design om noggrannhet är viktig. |
| Farlig eller okänd spänning | Isolerad mätmodul eller färdig skyddad lösning | Koppla inte direkt till Arduino. |

Det är fullt acceptabelt att använda färdiga moduler. I en praktisk Arduino-bok är det ofta det bästa valet. Men även när du använder en modul behöver du förstå vad modulen ungefär gör, annars blir felsökningen svår.

## Spänningsdelaren som första verktyg

En spänningsdelare är den enklaste formen av nivåanpassning för en analog spänning. Den består av två resistorer i serie mellan signalen och GND. Mittpunkten ger en lägre spänning till ADC-ingången.

Formeln är:

```text
Vout = Vin * R2 / (R1 + R2)
```

Där R1 sitter mellan Vin och Vout, och R2 sitter mellan Vout och GND.

Exempel: du vill mäta ett 12 V-batteri med en analog ingång som aldrig får se mer än 3,3 V. Då kan du välja resistorer så att 15 V på ingången blir under 3,3 V på ADC:n. Det ger marginal för laddningstoppar och variation.

En spänningsdelare är enkel, men den har flera praktiska detaljer:

- Den drar alltid ström så länge den är inkopplad.
- För höga resistansvärden gör signalen mer känslig för brus och ADC-fel.
- För låga resistansvärden slösar ström.
- Den skyddar inte automatiskt mot stora transienter.
- Den kan behöva en kondensator för att ge stabilare ADC-värden.
- Den måste dimensioneras för maxspänning, inte bara normalspänning.

### Exempel: enkel batterimätning

Anta att du vill mäta ett batteri som normalt ligger mellan 9 V och 12,6 V. Du vill att ADC-ingången aldrig ska gå över 3,3 V. Du kan sikta på att 15 V ska bli ungefär 3,0 V.

Med R1 = 100 kΩ och R2 = 27 kΩ blir förhållandet:

```text
Vout = Vin * 27 / (100 + 27)
Vout är ungefär Vin * 0,213
```

Vid 15 V blir Vout ungefär 3,2 V.

Det är nära gränsen men fortfarande under 3,3 V i detta förenklade exempel. I ett verkligt projekt bör du lägga mer marginal, kontrollera toleranser och skydda ingången.

### Kod för att räkna tillbaka spänningen

```cpp
const int batteryPin = A0;

const float adcReferenceVoltage = 3.3;
const int adcMaxValue = 4095;

const float r1 = 100000.0;
const float r2 = 27000.0;

float readBatteryVoltage() {
  int raw = analogRead(batteryPin);
  float adcVoltage = (raw * adcReferenceVoltage) / adcMaxValue;
  float inputVoltage = adcVoltage * ((r1 + r2) / r2);
  return inputVoltage;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  float voltage = readBatteryVoltage();

  Serial.print("Battery voltage: ");
  Serial.print(voltage, 2);
  Serial.println(" V");

  delay(1000);
}
```

Det här är inte en exakt mätlösning. Den saknar kalibrering, toleranshantering, filtrering och skydd. Men den visar principen.

## Resistiva sensorer: FSR, flexsensorer och enkla trycksensorer

Många vanliga butikssensorer är i grunden bara variabla resistorer. De ger inte ett färdigt mätvärde i volt, utan ändrar resistans när något händer i omgivningen.

Vanliga exempel är:

- **FSR** (force-sensitive resistor), som ändrar resistans när den belastas.
- **Flexsensor**, som ändrar resistans när den böjs.
- Enkla tryck-, kläm- eller kontaktsensorer som beter sig ungefär som varierande motstånd.
- Vissa enkla ljus-, fukt- eller materialbaserade sensorer.

De här sensorerna kopplas ofta som en spänningsdelare: sensorn bildar ena halvan, ett fast motstånd den andra. Mittpunkten läses med en analog ingång.

Det viktiga är att förstå begränsningen: många resistiva sensorer är **bra på att visa förändring**, men sämre på att ge exakta fysikaliska värden. En FSR är till exempel användbar för att avgöra om något trycks ned hårdare eller lösare, men den är inte automatiskt en noggrann våg.

### Praktiskt val av fast motstånd

Det fasta motståndet avgör var i ADC-området signalen hamnar. En praktisk metod är:

1. Mät sensorresistansen i två eller tre relevanta lägen.
2. Välj ett fast motstånd i ungefär samma storleksordning som sensorresistansen i det område du bryr dig mest om.
3. Läs råvärden med `analogRead()`.
4. Justera motståndet om nästan alla värden hamnar nära 0 eller nära max.

För en enkel knapp- eller tryckliknande funktion kan du ofta använda ett tröskelvärde i kod. För mer seriös mätning behöver du kalibrera mot kända belastningar, böjningar eller trycknivåer.

### När de passar

Resistiva sensorer passar bra när du vill bygga:

- enkel tryckkänning
- berörings- eller klämdetektering
- mjuka gränssnitt
- böj- eller rörelsedetektering
- projekt där relativ förändring är viktigare än exakt mätning

De passar sämre när projektet kräver hög noggrannhet, långsiktig stabilitet eller kalibrerade mätvärden.

## Skydd av analoga ingångar

En analog ingång är ofta mer ömtålig än den ser ut. Det räcker med fel spänning, fel jord, induktiv störning eller felkopplad sensor för att skada mikrokontrollern.

Vanliga skyddsstrategier är:

- seriemotstånd mellan signal och ingång
- spänningsdelare med säkra dimensioner
- Schottky-dioder eller clamp-dioder mot matning och GND
- zenerdiod eller TVS-diod för överspänningsskydd
- RC-filter som dämpar snabba transienter
- optokoppling eller isolerad modul när signalen kommer från en annan elektrisk domän
- säkring eller PTC-skydd i mer robusta system

I testmiljö räcker det ofta att vara konservativ:

- Mät signalen med multimeter innan du ansluter den.
- Anslut GND korrekt innan signalen kopplas in.
- Använd seriemotstånd om signalens ursprung är osäkert.
- Bygg först med låg spänning.
- Koppla inte nätspänning eller okända industrisignaler direkt till Arduino.

### En enkel försiktig ingång

För en långsam analog signal kan du ofta börja med:

- en spänningsdelare om signalen kan vara för hög
- ett seriemotstånd på några kiloohm
- en liten kondensator från ADC-ingången till GND
- programvarufiltrering
- tydlig gemensam jord

Det är ingen universallösning, men det är en bättre start än att dra en okänd analog ledning direkt till A0.

## RC-filter: när signalen är för brusig

Ett RC-filter består av en resistor och en kondensator. I Arduino-sammanhang används det ofta som ett lågpassfilter: långsamma förändringar släpps igenom, snabba störningar dämpas.

Ett typiskt exempel är en analog sensor som mäter ljus eller temperatur. Värdet ska inte hoppa snabbt, men ADC-avläsningen gör det ändå på grund av brus, kablar, matning eller intern ADC-osäkerhet.

Ett enkelt lågpassfilter kan byggas så här:

```text
Signal -- resistor -- ADC-ingång
                     ned till kondensator
                     ned till GND
```

Filtret gör inte signalen “mer sann”. Det gör signalen långsammare och jämnare. Det är bra när det du mäter faktiskt är långsamt. Det är dåligt när du behöver snabb respons.

### Filter i hårdvara och kod

Du kan filtrera både elektriskt och i kod.

Ett enkelt medelvärde i kod:

```cpp
const int sensorPin = A0;

int readAveragedAnalog(int samples) {
  long sum = 0;

  for (int i = 0; i < samples; i++) {
    sum += analogRead(sensorPin);
    delayMicroseconds(500);
  }

  return sum / samples;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  int raw = analogRead(sensorPin);
  int averaged = readAveragedAnalog(16);

  Serial.print("Raw: ");
  Serial.print(raw);
  Serial.print("  Averaged: ");
  Serial.println(averaged);

  delay(200);
}
```

Medelvärde är lätt att förstå, men det blockerar programmet under mätningen. För långsamma system är det ofta okej. För mer responsiva system kan ett löpande filter vara bättre.

Ett enkelt exponentiellt filter:

```cpp
const int sensorPin = A0;
float filteredValue = 0.0;

void setup() {
  Serial.begin(115200);
  filteredValue = analogRead(sensorPin);
}

void loop() {
  int raw = analogRead(sensorPin);

  const float alpha = 0.1;
  filteredValue = alpha * raw + (1.0 - alpha) * filteredValue;

  Serial.print("Raw: ");
  Serial.print(raw);
  Serial.print("  Filtered: ");
  Serial.println(filteredValue);

  delay(50);
}
```

Lägre `alpha` ger jämnare men långsammare signal. Högre `alpha` ger snabbare men mer hoppig signal.

## Offset: när signalen inte börjar vid noll

Många sensorsignaler passar inte direkt i ADC:ns område. En signal kan vara centrerad kring 0 V, till exempel från en AC-kopplad sensor eller vissa strömsensorer. En vanlig Arduino-ADC kan normalt inte mäta negativa spänningar. Då behöver signalen flyttas upp med en offset.

Ett enkelt exempel är att skapa en virtuell mittpunkt på halva matningsspänningen. Signalen kan då svänga runt mittpunkten i stället för runt GND.

Om ADC-området är 0 V till 3,3 V kan du lägga vilonivån vid cirka 1,65 V. Då kan en liten AC-signal svänga både uppåt och nedåt utan att bli negativ för ADC:n.

Det här används ofta vid:

- enkla mikrofonförstärkare
- AC-strömsensorer
- vibrationsmätning
- signaler där förändringen är viktigare än absolutnivån

Men offset kräver att du håller ordning på vad ADC-värdet betyder. Ett värde runt mitten betyder “nollsignal”, inte halv skala i vanlig mening.

## Op-förstärkaren som praktiskt verktyg

En op-förstärkare, ofta kallad op-amp, är en analog krets som kan användas för att förstärka, buffra, filtrera eller jämföra signaler. I Arduino-projekt används den vanligast för tre saker:

- göra en svag signal större
- göra en högimpediv signal lättare att läsa
- skapa ett aktivt filter eller en signalanpassning

Det finns många op-förstärkarkopplingar, men i Arduino-sammanhang räcker det ofta att förstå några få mönster.

### Buffert

En buffert, eller spänningsföljare, har förstärkning 1. Den gör inte signalen större, men den gör att sensorn inte belastas lika mycket av ADC-ingången.

Det är användbart när:

- sensorn har hög utgångsimpedans
- spänningsdelaren har höga resistansvärden
- ADC-värdet blir instabilt när du kopplar in ingången
- flera delar av kretsen behöver läsa samma signal

Begreppsligt:

```text
Sensor -> op-förstärkarbuffert -> ADC
```

Bufferten fungerar som en mellanhand. Den lyssnar på sensorn utan att belasta den mycket och driver sedan ADC-ingången med lägre impedans.

### Icke-inverterande förstärkare

En icke-inverterande förstärkare gör en signal större utan att vända polariteten.

Förstärkningen bestäms av två resistorer:

```text
Gain = 1 + Rf / Rg
```

Om Rf = 90 kΩ och Rg = 10 kΩ blir förstärkningen 10.

Det kan vara användbart om en sensor bara ger 0,1 V förändring men du vill utnyttja mer av ADC-området.

Viktigt: op-förstärkaren kan inte skapa utspänning utanför sitt matningsområde. Om den matas med 3,3 V kan den inte leverera 5 V ut. Många op-förstärkare når inte heller hela vägen till matningsskenorna.

### Inverterande förstärkare

En inverterande förstärkare vänder signalens polaritet. Den är vanlig i analog elektronik men ofta mindre intuitiv i Arduino-projekt. Den kan vara användbar, men för bokens praktiska nivå är det viktigare att du känner igen den än att du börjar med den.

### Transimpedansförstärkare

Vissa sensorer ger ström snarare än spänning. Fotodioder är ett vanligt exempel. Då kan en op-förstärkare användas för att omvandla strömmen till en spänning.

Detta är kraftfullt men känsligt för komponentval, layout och brus. För snabba tester är en färdig ljussensormodul ofta enklare. För noggranna optiska mätningar kan transimpedansförstärkaren vara rätt väg, men då bör du läsa datablad och applikationsnoter noggrant.

## Op-förstärkare är inte idealiska

På papperet är op-förstärkare nästan magiska. I verkligheten har de begränsningar som spelar stor roll i mikrokontrollerprojekt.

| Egenskap | Varför den spelar roll |
|---|---|
| Matningsspänning | Op-förstärkaren måste fungera vid den spänning du använder, ofta 3,3 V eller 5 V. |
| Input common-mode range | Ingångarna måste tåla signalnivåerna du försöker mäta. |
| Output swing | Utgången kanske inte kan nå ända ned till GND eller upp till VCC. |
| Rail-to-rail | Betyder ofta bättre nära matningsskenorna, men kontrollera databladet. |
| Bandbredd | Förstärkaren måste vara snabb nog för signalen och förstärkningen. |
| Slew rate | Utgången måste hinna ändra sig tillräckligt snabbt. |
| Offsetspänning | Små fel på ingången kan förstärkas och ge mätfel. |
| Brus | Förstärkaren kan lägga till eget brus. |
| Ingångsbiasström | Kan påverka mätningar med höga resistansvärden. |
| Stabilitet | Vissa kopplingar kan oscillera om layout eller belastning är olämplig. |

För Arduino-projekt är en bra start att välja en op-förstärkare som uttryckligen fungerar med single supply vid 3,3 V eller 5 V och vars in- och utgångsområde passar signalen.

Undvik att bara ta “vilken op-amp som helst” ur en komponentlåda. Klassiska op-förstärkare kan vara utmärkta i rätt sammanhang men olämpliga vid låg matningsspänning och signaler nära GND.

## Komparatorn: när du bara behöver ett beslut

En komparator jämför två analoga spänningar och ger en digital utgång. Den svarar i princip på frågan:

```text
Är signalen högre än referensen?
```

Om svaret är ja blir utgången ett logiskt läge. Om svaret är nej blir den det andra logiska läget.

Det är användbart när du inte behöver hela analogvärdet, utan bara ett beslut:

- är det tillräckligt ljust?
- är batteriet under en gräns?
- passerade signalen en tröskel?
- är vätskenivån över en punkt?
- är vibration stark nog för att räknas?
- har strömmen blivit för hög?

Du kan göra tröskelbeslut i kod med `analogRead()`. Det är ofta enklast. Men en komparator har fördelar:

- snabbare respons
- ren digital signal
- kan väcka mikrokontroller från sleep
- kan fungera utan att ADC:n samplar hela tiden
- kan avlasta programmet
- kan ge tydligare gräns i hårdvara

### Komparator eller op-förstärkare?

En op-förstärkare kan ibland användas som komparator i enkla tester, men det är inte alltid bra. En riktig komparator är byggd för att snabbt växla mellan logiska nivåer. Den hanterar ofta mättnad och utgångslogik bättre.

Använd en riktig komparator när tröskelbeslutet är viktigt, snabbt eller ska vara robust.

Använd op-förstärkare när du vill förstärka eller forma en analog signal som fortfarande ska mätas analogt.

### Hysteres

Om signalen ligger nära tröskeln kan en komparator slå av och på snabbt på grund av brus. Hysteres löser detta genom att ha två trösklar:

- en tröskel för att slå på
- en annan tröskel för att slå av

Det är samma idé som en termostat. Den kanske startar värmen under 19 °C men stänger först av när temperaturen nått 21 °C. Utan hysteres skulle den kunna slå av och på hela tiden nära gränsen.

Du kan skapa hysteres i hårdvara med återkoppling runt komparatorn, eller i kod.

Exempel på hysteres i kod:

```cpp
const int sensorPin = A0;
const int outputPin = 8;

const int turnOnThreshold = 700;
const int turnOffThreshold = 600;

bool outputActive = false;

void setup() {
  pinMode(outputPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int value = analogRead(sensorPin);

  if (!outputActive && value > turnOnThreshold) {
    outputActive = true;
  }

  if (outputActive && value < turnOffThreshold) {
    outputActive = false;
  }

  digitalWrite(outputPin, outputActive ? HIGH : LOW);

  Serial.print("Value: ");
  Serial.print(value);
  Serial.print("  Active: ");
  Serial.println(outputActive ? "yes" : "no");

  delay(50);
}
```

Det här är mjukvaruvarianten av ett mycket viktigt analogt mönster.

## Instrumentförstärkare och differenssignaler

Ibland vill du mäta skillnaden mellan två signaler, inte en signal mot GND. Det är vanligt vid:

- shuntmätning
- lastceller
- bryggsensorer
- små differenssignaler i brusig miljö
- vissa tryck- och kraftsensorer

En enkel op-förstärkare kan förstärka signaler, men små differenssignaler kräver ofta bättre matchning och högre common-mode-rejection. Då används instrumentförstärkare.

En instrumentförstärkare är gjord för att förstärka skillnaden mellan två ingångar och samtidigt ignorera mycket av det som är gemensamt för båda. Det är exakt vad du vill ha när nyttosignalen är liten men båda ledningarna ligger ovanpå en större gemensam spänning.

För Arduino-projekt finns två praktiska vägar:

- använd en färdig modul med instrumentförstärkare
- använd en specialiserad ADC-modul med inbyggd förstärkning

Lastceller är ett bra exempel. Det är oftast bättre att använda en HX711-liknande modul än att själv bygga hela förstärkarkedjan från grunden. Du kan fortfarande förstå principen, men modulen löser förstärkning, differensmätning och digital avläsning på ett mer reproducerbart sätt.

## Vågceller och HX711

En vågcell, ofta kallad **load cell**, används för att mäta vikt eller kraft. Den bygger vanligtvis på töjningsgivare i en bryggkoppling. Signalen från bryggan är mycket liten, ofta bara några millivolt, och den kan inte kopplas direkt till en vanlig Arduino-ADC på ett meningsfullt sätt.

Det är därför HX711-moduler är så vanliga i Arduino-projekt. HX711 kombinerar förstärkning och högupplöst analog-till-digital-omvandling för vågceller. Mikrokontrollern läser sedan värdet digitalt från modulen.

En typisk kedja ser ut så här:

```text
Vågcell → HX711-modul → Arduino-kort
```

Det här är ett bra exempel på när en färdig analog front-end är bättre än att försöka bygga allt själv på breadboard.

### Det du behöver tänka på

När du använder vågceller och HX711 är det ofta mekaniken och kalibreringen som avgör resultatet:

- Vågcellen måste monteras så att kraften faktiskt belastar den på rätt sätt.
- Konstruktionen måste vara stabil och inte böja sig på oväntade ställen.
- Du behöver kalibrera mot en känd vikt eller kraft.
- Signalen kan driva något över tid, särskilt i billiga mekaniska byggen.
- Matning, jordning och kabeldragning påverkar stabiliteten.
- En vågcell tål bara belastning inom sitt specificerade område.

HX711 gör mätningen mycket enklare, men den gör inte automatiskt projektet noggrant. Se den som en praktisk mätmodul som fortfarande kräver mekanisk omsorg och kalibrering.

### När HX711 är rätt val

Använd HX711-liknande modul när du vill bygga:

- enkel köksvåg
- paketvåg
- kraftmätare
- belastningsindikator
- projekt där en konstruktion ska känna om något ligger på en platta

Välj något annat om du bara behöver veta om något trycks ned. Då kan en FSR eller mikrobrytare vara enklare.

## LM393 och digitala tröskelmoduler

LM393 är en vanlig komparator på billiga sensormoduler. Du möter den ofta på moduler för ljus, ljud, regn, jordfukt, vibration eller hinderindikering. Modulen har då ofta en sensor, en potentiometer och en digital utgång märkt till exempel `D0`.

Potentiometern ställer inte in en exakt mätning. Den ställer in en tröskel: när sensorns signal passerar gränsen växlar den digitala utgången.

Det gör LM393-moduler praktiska när projektet bara behöver veta om något har hänt:

- det blev ljusare än en viss nivå
- ljudet passerade en enkel gräns
- en regn- eller fuktmodul gav utslag
- en vibrationssensor registrerade en händelse

Men det är viktigt att inte blanda ihop tröskel med mätvärde. Den digitala utgången säger bara ungefär “under eller över inställd gräns”. Den berättar inte hur mycket ljus, ljud, fukt eller vibration som finns.

Använd därför gärna den analoga utgången först när modulen har både `A0` och `D0`. Då kan du se hur signalen varierar i Serial Monitor, välja en rimlig tröskel och först därefter använda den digitala utgången om projektet bara behöver ett ja/nej-beslut.

Se särskilt upp med:

- att potentiometern kan vara mycket känslig
- att vissa moduler saknar bra hysteres och därför kan fladdra nära gränsen
- att digital utgång kan vara aktiv HIGH eller aktiv LOW beroende på modul
- att modulens matning och logiknivå måste passa kortet

En LM393-modul är alltså bra för enkel händelsedetektering, men inte ett bra val när du behöver noggrann eller kalibrerad mätning.

## Analog mätning eller digital tröskel?

Många sensormoduler har både analog och digital utgång. Den digitala utgången kommer ofta från en komparator på modulen, ibland med en liten potentiometer för tröskel.

Exempel:

- ljudsensor med analog nivå och digital trigger
- ljussensor med analog nivå och digital tröskel
- regnsensor med analog nivå och digital tröskel
- vibrationssensor med digital händelseutgång

Det kan verka praktiskt, men du bör förstå skillnaden.

| Utgång | Fördel | Nackdel |
|---|---|---|
| Analog | Du ser hur signalen varierar | Kräver ADC, filtrering och gränser i kod. |
| Digital | Enkel att använda som händelse | Döljer information och beror på tröskelinställning. |
| Båda | Bra för test och kalibrering och kalibrering | Kräver att du vet vilken utgång du faktiskt använder. |

En bra arbetsmetod är att börja med den analoga utgången för att förstå signalen. Därefter kan du använda digital utgång om du bara behöver ett beslut.

## Referensmönster: analog tröskel med hysteres

Det här referensmönstret visar en enkel tröskeldetektor. Du kan använda en potentiometer, en LDR-modul eller en annan långsam analog sensor. Mönstret jämför tre sätt att arbeta:

- läsa rå analog signal
- filtrera signalen i kod
- fatta ett digitalt beslut med hysteres

Använd till exempel:

- ett Arduino-kompatibelt kort
- en potentiometer eller analog sensor
- en LED med seriemotstånd
- kopplingskablar
- eventuellt en kondensator på 100 nF till 1 µF för enkel lågpassfiltrering

Koppla potentiometern så här:

- ena ytterbenet till VCC
- andra ytterbenet till GND
- mittbenet till en analog ingång
- LED med seriemotstånd till en digital utgång

Om du använder ett 3,3 V-kort ska potentiometern kopplas mellan 3,3 V och GND, inte 5 V.

### Kod: analog tröskel med hysteres

```cpp
const int sensorPin = A0;
const int ledPin = 8;

const int samples = 8;
const int turnOnThreshold = 700;
const int turnOffThreshold = 600;

bool alarmActive = false;
float filteredValue = 0.0;

int readAveragedSensor() {
  long sum = 0;

  for (int i = 0; i < samples; i++) {
    sum += analogRead(sensorPin);
    delayMicroseconds(300);
  }

  return sum / samples;
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);

  filteredValue = analogRead(sensorPin);
}

void loop() {
  int raw = analogRead(sensorPin);
  int averaged = readAveragedSensor();

  const float alpha = 0.15;
  filteredValue = alpha * averaged + (1.0 - alpha) * filteredValue;

  if (!alarmActive && filteredValue > turnOnThreshold) {
    alarmActive = true;
  }

  if (alarmActive && filteredValue < turnOffThreshold) {
    alarmActive = false;
  }

  digitalWrite(ledPin, alarmActive ? HIGH : LOW);

  Serial.print("Raw: ");
  Serial.print(raw);
  Serial.print("  Averaged: ");
  Serial.print(averaged);
  Serial.print("  Filtered: ");
  Serial.print(filteredValue);
  Serial.print("  Alarm: ");
  Serial.println(alarmActive ? "on" : "off");

  delay(50);
}
```

### Kontrollera detta

Vrid potentiometern långsamt runt tröskelområdet. Titta på seriell monitor eller seriell plotter.

Notera:

- Råvärdet hoppar mer än du kanske väntar dig.
- Medelvärdet är stabilare men lite långsammare.
- Det filtrerade värdet rör sig mjukare.
- Hysteres hindrar LED:n från att fladdra nära gränsen.

Testa sedan att ändra avståndet mellan `turnOnThreshold` och `turnOffThreshold`.

Om de ligger nära varandra blir systemet känsligare men kan fladdra. Om de ligger långt ifrån varandra blir systemet stabilare men mindre exakt i gränsområdet.

## Referensmönster: enkel analog lågpassfiltrering

Bygg vidare på samma koppling. Lägg en kondensator mellan analog ingång och GND. Börja med 100 nF. Testa sedan 1 µF om du har det.

Kontrollera:

- Blir råvärdet jämnare?
- Blir responsen långsammare?
- Känns systemet bättre eller sämre?
- Vad händer när du vrider potentiometern snabbt?

Det här visar en viktig princip: filtrering är alltid en avvägning mellan stabilitet och snabbhet.

## I2C logic level converter

En I2C logic level converter är en liten nivåomvandlarmodul som används när ett 5 V-kort ska kommunicera med en 3,3 V-modul. Den är särskilt vanlig tillsammans med I2C-sensorer, OLED-displayer, RFID-moduler och moderna breakoutkort.

Problemet uppstår eftersom I2C använder pull-up-motstånd på SDA och SCL. Om bussen dras upp till 5 V kan en 3,3 V-sensor få för hög spänning på sina signalpinnar. En nivåomvandlare gör att lågspänningssidan kan ligga på 3,3 V medan högspänningssidan ligger på 5 V.

Typiska anslutningar är:

- `LV` till 3,3 V
- `HV` till 5 V
- `GND` till gemensam jord
- `LV1/LV2` till SDA/SCL på 3,3 V-sidan
- `HV1/HV2` till SDA/SCL på 5 V-sidan

Namnen varierar mellan moduler, så följ alltid modulens märkning. Koppla inte låg- och högsida “efter färg” eller efter en bild från en annan modul.

En I2C-nivåomvandlare är rätt val när:

- ett 5 V Arduino-kort ska prata med en 3,3 V I2C-sensor
- en OLED- eller RFID-modul saknar tydlig 5 V-tolerans
- flera I2C-enheter på samma buss har olika logiknivåer
- du vill undvika att 5 V-pullups hamnar direkt på en 3,3 V-modul

Den är däremot inte automatiskt rätt för alla signaler. Snabb SPI, enkelriktade styrsignaler och mycket höga hastigheter kan kräva andra nivåskiftare.

Grundregeln är enkel: kontrollera både matningsspänning och signalnivå. Att en modul kan matas med 5 V betyder inte alltid att dess I2C-signaler tål 5 V.

## När du bör välja en färdig modul

Det är pedagogiskt värdefullt att förstå op-förstärkare och komparatorer, men det är inte alltid klokt att bygga hela kedjan själv.

Välj ofta färdig modul när:

- signalen är mycket svag
- noggrannheten är viktig
- sensorn kräver kalibrering
- differenssignalen är liten
- mätningen gäller ström, vikt, pH eller andra känsliga storheter
- layout och brus kan dominera resultatet
- du vill fokusera på system och kod i stället för analog konstruktion

Exempel på modultyper där färdig lösning ofta är rätt:

- lastcellförstärkare, till exempel HX711
- pH-modul
- termoelementförstärkare
- strömsensormodul
- högupplöst ADC-modul
- mikrofonmodul med förstärkare
- isolerad mätmodul
- färdig nivåomvandlare eller skyddsmodul

Det betyder inte att moduler alltid är perfekta. Billiga moduler kan ha dålig dokumentation, felaktiga komponentvärden eller otydlig matningslogik. Men de ger ofta en bättre startpunkt än en känslig analog egenkonstruktion på breadboard.

## Riskkontroll före analog inkoppling

Analoga kretsar bör kontrolleras både vid normal signal och vid fel.

- Kontrollera minsta och högsta möjliga sensorsignal.
- Kontrollera att signalen aldrig kan gå utanför kortets tillåtna ingångsområde.
- Kontrollera vad som händer om sensorn kopplas loss.
- Kontrollera att op-förstärkare eller komparator fungerar vid vald matningsspänning.
- Kontrollera om utgången verkligen når nivåer som ADC eller digital ingång kan läsa.
- Kontrollera om signalen behöver filter, hysteres eller buffert.
- Testa först med potentiometer eller känd signal innan du kopplar in en dyr sensor.

Målet är inte att göra varje analog koppling avancerad, utan att undvika att en liten signalbehandling blir en dold felkälla.

## Vanliga misstag

- **Misstag: Att förstärka innan signalområdet är känt.**
  - Varför det händer: Det är lätt att se en svag signal och direkt tänka “mer gain”.
  - Hur du undviker det: Mät eller uppskatta min-, max- och normalnivå innan du väljer förstärkning.

- **Misstag: Att använda en op-förstärkare som inte fungerar vid 3,3 V.**
  - Varför det händer: Många op-förstärkare ser ut att vara generella komponenter.
  - Hur du undviker det: Kontrollera databladets matningsområde, input common-mode range och output swing.

- **Misstag: Att tro att rail-to-rail alltid betyder perfekt från 0 V till VCC.**
  - Varför det händer: Namnet låter absolut.
  - Hur du undviker det: Läs de faktiska gränserna vid din matningsspänning och last.

- **Misstag: Att göra spänningsdelaren för högohmig.**
  - Varför det händer: Hög resistans minskar viloströmmen.
  - Hur du undviker det: Balansera viloström mot ADC-stabilitet, och använd buffert eller kondensator vid behov.

- **Misstag: Att filtrera bort signalen du vill mäta.**
  - Varför det händer: Ett större filter gör värdena lugnare och ser bättre ut.
  - Hur du undviker det: Kontrollera hur snabbt den verkliga signalen behöver följas.

- **Misstag: Att låta en digital komparatorutgång ersätta förståelse av den analoga signalen.**
  - Varför det händer: Digital utgång känns enklare.
  - Hur du undviker det: Läs den analoga signalen först under testfasen och sätt tröskeln därefter.

- **Misstag: Att glömma hysteres.**
  - Varför det händer: En enkel gräns i kod fungerar ofta i första testet.
  - Hur du undviker det: Använd separata på- och avtrösklar när signalen är brusig.

- **Misstag: Att koppla en okänd signal direkt till ADC:n.**
  - Varför det händer: Arduino-projekt uppmuntrar snabb koppling.
  - Hur du undviker det: Mät först, begränsa strömmen, använd spänningsdelare eller skydd och bygg med marginal.

## Felsökning

- Om värdet hoppar: kontrollera jordning, kabellängd, referensspänning och om signalen behöver lågpassfiltreras.
- Om värdet fastnar nära 0 eller max: kontrollera att signalen ligger inom ADC:ns tillåtna område.
- Om op-förstärkaren inte följer signalen: kontrollera matningsspänning, common-mode-område och om utgången kan nå önskad nivå.
- Om tröskeln fladdrar: lägg till hysteres i kod eller hårdvara.
- Om mätningen ändras när en annan last slås på: separera matning, förbättra avkoppling och kontrollera jorddragningen.

## Snabb sammanfattning

- Analog signalanpassning gör sensorsignaler säkra, mätbara och användbara för mikrokontrollern.
- En spänningsdelare är enkel men måste dimensioneras för maxspänning, toleranser, strömförbrukning och ADC-stabilitet.
- FSR, flexsensorer och andra resistiva sensorer kan ofta läsas som spänningsdelare, men de ger främst relativa värden.
- RC-filter och programvarufilter kan göra långsamma signaler stabilare, men de gör också systemet långsammare.
- Op-förstärkare kan förstärka, buffra och filtrera signaler, men de måste väljas för rätt matningsspänning och signalområde.
- En komparator är rätt verktyg när du bara behöver ett digitalt beslut kring en analog tröskel.
- Hysteres hindrar utgångar från att fladdra när signalen ligger nära gränsen.
- Differenssignaler och mycket små signaler kräver ofta instrumentförstärkare, extern ADC eller färdig modul.
- Vågceller bör normalt läsas med HX711 eller liknande modul och kalibreras mot känd belastning.
- Börja gärna med analog avläsning för att förstå signalen, även om den slutliga lösningen använder digital tröskel.
- Koppla aldrig okända eller farliga spänningar direkt till en analog ingång.

## Säkerhetsruta: analog signalanpassning kräver marginaler

Op-förstärkare, komparatorer och filter kan få signaler att se enkla ut i koden, men de kan också skapa fel om matningsspänning, ingångsområde eller utgångssving inte passar mikrokontrollern.

Kontrollera alltid att den analoga kretsens utgång håller sig inom kortets tillåtna ingångsspänning, även vid fel, startögonblick och bortkopplad sensor.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Anpassas till kortets ingångsområde |
| Typiskt gränssnitt | Analogt till ADC eller digitalt via komparator |
| Välj när | sensorsignalen behöver förstärkas, filtreras eller jämföras |
| Välj inte när | en färdig kalibrerad modul ger säkrare resultat |
| Vanliga fel | mättad op-förstärkare, fel common mode, utgång utanför ADC-område |
| Vanliga enkla sensorer | FSR, flexsensorer och andra resistiva sensorer via spänningsdelare |
| Vanliga specialmoduler | HX711 för vågceller, instrumentförstärkare, extern ADC |
| Alternativ att överväga | färdig sensor, digital sensor, komparator, instrumentförstärkare |

Använd referensrutan som en snabb kontroll innan du bygger vidare. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När ett analogt värde verkar fel, kontrollera först ADC, referensspänning och sampling i kapitel 6.
- När signalen kommer från fukt-, gas-, ljus- eller ljudmoduler, jämför med kapitel 23, 24 och 27.
- När problemet gäller 5 V mot 3,3 V, använd detta kapitel tillsammans med bussgenomgången i kapitel 9.
- När mätfelet följer matning, jordning eller brus, gå vidare till kapitel 34 och felsök systematiskt med kapitel 35.

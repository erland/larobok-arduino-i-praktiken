# 21. Reläer, MOSFET:ar, solenoider och andra laster

## Riskbild och styrprincip
I kapitel 17 till 20 har vi arbetat med ljus, ljud och rörelse. Vi har sett att en Arduino-kompatibel enhet ofta är utmärkt som beslutsfattare, tidtagare och signalgenerator, men ganska svag som kraftkälla. En GPIO-pinne kan visa en signal. Den ska normalt inte vara den komponent som faktiskt driver en större last.

Det här kapitlet handlar om gränsen mellan mikrokontrollerlogik och fysisk effekt. En LED-indikator kan ibland kopplas direkt via ett motstånd. En LED-strip, ventil, solenoid, reläspole, motor, pump, fläkt, värmetråd eller kraftigare lampa kräver däremot nästan alltid ett mellanled. Mellanledet kan vara ett relä, en MOSFET, en transistorarray, en färdig drivmodul eller en särskild drivkrets.

Kapitlets huvudidé är enkel:

- Arduino-pinnen ska styra.
- Drivsteget ska bära lasten.
- Strömförsörjningen ska dimensioneras för lasten.
- Skyddskomponenter ska hantera det som händer när lasten slås av, startar eller stör.

Det här är ett av de kapitel där små elektriska detaljer spelar stor roll. Ett program kan vara helt korrekt och ändå fungera dåligt om lasten saknar gemensam jord, om MOSFET:en inte öppnar ordentligt vid 3,3 V, om relämodulen triggas med omvänd logik, om solenoiden saknar flyback-diod eller om den externa matningen får mikrokontrollern att starta om.

Målet är inte att göra dig till kraftelektronikkonstruktör. Målet är att du ska kunna välja en rimlig styrprincip, läsa modulens viktigaste data, koppla säkert på lågspänningssidan, skriva robust kod och veta när du bör välja en färdig modul eller en annan lösning.

I praktiken används kapitlet när en mikrokontroller ska styra något som drar mer ström än en GPIO-pinne bör leverera: LED-strip, fläkt, pump, ventil, solenoid, reläspole, värmelast eller annan lågspänd last.

## Förutsättningar

Det här kapitlet bygger på flera tidigare delar:

- från kapitel 4: spänning, ström, effekt, gemensam jord och nivåskiftning
- från kapitel 5: digitala utgångar, logiska signaler och aktiv hög/låg styrning
- från kapitel 7: PWM och icke-blockerande tidsstyrning
- från kapitel 20: motorströmmar, stallström och behovet av drivare

Vi kommer att använda Arduino-kortet som styrlogik och en extern last som kräver mer än en vanlig GPIO-pinne bör leverera. Exemplen håller sig till lågspänd DC. Nätspänning, fasta installationer och starkströmsarbete kräver annan kunskap, rätt komponenter, kapsling, skydd och ofta behörighet. I den här boken ska nätspänning behandlas som något du inte experimenterar med direkt på breadboard.

## Grundprincipen: styrsignal och lastström är olika saker

En vanlig nybörjarfälla är att tänka “pinnen är HIGH, alltså driver den lasten”. För små indikatorer kan det stämma. För nästan allt annat är det bättre att tänka i två separata kretsar.

Styrsidan är mikrokontrollerns värld:

- GPIO-pinne
- 3,3 V eller 5 V logik
- små strömmar
- kod, timing och signalnivåer

Lastsidan är effektens värld:

- separat matning
- högre ström
- störningar
- värme
- spänningsspikar
- mekaniska eller induktiva beteenden

Drivsteget ligger mellan sidorna. Det översätter en liten styrsignal till en större strömväg.

Ett enkelt exempel är en MOSFET som styr en 12 V LED-strip. Arduino-pinnen ger bara en styrsignal till MOSFET-gaten. LED-strippen får sin energi från en separat 12 V-matning. MOSFET:en fungerar som en elektronisk brytare på lågspänningssidan av lasten. Arduino-kortet behöver inte leverera stripens ström, men Arduino och 12 V-matningen måste normalt dela jord så att styrsignalen har samma referens.

## Översikt: vanliga sätt att styra laster

| Lösning | Passar bäst för | Styrka | Begränsning |
|---|---|---|---|
| Mekaniskt relä | Av/på-styrning, galvanisk separation, växlande kontakt | Enkelt att förstå och kan bryta flera typer av laster | Långsamt, klickar, slits och passar dåligt för snabb PWM |
| Reed-relä | Små signaler och isolerade kopplingar | Tystare och mindre än många reläer | Begränsad ström och inte för stora laster |
| MOSFET | DC-laster, PWM, LED-strippar, solenoider, små pumpar | Snabb, effektiv och tyst | Kräver rätt typ, rätt koppling och skydd |
| Bipolär transistor | Små till medelstora laster | Enkel och billig | Spänningsfall och basström måste dimensioneras |
| ULN2803/ULN2003 | Flera små induktiva eller digitala laster | Många kanaler och inbyggda skyddsdioder | Begränsad ström och inte lika effektiv som MOSFET |
| Färdig relämodul | Snabb prototyp för av/på | Skruvplintar och ofta indikering | Modulernas logik och isolering varierar |
| Färdig MOSFET-modul | Snabb prototyp för DC-last | Enklare koppling och ofta terminaler | Kvalitet, MOSFET-typ och märkdata måste kontrolleras |
| Solid state relay | Tyst brytning utan mekaniskt slitage | Bra för vissa av/på-fall | Typen måste matcha AC/DC och lastens ström |

Det finns ingen universell vinnare. Rätt lösning beror på om lasten är DC eller AC, hur mycket ström den drar, om den är induktiv, om du behöver PWM, om du behöver galvanisk isolation, om brytningen sker ofta och hur robust konstruktionen måste vara.

## Reläer: när en elektrisk brytare är rätt idé

Ett relä är i grunden en styrd brytare. En liten styrsignal påverkar en spole eller intern elektronik som i sin tur öppnar eller stänger en kontakt. För programmerare är reläer attraktiva eftersom de motsvarar ett enkelt booleskt beslut: på eller av.

Reläer är användbara när du behöver:

- slå av eller på en last sällan eller måttligt ofta
- separera styrkrets och lastkrets
- växla mellan två kontakter
- styra en last där PWM inte behövs
- använda en färdig modul med skruvplintar

Reläer är mindre bra när du behöver:

- snabb dimning
- tyst drift
- mycket hög växlingsfrekvens
- lång livslängd vid många växlingar
- exakt timing på millisekundnivå
- kompakt batteridriven konstruktion

Ett mekaniskt relä har ofta tre kontaktnamn som är viktiga att förstå:

| Kontakt | Betydelse | Praktisk tolkning |
|---|---|---|
| COM | Common | Gemensam kontakt |
| NO | Normally open | Inte ansluten till COM när reläet är vilande |
| NC | Normally closed | Ansluten till COM när reläet är vilande |

NO används ofta när lasten ska vara avstängd som standard. NC används när lasten ska vara på i viloläge eller när ett fel i styrningen ska ge ett visst säkert beteende. Den frågan är inte bara teknisk. Den handlar om vad som ska hända vid omstart, kabelbrott, programfel eller strömavbrott.

## Relämoduler och aktiv låg logik

Många relämoduler för Arduino har ingångar som inte beter sig som man först tror. En modul kan vara aktiv hög eller aktiv låg.

Aktiv hög betyder:

- `HIGH` aktiverar reläet
- `LOW` avaktiverar reläet

Aktiv låg betyder:

- `LOW` aktiverar reläet
- `HIGH` avaktiverar reläet

Aktiv låg är vanligt i moduler med optokopplare eller transistorsteg. Det gör att ett program som ser rimligt ut kan göra motsatsen mot vad du tänkte. Därför bör relämoduler alltid testas utan kritisk last först.

Ett säkrare kodmönster är att abstrahera logiken:

```cpp
const int RELAY_PIN = 7;
const bool RELAY_ACTIVE_LOW = true;

void setRelay(bool on) {
  if (RELAY_ACTIVE_LOW) {
    digitalWrite(RELAY_PIN, on ? LOW : HIGH);
  } else {
    digitalWrite(RELAY_PIN, on ? HIGH : LOW);
  }
}

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  setRelay(false);
}

void loop() {
  setRelay(true);
  delay(1000);
  setRelay(false);
  delay(1000);
}
```

Det här exemplet använder `delay()` bara för ett isolerat test. I ett integrerat system bör samma idé skrivas med `millis()` så att relästyrningen inte blockerar sensorer, display eller kommunikation.

## MOSFET: elektronisk brytare för DC-laster

En MOSFET är ofta rätt val för lågspända DC-laster. Den kan slå av och på snabbt, arbeta tyst, styras med PWM och vara mycket effektiv om den är rätt vald.

För Arduino-projekt används ofta N-kanals MOSFET som low-side switch. Det betyder att lasten ligger mellan positiv matning och MOSFET:ens drain, medan MOSFET:ens source går till jord. När gaten får rätt spänning i förhållande till source börjar MOSFET:en leda och ström kan gå genom lasten.

En förenklad low-side-koppling ser ut så här i ord:

- lastens plus till extern plusmatning
- lastens minus till MOSFET drain
- MOSFET source till extern jord
- Arduino GND till extern jord
- Arduino GPIO via litet motstånd till MOSFET gate
- gate till jord via pulldown-motstånd
- flyback-diod över induktiv last där det behövs

Det viktiga är att Arduino inte driver lasten. Arduino styr bara gaten.

## Logic-level MOSFET

Alla MOSFET:ar som “tål mycket ström” är inte bra som Arduino-styrda brytare. Det avgörande är inte bara maximal drainström på förpackningen, utan om MOSFET:en leder tillräckligt bra vid den gate-spänning ditt kort kan ge.

För Arduino-sammanhang vill du ofta ha en logic-level MOSFET. Det betyder att den är avsedd att kunna styras med logiknivåer som 5 V, och helst även 3,3 V om du använder ESP32, Pico, många moderna Arduino-kort eller andra 3,3 V-plattformar.

Titta särskilt efter:

- låg `Rds(on)` vid relevant gate-spänning
- specifikationer vid 4,5 V eller 2,5 V gate drive, inte bara vid 10 V
- tillräcklig ström- och spänningsmarginal
- rimlig kapsling för värmeutvecklingen
- om modulen redan innehåller gate-motstånd och pulldown

`Vgs(th)` är ofta missförstått. Det är tröskeln där MOSFET:en precis börjar leda en liten testström. Det är inte samma sak som att den är fullt påslagen och lämplig för din last. För praktiskt bruk är `Rds(on)` vid din styrspänning mycket mer intressant.

## Gate-motstånd och pulldown

En MOSFET-gate beter sig delvis som en liten kapacitiv last. Den behöver inte kontinuerlig ström på samma sätt som en bipolär transistorbas, men den behöver laddas och urladdas när signalen ändras.

Två enkla komponenter gör många kopplingar mer robusta:

- ett litet seriemotstånd mellan GPIO och gate
- ett pulldown-motstånd från gate till jord

Seriemotståndet begränsar korta laddningsströmmar och kan minska ringningar. Pulldown-motståndet gör att MOSFET:en hålls avstängd när mikrokontrollern startar, startar om eller när pinnen ännu inte är konfigurerad.

I hobbyprojekt är typiska värden ofta i storleksordningen 100 ohm till 330 ohm för gate-seriemotstånd och 10 kiloohm till 100 kiloohm för pulldown. Det är inte magiska värden, men de illustrerar principen.

## Induktiva laster och flyback-diod

Solenoider, reläspolar, DC-motorer, pumpar och många elektromekaniska laster är induktiva. En induktiv last vill fortsätta driva ström när du stänger av den. Resultatet kan bli en hög spänningsspik som stör mikrokontrollern eller förstör drivsteget.

En flyback-diod, även kallad frilöpsdiod, ger strömmen en säker väg när lasten stängs av. För en DC-solenoid eller reläspole kopplas dioden normalt parallellt med lasten, spärrad under normal drift och ledande när spänningen vänder vid avstängning.

I ord:

- diodens katod mot lastens plus
- diodens anod mot MOSFET-sidan eller lastens minus
- dioden leder inte när lasten är på
- dioden leder kort när lasten stängs av och spänningsspiken annars skulle bli hög

Många relämoduler och drivkretsar har redan skyddsdioder. Det betyder inte att du kan ignorera frågan. Det betyder att du ska kontrollera om skyddet finns, var det sitter och om det passar just din koppling.

## Elektromagneter, solenoider och andra spolar

En elektromagnet, solenoid, reläspole eller magnetventil är inte bara en vanlig förbrukare. Den är en induktiv last. Det betyder att spolen lagrar energi i ett magnetfält när ström går genom den och kan skapa en hög spänningsspik när strömmen bryts.

Behandla därför spolar på samma sätt som andra induktiva laster:

- driv dem inte direkt från en Arduino-pinne
- använd MOSFET, transistorsteg, relämodul eller lämplig drivmodul
- använd ofta separat matning för själva lasten
- dela jord mellan Arduino och drivsteg när styrsignalen behöver samma referens
- kontrollera att flyback-diod, frilöpsdiod eller motsvarande transientskydd finns
- dimensionera komponenterna efter verklig ström, inte bara efter märkspänning

En solenoid är en spole som skapar en mekanisk rörelse när ström går genom den. Magnetventiler, låsmekanismer och små slagaktuatorer beter sig ofta på samma sätt. En elektromagnet kan i stället vara gjord för att hålla fast något, lyfta något eller skapa ett magnetfält utan tydlig slaglängd. Elektriskt är grundfrågan ändå densamma: spolen vill ha mer ström än en GPIO-pinne kan leverera och den behöver skydd när den stängs av.

Spolar är enkla att förstå men kan vara elektriskt och mekaniskt hårda:

- de kan dra hög startström
- de blir varma vid kontinuerlig aktivering
- de skapar spänningsspikar när de stängs av
- de kan få matningen att sjunka när de slår till
- de kan skapa mekaniskt ljud, vibrationer och stötar
- magnetkraften påverkas av ström, luftgap, kärnmaterial och hur mekaniken är byggd

I praktiska Arduino-projekt är korta aktiveringstider ofta säkrare än att låta spolen vara på hela tiden. Många elektromagneter och solenoider är inte avsedda för kontinuerlig drift. Börja med låg risk: separat strömbudget, korta pulser, temperaturkontroll och tydlig mekanisk frigång. En spole som snabbt blir för varm för att vidröra är inte dimensionerad för den drift du ger den.

För vissa solenoider kan man använda en kraftigare startpuls och sedan lägre hållström. Det minskar värme och energiförbrukning, men kräver mer avancerad styrning. I en nybörjarvänlig konstruktion är det bättre att först få en enkel MOSFET-koppling med rätt skydd att fungera stabilt.

## Relä eller MOSFET?

Valet mellan relä och MOSFET är ett återkommande designbeslut.

Välj relä när:

- du bara behöver av/på
- växling sker sällan
- du vill ha galvanisk separation
- lasten inte ska PWM-styras
- du behöver växlande kontakt, till exempel NO/NC
- det är viktigare att förstå kopplingen än att den är snabb och tyst

Välj MOSFET när:

- lasten är lågspänd DC
- du vill kunna PWM-styra
- växling sker ofta
- du vill ha tyst drift
- du vill ha hög effektivitet
- du styr LED-strip, solenoid, liten pump, fläkt eller annan DC-last

Välj färdig drivmodul när:

- du vill komma igång snabbt
- du inte vill dimensionera alla skyddskomponenter själv
- lasten är inom modulens tydliga märkdata
- modulen är väl dokumenterad

Välj annan lösning när:

- lasten är AC eller nätspänning
- säkerhetskraven är höga
- lasten är stor, dyr eller farlig
- konstruktionen ska användas utan tillsyn
- du saknar tydlig dokumentation för modulen

Snabb beslutsrad:

- **Relä** passar bäst för sällan växlad av/på-styrning och tydlig elektrisk separation.
- **MOSFET** passar bäst för lågspända DC-laster, PWM och tyst snabb växling.
- **Färdig modul** passar bäst när märkdata, koppling och skydd är tydligt dokumenterade.
- **Avstå från experimentkoppling** om lasten är nätspänning, okänd eller svår att kapsla säkert.

## Aktiv säker startlogik

När du styr laster är startbeteendet viktigt. Många Arduino-pinnar är ingångar vid reset. Vissa kort har boot pins som kan påverka uppstarten. Vissa moduler triggas när pinnen flyter. Vissa relämoduler är aktiva låga och kan slå till kort under start.

Säker startlogik betyder att konstruktionen ska hamna i ett ofarligt läge även när programmet inte har hunnit börja.

Praktiska metoder:

- använd pulldown eller pullup på styrsignalen där det behövs
- välj pinne som inte påverkar boot-läge
- sätt utgångar till säkert läge tidigt i `setup()`
- undvik att kritiska laster är aktiva vid reset
- testa vad som händer när USB ansluts, extern matning slås på och kortet startas om
- dokumentera om modulen är aktiv hög eller aktiv låg

För ESP8266 och ESP32 är pinval extra viktigt eftersom vissa pinnar påverkar boot-läge eller har särskilda funktioner under uppstart. För klassiska AVR-kort är beteendet ofta enklare, men även där bör externa drivsteg inte lämnas flytande.

## Exempel: MOSFET-styrd DC-last utan blockering

Följande exempel visar en enkel laststyrning där en last slås på i två sekunder och sedan hålls av i fem sekunder. Koden använder `millis()` i stället för `delay()` och har en funktion som abstraherar styrningen.

Exemplet kan användas för en liten lågspänd DC-last via MOSFET, till exempel en liten LED-strip, en liten fläkt eller en testlast. Anpassa alltid matning, MOSFET och skydd efter faktisk last.

```cpp
const int LOAD_PIN = 6;
const bool LOAD_ACTIVE_HIGH = true;

const unsigned long ON_TIME_MS = 2000;
const unsigned long OFF_TIME_MS = 5000;

bool loadOn = false;
unsigned long lastChangeMs = 0;

void setLoad(bool on) {
  loadOn = on;

  if (LOAD_ACTIVE_HIGH) {
    digitalWrite(LOAD_PIN, on ? HIGH : LOW);
  } else {
    digitalWrite(LOAD_PIN, on ? LOW : HIGH);
  }
}

void setup() {
  pinMode(LOAD_PIN, OUTPUT);
  setLoad(false);
  lastChangeMs = millis();
}

void loop() {
  unsigned long now = millis();

  if (loadOn && now - lastChangeMs >= ON_TIME_MS) {
    setLoad(false);
    lastChangeMs = now;
  }

  if (!loadOn && now - lastChangeMs >= OFF_TIME_MS) {
    setLoad(true);
    lastChangeMs = now;
  }
}
```

Lägg märke till att koden inte vet om lasten är en LED-strip, en fläkt eller en solenoid. Den styr bara en logisk last. Den elektriska kopplingen avgör om detta är säkert och rimligt.

## Exempel: relästyrning med minsta växlingstid

Reläer bör inte slås av och på mycket snabbt. Ett sätt att skydda reläet och lasten är att införa minsta tid mellan växlingar.

```cpp
const int RELAY_PIN = 7;
const bool RELAY_ACTIVE_LOW = true;

const unsigned long MIN_SWITCH_INTERVAL_MS = 3000;

bool relayOn = false;
unsigned long lastSwitchMs = 0;

void writeRelay(bool on) {
  if (RELAY_ACTIVE_LOW) {
    digitalWrite(RELAY_PIN, on ? LOW : HIGH);
  } else {
    digitalWrite(RELAY_PIN, on ? HIGH : LOW);
  }
}

bool setRelay(bool on) {
  unsigned long now = millis();

  if (on == relayOn) {
    return true;
  }

  if (now - lastSwitchMs < MIN_SWITCH_INTERVAL_MS) {
    return false;
  }

  relayOn = on;
  writeRelay(relayOn);
  lastSwitchMs = now;
  return true;
}

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  writeRelay(false);
  relayOn = false;
  lastSwitchMs = millis();
}

void loop() {
  unsigned long now = millis();

  bool shouldBeOn = (now / 10000) % 2 == 0;
  setRelay(shouldBeOn);
}
```

Det här är fortfarande bara ett mönster. I ett riktigt system skulle `shouldBeOn` kunna komma från temperatur, nivå, tid, nätverkskommando eller en säkerhetslogik.

## Säker koppling: styr en lågspänd last med MOSFET

### Vad kopplingen visar

Kopplingen visar en kontrollerad lastutgång som slår av och på en lågspänd DC-last utan att driva lasten direkt från Arduino-pinnen. Fokus ligger på extern matning, gemensam jord, MOSFET-styrning, säker start och icke-blockerande kod.

### Det här används i exemplet

- Ett Arduino-kompatibelt kort
- En logic-level N-kanals MOSFET eller dokumenterad MOSFET-modul
- En lågspänd DC-last, till exempel liten LED-strip, liten fläkt eller testlampa
- Extern matning som passar lasten
- Motstånd för gate-serie och pulldown om de inte finns på modulen
- Flyback-diod om lasten är induktiv
- Multimeter
- Kopplingskablar och gärna skruvplint eller kopplingskort för lastsidan

Undvik okända stora laster i första försöket. Börja med en last där strömmen är lätt att uppskatta och där fel inte skadar något viktigt.

### Koppling i ord

För en typisk low-side MOSFET-koppling:

1. Koppla lastens plus till extern plusmatning.
2. Koppla lastens minus till MOSFET drain.
3. Koppla MOSFET source till extern jord.
4. Koppla Arduino GND till extern jord.
5. Koppla Arduino-styrpinne till MOSFET gate via ett litet seriemotstånd.
6. Koppla gate till jord via pulldown om det inte redan finns.
7. Koppla flyback-diod över lasten om lasten är induktiv.
8. Kontrollera med multimeter att jordarna verkligen är gemensamma.
9. Starta med lasten frånkopplad eller med låg risk innan du ansluter den riktiga lasten.

### Kod

Använd MOSFET-exemplet ovan som start. Byt `LOAD_PIN` till din valda pinne och justera tiderna. Om du använder en modul som är aktiv låg sätter du `LOAD_ACTIVE_HIGH` till `false`.

### Förväntat resultat

Lasten ska slå på och av med tydliga intervall. Arduino-kortet ska inte starta om när lasten slås på. MOSFET:en ska inte bli märkbart varm vid den ström du testar. Om lasten är induktiv ska avstängningen inte orsaka slumpmässiga reset, konstiga seriella tecken eller störningar i andra delar av systemet.

### Variationer

- Byt från av/på till PWM för en LED-strip eller liten DC-fläkt.
- Lägg till en knapp som tillåter manuell aktivering.
- Lägg till en max-tid så att lasten aldrig kan vara på längre än ett säkert intervall.
- Styr lasten från ett sensormätvärde med hysteresis.
- Jämför MOSFET-modul och relämodul för samma av/på-uppgift.

## Kontrollera relämodulens viloläge

Innan en relämodul får styra en riktig last bör du kontrollera hur den beter sig vid start, reset och styrsignal.

- Använd först bara reläets indikator eller klickljud, inte en kritisk last.
- Kontrollera om reläet aktiveras av `HIGH` eller `LOW`.
- Sätt reläet i säkert läge tidigt i `setup()`.
- Tryck reset och observera om reläet klickar under uppstart.
- Bryt och återanslut matningen och observera startläget.
- Välj styrpinne, startkod och eventuell inverterad logik utifrån det faktiska beteendet.
## När en annan lösning passar bättre

Det är lätt att vilja lösa allt med relä eller MOSFET, men ibland är en annan väg bättre.

En motor ska ofta styras med en riktig motordrivare, inte bara en enkel MOSFET, om du behöver riktningsstyrning, bromsning, strömlimit eller skydd. En LED-matris kan behöva en särskild LED-drivare. En värmelast kan behöva temperaturövervakning och oberoende säkerhetsbrytning. En nätspänningslast bör inte byggas på breadboard och bör inte behandlas som ett vanligt Arduino-projekt.

Ett bra designbeslut är ofta att välja en färdig, dokumenterad modul med tydliga märkdata i stället för att konstruera drivsteget själv. Men modulen är inte magisk. Du behöver fortfarande förstå aktiv nivå, strömgräns, värme, skydd och kopplingssätt.


## Riskkontroll före lasttest

Gör en kort riskkontroll innan du kopplar in en verklig last.

- Identifiera om lasten är resistiv, induktiv, motoriserad, värmande eller elektronisk.
- Kontrollera lastens spänning, normalström och möjlig startström.
- Kontrollera att drivsteget tål både strömmen och spänningen med marginal.
- Kontrollera om lasten behöver flyback-diod, snubber eller annat transientskydd.
- Kontrollera att styrsignalen har säker vilonivå vid reset och uppstart.
- Testa först med lågspänningslast eller indikator innan du ansluter något dyrare.
- Bryt matningen om relä, MOSFET, kabel eller regulator blir varm.

För nätspänning, fast installation eller okända energikällor ska bokens testkopplingar inte användas.

## Vanliga misstag

- **Misstag: Att driva lasten direkt från GPIO-pinnen.**
  - Varför det händer: Lasten ser liten ut eller fungerar kort i ett test.
  - Hur man undviker det: Låt GPIO-pinnen styra ett drivsteg och låt drivsteget bära lastströmmen.

- **Misstag: Att glömma gemensam jord mellan Arduino och extern matning.**
  - Varför det händer: Man tänker på matningarna som separata och glömmer signalens referens.
  - Hur man undviker det: Koppla ihop jord på styrsida och lastsida när styrsignalen inte är galvaniskt isolerad.

- **Misstag: Att välja MOSFET efter maximal ström men inte efter gate-spänning.**
  - Varför det händer: Datablad och webbutiker lyfter ofta stora strömtal.
  - Hur man undviker det: Kontrollera `Rds(on)` vid den gate-spänning ditt kort faktiskt ger.

- **Misstag: Att tolka `Vgs(th)` som full påslagning.**
  - Varför det händer: Tröskelspänning låter som “spänningen där MOSFET:en slår på”.
  - Hur man undviker det: Använd `Vgs(th)` som varningsinformation, inte som dimensioneringsvärde för lastström.

- **Misstag: Att sakna flyback-skydd på induktiv last.**
  - Varför det händer: Lasten fungerar några gånger även utan skydd.
  - Hur man undviker det: Sätt skyddsdiod eller lämpligt transientskydd över spolar, reläer och solenoider där modulen inte redan hanterar det.

- **Misstag: Att använda relä för snabb PWM.**
  - Varför det händer: Reläet uppfattas som en generell brytare.
  - Hur man undviker det: Använd MOSFET eller drivare för snabb växling och PWM.

- **Misstag: Att inte testa start- och resetbeteende.**
  - Varför det händer: Man testar bara när programmet redan kör.
  - Hur man undviker det: Testa power-on, reset, uppladdning och felstart innan lasten kopplas till något viktigt.

- **Misstag: Att lita blint på modulens märkdata.**
  - Varför det händer: Modulen marknadsförs med höga ström- eller spänningsvärden.
  - Hur man undviker det: Lägg marginal, kontrollera värme och använd bara väldokumenterade moduler för viktiga projekt.

## Snabb sammanfattning

- Arduino-pinnen ska normalt styra ett drivsteg, inte driva lasten direkt.
- Reläer passar bra för enkel av/på-styrning och galvanisk separation, men inte för snabb PWM.
- MOSFET:ar passar bra för lågspända DC-laster, PWM och tyst snabb styrning.
- Logic-level MOSFET är viktigt, särskilt med 3,3 V-kort.
- `Vgs(th)` betyder inte att MOSFET:en är fullt påslagen.
- Induktiva laster som reläspolar, solenoider och motorer behöver skydd mot spänningsspikar.
- Extern matning kräver normalt gemensam jord med Arduino om styrningen inte är isolerad.
- Aktiv låg logik är vanligt i relämoduler och måste testas.
- Säker startlogik är en del av konstruktionen, inte en eftertanke.
- Testa alltid med låg risk innan lasten kopplas till något dyrt, starkt eller mekaniskt farligt.

## Sista kontroll före inkoppling

Gå igenom punkterna innan lasten kopplas in i ett eget projekt.

- GPIO-pinnen styr bara drivsteget, inte lasten direkt.
- Lastens ström och spänning ligger inom drivstegets och matningens gränser.
- MOSFET, relä eller drivmodul är vald efter lasttyp och styrbehov.
- Gemensam jord finns där kopplingen kräver det.
- Induktiva laster har lämpligt skydd, till exempel flyback-diod eller annan transienthantering.
- Startläge och resetbeteende är kontrollerade innan lasten blir kritisk.
- Koden har säkert av-läge och gärna max-tid för laster som inte får bli påslagna för länge.
## Säkerhetsruta: håll nätspänning utanför experimentkopplingen

Reläer och MOSFET:ar används ofta för att styra laster, men den här boken utgår från lågspänningsprojekt. Koppla inte nätspänning på breadboard eller lösa testkablar.

Om ett projekt behöver styra nätspänning bör du använda färdiga, kapslade och godkända moduler, följa lokala regler och låta behörig kompetens granska konstruktionen. För lärande och prototypande räcker lågspänningslaster som LED-strippar, små pumpar, fläktar och solenoider.

## Snabbval

| Fråga | Kort svar |
|---|---|
| Typisk spänning | Lastmatning separat från logik |
| Typiskt gränssnitt | Digital styrsignal, ibland PWM |
| Välj när | du ska slå av/på eller modulera en last |
| Välj inte när | lasten är farlig eller okänd och du saknar kapsling/skydd |
| Vanliga fel | fel MOSFET-typ, saknad flyback-diod, delad jord saknas |
| Alternativ att överväga | färdig drivmodul, solid state-relä, lågspänningslast |

Använd referensrutan som en snabb kontroll innan du bygger projektet. Läs sedan kapiteltexten när du behöver förstå begränsningarna bakom valet.

## Relaterat

- När lasten är motor, servo eller stegmotor, läs kapitel 20 och välj drivning med hjälp av kapitel 31.
- När du styr solenoid, reläspole eller annan induktiv last, kontrollera skyddsdiod, matning och jord innan du fortsätter.
- När lasten påverkar hela projektet, dimensionera matningen med kapitel 34.
- När beteendet är intermittent, felsök först koppling, jord och spänningsfall enligt kapitel 35.

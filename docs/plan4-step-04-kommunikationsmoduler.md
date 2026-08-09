# [PLAN4] Steg 4: Kommunikationsmoduler bortom Wi-Fi och BLE

## Syfte

Steget kompletterar boken med vanliga kommunikationsmoduler och robusta bussar som ofta finns i elektronikbutiker och Arduino-projekt, men som inte passar in i den vanliga jämförelsen mellan UART, I2C, SPI och 1-Wire.

Fokus ligger på när Wi-Fi och BLE inte är rätt val.

## Ändrade kapitel

- `chapters/kommunikation-bussar-09.md`
- `chapters/referens-snabbvalsguider-38.md`

## Tillägg

Kapitel 9 har fått en ny sektion:

- `När Wi-Fi och BLE inte är rätt val`

Den behandlar:

- nRF24L01
- 433 MHz RF
- RS485
- CAN
- LoRa

Kapitel 38 har fått motsvarande rader i snabbvalet för kommunikationsbussar och nya tumregler för när respektive alternativ passar.

## Redaktionell princip

Tilläggen ska inte göra boken till en fullständig kommunikationsbok. De ska hjälpa läsaren känna igen vanliga moduler i elektronikbutiken och välja rimlig riktning:

- nRF24L01 för små datapaket mellan noder
- 433 MHz för enkla fjärrsignaler
- RS485 för robust seriell kabelkommunikation
- CAN för robusta fler-nodssystem
- LoRa för små datamängder över lång räckvidd

## Status

Steget är genomfört. `build/book.md` och exportfilerna ska uppdateras efter validering.

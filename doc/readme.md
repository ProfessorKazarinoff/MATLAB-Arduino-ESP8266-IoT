# MATLAB-Arduino-ESP8266-IoT Student Project Trouble Shooting
 
Problem Statement: 
    Upload light sensor data wirelessly using an Arduino and ESP8266
 
Assumptions: 
    No admin access on PC, can’t install drivers or software
 
Summary: 
1. Assemble Hardware
2. ESP8266 refresh and test
3. ESP8266 set default baud rate 9600
4. Arduino - Upload Code, test photo cell
5. Arduino - ESP8266 soft serial test to PC
6. Arduino - Upload Code, test software serial to ESP8266
7. ThingSpeak - set up channel
8. Arduino - Upload code, push sensor readings to ThingSpeak
9. PC - view sensor data on ThingSpeak
 
## Assemble Hardware:

### Bill of Materials
    
| Component     | URL           |
| ------------- | ------------- |
| Arduino - Sparkfun Redboard  |![Redboard at Sparkfun](https://www.sparkfun.com/products/13975?_ga=2.75723669.1619575078.1498623788-1288264142.1469139950) |
| ESP8266  | ![ESP8266 on Amazon](https://www.amazon.com/gp/product/B01MT6T73L/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)  |
| Bi-directional logic converter  | ![Logic Converter on Amazon](https://www.amazon.com/gp/product/B014MC1OAG/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)  |
| Breadboard Power Supply | Amazon |
| M/M Jumper Wires  | ![M/M 6" Jumper wires at Sparkfun](https://www.sparkfun.com/products/8431)  |
| Breadboard  | Sparkfun  |
| Mini-B USB Cable  | ![Mini-B to A USB cable at Sparkfun](https://www.sparkfun.com/products/11301?_ga=2.114882823.1619575078.1498623788-1288264142.1469139950)  |
    
    Fritzing Diagram
    Connection Chart
    Picture
 
2. ESP8266 refresh and test:
    Asseble PC --> Arduino --> Logic Level Converter --> ESP8266
    A couple notes: The pin labeled RX on the Arduino connects to RX on the ESP8266 (Arduino labeling corresponds to what to connect the pin to, not what the pin is in this case)
    The Arduino serial runs at 5V and this can damage the 3.3V ESP8266, so a logic converter is used to step down the voltage. A common ground must also be connected to the logic converter.
    The Reset pin on the Arduino needs to be grounded to put the Arduino is the mode where it just reads serial communcation and does not run or accept code.
    
    ![Alt Name](/doc/Redboard_ESP8266_passthru_serial_bb.png)
    
    
    Plug in ESP 8266 with USB cable
    open Arduin0 Serial monitor: 11520 baud, Both RL / TL
    ```
    AT —> ready
    AT-RST —> ready
    AT-GMR —> firmware version
    install python
    pip install esptool
    download firmware .bin files
    command line: esptool.py —hardware — bin register 0x00000
    Test: AT —> ready
    AT-RST —> ready
    AT-GMR —> firmware version
    ```
 
3. ESP8266 set baud rate 9600 and test:
    Change ESP8266 Serial baud rate - AT+UART_DEF(9600,0,0,1) 
    Connect ESP8266 RX-TX, TX-RX, RST-3.3V CHMD-3.3V GND-GND VCC-3.3V
    Serial Monitor: 9600 Baud, Both RL / NL
    ```
    Test: AT —> Ready AT-RST, AT-GMR
    ```
    Test ESP8266 can log onto network
    ```
    AT+CMR=? (which mode)
    AT+CMR=3 (client mode)
    AT+CMR=‘netID’ ‘password’ (WiFi connect)
    AT + CMR = disconnect
    AT + RST
    AT
    ```
 
4. Arduino: Upload code test photocell
    Connect Arduino and Photocell, LED
    Upload sketch
    View Serial Monitor, 9600 for photocell readings
 
5. Arduino Software Serial to PC Test:
    install software serial library
    Connect Arduino D8, D9 to TTL converter
    Upload Sketch and test software serial between Arduino and PC.
    View Serial Monitor, 9600 for photocell readings
    Upload Sketch and test software serial between PC and Arduino
    Type H, L see LED turn on and off
    
 
6. Arduino Software Serial to ESP8266 Test:

    Connect Arduino - logicconverter- ESP8266
    
    ![Alt Name](/doc/Redboard_ESP8266_software_serial.png)
    
    Upload Sketch
    Test Arduino - ESP8266 software serial
 ```
    >> AT
    >> AT+RST
    >> AT+GMR
    >> AT+CMR?
    >> AT+CMR3
    >> AT+CMR=‘netID’ ‘password’
 ```
7. ThingSpeak - set up channel:
    ThingSpeark account
    ThingSpeak channel
    Channel ID
    API write Key
    API read Key
 
8. Arduino - Upload code, push sensor readings to ThingSpeak
    Arduino code, include channel, API keys
    Upload sketch
    View Serial Monitor, 9600
    upload sensor data every 20 sec
 
9. PC - view sensor data on ThingSpeak:
    View sensor readings on ThingSpeak
    Use web browser and API http: channelID,field1,

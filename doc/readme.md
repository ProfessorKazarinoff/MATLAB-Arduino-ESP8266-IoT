# MATLAB-Arduino-ESP8266-IoT Student Project Trouble Shooting
 
Problem Statement: 
    Upload light sensor data wirelessly to ThingSpeak.com using an Arduino and ESP8266 in a college engineering lab.
 
Assumptions: 
    No admin access on PC, can’t install drivers or software. Encripted WiFi connection that requires a username and password in addition to an SSID.
 
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
| Breadboard Power Supply | ![Breadboard Power Supply on Amazon](https://www.amazon.com/UCEC-Breadboard-Supply-Arduino-Solderless/dp/B01ELAGIO6/ref=sr_1_fkmr0_1?s=electronics&ie=UTF8&qid=1504628907&sr=1-1-fkmr0&keywords=UCES+MB102+3.3V%2F5V+Breadboard) |
| M/M Jumper Wires  | ![M/M 6" Jumper wires at Sparkfun](https://www.sparkfun.com/products/8431)  |
| Breadboard  | ![Mini Breadboard at Sprakfun](Sparkfun )|
| Breadboard Adapter for ESP8266 | ![ESP8266 breadboard breakout adapter on Amazon](https://www.amazon.com/DIYmall-ESP8266-Breakout-Breadboard-Transceiver/dp/B01G6HK3KW/ref=sr_1_sc_1?s=electronics&ie=UTF8&qid=1504629134&sr=1-1-spell&keywords=DIY+mall+esp8266+esp-01+Breakout+board)|
| Mini-B USB Cable  | ![Mini-B to A USB cable at Sparkfun](https://www.sparkfun.com/products/11301?_ga=2.114882823.1619575078.1498623788-1288264142.1469139950)  |
| USB FTDI Basic Breakout | [Serial TTL converter](http://a.co/9YehAMI) |
    
    Fritzing Diagram
    Connection Chart
    Picture
 
2. ESP8266 refresh and test:
    Asseble PC --> Arduino --> Logic Level Converter --> ESP8266
    A couple notes: The pin labeled RX on the Arduino connects to RX on the ESP8266 (Arduino labeling corresponds to what to connect the pin to, not what the pin is in this case)
    The Arduino serial runs at 5V and this can damage the 3.3V ESP8266, so a logic converter is used to step down the voltage. A common ground must also be connected to the logic converter.
    The Reset pin on the Arduino needs to be grounded to put the Arduino is the mode where it just reads serial communcation and does not run or accept code.
    
    ![Alt Name](/doc/Redboard_ESP8266_passthru_serial_bb.png)
    
    
    Plug in the USB cable from the Arduino to the computer. This will connect the ESP8266 (through the Arduino) to the computer.
    Open the Arduino Serial monitor: 11520 baud, Both RL / TL. This allows us to directly communicate with the ESP8266. 
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
    To change ESP8266 Serial baud rate - AT+UART_DEF=9600,8,1,0,0
    (may be used on other ESP8266 boards: AT+UART_DEF(9600,0,0,1) ) 
    
    Connect ESP8266 RX-TX, TX-RX, RST-3.3V CHMD-3.3V GND-GND VCC-3.3V
    Serial Monitor: 115200  baud, Both RL / NL
    With an ESP8266-01S ```>>> AT+GMR``` returned AT and SDK versions of
    ```
    AT+GMR
    AT version:1.2.0.0(Jul  1 2016 20:04:45)
    SDK version:1.5.4.1(39cb9a32)
    Ai-Thinker Technology Co. Ltd.
    Dec  2 2016 14:21:16
    OK
    ```
    
    To change ESP8266 Serial baud rate - (may be used on other ESP8266 boards AT+UART_DEF(9600,0,0,1) ) 
    ```
    AT+UART_DEF=9600,8,1,0,0
    ```
    Then change to 9600 baud on the Serial Monitor
    Serial Monitor: 115200  baud, Both RL / NL
    
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
    Upload Arduino sketch. Ensure COM port is set correclty.
    View Serial Monitor, 9600 for photocell readings
 
5. Arduino Software Serial to PC Test:
    In Arduino IDE, install software serial library
    Connect Arduino D8, D9 to TTL converter
    Upload Sketch and test software serial between Arduino and PC.
    View Serial Monitor, 9600 for photocell readings
    Upload Sketch and test software serial between PC and Arduino
    Type H, L see LED turn on and off
    
 
6. Arduino Software Serial to ESP8266 Test:

    Connect Arduino D8, D9, 5v, GND - logicconverter- ESP8266
    
    
    
    Upload software serial pass through sketch to Arudino
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

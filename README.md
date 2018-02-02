# MATLAB-Arduino-ESP8266-IoT
A student project for ENGR114 at Portland Community College. Uses MATLAB connected to an Arudino over serial to control an ESP8266 over serial that can connect over WiFi to an IoT server.

## Problem Statement: 
Wirelessly upload light sensor data using an Arduino connected to an ESP8266 over serial.
 
### Assumptions: 
No admin access on college computers, students can’t install drivers or new software. WiFi network requires student username and student G#.
 
## Summary:
1. Assemble Hardware
2. Wire together ESP8266, logic converter, Arudio and power supply
3. ESP8266 test
   * ESP8266 set default baud rate 9600
   * Upload new firmware with esptool.py
4. Arduino - Upload Code, test photo cell
5. Arduino - ESP8266 soft serial test to PC
6. Arduino - Upload Code, test software serial to ESP8266
   consider changing soft serial baud rate to 4800 and ESP8266 baud rate to 4800 and increasing software serial cache size
   mySerial swSerial(4800,false,256)?
7. ThingSpeak - set up channel
8. Arduino - Upload code, push sensor readings to ThingSpeak
9.  PC - view sensor data on ThingSpeak

### Assemble Hardware

#### Bill of Materials
    
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

### Wire together ESP8266-Logic Converter-Arduino and Power Supply

Asseble PC --> Arduino --> Logic Level Converter --> ESP8266 <-- Power Supply

![Alt Name](/doc/Redboard_ESP8266_passthru_serial_bb.png)

##### Hookup Guide

| Arudino Pin   | HV Logic Converter Pin | LV Logic Converter Pin | ESP8266 Pin | Power Supply Pin |
| ------------- | ---------------------- | ---------------------- | ------------| ---------------- |
| RST -to- GRN  |                        |                        |             |                  |
| 5V            | HV                     | LV                     | VCC         |   +3.3 V         |
| GND           | GND                    | GND                    | GND         |    GND           |
| TX-->1        | HV1                    | LV1                    | TXD         |                  |
| RX<--0        | HV2                    | LV2                    | RXD         |                  |
|               |                        |                        | CHPD        |   +3.3 V         |
|               |                        |                        | RST         |   +3.3 V         |

### ESP8266 reflesh and test
```
>> AT+GMR

AT+GMR
AT version:1.2.0.0(Jul  1 2016 20:04:45)
SDK version:1.5.4.1(39cb9a32)
Ai-Thinker Technology Co. Ltd.
Dec  2 2016 14:21:16
OK
```



### ESP8266 set default baud rate 9600

```
>> AT+UART_DEF=9600,8,1,0,0'
```
In the Arduino serial monitor, select 9600 baud. Check to confirm serial communication
 ```
 >> AT
 
 AT
 
 OK


>> AT+RST


OK
c_�RS�fJ[zfJ[:fN��O�G�G��SO�
X�������
Ai-Thinker Technology Co. Ltd.

ready

>> AT+GMR
 AT+GMR
 AT version:1.2.0.0(Jul  1 2016 20:04:45)
 SDK version:1.5.4.1(39cb9a32)
 Ai-Thinker Technology Co. Ltd.
 Dec  2 2016 14:21:16
OK
```
Attempt to connect to WiFi network
```
>> AT+CWJAP?

No AP

OK
>> AT+CWMODE=3


OK

>> AT+CWMODE?

+CWMODE:3

OK
>> AT+CWJAP="Your SSID","Your WiFi Password"

WIFI CONNECTED
WIFI GOT IP

OK

>>  AT+CWJAP?

+CWJAP:"Your SSID","e8:89:2c:0f:f5:80",1,-45

OK

>> AT+CWLAP

[list of connected devices connected to the netwrok]

>> AT+CWQAP


OK
WIFI DISCONNECT

>>AT+CWJAP?

No AP

OK
```




## License:
GNU GENERAL PUBLIC LICENSE, Version 3

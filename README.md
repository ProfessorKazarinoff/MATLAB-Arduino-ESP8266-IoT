# MATLAB-Arduino-ESP8266-IoT
A student project for ENGR114 at Portland Community College. Uses MATLAB connected to an Arudino over serial to control an ESP8266 over serial that can connect over WiFi to an IoT server.

## Problem Statement: 
Wirelessly upload light sensor data using an Arduino connected to an ESP8266 over serial.
 
### Assumptions: 
No admin access on PC's, students can’t install drivers or new software.
 
## Summary:
- Assemble Hardware
- ESP8266 reflesh and test
- ESP8266 set default baud rate 9600
- Arduino - Upload Code, test photo cell
- Arduino - ESP8266 soft serial test to PC
- Arduino - Upload Code, test software serial to ESP8266
   consider changing soft serial baud rate to 4800 and ESP8266 baud rate to 4800 and increasing software serial cache size
   mySerial swSerial(4800,false,256)?
- ThingSpeak - set up channel
- Arduino - Upload code, push sensor readings to ThingSpeak
- PC - view sensor data on ThingSpeak

### Assemble Hardware

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

In the Arduino serial monitor, select 9600 baud
 `>> AT
 
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

+CWLAP:(4,"SSID1",-44,"e8:89:2c:0f:f5:80",1,32767,0)
+CWLAP:(4,"SSID2",-64,"b0:7f:b9:3b:19:aa",1,1,0)
+CWLAP:(4,"SSID3",-72,"60:02:92:aa:ac:a0",1,-6,0)
+CWLAP:(0,"xfinitywifi",-72,"60:02:92:aa:ac:a2",1,-6,0)
+CWLAP:(0,"xfinitywifi",-34,"e6:89:2c:0f:f5:80",1,32767,0)

>> AT+CWQAP


OK
WIFI DISCONNECT

>>AT+CWJAP?

No AP

OK
```




## License:
GNU GENERAL PUBLIC LICENSE, Version 3

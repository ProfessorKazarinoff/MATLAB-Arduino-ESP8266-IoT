### How to set the ESP8266 default baud rate

If the ESP8266 does not respond to the ```AT``` commands typed into the Serial Monitor, it might be becuase the ESP8266 is trying to communicate at a different baudrate.

To change the baud rate:

1. Try to connect to the ESP8266 at 115200 baud using the Serial Monitor. Ensure the Serial Monitor is set to ```Both NL & CR```

2. Type the following command into the Serial Monitor. If the first command does not work, some ESP8266 boards use the second command instead

```
AT+UART_DEF=9600,8,1,0,0
```

or

```
AT+UART_DEF(9600,0,0,1)
```

3. Set the Serial Monitor to 9600 baud and try the following commands:

```
AT
AT+RST
AT+GMR
```

The full output as a result of these commands should be something like:

```
>> AT

OK

>> AT+RST

c_�RS�fJ[zfJ[:fN��O�G�G��SO�
Ai-Thinker Technology Co. Ltd.

ready

>> AT+GMR

AT version:1.2.0.0(Jul  1 2016 20:04:45)
SDK version:1.5.4.1(39cb9a32)
Ai-Thinker Technology Co. Ltd.
Dec  2 2016 14:21:16
OK
```

If this works, you successfully changed the ESP8266 baud rate. Go back to the [main readme](../README.md) and try the full set of ```AT``` commands in the Serial Monitor.

### How to set the ESP8266 default baud rate

If the ESP8266 does not respond to the ```AT``` commands typed into the Serial Monitor, it might be becuase the ESP8266 is trying to communicate at a different baudrate.

To change the baud rate:

1. Connect at 11152 baud using the Serial Monitor

2. Type the following command into the Serial Monitor. If the first command does not work, some ESP8266 boards use the second command instead

```
AT...
```

or

```
AT...
```

3. Set the Serial Monitor to 9600 baud and try the following commands:

```
AT
AT+RST
AT+GMR
```

If this works, you are successful, go back to the [main readme](../README.md) and try the full set of ```AT``` commands in the Serial Monitor
### Possible option to use micropython on Adafruit Feather Huzzah ESP8266

Load micropython onto Feather Huzzah using esptool

https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266

Function for connecting to network with Feather Huzzah
https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_basics.html

```

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

```

Function to make an http GET request
https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_tcp.html

```

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break

```

To post to thingspeak:
https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1=87
Class API key on D2L:
Module 2 Arduino IoT Project Example MATLAB code to post data to ThingSpeak.com


Hook up an analog sensor to the ADC Pin

```
>>> import machine
>>> adc = machine.ADC(0)
>>> data_int = adc.read()
>>> data_str = str(data_int)
>>> base_url = 'https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1='
>>> url = base_url + data_str
>>> #enter connect to WiFi function and run
>>> #enter http_get function
>>> http_get(url)
>>> # will return a bunch of stuff. Number at end is data point number in thingspeak
```





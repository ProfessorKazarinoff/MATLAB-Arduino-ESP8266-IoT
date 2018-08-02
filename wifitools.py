import urequests

#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_basics.html
def connect(SSID,password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_tcp.html
def http_get(url):
    import socket
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

def thingspeak_post(API_key,data):
    if not isinstance(data, str):
        data = str(data)
    #base_url = 'https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1=87'
    base_url = 'https://api.thingspeak.com/update?api_key='
    mid_url = '&field1='
    url = base_url + API_key + mid_url + data
    http_get(url)

def getmac():
    import network
    import ubinascii
    return ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

def flaskiot_post(API_key,mac_address,field, data):
    if not isinstance(data, str):
        data = str(data)
    if not isinstance(field, str):
        field = str(field)
    # https://freetemp.org/update/API_key=ASCIISTR/mac=6c:rf:7f:2b:0e:g8/field=1/data=72.3
    base_url = 'https://freetemp.org/update'
    api_key_url = '/API_key=' + API_key
    mac_url = '/mac=' + mac_address
    field_url = '/field=' + field
    data_url = '/data=' + str(data)
    url = base_url + api_key_url + mac_url + field_url + data_url
    print(url)
    response = urequests.get(url)
    print(response.text)

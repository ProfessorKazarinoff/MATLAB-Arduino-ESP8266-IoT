# ESP8266 Feather Huzzah Weather Station, connected to flask IoT server

import wifitools
import MCP9808
import time
import config

def main():
    api_key = config.API_KEY
    mac_address = config.MAC_ADDRESS
    field = '1'
    ssid = config.SSID
    password = config.WIFI_PASSWORD
    wifitools.connect(ssid,password)
    time.sleep(5)

    for i in range(60*8):
        data = MCP9808.readtemp()
        wifitools.flaskiot_post(api_key,mac_address,field,data)
        time.sleep(60)

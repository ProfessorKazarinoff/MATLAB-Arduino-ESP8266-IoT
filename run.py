# ESP8266 Feather Huzzah Weather Station, connected to flask IoT server

import wifitools
import MCP9808
import time
import config

def main():
    ssid = config.SSID
    password = config.WIFI_PASSWORD
    api_key = config.API_KEY
    mac_address = config.MAC_ADDRESS
    field = '1'

    wifitools.connect(ssid,password)
    time.sleep(5)

    for i in range(60*8):
        data = MCP9808.readtemp()
        try:
            wifitools.flaskiot_post(api_key,mac_address,field,data)
        except:
            pass
        time.sleep(60)

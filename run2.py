# ESP8266 Feather Huzzah Weather Station, connected to flask IoT server

import wifitools
import BMP280
import time
import config
import machine

def main():
    ssid = config.SSID
    password = config.WIFI_PASSWORD
    api_key = config.API_KEY
    mac_address = config.MAC_ADDRESS
    field = '2'                         # 2nd temperature sensor is field 2
    wifitools.connect(ssid,password)
    time.sleep(5)
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
    sensor = BMP280.BMP280(i2c)

    for i in range(60*8):
        data = str(sensor.values[0])
        try:
            wifitools.flaskiot_post(api_key,mac_address,field,data)
        except:
            pass
        time.sleep(60)

### Upload new firmware to the ESP8266

If the ```AT``` commands still are not working after attempting to connect at 9600 baud, then changing the defaut baud rate to 9600 baud, you might need to update the ESP8266 firmware. This is a fairly complex procedure involving a tool called [esptool.py](https://github.com/espressif/esptool). The rough steps are below:

1. Install Python
The esptool uses the Python programming language. You need to install Python in order to run the tool. I recommend downloading and installing the [Anaconda version of Python](https://www.anaconda.com/download).

2. Install the esptool package using pip
Open the Anaconda Prompt and type:

```
pip install esptool
```

3. Verify the esptool package is installed
In the Anaconda Prompt type:

```
esptool.py write_flash -h
```

You should see the help file for writing to the ESP8266 flash memory.

4. Get the .bin files

You need to locate and aquire the proper .bin files in order to write them to the ESP8266. Getting the .bin files is a little complicated. Follow the README in this repo ([ESP8266_RTOS_SDK](https://github.com/espressif/ESP8266_RTOS_SDK)), created by espressif, the company that makes the ESP8266. At the end of it you should end up with a couple .bin files.

5. Put the ESP8266 in bootloader mode

The ESP8255 has two modes. The first mode is normal opperating mode. ESP8266 is usually in normal opperating mode. In normal opperating mode, ```AT``` command can be sent back and forth, the ESP8266 can connect to WiFi, the ESP8266 can communicate over the Serial Monitor,  etc. In normal opperating mode you can't upload new firmware or programs on the ESP8266. 

The second mode is bootloader mode. In bootloader mode, the ESP8266 is set up to accept new firmware or a new program. In bootloader mode, you can't connect to WiFi or run AT commands. You only put the ESP8266 in bootloader mode when you want to upload new firmware or programs. 

Since we want to upload new firmware, we need to set the ESP8266 in bootloader mode. You can put the ESP8266 in bootloader mode by turning off the power to the ESP8266, then connecting the GPIO1 pin to ground, then turning the ESP8266 power back on. When GPIO1 is connected to ground, the ESP8266 is in bootloader mode and the firmware can be uploaded. Once the firmware has been uploaded, turn the power off, and unhook the GPIO1 from ground. Then turn the power back on and the ESP8266 will be back in normal opperating mode.

6. Write the .bin files to the ESP8266 flash memory

Once the .bin files are in the current folder and the ESP8266 is in bootloader mode, run the following command in the Anaconda Prompt to uploaded the .bin firmware to the ESP8266. You will need to check the port and change the .bin file name(s):

```
esptool.py --port COM4 write_flash 0x1000 my_app-0x01000.bin
```

To verify that the flash memory has been written correctly run the following in the Anaconda Prompt. You will need to change the flash address ```0x40000``` and the .bin file name corresponding to the flash address and .bin file name used above when the ```write_flash``` command was called.

```
esptool.py verify_flash 0x40000 my_app.elf-0x40000.bin
```

7. Power down the ESP8266 and disconnect the GPIO1 pin from ground. Then turn the power back on. 

The ESP8266 is back in normal opperating mode. Try the simple AT commands in the Serial Monitor to test the ESP8266 and it's new firmware:

```
AT
AT+RST
AT+GMR
```

If everything works correctly, go back to the [main readme](../README.md) and test the full set of ```AT``` commands.

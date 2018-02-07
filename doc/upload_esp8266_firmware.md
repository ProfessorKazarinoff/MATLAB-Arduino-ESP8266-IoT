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

4. Locate the .bin files
You need to locate and download the proper .bin files in order to write them to the ESP8266

5. Put the ESP8266 in bootloader mode
The ESP8255 has two modes. The first mode is normal opperating mode. ESP8266 is usually in normal opperating mode the. In normal opperating mode ```AT``` command can be sent back and forth, the ESP8266 can connect to WiFi etc. In normal opperating mode you can't upload new firmware or programs on the ESP8266. 

The second mode is bootloader mode. In bootloader mode, the ESP8266 is set up to accept new firmware or a new program. In bootloader mode, you can't connect to WiFi or run AT commands. You only put the ESP8266 in bootloader mode when you want to upload new firmware or programs. 

Since we want to upload new firmware, we need to set the ESP8266 in bootloader mode. You can put the ESP8266 in bootloader mode by connecting the GPIO1 pin to ground. Once the firmware has been uploaded, turn the power off, and unhook the GPIO1 from ground. Then turn the power back on and the ESP8266 will be back in normal opperating mode.

6. Write the .bin files to the ESP8266 flash memory
Once the .bin files are in the current folder, run the following command in the Anaconda Prompt to 

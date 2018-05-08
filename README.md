# Vigilo
This repo contains our efforts to make a smart security system. 

### Prerequisites 

#### Hardware
The following hardware was used to for the Vigilo Security System:
  * Raspberry Pi 3 B+ Starter Kit [Amazon](https://www.amazon.com/gp/product/B07BCC8PK7/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)
  * Adafruit Magnetic Sensor [Amazon](https://www.amazon.com/gp/product/B01GQFUYAS/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
  * Logitech C270 Webcam [Amazon](https://www.amazon.com/Logitech-Widescreen-Recording-Certified-Refurbished/dp/B071KT6W9P/ref=sr_1_1?ie=UTF8&qid=1525758605&sr=8-1&keywords=logitech+c270&dpID=41HVqwN850L&preST=_SX300_QL70_&dpSrc=srch)
  * USB Hub with External Power [Amazon](https://www.amazon.com/Adesso-AUH-2070P-Port-Power-Adapter/dp/B07BK5539K/ref=sr_1_5?s=electronics&ie=UTF8&qid=1525758650&sr=1-5&keywords=adesso+usb+hub)
  * Jumper Wires [Amazon](https://www.amazon.com/120pcs-Multicolored-Breadboard-Arduino-raspberry/dp/B01LZF1ZSZ/ref=sr_1_fkmr0_1?s=electronics&ie=UTF8&qid=1525758697&sr=1-1-fkmr0&keywords=heirtronic+jumper+wires)

#### Dependencies
To install dependencies run the following commands on your RasberryPi (running Raspbian):
  * ARP Scan:
    `sudo apt-get install arp-scan -y`
  * FS Webcam:
    `sudo apt-get install fswebcam -y`
  * Python Libraries:
     * To install of the pythond dependencies run from the root directory:
        `pip3 install -r requirements.txt`
     
     Alternatively, you can run `pip3 install imgurpython` and `pip3 install twilio.rest`
     
#### Configuration Variables
Create a file at `./src/credentials.ini` and populate with relevant credentials: 
```
[Imgur]
USERNAME = *****
PASSWORD = *****
CLIENT_ID = *****
CLIENT_SECRET = *****
ACCESS_TOKEN = *****
REFRESH_TOKEN = *****
[Twilio]
SID = *****
TOKEN = *****
TO = *****
FROM = *****
[User]
NAME = *****
MAC = *****
PICTURE *****
```

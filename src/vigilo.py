import configparser
import os
import subprocess
import time

import RPi.GPIO as GPIO
from imgurpython import ImgurClient
from twilio.rest import Client

# Getting configuration variables
configurations = configparser.ConfigParser()
configurations.read('credentials.ini')
    
# Pi and pin setup
GPIO.setmode(GPIO.BCM)
DOOR_SENSOR_PIN = 18
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# User setup
last_scan = None    # We keep track of when the last scan was done
network = None      # The current state of the network
individual = configurations.get("User", "NAME") # The individual who's device must be on the network
address = configurations.get("User", "MAC")  # The device's MAC address
picture_path = configurations.get("User", "PICTURE") # The location of stored picture ¨./intruder.jpg¨ recomended 
# print(individual, address, picture_path)

# Twilio setup
twilio_account = configurations.get("Twilio", "SID") 
twilio_token = configurations.get("Twilio", "TOKEN") 
txt_to = configurations.get("Twilio", "TO")
txt_from = configurations.get("Twilio", "FROM")
twilio = Client(twilio_account, twilio_token)
# print(twilio_account, twilio_token, txt_to, txt_from)

# Imgur setup
imgur_id = configurations.get('Imgur', 'CLIENT_ID')
imgur_secret = configurations.get('Imgur', 'CLIENT_SECRET')
imgur_access = configurations.get('Imgur', 'ACCESS_TOKEN')
imgur_refresh = configurations.get('Imgur', 'REFRESH_TOKEN')
imgur = ImgurClient(imgur_id, imgur_secret, imgur_access, imgur_refresh)
imgur_config = {
    'album': None,
    'name':  'Intruder!',
    'title': 'Intruder!',
    'description': 'Possible Intruder'
}
# print(imgur_id, imgur_secret, imgur_access, imgur_refresh)

# This function returns true if the mac address registered is scanned
# on the wifi, false otherwise. 
def is_home():
    global network
    global last_scan
    # Check if this is the first run or if the last network scan occured
    # more than five minutes ago, if so run a new scan
    if network is None or time.time() - last_scan >= 300:
        network = subprocess.check_output("sudo arp-scan -l", shell=True)
        network = network.decode("utf-8")
        last_scan = time.time()
        print(network)
    # a timer to make sure the arp-scan was finished
    # time.sleep(30)
    if address in network:
        print(individual + " is home")
        return True
    else:
        print("No one is home")
        return False
    
    
# This function takes a picture of an intruder, returns true if successful
# and false otherwise
def take_picture():
    picture = subprocess.run("fswebcam " + picture_path, shell=True, check=True)
    return os.path.isfile(picture_path)


# This function uploads an image located at the default location to Imgur and
# returns the url, otherwise it returns none
def upload():
    image = imgur.upload_from_path(picture_path, config=imgur_config, anon=True)
    os.remove(picture_path)
    return image["link"]
    

# This function sends an alert to the registered phone number
def send_text(url):
    text = "Intruder detected! Check out the intruder at " + url 
    message = twilio.messages.create(to=txt_to, from_=txt_from, body=text)


# If the script will be run on boot, the following line will give the Pi
# time to connect to the network
# sleep(60)
isOpen = 0
oldIsOpen = None

while True:
    oldIsOpen = isOpen
    isOpen = GPIO.input(DOOR_SENSOR_PIN)
    # print(isOpen)

    if (isOpen and (isOpen > oldIsOpen)):
        print("Door opened!")
        if not is_home():
            if take_picture():
                url = upload()
                send_text(url)
            else:
                print("Unable  to take a picture")
        else:
            print(individual + " is home, no text will be sent")
        

    time.sleep(0.1)


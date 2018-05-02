import RPi.GPIO as GPIO
import time
from twilio.rest import Client

# Pi and pin setup
GPIO.setmode(GPIO.BCM)
DOOR_SENSOR_PIN = 18
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# We keep track of when the last scan was done
last_scan = None
# The individual who's device must be on the network
individual = "NAME"
# The device's MAC address
address = "xx:xx:xx:xx:xx:xx"
# The current state of the network
network = None

def isHome():
    # Check if this is the first run or if the last network scan occured
    # more than five minutes ago, if so run a new scan
    if network is None or time.time() - last_scan >= 300:
        network = subprocess.check_output("sudo arp-scan -l", shell=True)
        last_scan = time.time()
    # a timer to make sure the arp-scan was finished
    sleep(30)

    if address in network:
        print(individual + "is home")
        return True
    else:
        print("No one is home")
        return False


# Twilio setup
account = 'secret'
token = 'secret'
txt_to = 'secret'
txt_from = 'secret'
twilio = Client(account, token)

def send_text():
    text = 'Intruder detected'
    if isHome():
        message = twilio.messages.create(to=txt_to, from_=txt_from, body=text)

isOpen = 0
oldIsOpen = None

# If the script will be run on boot, the following line will give the Pi
# time to connect to the network
# sleep(60)

while True:
    oldIsOpen = isOpen
    isOpen = GPIO.input(DOOR_SENSOR_PIN)
    print(isOpen)

    if (isOpen and (isOpen > oldIsOpen)):
        send_text()
        print("Door opened!")

    time.sleep(0.1)

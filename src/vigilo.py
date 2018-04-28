import RPi.GPIO as GPIO
import time
from twilio.rest import Client

# Pi and pin setup
GPIO.setmode(GPIO.BCM) 
DOOR_SENSOR_PIN = 18
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Twilio setup
account = 'secret'
token = 'secret'
txt_to = 'secret'
txt_from = 'secret'
twilio = Client(account, token)

def send_text():
    text = 'Intruder detected'
    message = twilio.messages.create(to=txt_to, from_=txt_from, body=text)

isOpen = 0
oldIsOpen = None

while True: 
    oldIsOpen = isOpen 
    isOpen = GPIO.input(DOOR_SENSOR_PIN)
    print(isOpen)
    
    if (isOpen and (isOpen > oldIsOpen)):
        send_text()
        print("Door opened!")
        
    time.sleep(0.1)
    

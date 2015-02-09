import RPi.GPIO as GPIO
import time

pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True:
    pin_value = GPIO.input(pin)
    print('High' if pin_value else 'Low')
    time.sleep(0.2)

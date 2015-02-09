import RPi.GPIO as GPIO
import time, math

GPIO.setmode(GPIO.BCM)
pin = 17
count = 0
R = 9
T = 5

def spin():
    global count
    count += 1
    print(count)

def calcspeed():
    

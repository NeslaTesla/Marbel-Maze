import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep


pin = 27
pin1 = LED(5)
pin2 = LED(6)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

while(True):
    if(GPIO.input(27)):
        print("Hey",pin)
        pin1.on()
        sleep(0.5)
        pin2.off()
        sleep(0.5)
        

    else:
        pin2.on()
        pin1.off()

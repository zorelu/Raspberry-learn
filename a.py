import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
a = [18]
GPIO.setup(a,GPIO.OUT)
while True:
            #for dc in range(0, 101, 5):
    GPIO.output(a,GPIO.HIGH)
            #for dc in range(100, -1, -5):
    #        GPIO.output(a,GPIO.LOW)
GPIO.cleanup()


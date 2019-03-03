import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin=18
GPIO.setup(pin,GPIO.OUT,initial=GPIO.LOW)
print(GPIO.input(pin))

try:
    while True:
            GPIO.cleanup()

             #print("111") 
#             GPIO.setup(pin,GPIO.OUT,False)

             #GPIO.output(pin,GPIO.LOW)
except KeyboardInterrupt:
            pass

GPIO.cleanup()


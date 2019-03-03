import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
a = 24
GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(a):
        print('Inpu was HIGH')
        time.sleep(3)
    else:
        print('Input was LOW')
        time.sleep(3)
GPIO.cleanup()


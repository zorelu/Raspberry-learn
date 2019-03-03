import RPi.GPIO as GPIO
import time
a = 22
b = 18
try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        if GPIO.input(a):
            GPIO.cleanup()
            print("off")
            time.sleep(0.3)
        else:
            #GPIO.cleanup()
            GPIO.setup(b,GPIO.OUT)
            GPIO.output(b,GPIO.LOW)
            print ("on")
            time.sleep(30)
except KeyboardInterrupt:
            pass

GPIO.cleanup()


import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
a = 23
GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
b =  [16,20,21]
GPIO.setup(b,GPIO.OUT)
try:
    while True:
        if GPIO.input(a):

            GPIO.output(b,GPIO.HIGH)
            os.system( "raspistill -o  -> zorelu.jpg")
           # time.sleep(60)
        else:
            GPIO.output(b,GPIO.LOW)
        #time.sleep(1)
           # print('Input was HIGH')
            #print('Input was LOW')
except KeyboardInterrupt:
            pass

GPIO.cleanup()


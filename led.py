import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
a = [21,16,20]
GPIO.setup(a,GPIO.OUT)

pwm = GPIO.PWM(21, 80)
pwm.start(0)
try:
    while True:
            #for dc in range(0, 101, 5):
                pwm.ChangeDutyCycle(100)
                GPIO.output(a,GPIO.HIGH)
                time.sleep(1)
            #for dc in range(100, -1, -5):
                pwm.ChangeDutyCycle(6)
    #        GPIO.output(a,GPIO.LOW)
                time.sleep(1)
except KeyboardInterrupt:
        pass
GPIO.cleanup()


import RPi.GPIO as GPIO
import time
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
a = [21,16,20]

@app.route('/')
def index():
    GPIO.setup(a,GPIO.OUT)
    try:
        while True:
            #for dc in range(0, 101, 5):
                GPIO.output(a,GPIO.HIGH)
                return "led up"
            #for dc in range(100, -1, -5):
    #        GPIO.output(a,GPIO.LOW)
    except KeyboardInterrupt:
            pass
            return "no ok"

@app.route('/down')
def down():
        GPIO.output(a, GPIO.LOW)
        return "led down"

app.run(host='0.0.0.0')

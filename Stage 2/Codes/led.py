import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(37,GPIO.OUT)#Blue
GPIO.setup(38,GPIO.OUT)#Green
GPIO.setup(40,GPIO.OUT)#Red
GPIO.output(40,0)
time.sleep(3)

GPIO.cleanup()

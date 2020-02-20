import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

PWMR = GPIO.PWM(24,60)
PWMR1 = GPIO.PWM(23,60)
PWML = GPIO.PWM(17,60)
PWML1 = GPIO.PWM(22,60)

PWMR.start(0)
PWMR1.start(0)
PWML.start(0)
PWML1.start(0)

while True:
    
    print "Going Forward"
    PWMR.ChangeDutyCycle(100)
    PWML.ChangeDutyCycle(100)
    time.sleep(5)
    PWML.ChangeDutyCycle(0)
    PWMR.ChangeDutyCycle(0)
    time.sleep(2)
    print "Going Backward"
    PWMR1.ChangeDutyCycle(100)
    PWML1.ChangeDutyCycle(100)
    time.sleep(5)
    PWML1.ChangeDutyCycle(0)
    PWMR1.ChangeDutyCycle(0)
    time.sleep(2)

PWMR.stop()
PWMR1.stop()
PWML.stop()
PWML1.stop()

GPIO.cleanup()

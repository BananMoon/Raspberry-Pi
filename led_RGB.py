#13 : Red / 19 : Green / 26 : Blue , led RGB를 번갈아 키는 실습
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)  #Red
GPIO.setup(19,GPIO.OUT)  #Green
GPIO.setup(26,GPIO.OUT)  #Blue

try:
    while True:
        GPIO.output(13,True)
        time.sleep(0.5)
        GPIO.output(13,False)
        GPIO.output(19,True)
        time.sleep(0.5)
        GPIO.output(19,False)
        GPIO.output(26,True)
        time.sleep(0.5)
        GPIO.output(26,False)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
#센서 인식되면 led 파란불이 켜지면서 콘솔에 출력하는 실습.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)   #LED 1 blue 연결
GPIO.setup(24,GPIO.IN)    #PIR 연결

try:
  while True:
    if GPIO.input(24) == True:
      GPIO.output(21,True)
      print("SENSOR ON!!")

    if GPIO.input(24) == False:
      GPIO.output(21,False)
      print("SENSOR OFF!!")

    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
finally:
  GPIO.cleanup()

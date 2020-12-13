#버튼 누르면 led 2개 파란색불이 들어오고 나가는 실습.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)                             #LED1 blue
GPIO.setup(26,GPIO.OUT)                             #LED2 blue
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)     #button
control=False
try:
 while True:
  button_state = GPIO.input(12)
  if button_state == False:  #button off
    if(control==True):       #True==button off
      control=False          #control off
    else:                    #False
      control=True           #control (on)
    print('button pressed')
  if control == True:        #control true (on)

    GPIO.output(21,True)
    time.sleep(0.1)
    GPIO.output(21,False)
    GPIO.output(26,True)
    time.sleep(0.1)
    GPIO.output(26,False)

  else:                      #control false (off)
    GPIO.output(21,False)    
    GPIO.output(26,False)
  time.sleep(0.2)

except KeyboardInterrupt:
  GPIO.cleanup()
finally:
  GPIO.cleanup() 

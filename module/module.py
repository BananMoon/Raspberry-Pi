import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def led_R():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(16,GPIO.OUT)
  GPIO.output(16,True)

def led_G():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(20,GPIO.OUT)
  GPIO.output(20,True)

def led_B():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(21,GPIO.OUT)
  GPIO.output(21,True)

def led_pwm_brightness():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    pwm_led = GPIO.PWM(16, 500)
    pwm_led.start(0)

    try:
     while True:
      for i in range(101):
       if(i==100):
         i=0
       pwm_led.ChangeDutyCycle(i)
       time.sleep(0.02)
    except KeyboardInterrupt:
      GPIO.output(16, False)
      GPIO.cleanup()
    
def led_blink():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT) # BCM 16번 출력으로 설정
    GPIO.setup(20,GPIO.OUT) # BCM 20번 출력으로 설정
    GPIO.setup(21,GPIO.OUT) # BCM 21번 출력으로 설정
    try:
      while True:
        GPIO.output(16,True) #16번 ON
        time.sleep(0.1)      #0.1초간 Delay
        GPIO.output(16,False) #16번 OFF
        time.sleep(0.1)
        GPIO.output(20,True)
        time.sleep(0.1)
        GPIO.output(20,False)
        time.sleep(0.1)
        GPIO.output(21,True)
        time.sleep(0.1)
        GPIO.output(21,False)
        time.sleep(0.1)
    except KeyboardInterrupt:
      GPIO.output(16, False)
      GPIO.output(20, False)
      GPIO.output(21, False)
      GPIO.cleanup()

def buzzer():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25,GPIO.IN)
    GPIO.setup(25,GPIO.OUT)
    
    def buzz():
      pitch = 1000
      duration=0.1
      period = 1.0/pitch
      delay=period/2
      cycles=int(duration*pitch)

      for i in range(cycles):
        GPIO.output(25,True)
        time.sleep(delay)
        GPIO.output(25,False)
        time.sleep(delay)
    buzz()

def sound():
    GPIO.setmode(GPIO.BCM)
    gpio_pin = 25
    scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
    GPIO.setup(gpio_pin, GPIO.OUT)
    list = [4, 4, 5, 5, 4, 4, 2, 4, 4, 2, 2, 1]
    try:
        p = GPIO.PWM(gpio_pin, 100)
        p.start(100)
        p.ChangeDutyCycle(90)
        for i in range(12):
            p.ChangeFrequency(scale[list[i]])
            if i == 6:
                time.sleep(1)
            else :
                time.sleep(0.5)
                p.stop()
    finally:
        GPIO.cleanup()
      
def led_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.OUT)     #led blue
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)     #button
    control=False
    try:
     while True:
      button_state = GPIO.input(12)
      if button_state == False: #버튼 누르면
        if(control==True): #제어 on상태면
          control=False  #제어 off
        else:
          control=True   #제어 off상태면 제어 on
        print('button pressed') 
      if control == True: #제어 on상태면(불을 켰다면)
        GPIO.output(21,True)
      else:               #제어 off상태면(불을 껐다면)
        GPIO.output(21,False)
      time.sleep(0.2)

    except KeyboardInterrupt:
      GPIO.output(21, False)
      GPIO.cleanup()

#버튼 누르면 led, 한번더 누르면 세 색깔이 blink
def blink_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT) # BCM 16번 출력으로 설정
    GPIO.setup(20,GPIO.OUT) # BCM 20번 출력으로 설정
    GPIO.setup(21,GPIO.OUT) # BCM 21번 출력으로 설정
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)#버튼
    check=False
    control=False
    
    try:
     while True:
      button_state = GPIO.input(12)
      if button_state == False: #버튼 누르면
        if(control==True): #제어 on상태면
          control=False  #제어 off
        else:
          control=True   #제어 off상태면 제어 on
        print('button pressed')
        
      if control == True: #제어 on상태면(불을 켰다면)
          if check==True: #눌린적이 있다면
              while True:
                  GPIO.output(16,True) #16번 ON
                  time.sleep(0.1)      #0.1초간 Delay
                  GPIO.output(16,False) #16번 OFF
                  time.sleep(0.1)
                  GPIO.output(20,True)
                  time.sleep(0.1)
                  GPIO.output(20,False)
                  time.sleep(0.1)
                  GPIO.output(21,True)
                  time.sleep(0.1)
                  GPIO.output(21,False)
                  time.sleep(0.1)
                  if button_state == False:
                        print('button pressed')
                        control=False
                        break
          if check==False:
                check=True
                GPIO.output(16,True)              
      else:               #제어 off상태면(불을 껐다면)
          GPIO.output(16,False)
          GPIO.output(20,False)
          GPIO.output(21,False)
      time.sleep(0.2)

    except KeyboardInterrupt:
      GPIO.output(16, False)
      GPIO.output(20, False)
      GPIO.output(21, False)
      GPIO.cleanup()

def led_pir():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)     #led red
    GPIO.setup(24,GPIO.IN)      #PIR

    try:
      while True:
        if GPIO.input(24) == True:
          GPIO.output(16,True)
          print("SENSOR ON!!")
        if GPIO.input(24) == False:
          GPIO.output(16,False)
          print("SENSOR OFF!!")
        time.sleep(1)
    except KeyboardInterrupt:
      GPIO.cleanup()

def blink_pir():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)     #led red
    GPIO.setup(24,GPIO.IN)      #PIR
    check=False
    
    try:
      while True:
        if GPIO.input(24) == True: #sensor켜지면
            if check == True:
                print("SENSOR ON!!")
                while True: #blink
                    GPIO.output(16,True) #16번 ON
                    time.sleep(0.1)      #0.1초간 Delay
                    GPIO.output(16,False) #16번 OFF
                    time.sleep(0.1)
                    GPIO.output(16,True) #16번 ON
                    time.sleep(0.1)      #0.1초간 Delay
                    GPIO.output(16,False) #16번 OFF
                    time.sleep(0.1)
                    GPIO.output(16,True) #16번 ON
                    time.sleep(0.1)      #0.1초간 Delay
                    GPIO.output(16,False) #16번 OFF
                    time.sleep(0.1)
                    if GPIO.input(24) == False:
                        print("SENSOR OFF!!")
                        break
            if check == False:  #sensor한번만 켜진 상태면
                print("SENSOR ON!!")
                check=True
                GPIO.output(16,True)
        if GPIO.input(24) == False: #sensor 꺼지면
            print("SENSOR OFF!!")
            #check=False
            GPIO.output(16, False)
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.output(16, False)
        GPIO.cleanup()
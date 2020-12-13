# 센서 인식되면 buzzer & led 1&2 blue 번갈아 깜빡 & lcd & camera on
# 버튼누르면 off
import RPi.GPIO as GPIO
import picamera                     #카메라
camera = picamera.PiCamera()
camera.resolution = (2592,1944)

from RPLCD.i2c import CharLCD         #LCD문자
lcd = CharLCD("PCF8574",0x27)         #LCD 설정                   
import time
import datetime                       #LCD에 시간표시할 용도
#DHT 설정
import Adafruit_DHT                   #온도센서(DHT)
dht_type = 11  #DHT 타입
bcm_pin = 23   #핀 번호

timer=0
intrusion_control=0

def buzz():                           #부저 설정.
  GPIO.setup(25,GPIO.OUT)
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
    
try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #버튼
        GPIO.setup(24,GPIO.IN)                              #PIR 모션감지
        GPIO.setup(21,GPIO.OUT)                            #LED1_Blue
        GPIO.setup(26,GPIO.OUT)                            #LED2_Blue
        if GPIO.input(24) == True:     #움직임이 감지되면
            print("SENSOR ON!!")
            while True:
                buzz()
                #LED 번갈아 깜빡
                GPIO.output(21,True)
                time.sleep(0.1)
                GPIO.output(21,False)
                GPIO.output(26,True)
                time.sleep(0.1)
                GPIO.output(26,False)
                GPIO.output(21,True)
                time.sleep(0.1)
                GPIO.output(21,False)
                GPIO.output(26,True)
                time.sleep(0.1)
                GPIO.output(26,False)
                    
                if  intrusion_control == 0:            #침범했으면 카메라on 
                    lcd.clear()
                    camera.capture("./camera/theif_face.jpg")  #theif_face.jpg라는 카메라 찍고
                    lcd.write_string('MOON YOON JI')           #LCD에 영문이름 출력
                    lcd.crlf()
                    lcd.write_string('201835652')              #LCD에 학번 출력
                    intrusion_control += 1            #침범상황에 신호이미 날렸다.는 의미 
                    
                if GPIO.input(12) == False:     #버튼을 누르면 모든걸 끝.
                    print("button pressed")
                    GPIO.cleanup()              #LED & buzzer off   
                    lcd.clear()                 #LCD 문구 없애고
                    
                    intrusion_control = 0       #침범상황 마무리한 상황 (다시 침범가능성on)
                    time.sleep(1)
                    break
                time.sleep(0.1)
        else:                                       #움직임이 감지되지 않으면
            GPIO.cleanup()                          #부저랑 LED off.
            #2초마다 온도 측정해서 출력 변경.timer를 놓지않으면 출력되기전에 계속 시간이 바뀜..
            if timer>2:
                timer=0                             #timer를 0으로 셋팅.
                lcd.clear()
                now = datetime.datetime.now()       #현재 시간
                nowTime = now.strftime('%H:%M:%S')  #현재 시각 Parsing
                humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)
                temp = str(round(temperature,1))
                print('Time:',nowTime,'Temp:',temp,'C')
                lcd.write_string(nowTime)
                lcd.crlf()
                lcd.write_string('TEMP ')
                lcd.write_string(temp)
                lcd.write_string('C ')
            timer+=0.1
            time.sleep(0.1)

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
finally:
    lcd.clear()
    GPIO.cleanup()
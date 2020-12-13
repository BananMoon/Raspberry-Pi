#dht를 이용하여 조건에 따른 led,lcd 변환.
from RPLCD.i2c import CharLCD         #LCD문자 import
import Adafruit_DHT                   #온도센서(DHT) import
import RPi.GPIO as GPIO               #LED import
import time

#LCD 설정
lcd = CharLCD('PCF8574',0x27)
#DHT 설정
dht_type = 11  #DHT 타입
bcm_pin = 23   #핀 번호
normal_temperature = 27

try:
    while True:
        time.sleep(3)
        lcd.clear()
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)
        humid = round(humidity,1)           #여기선 연산비교를 해야되서 str()하면 안됨.
        temp = round(temperature,1)
        print(temp,humid)                 #초기 : 콘솔에 현재 온/습도 출력
        GPIO.setmode(GPIO.BCM)            #LED 설정
        GPIO.setup(16,GPIO.OUT)           #LED1 red
        
        if normal_temperature<temp:       #일정 온도(27도)보다 높을 때
            lcd.write_string('201835652')       #학번 띄우고
            lcd.crlf()
            lcd.write_string('Need Cooling')    # 출력
            GPIO.output(16, True)               # LED1 red on
        else:                               #일정 온도 이하로 내려가면
            GPIO.cleanup()                  #LED off
            lcd.write_string('Temp ')       #현재 온/습도 띄우기
            lcd.write_string(str(temp))     #대신 lcd에 띄울때 str()해야함.
            lcd.write_string('C ')
            lcd.crlf()
            lcd.write_string('Humid ')
            lcd.write_string(str(humid))
            lcd.write_string('% ')
except KeyboardInterrupt:                  # 프로그램 종료 시 lcd차단, led화면 지움.
    GPIO.cleanup()
    lcd.clear()
    GPIO.setwarnings(False)
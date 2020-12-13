#dht를 이용해 습도,온도를 측정하고 lcd 화면에 표시하는 실습.
from RPLCD.i2c import CharLCD
import Adafruit_DHT
import time

dht_type = 11  # DHT 타입
bcm_pin = 23   # 핀 번호
lcd = CharLCD('PCF8574',0x27)

try:
    while True:
        time.sleep(3)
        lcd.clear()
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)  #read_retry(sensor, pin) : DHT 센서의 값을 읽어옴.
        humid = str(round(humidity,1))       #습도 소수점 1째자리에서 올림하고 문자화(str)
        temp = str(round(temperature,1))     #온도 소수점 1째자리에서 올림하고 문자화(str)
        print(temp,humid)             #콘솔에도 띄우기
        lcd.write_string('TEMP ')
        lcd.write_string(temp)      
        lcd.write_string('C ')        # ex) TEMP 36C
        lcd.crlf()                    # 한줄 띄움.
        lcd.write_string('HUMID ')
        lcd.write_string(humid)
        lcd.write_string('% ')        # ex) HUMID 80%
except KeyboardInterrupt:
    lcd.clear()                  #프로그램 종료 시 LCD 화면의 문자를 지우고 커서 위치 원상복귀.
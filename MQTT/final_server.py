import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import Adafruit_DHT                   #온도센서(DHT)
dht_type = 11
dht_pin = 23
import time

from RPLCD.i2c import CharLCD         #LCD문자 import
lcd = CharLCD('PCF8574',0x27)

try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)   #BUTTON
        time.sleep(1)
        lcd.clear()
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, dht_pin)
        temp = str(round(temperature,1))
        lcd.write_string('TEMP ')
        lcd.write_string(temp)
        lcd.write_string('C ')
        lcd.crlf()
        lcd.write_string('MOON YOON JI')
        time.sleep(1)
        if GPIO.input(12) == False:     #버튼을 누르면 흰색 LED2개 ON
            print("button pressed")
            #LED1
            GPIO.setup(16,GPIO.OUT)
            GPIO.setup(20,GPIO.OUT)
            GPIO.setup(21,GPIO.OUT)
            #LED2
            GPIO.setup(13,GPIO.OUT)
            GPIO.setup(19,GPIO.OUT)
            GPIO.setup(26,GPIO.OUT)            

            GPIO.output(16,True)
            GPIO.output(20,True)
            GPIO.output(21,True)
            GPIO.output(13,True)            
            GPIO.output(19,True)     
            GPIO.output(26,True)
            
except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
finally:
    lcd.clear()
    GPIO.cleanup()
    
            
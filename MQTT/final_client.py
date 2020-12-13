#RPi에 LCD-온도&이름표시 - button 누르면 server로 '시간','학번이름' publish
#pub으로부터 msg'on-학번' 수신-> led1,2 흰색 동시에 on. & server(pub)로 "LED-학번" publish
import paho.mqtt.client as mqtt
import time
import datetime
import Adafruit_DHT as dht
import json
import RPi.GPIO as GPIO

from RPLCD.i2c import CharLCD         #LCD문자 import
lcd = CharLCD('PCF8574',0x27)

GPIO.setwarnings(False)
dht_type = 11
dht_pin = 23

#Define Variables
MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "/CCL/IoTP-UP"

#Define on_publish event function
def on_publish(client, userdata, mid):
    print("Message Published...")
    
def on_connect(client, userdata, flags, rc):
    print("Connect with result code"+str(rc))
    client.subscribe("/CCL/IoTP-DN")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))  #서버로부터 받은 msg.
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)
    if (msg.payload.decode('utf-8')=="on-201835652"):      #'on-학번'msg 받으면 흰색 LED2개 on
        GPIO.output(16,True)
        GPIO.output(20,True)
        GPIO.output(21,True)
        GPIO.output(13,True)            
        GPIO.output(19,True)
        GPIO.output(26,True)
        data = {'LED-201835652'}
        client.publish(MQTT_TOPIC, str(data))               # 서버로 "LED-학번"전송
    else:
        GPIO.cleanup()
         
# Initiate MQTT Client
client = mqtt.Client()
# Register publish callback function
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message

# Connect with MQTT Broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()

try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)   #BUTTON
        humidity, temperature = dht.read_retry(dht_type, dht_pin)
        
        if humidity is not None and temperature is not None:
            time.sleep(1)
            lcd.clear()
            temp = str(round(temperature,1))
            lcd.write_string('TEMP ')
            lcd.write_string(temp)
            lcd.write_string('C ')
            lcd.crlf()
            lcd.write_string('MOON YOON JI')
            if GPIO.input(12) == False:         #버튼을 누르면 시간&학번이름 전송
                print("button pressed")            
                now = datetime.datetime.now()   #현재 시간
                nowTime = now.strftime('%H:%M:%S')  #현재 시각 Parsing
                data = {'time':'nowTime', 'name':'201835652 moonyoonji'}
                client.publish(MQTT_TOPIC, str(data))          #publish msg
            print('Published.Sleeping...')
        else:
            print('Failed to get reading. Skipping...')
except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
finally:
    GPIO.cleanup()
    lcd.clear()



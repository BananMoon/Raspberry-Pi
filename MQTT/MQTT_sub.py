#subscribe는 구독한 서버로부터 topic으로 publish가 발행됐을때 broker로부터 그 topic을 가져와. 가져오면 뜨는 함수
#on_connect : 연결됐을때 호출.  on_message : publish message
#토픽명으로 구독하고,  #client.subscribe("토픽명:)
#publish와 연결되면 뜨는 함수,  on_connect
#publish로부터 메시지 받으면 호출되는 함수를 정의하고   on_message()
#브로커에 연결!      client.connect("localhost",1883,60)

import paho.mqtt.client as mqtt

#서버로부터 CONNTACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("IOT-P") #구독 "IOT-P"
    
#서버로부터 publish message를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))  #토믹과 메시지를 출력한다.
    
client = mqtt.Client() #client 오브젝트 생성
client.on_connect = on_connect   #콜백설정
client.on_message = on_message   #콜백 설정

client.connect("localhost",1883, 60) #라즈베리파이3 MQTT 브로커에 연결
client.loop_forever()

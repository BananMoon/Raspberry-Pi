import paho.mqtt.client as mqtt

mqtt = mqtt.Client("MQTT_pub")
mqtt.connect("localhost", 1883)

mqtt.publish("IOT-P", "led ON!") #IoT-P 토픽으로 message publish
mqtt.publish("IOT-P", "led off")

mqtt.loop(2)
### Raspberry-Pi 3b+  (Practice using raspberry pi)

* led_RGB.py              : led red,green,blue on

* led_pwm_brightness.py   : led brightness

* led_pir.py              : pir 센서인식하면 led on

* ledblink_button.py      : button 누르면 led blink

* lcd_temp.py             : dht(온/습도센서)로 lcd에 출력

* lcd_temp_led.py         : dht & led & lcd 이용

* camera_button_capture.py: button 누르면 camera on

* Smart_Home_System.py    : pir 센서 인식되면 led&camera&lcd&buzzer 작동 -> button 누르면 off.

* module  : 함수를 정의한 file을 import하여 keyboard input으로 제어하는 실습.
  * module.py   : 함수 정의 파일
  * Keyboard_Control.py   : module.py를 import하여 RPi 제어하는 파일
  
* MQTT    : 발행-구독 기반의 메시징 프로토콜 이용한 실습.
  * MQTT_pub.py       : publishier(just send)
  * MQTT_sub.py       : subscriber(just subscribe&receive)
  * final_server.py   : publishier(RPi동작 포함)
  * final_client.py   : subscriber(RPi동작 포함)

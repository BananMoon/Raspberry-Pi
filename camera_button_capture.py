#버튼 누르면 카메라 on.
import picamera
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)     #button
camera = picamera.PiCamera()
camera.resolution = (2592,1944)  #최대 해상도 2592 x 1944
try:
    while True:                  #무한 루프
        button_state = GPIO.input(12)    #버튼 상태 변수
        if button_state == False:  #버튼이 눌리면 False
            print('button pressed')
            time.sleep(2)
            camera.capture('./camera/example3.jpg')  #찍힌 사진이 저장될 경로를 지정하여 찍음.
            break
    time.sleep(0.2)               #0.2초마다 버튼이 눌렸는지 감지

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
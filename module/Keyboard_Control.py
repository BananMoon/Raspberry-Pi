# module01.py를 import하여 키보드로 제어하는 실습.
import RPi.GPIO as GPIO
import time
import module01

while True:
    sel = input("Select option (R:Red On, G:Green On, B:Blue On, M:Bright Control,X:Led Blink, Bz:Buzzer On, S:Sound, BL:Button Press&Led, P:PIR&led, PB:PIR&Blink, O:All Off):")

    if (sel =='R'):
        module01.led_R()       #led red on
    if (sel=='G'):
        module01.led_G()       #led green on
    if (sel == 'B'):
        module01.led_B()       #led blue on
    if (sel == 'M'):
        module01.led_pwm_brightness()       #led red 점점 밝게
    if (sel == 'X'):
        module01.led_blink()   #led RGB blink
    if (sel == 'Bz'):
        module01.buzzer()      #buzzer on
    if (sel == 'S'):
        module01.sound()       #sound on (멜로디)
    if (sel == 'BL'):
        module01.led_button()  #버튼으로 led blue 제어
    if (sel == 'BB'):
        module01.blink_button() #button으로 led RGB blink 제어
    if (sel == 'P'):
        module01.led_pir()      #센서인식하면 led red on
    if (sel == 'PB'):
        module01.blink_pir()    #센서인식하면 led red blink
    if (sel == 'O'):
        GPIO.cleanup()          #all off

GPIO.cleanup()


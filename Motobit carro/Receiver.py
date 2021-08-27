from microbit import *
from motobit import *
import radio

radio.on()

while True:
        if button_a.is_pressed():
            Motor.enable()
            motor_left.set_speed(100)
            motor_right.set_speed(100)
            sleep(1000)
            motor_left.set_speed(100, Motor.REVERSE)
            motor_right.set_speed(100)
            sleep(200)
            motor_left.set_speed(100)
            motor_right.set_speed(100)
            sleep(1000)
            Motor.disable()
            
        

        l = motor_left
        r = motor_right

        if radio.receive() == 'left':
        
            l.set_speed(25)
            r.set_speed(50)
            sleep(1000)
            
        
        if radio.receive() == 'front':
            
            l.set_speed(50)
            r.set_speed(50)
            
        
        if radio.receive() == 'right':
            l.set_speed(50)
            r.set_speed(25)

        

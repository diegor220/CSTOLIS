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
        
            Motor.enable()
            l.set_speed(150)
            r.set_speed(100)
            sleep(1)
            Motor.disable()
            
        
        if radio.receive() == 'front':
            
            Motor.enable()
            l.set_speed(150)
            r.set_speed(150)
            sleep(1)
            Motor.disable()
            
        
        if radio.receive() == 'right':
            
            Motor.enable()
            l.set_speed(100)
            r.set_speed(150)
            sleep(1)
            Motor.disable()
            

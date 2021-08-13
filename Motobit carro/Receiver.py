from microbit import *
import radio

while True:
    radio.on()

    motobit = MotoBit()

    motobit.enable() # Enable motor driver
    
    l = motobit.left_motor() # Acquire motor object
    r = motobit.right_motor(invert=True) # Enable invert polarity
    
    
    if radio.receive("left"):
        l.forward(25)
        r.reverse(50)
        
    if radio.receive("front"):
        l.forward(50)
        r.reverse(50)
    
    if radio.receive("right"):
        l.forward(50)
        r.reverse(25)

from microbit import *
import radio

while True:
    moviex = accelerometer.get_x()
    
    radio.on()
    
    if -1024<moviex<-342 and button_a.is_pressed() :
        radio.send("left")
    
    if -341<moviex<341 and button_a.is_pressed():
        radio.send("front")
    
    if 342<moviex<1024 and button_a.is_pressed():
        radio.send("right")

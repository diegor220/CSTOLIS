from microbit import *

while True:
    moviex = accelerometer.get_x()
    moviey = accelerometer.get_y()
    if button_a.is_pressed():
        print (moviex)
        
    if button_b.is_pressed():
        print (moviey)
        
    pointx=2
    pointy=2
    
    if -1024<moviex<-513:
        pointx=0
    elif -512<moviex<-46:
        pointx=1
    elif -45<moviex<45:
        pointx=2
    elif 46<moviex<511:
        pointx=3
    elif 512<moviex<1024:
        pointx=4
        
    if -1024<moviey<-513:
        pointy=0
    elif -512<moviey<-46:
        pointy=1
    elif -45<moviey<45:
        pointy=2
    elif 46<moviey<511:
        pointy=3
    elif 512<moviey<1024:
        pointy=4
        
    
    display.set_pixel(pointx,pointy,9)
    display.clear()
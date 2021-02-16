# Tomas de Camino Beck with slight editions by Diego Rodríguez
#CS course with Pyhton

# Simple press button code that shows binary numbers and does a parity check as well

# button list
# list is organized [x,y,size, True/False]

buttons = [
           [10,10,50,False,128,1],
           [60,10,50, False,64,1],
           [110,10,50, False,32,1],
           [160,10,50, False,16,1],
           [210,10,50, False,8,1],
           [260,10,50, False,4,1],
           [310,10,50, False,2,1],
           [360,10,50, False,1,1],
           ]




def setup():
    size(500, 500)


def draw():
    background(0)
    stroke(200)
    global buttons
    c=0
    d=0
    check= 0
    # draw buttons
    for button in buttons:
        if button[3]:
            fill(255)
            
            c= c+button[4]
            d= d+button[5]
            check= d & 1
            
            
        else:
            fill(0)
        rect(button[0], button[1], button[2], button[2])
        if check == 1:
            fill (225)
        else:
            fill (0)
        rect(430,10,50,50)
    fill(255)
    text(c,212,212)
    text(check,442,212)
           

# event that is triggered when mouse button pressed
def mousePressed():
    pressButtons() 
    
# check if mouse is over a button
def pressButtons():
    global buttons
    for button in buttons:
        if (button[0]< mouseX < (button[0]+button[2]) and button[1]< mouseY < (button[1]+button[2])):
            button[3] = not button[3]

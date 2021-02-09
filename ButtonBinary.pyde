# Tomas de Camino Beck with slight editions by Diego Rodríguez
#CS course with Pyhton

# Simple press button code

# button list
# list is organized [x,y,size, True/False]

buttons = [
           [10,10,50,False,8],
           [60,10,50, False,4],
           [110,10,50, False,2],
           [160,10,50, False,1]
           ]




def setup():
    size(300, 300)


def draw():
    background(0)
    stroke(200)
    global buttons

    # draw buttons
    for button in buttons:
        if button[3]:
            fill(255)
            c=0
            c= c+button[4]
            fill(255)
            text(c,150,150)
        else:
            fill(0)
        rect(button[0], button[1], button[2], button[2])
 
           

# event that is triggered when mouse button pressed
def mousePressed():
    pressButtons() 

# check if mouse is over a button
def pressButtons():
    global buttons
    for button in buttons:
        if (button[0]< mouseX < (button[0]+button[2]) and button[1]< mouseY < (button[1]+button[2])):
            button[3] = not button[3]

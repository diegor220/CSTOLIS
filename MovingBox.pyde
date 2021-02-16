# Tomas de Camino Beck with slight changes by Diego Rodríguez
# UG: program dinamical objects and interaction, simulation physics

posX = 200
posY = 200
speedX = 0
speedY = 0

rocks= [
        [600,300,200]
        ]
       
def keyPressed():
    global speedX, speedY
    print(keyCode)
    if keyCode == 68:
        speedX *= 1.1
        speedY *= 1.1
        
    if keyCode == 65:
        speedX *= 0.9
        speedY *= 0.9
     
    if keyCode == UP:
        speedX = 0
        speedY = -8

    elif keyCode == DOWN:
        speedX = 0
        speedY = 8
  

    elif keyCode == LEFT:
        speedX = -8
        speedY = 0

    elif keyCode == RIGHT:
        speedX = 8
        speedY = 0
   
def setup():
    size(1200,600)
    frameRate(30)
    background(0)
    noStroke()
    rectMode(CENTER)
    #ernest = createFont('Ernest.ttf', 30)
    #textFont(ernest)
    #rectMode(CENTER)


def draw():
    global posX, posY, speedX, speedY,rocks
    posX += speedX
    posY += speedY
    
    if posX<0 or posX>width :
        speedX*=-1
            

    if posY<0 or posY>height :
        speedY*=-1

       
        
    fill(0,160)
    rect(width/2,height/2, width/2,height/2)

    fill('#FFFFFF')
    rect(posX, posY, 10, 10)
    
    for rock in rocks:
        fill(180)
        rect(rock[0],rock[1],rock[2],rock[2])
        
        if dist(posX,posY,rock[0],rock[1])<rock[2]-rock[2]/2:
            speedX*=-1
            speedY*=-1
    
            

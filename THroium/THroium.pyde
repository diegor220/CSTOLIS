import random

class Neutron (object):
    def __init__ (self):
        self.posx=0
        self.speedx=1
        self.speedy= random.uniform(-0.5,0.5)
        self.posy= random.uniform(200,300)
        self.c=color(225)
        self.inversey=self.posy*-1
    
    def move(self):
        self.posx+=self.speedx
        self.posy+=self.speedy
    
    def display(self):
        ellipseMode(CENTER)
        fill (self.c)
        ellipse(self.posx,self.posy,10,10)
    
    def collision(self,atom):
        if dist(self.posx,self.posy,atom.x,atom.y)<25:
            self.ballpass = True
            

            
            
        
        

class Atom (object):
    def __init__ (self):
        self.x= random.randint(100,360)
        self.y= random.randint(100,360)
        self.c= "#0FFFD5"
    def display (self):
        ellipseMode(CENTER)
        fill (self.c)
        ellipse(self.x,self.y, 40,40)
        
    def collision (self,neut):
        if dist(self.x,self.y,neut.posx,neut.posy)<25:
            self.c = "#CA0FFF"
        
myneut= [Neutron(),Neutron(),Neutron(),Neutron()]
myatom= [Atom(),Atom(),Atom(),Atom()]


def setup():
    size (500,500)
    background(0)

def draw():
    fill(0,125)
    rect(0,0, width,height)
        
    for neut in myneut:
        neut.move()
        neut.display()
        for atom in myatom:
            if dist (neut.posx,neut.posy,atom.x,atom.y)<25:
                ellipse(neut.posx ,10,10)
            
            
    for atom in myatom:
#       for neut in myneut:
#           atom.collision(neut)
#           
       atom.display()

       
        
        
        
   

        
    
    

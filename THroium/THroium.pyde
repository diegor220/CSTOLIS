import random

class Neutron (object):
    def __init__ (self):
        self.posx=0
        self.speedx=1
        self.speedy= random.uniform(-0.5,0.5)
        self.posy= random.uniform(200,300)
        self.posy2= self.posy
        self.c=color(225)
        self.block= False
   
    def move(self):
        self.posx+=self.speedx
        self.posy+=self.speedy
        if self.block:
           self.posy2+=-self.speedy
   
    def display(self):
        ellipseMode(CENTER)
        fill (self.c)
        ellipse(self.posx,self.posy,10,10)
        if self.block:
          ellipse(self.posx,self.posy2,10,10)  
   
    def collision(self,atom):
        pass
         
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
        if dist(self.x,self.y,neut.posx,neut.posy)<27 :
            self.c = "#CA0FFF"
            neut.block = True
        if neut.block == True:
            if dist(self.x,self.y,neut.posx,neut.posy2)<27 :
                self.c = "#CA0FFF"
            
myneut= [Neutron()]
myatom= [Atom(),Atom(),Atom(),Atom(),Atom(),Atom(),Atom(),Atom(),Atom(),Atom(),Atom(),Atom()]


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
       for neut in myneut:
           atom.collision(neut)
           
       atom.display()

    
        
        
        


        
    
    

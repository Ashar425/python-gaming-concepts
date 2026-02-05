import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

screen.fill("white")

class myCircle():
    def __init__(self,color,pos,rad,wid=0):
        self.color=color
        self.pos=pos
        self.rad=rad
        self.wid=wid
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.rad,self.wid)

    def grow(self,x):
        self.rad= self.rad+x
        pygame.draw.circle(self.screen,self.color,self.pos,self.rad,self.wid)

position=(300,300)
radius=50
wid=2
pygame.draw.circle(screen,"red",position,radius,wid)
pygame.display.update()

blueCircle=myCircle("darkblue",position,radius+60)
redCircle=myCircle("darkred",position,radius+40)
yellowCircle=myCircle("yellow",position,radius,5)
greenCircle=myCircle("darkgreen",position,radius,20)

while(1):
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            blueCircle.grow(2)
            redCircle.grow(2)
            yellowCircle.grow(2)
            greenCircle.grow(2)
            pygame.display.update()
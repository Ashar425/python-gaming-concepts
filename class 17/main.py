import pygame
import sys

pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()

class ShapeDrawer():
    def __init__(self,screen):
        self.screen=screen
        self.shapes=[]

    def add_rectangle(self):
        self.shapes.append(("rect", pygame.Rect(200,150,200,100)))

    def add_circle(self):
        self.shapes.append(("circle",(400,300,60)))

    def add_line(self):
        self.shapes.append(("line",((100,500),(500,700))))

    
    def draw(self):
        for shape in self.shapes:
            if shape[0]=="rect":
                pygame.draw.rect(self.screen,"turquoise",shape[1],2)

            elif shape[0]=="circle":
                x,y,r=shape[1]
                pygame.draw.circle(self.screen,"cyan",(x,y),r,2)
            
            elif shape[0]=="line":
                start,end=shape[1]
                pygame.draw.line(self.screen,"teal",start,end,3)

class Game:
    def __init__(self):
        self.drawer=ShapeDrawer(screen)

    def run(self):
        while True:
            screen.fill("black")

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        self.drawer.add_rectangle()
                    elif event.key==pygame.K_c:
                        self.drawer.add_circle()
                    elif event.key ==pygame.K_l:
                        self.drawer.add_line()

            self.drawer.draw()
            pygame.display.update()
            clock.tick(60)

Game().run()

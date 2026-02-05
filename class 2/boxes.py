#importing the modules
import pgzrun
from random import randint

#making width and height
WIDTH=300
HEIGHT=300


#making a function for dranwing the program
def draw():
    r=255
    g=125
    b=randint(120,255)
    screen.fill("black")
    width=WIDTH
    height=HEIGHT-200

#repeting the draw part from the function
    for i in range(20):
        rect=Rect((0,0),(width,height))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))

        r=r-10
        g+=2
        width=width-10
        height=height+10


pgzrun.go()
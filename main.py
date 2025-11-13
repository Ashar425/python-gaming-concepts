import pgzrun
import random

HEIGHT=500
WIDTH=800

def mrect():
    w=random.randint(10,200)
    h=random.randint(10,100)

    x=random.randint(0,WIDTH-w)
    y=random.randint(0,HEIGHT-h)

    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)

    return Rect(x,y,w,h),color


def draw():
    screen.fill("black")
    for i in range(25):
        rect,color=mrect()

        screen.draw.filled_rect(rect,color)

pgzrun.go()
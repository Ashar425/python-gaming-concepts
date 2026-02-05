import pgzrun
import random
import time

WIDTH=600
HEIGHT=600

score=0
timer=0
game_over=False

honey=Actor("honey")
honey.pos=200,200

winnie=Actor("winnie")
winnie.pos=100,100

def draw():
    screen.blit("landskape",(0,0))
    honey.draw()
    winnie.draw()
    screen.draw.text("scores: "+str(score),color="black",topleft=(10,10))
    screen.draw.text("timer: "+str(timer),color="black",topleft=(10,30))

def update():
    global score,timer
    timer=timer+0.05

    if keyboard.left:
        winnie.x=winnie.x-2
    if keyboard.right:
        winnie.x=winnie.x+2
    if keyboard.up:
        winnie.y=winnie.y-2
    if keyboard.down:
        winnie.y=winnie.y+2

    honey_collected=winnie.colliderect(honey)
    if honey_collected:
        score=score+2

        honey_pos()

def honey_pos():
    honey.x=random.randint(50,550)
    honey.y=random.randint(50,550)

pgzrun.go()
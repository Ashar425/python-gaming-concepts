import pgzrun 
from random import randint

WIDTH=600
HEIGHT=500

score=0
game_over=False

cheese=Actor("cheese")
cheese.pos=200,200

mouse=Actor("mouse")
mouse.pos=100,100

def draw():
    screen.blit("sky",(0,0))
    cheese.draw()
    mouse.draw()
    screen.draw.text("scores: "+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Time is up! Your final score: "+str(score),midtop=(WIDTH/2,10),fontsize=40,color="violet")

def place_cheese():
    cheese.x=randint(50,(WIDTH-50))
    cheese.y=randint(50,(HEIGHT-50))

def time_up():
    global game_over
    game_over=True

def update():
    global score

    if keyboard.left:
        mouse.x=mouse.x-2
    if keyboard.right:
        mouse.x=mouse.x+2
    if keyboard.up:
        mouse.y=mouse.y-2
    if keyboard.down:
        mouse.y=mouse.y+2

    cheese_collected=mouse.colliderect(cheese)

    if cheese_collected:
        score=score+10
        place_cheese()

clock.schedule(time_up,60.0)

pgzrun.go()
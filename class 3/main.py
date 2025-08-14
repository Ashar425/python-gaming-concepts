import pgzrun
from random import randint

TITLE="Good shot"
WIDTH=500
HEIGHT=500

message=""

balloon=Actor("balloon")

def draw():
    screen.clear()
    screen.fill("black")
    balloon.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

def place_balloon():
    balloon.x=randint(50,WIDTH-50)
    balloon.y=randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if balloon.collidepoint(pos):
        message="good shot"
        place_balloon()
    else:
        message="you missed"

place_balloon()
pgzrun.go()
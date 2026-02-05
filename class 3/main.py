#importing modules
import pgzrun
from random import randint

#creating width and height
TITLE="Good shot"
WIDTH=500
HEIGHT=500

message=""

balloon=Actor("balloon")

#creating draw function
def draw():
    screen.clear()
    screen.fill("black")
    balloon.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

#creating balloon funktion
def place_balloon():
    balloon.x=randint(50,WIDTH-50)
    balloon.y=randint(50,HEIGHT-50)

#creating the mouse collision function
def on_mouse_down(pos):
    global message
    if balloon.collidepoint(pos):
        message="good shot"
        place_balloon()
    else:
        message="you missed"

#running the program
place_balloon()
pgzrun.go()
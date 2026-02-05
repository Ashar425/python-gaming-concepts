import pgzrun

WIDTH = 300
HEIGHT = 300
def draw():
    w=WIDTH  -100
    h=HEIGHT -100

    for i in range(20):
        r = Rect((0,0),(w,h))
        r.center=150,150
        screen.draw.rect(r,"yellow")        
        w=w-10
        h=h-10

pgzrun.go()
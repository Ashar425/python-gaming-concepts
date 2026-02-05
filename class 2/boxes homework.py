import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 125
    b = randint(120, 255)
    screen.fill("black")

    width = WIDTH
    height = HEIGHT - 200
    cx, cy = 150, 150  

    for i in range(20):
        points = [
            (int(cx),           int(cy - height / 2)),   
            (int(cx - width/2), int(cy + height / 2)),  
            (int(cx + width/2), int(cy + height / 2)),
        ]

        try:
            screen.draw.polygon(points, (r, g, b))
        except AttributeError:
            import pygame
            pygame.draw.polygon(screen.surface, (r, g, b), points, 1)

        r = max(0, r - 10)
        g = min(255, g + 2)
        width -= 10
        height += 10

pgzrun.go()

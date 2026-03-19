import pygame

pygame.init()

WIDTH=800
HEIGHT=800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("basic 1")
r1=pygame.Rect(300,300,20,20)
r2=pygame.Rect(500,500,10,10)
points=[[70,10],[30,100],[100,100]]
points2=[[200,10],[300,110],[300,180],[100,180],[100,110]]
points3=[[650,120],[685,132],[708,160],[708,195],[685,223],[650,235],[615,223],[592,195],[592,160],[615,132]]
spaceship_image=pygame.image.load("class 24\spaceship.png").convert_alpha()
car_image=pygame.image.load("class 24\car.png").convert_alpha()
sword_image=pygame.image.load("class 24\Sword.png").convert_alpha()
r3=pygame.Rect(600,600,50,50)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.draw.rect(screen,"green",r1)
    pygame.draw.rect(screen,"yellow",r2)
    pygame.draw.circle(screen,"red",(200,200),50)
    pygame.draw.polygon(screen,"purple",points)
    pygame.draw.polygon(screen,"white",points2)
    pygame.draw.polygon(screen,"turquoise",points3)
    pygame.draw.circle(screen,"orange",(200,500),75)
    screen.blit(spaceship_image,r3)
    screen.blit(car_image,r2)
    screen.blit(sword_image,r1)
    pygame.display.update()

pygame.quit()
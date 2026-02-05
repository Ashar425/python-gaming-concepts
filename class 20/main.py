import pygame

pygame.init()

WIDTH=800
HEIGHT=600

PLAYER_W=150
PLAYER_H=150

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket Launcher")

clock=pygame.time.Clock()
FPS=60

bg_img=pygame.image.load("class 20/images/space.jpg")
bg_img=pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

ch_img=pygame.image.load("class 20/images/rocket.png")
ch_img=pygame.transform.scale(ch_img,(PLAYER_W,PLAYER_H))

player_x=225
player_y=225
speed=5

keys=[False,False,False,False]

gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    
    screen.blit(bg_img,(0,0))
    pygame.display.update()
    clock.tick(FPS)




pygame.quit()
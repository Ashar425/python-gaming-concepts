import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Suprise Cards")

font=pygame.font.SysFont("Comic Sans MS", 40)

img=pygame.image.load("class 19/images/m1.jpg")
img=pygame.transform.scale(img,(WIDTH,HEIGHT))

img2=pygame.image.load("class 19/images/m2.jpg")
img2=pygame.transform.scale(img2,(WIDTH,HEIGHT))

img3=pygame.image.load("class 19/images/fathers day 1.jpg")
img3=pygame.transform.scale(img3,(WIDTH,HEIGHT))

img4=pygame.image.load("class 19/images/fathers day 2.jpg")
img4=pygame.transform.scale(img4,(WIDTH,HEIGHT))

img5=pygame.image.load("class 19/images/cool 1.jpg")
img5=pygame.transform.scale(img5,(WIDTH,HEIGHT))

img6=pygame.image.load("class 19/images/cool 2.jpeg")
img6=pygame.transform.scale(img6,(WIDTH,HEIGHT))


while True:

    """t1=font.render("Happy",True,"pink")
    t2=font.render("Mothers Day",True,"pink")

    t3=font.render("Your The",True,"purple")
    t4=font.render("Best Mom",True,"purple")

    t5=font.render("Happy",True,"darkblue")
    t6=font.render("Fathers Day",True,"darkblue")

    t7=font.render("Your The",True,"turquoise")
    t8=font.render("Best Dad",True,"turquoise")

    t9=font.render("I Am",True,"green")
    t10=font.render("The Best",True,"green")

    t11=font.render("I Am",True,"white")
    t12=font.render("Very Smart",True,"White")"""

    screen.blit(img,(0,0))
   # screen.blit(t1,(400,400))
    time.sleep(2)
    
    screen.blit(img2,(0,0))
    time.sleep(2)

    screen.blit(img3,(0,0))
    time.sleep(2)

    screen.blit(img4,(0,0))
    time.sleep(2)

    screen.blit(img5,(0,0))
    time.sleep(2)

    screen.blit(img6,(0,0))
    time.sleep(2)

    pygame.display.update()
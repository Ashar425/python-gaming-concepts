import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Birthday Card")

img=pygame.image.load("C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday1.jpg")
img=pygame.transform.scale(img,(WIDTH,HEIGHT))

while True:
    font=pygame.font.SysFont("Comic Sans MS",40)
    t1=font.render("Happy",True,"pink")
    t2=font.render("Birthday",True,"skyblue")
    screen.blit(img,(0,0))
    screen.blit(t1,(300,250))
    screen.blit(t2,(280,290))

    pygame.display.update()
    time.sleep(2)
    
    img1=pygame.image.load("C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday2.jpg")
    img1=pygame.transform.scale(img1,(WIDTH,HEIGHT))

    t3=font.render("Have A",True,"purple")
    t4=font.render("Great Day",True,"blue")
    screen.blit(img1,(0,0))
    screen.blit(t3,(300,250))
    screen.blit(t4,(300,290))

    pygame.display.update()
    time.sleep(2)

    img3=pygame.image.load("C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday3.jpg")
    img3=pygame.transform.scale(img3,(WIDTH,HEIGHT))

    t5=font.render("May You",True,"yellow")
    t6=font.render("Live Long",True,"orange")
    screen.blit(img3,(0,0))
    screen.blit(t5,(300,250))
    screen.blit(t6,(310,290))

    pygame.display.update()
    time.sleep(2)

    img4=pygame.image.load("C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday4.jpg")
    img4=pygame.transform.scale(img4,(WIDTH,HEIGHT))

    t7=font.render("May Your Wishes",True,"purple")
    t8=font.render("Become True",True,"pink")
    screen.blit(img4,(0,0))
    screen.blit(t7,(270,250))
    screen.blit(t8,(320,290))
    
    pygame.display.update()
    time.sleep(2)
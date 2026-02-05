import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Card")

font = pygame.font.SysFont("Comic Sans MS", 40)

balloon = pygame.image.load(
    "C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/balloon1.png"
)
balloon = pygame.transform.scale(balloon, (80, 120))

while True:

    img = pygame.image.load(
        "C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday1.jpg"
    )
    img = pygame.transform.scale(img, (WIDTH, HEIGHT))

    t1 = font.render("Happy", True, "pink")
    t2 = font.render("Birthday", True, "skyblue")

    balloon_y = HEIGHT

    for i in range(100):
        screen.blit(img, (0, 0))
        screen.blit(t1, (300, 250))
        screen.blit(t2, (280, 290))
        screen.blit(balloon, (50, balloon_y))

        balloon_y -= 3
        pygame.display.update()
        time.sleep(0.03)

    time.sleep(1)

    img2 = pygame.image.load(
        "C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday2.jpg"
    )
    img2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))

    t3 = font.render("Have A", True, "purple")
    t4 = font.render("Great Day", True, "blue")

    balloon_y = HEIGHT

    for i in range(100):
        screen.blit(img2, (0, 0))
        screen.blit(t3, (300, 250))
        screen.blit(t4, (300, 290))
        screen.blit(balloon, (50, balloon_y))

        balloon_y -= 3
        pygame.display.update()
        time.sleep(0.03)

    time.sleep(1)

    img3 = pygame.image.load(
        "C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday3.jpg"
    )
    img3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))

    t5 = font.render("May You", True, "yellow")
    t6 = font.render("Live Long", True, "orange")

    balloon_y = HEIGHT

    for i in range(100):
        screen.blit(img3, (0, 0))
        screen.blit(t5, (300, 250))
        screen.blit(t6, (310, 290))
        screen.blit(balloon, (50, balloon_y))

        balloon_y -= 3
        pygame.display.update()
        time.sleep(0.03)

    time.sleep(1)

    img4 = pygame.image.load(
        "C:/Users/gulqa/OneDrive/Desktop/programing gaming concept/class 18/birthday4.jpg"
    )
    img4 = pygame.transform.scale(img4, (WIDTH, HEIGHT))

    t7 = font.render("May Your Wishes", True, "purple")
    t8 = font.render("Become True", True, "pink")

    balloon_y = HEIGHT

    for i in range(100):
        screen.blit(img4, (0, 0))
        screen.blit(t7, (270, 250))
        screen.blit(t8, (320, 290))
        screen.blit(balloon, (50, balloon_y))

        balloon_y -= 3
        pygame.display.update()
        time.sleep(0.03)

    time.sleep(2)

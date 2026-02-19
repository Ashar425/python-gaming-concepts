import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_W = 150
PLAYER_H = 150
FPS = 60
speed = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Honey Bee")
clock = pygame.time.Clock()

def load_image(path, size):
    try:
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, size)
        return img
    except:
        surf = pygame.Surface(size, pygame.SRCALPHA)
        surf.fill((255, 255, 0, 180))
        return surf

bg_img = load_image("class 21/park.jpg", (WIDTH, HEIGHT))
ch_img = load_image("class 21/bee.png", (PLAYER_W, PLAYER_H))

player_x = 225
player_y = 225

keys = [False, False, False, False]

gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[1] = True
            if event.key == pygame.K_LEFT:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[1] = False
            if event.key == pygame.K_LEFT:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]:
        player_y -= speed
    if keys[1]:
        player_y += speed
    if keys[2]:
        player_x -= speed
    if keys[3]:
        player_x += speed

    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - PLAYER_W:
        player_x = WIDTH - PLAYER_W
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - PLAYER_H:
        player_y = HEIGHT - PLAYER_H

    screen.blit(bg_img, (0, 0))
    screen.blit(ch_img, (player_x, player_y))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

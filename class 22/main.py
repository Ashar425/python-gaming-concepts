import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Connect the game")

font=pygame.font.SysFont("Comic Sans MS",30)

subway=pygame.image.load("class 22/images/subway surfers.jpg")
subway=pygame.transform.scale(subway,(50,50))
minecraft=pygame.image.load("class 22/images/minecraft.png")
minecraft=pygame.transform.scale(minecraft,(50,50))
block=pygame.image.load("class 22/images/block blast.png")
block=pygame.transform.scale(block,(50,50))
tempel=pygame.image.load("class 22/images/tempel run.jpg")
tempel=pygame.transform.scale(tempel,(50,50))

text=[("Block Blast",(350,120)),("Minecraft",(350,220)),("Subway Surfers",(350,320)),("Tempel Run",(350,420))]
lines=[]
start_pos=lines

def draw_screen():
    screen.fill("black")
    screen.blit(subway,(150,100))
    screen.blit(block,(150,200))
    screen.blit(minecraft,(150,300))
    screen.blit(tempel,(150,400))

    for t,p in text:
        img=font.render(t,True,"red")
        screen.blit(img,p)

    for line in lines:
        pygame.draw.line(screen,"blue",line[0],line[1],5)
        pygame.draw.circle(screen,"white",line[0],20,2)
        pygame.draw.circle(screen,"white",line[1],20,2)
        
    pygame.display.update()

clock=pygame.time.Clock()
FPS=60

running=True
while running:
    draw_screen()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            start_pos=pygame.mouse.get_pos()
        elif event.type==pygame.MOUSEBUTTONUP:
            if start_pos is not None:
                end_pos=pygame.mouse.get_pos()
                lines.append((start_pos,end_pos))
                start_pos=None
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
import pgzrun
import random

HEIGHT = 500
WIDTH = 800

trophy=Actor("trophy")
trophy.pos=(750,450)

player_radius = 10
player_speed = 5

rectangles = []
game_over = False
player_x = 0
player_y = 0


def reset_game():
    global rectangles, game_over, player_x, player_y

    rectangles = []
    game_over = False

    player_x = WIDTH // 2
    player_y = HEIGHT // 2

    for i in range(25):
        rectangles.append(mrect())


def mrect():
    w = random.randint(10, 200)
    h = random.randint(10, 100)
    x = random.randint(0, WIDTH - w)
    y = random.randint(0, HEIGHT - h)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return Rect(x, y, w, h), color


reset_game()  


def draw():
    global player
    screen.fill("black")

    trophy.draw()

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=80, color="red")
        screen.draw.text("Press SPACE to Restart", center=(WIDTH//2, HEIGHT//2 + 60),
                         fontsize=40, color="white")
        return

    for rect, color in rectangles:
        screen.draw.filled_rect(rect, color)

    player=screen.draw.filled_circle((player_x, player_y), player_radius, "white")


def update():
    global player_x, player_y, game_over

    if game_over:
        if keyboard.space:
            reset_game()
        return

    if keyboard.left:
        player_x -= player_speed
    if keyboard.right:
        player_x += player_speed
    if keyboard.up:
        player_y -= player_speed
    if keyboard.down:
        player_y += player_speed

    if player_x < player_radius:
        player_x = player_radius
    if player_x > WIDTH - player_radius:
        player_x = WIDTH - player_radius
    if player_y < player_radius:
        player_y = player_radius
    if player_y > HEIGHT - player_radius:
        player_y = HEIGHT - player_radius

    for rect, color in rectangles:
        if circle_rect_collision(player_x, player_y, player_radius, rect):
            game_over = True


def circle_rect_collision(cx, cy, radius, rect):
    closest_x = max(rect.left, min(cx, rect.right))
    closest_y = max(rect.top, min(cy, rect.bottom))
    distance_x = cx - closest_x
    distance_y = cy - closest_y
    return (distance_x**2 + distance_y**2) <= radius**2


player_collected=trophy.colliderect(player)
if player_collected():
    message=("Congratulations you completed the game")


pgzrun.go()
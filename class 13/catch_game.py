import random

WIDTH = 800
HEIGHT = 600

basket_width = 100
basket_height = 20
basket_speed = 6

basket = Rect((WIDTH // 2 - basket_width // 2, HEIGHT - 40),
              (basket_width, basket_height))

circles = []
circle_speed = 4

score = 0
misses = 0
max_misses = 5
game_over = False

def spawn_circle():
    x = random.randint(20, WIDTH - 20)
    y = -20
    radius = 20
    circles.append([x, y, radius])

def reset_game():
    global circles, score, misses, game_over, basket
    circles = []
    score = 0
    misses = 0
    game_over = False
    basket.x = WIDTH // 2 - basket_width // 2
    basket.y = HEIGHT - 40

def update():
    global score, misses, game_over

    if game_over:
        if keyboard.space:
            reset_game()
        return

    if keyboard.left:
        basket.x -= basket_speed
    if keyboard.right:
        basket.x += basket_speed

    if basket.left < 0:
        basket.left = 0
    if basket.right > WIDTH:
        basket.right = WIDTH

    if random.randint(1, 30) == 1:
        spawn_circle()

    for circle in circles[:]:
        circle[1] += circle_speed

        if circle[1] > HEIGHT + circle[2]:
            circles.remove(circle)
            misses += 1
            if misses >= max_misses:
                game_over = True
            continue

        cx, cy, r = circle

        if (basket.left <= cx <= basket.right and
            basket.top <= cy + r <= basket.bottom):
            circles.remove(circle)
            score += 1

def draw():
    screen.fill((0, 0, 30))

    screen.draw.filled_rect(basket, (50, 200, 255))

    for x, y, r in circles:
        screen.draw.filled_circle((x, y), r, (255, 80, 80))

    screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")
    screen.draw.text(f"Misses: {misses}/{max_misses}", (10, 60), fontsize=35, color="red")

    if game_over:
        screen.draw.text("GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2 - 20),
            fontsize=80,
            color="yellow")
        screen.draw.text("Press SPACE to restart",
            center=(WIDTH // 2, HEIGHT // 2 + 40),
            fontsize=40,
            color="lightgreen")

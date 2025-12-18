import pgzrun
import random

TITLE = "Flappy Balls (OOP)"
WIDTH = 800
HEIGHT = 600
GRAVITY = 2000.0

balls=(0,70)

class Ball:
    def __init__(self, x, y, color, vx):
        BALL_RADIUS = random.randint(0,70)

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = 0
        self.radius = BALL_RADIUS
        self.color = color

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self, dt):
        uy = self.vy
        self.vy += GRAVITY * dt
        self.y += (uy + self.vy) * 0.5 * dt

        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * 0.9

        self.x += self.vx * dt

        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx


balls = [
    Ball(100, 100, (255, 0, 0), 200),
    Ball(200, 100, (0, 255, 0), 250),
    Ball(300, 100, (0, 0, 255), 150),
    Ball(400, 100, (255, 255, 0), 300)
]


def draw():
    screen.clear()
    for ball in balls:
        ball.draw()


def update(dt):
    for ball in balls:
        ball.update(dt)


def on_key_down(key):
    if key == keys.SPACE:
        for ball in balls:
            ball.vy = -500


pgzrun.go()
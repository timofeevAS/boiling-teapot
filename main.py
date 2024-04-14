import math
import random
import sys

import time
from enum import Enum

import pygame as pg

from components.bubble import Bubble

# Initialize pygame
pg.init()


class BubblyType(Enum):
    BIG_BUBBLE_AREA1 = 1
    SMALL_BUBBLE_BACKGROUND = 2
    MIDDLE_BUBBLE_AREA2 = 3


# Screen dimension
WIDTH, HEIGHT = 1245, 700

# Areas
BIG_BUBBLES_AREA = [((270, 510), (310, 10)),
                    ((310, 10), (860, 10)),
                    ((860, 10), (880, 110)),
                    ((880, 110), (550, 240)),
                    ((550, 240), (500, 400)),
                    ((500, 400), (910, 520)),
                    ((910, 520), (580, 550)),  # Bottom of teapot line
                    ((580, 550), (270, 510)),  # Bottom of teapot line
                    ]

SMALL_BUBBLES_AREA = [((885, 115), (555, 245)),
                      ((555, 245), (510, 395)),
                      ((510, 395), (910, 515)),
                      ((910, 515), (885, 115))
                      ]

TEAPOT_MAX_X = 910
TEAPOT_MIN_X = 270

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
ORANGE = (255, 165, 0)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 25, 25)

BLUE = (0, 0, 255)
TRANSPARENT_BLUE = (64, 128, 255, 64)  # 50% transparency (128/255)

# Create the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load('media/teapot_background_blue.png')
background = pg.transform.scale(background, (WIDTH, HEIGHT))
pg.display.set_caption("Boiling Kettle")


class SmallBackgroundBubble(Bubble):
    def __init__(self):
        super().__init__()

    def shape(self):
        self.x = random.randint(TEAPOT_MIN_X + 50,
                                TEAPOT_MAX_X - 50)  # - 50 because we haven't ideal horizontal line in right side
        self.y = 500 - random.randint(0, 470)
        self.radius = random.randint(3, 5)
        self.speed_y = -random.randint(2, 10)
        self.speed_x = 0.1 * math.sqrt(abs(self.speed_y))

    def draw(self, surface):
        surface = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
        pg.draw.circle(surface, TRANSPARENT_BLUE, (self.radius, self.radius), self.radius)
        pg.draw.circle(surface, (255, 255, 255, 192), (self.radius / 2, self.radius / 2), self.radius / 2)
        screen.blit(surface, (self.x - self.radius, self.y - self.radius))

    def update(self, speed_delta):
        self.x += self.speed_x + speed_delta
        self.y += self.speed_y + speed_delta
        self.speed_x += 0.01  # Simulate gravity

        # If the circle goes above the screen, reset it
        if self.x > TEAPOT_MAX_X - 50 or self.radius < 0.5 or self.y < 40:
            self.shape()
        else:
            self.radius -= self.radius * 0.05


big_bubbles_speed = 0.1
small_bubbles_speed = 0

bubbles = []
small_bubbles = []

for bubble in range(0, 800):
    small_bubbles.append(SmallBackgroundBubble())

running = True
clock = pg.time.Clock()

start_time = time.time()

background_switched = False

while running:
    screen.blit(background, (0, 0))

    '''
    for point in BIG_BUBBLES_AREA:
        pg.draw.line(screen, GREEN, point[0], point[1], 5)

        font = pg.font.Font(None, 20)
        x1, y1 = point[0]
        x2, y2 = point[1]
        text = font.render(f'({x1}, {y1})', True, (0, 0, 0))
        screen.blit(text, (x1, y1))

        text = font.render(f'({x2}, {y2})', True, (0, 0, 0))
        screen.blit(text, (x2, y2))

    for point in SMALL_BUBBLES_AREA:
        pg.draw.line(screen, ORANGE, point[0], point[1], 5)

    for x in range(0, WIDTH, 50):
        for y in range(0, HEIGHT, 50):
            point = (x,y)
            color = GREEN if point_in_polygon(point, BIG_BUBBLES_AREA) else RED
            pg.draw.circle(screen, color, point, 5)
    '''

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    big_bubbles_speed += 0.001
    small_bubbles_speed += 0.0005

    for bubble in bubbles:
        bubble.update(big_bubbles_speed)
        bubble.draw(screen)

    for bubble in small_bubbles:
        bubble.update(small_bubbles_speed)
        bubble.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.flip()
    clock.tick(1000)
    print(time.time() - start_time)
    if time.time() - start_time > 10 and not background_switched:
        background = pg.image.load('media/teapot_background_white.png')
        background = pg.transform.scale(background, (WIDTH, HEIGHT))
        background_switched = True

pg.quit()
sys.exit()

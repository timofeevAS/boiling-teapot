import math
import random
import sys

import time
from enum import Enum

import pygame as pg

from components.bubble import Bubble
from components.mid_area2_bubble import MidArea2Bubble
from components.small_background_bubble import SmallBackgroundBubble
from components.big_area1_bubble import BigArea1Bubble
from utils.utils import point_in_polygon
from utils.utils_const import *

# Initialize pygame
pg.init()

DEBUG_MODE = True

# Create the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load('media/teapot_background_blue.png')
background = pg.transform.scale(background, (WIDTH, HEIGHT))
pg.display.set_caption("Boiling Kettle")




big_bubbles_speed = 0.1
small_bubbles_speed = 0

big_bubbles_area1 = []
mid_bubbles_area2 = []
small_bubbles = []

for bubble in range(0, 400):
    small_bubbles.append(SmallBackgroundBubble())

for bubble in range(0, 150):
    big_bubbles_area1.append(BigArea1Bubble())

for bubble in range(0, 100):
    mid_bubbles_area2.append(MidArea2Bubble())

running = True
clock = pg.time.Clock()

start_time = time.time()

background_switched = False

while running:
    screen.blit(background, (0, 0))

    if DEBUG_MODE:
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


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    big_bubbles_speed += 0.001
    small_bubbles_speed += 0.0005

    for bubble in big_bubbles_area1:
        bubble.update(big_bubbles_speed)
        bubble.update_collisions(big_bubbles_area1)
        bubble.draw(screen)

    for bubble in mid_bubbles_area2:
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

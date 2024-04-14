import math
import random

from components.bubble import Bubble
from utils.utils_const import *
import pygame as pg


class BigArea1Bubble(Bubble):
    def __init__(self):
        super().__init__()

    def shape(self):
        self.x = random.randint(TEAPOT_MIN_X + 50, TEAPOT_MAX_X - 50)
        self.y = TEAPOT_MAX_Y
        self.radius = random.randint(10, 20)
        self.speed_y = -random.randint(2, 10)
        self.speed_x = (random.randint(1, 10) / 10) * math.sqrt(abs(self.speed_y))
        self.angle = random.randint(40, 80) / 100

    def draw(self, surface):
        screen = surface
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
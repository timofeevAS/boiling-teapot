import math
import random

from components.bubble import Bubble
from utils.utils import point_in_polygon
from utils.utils_const import *
import pygame as pg


class BigArea1Bubble(Bubble):
    def __init__(self):
        super().__init__()

    def shape(self):
        self.x = random.randint(TEAPOT_MIN_X + 50, TEAPOT_MAX_X - 50)
        self.y = TEAPOT_MAX_Y
        self.radius = random.randint(20, 30)
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
        if not point_in_polygon((self.x, self.y), BIG_BUBBLES_AREA):
            pass

        self.x += self.speed_x * speed_delta
        self.y += self.speed_y * speed_delta

        if self.y >= (TEAPOT_MAX_Y+TEAPOT_MIN_Y)/2:
            self.speed_x += 0.001  # Simulate gravity
            self.angle += 0.001
            self.x = self.x - self.radius * self.angle * math.cos(self.angle)
            self.y = self.y - self.radius * self.angle * math.sin(self.angle)
        else:
            self.speed_x += 0.001  # Simulate gravity
            self.angle += 0.001


            self.x = self.x + random.choice([-1,1])*self.radius * self.angle * math.cos(self.angle)

            self.y = self.y - self.radius * self.angle * math.sin(self.angle)


        # If the circle goes above the screen, reset it
        if self.x < TEAPOT_MIN_X + 50 or self.radius < 0.5 or self.y < TEAPOT_MIN_Y:
            self.shape()
        else:
            self.radius += self.radius * 0.001

    def update_collisions(self, bubbles):
        for other_bubble in bubbles:
            if other_bubble != self:
                distance = math.sqrt((self.x - other_bubble.x) ** 2 + (self.y - other_bubble.y) ** 2)
                if distance < self.radius + other_bubble.radius:
                    angle = math.atan2(other_bubble.y - self.y, other_bubble.x - self.x)
                    self.x -= math.cos(angle)
                    self.y -= math.sin(angle)

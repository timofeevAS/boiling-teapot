import pygame as pg

from utils.utils_const import *
import random


class Bubble:
    def __init__(self):
        self.angle = None
        self.speed, self.speed_x, self.speed_y = None, None, None
        self.x, self.y = None, None
        self.radius = None
        self.main_color = TRANSPARENT_BLUE
        self.shape()

    def shape(self):
        # Generate shape
        pass

    def update(self, speed_delta):
        # Update self params
        pass

    def draw(self, surface):
        screen = surface
        surface = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
        pg.draw.circle(surface, self.main_color, (self.radius, self.radius), self.radius)
        # Выбор случайных координат для внутреннего круга
        inner_radius = self.radius / 2
        inner_x = random.uniform(inner_radius, self.radius * 2 - inner_radius)
        inner_y = random.uniform(inner_radius, self.radius * 2 - inner_radius)

        # Отрисовка внутреннего круга
        pg.draw.circle(surface, LIGHT_GRAY, (int(inner_x), int(inner_y)), int(inner_radius))
        screen.blit(surface, (self.x - self.radius, self.y - self.radius))

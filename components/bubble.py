import pygame as pg

from utils.utils_const import *


class Bubble:
    def __init__(self):
        self.angle = None
        self.speed, self.speed_x, self.speed_y = None, None, None
        self.x, self.y = None, None
        self.radius = None
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
        pg.draw.circle(surface, TRANSPARENT_BLUE, (self.radius, self.radius), self.radius)
        pg.draw.circle(surface, LIGHT_GRAY, (self.radius / 2, self.radius / 2), self.radius / 2)
        screen.blit(surface, (self.x - self.radius, self.y - self.radius))

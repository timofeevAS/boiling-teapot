import math
import random

from components.bubble import Bubble
from utils.utils import point_in_polygon
from utils.utils_const import *
import pygame as pg


class MidArea2Bubble(Bubble):
    def __init__(self):
        self.base_x = 600
        self.base_y = 800
        super().__init__()
        self.main_color = TRANSPARENT_BLUE


    def setPoint(self, point):
        self.x, self.y = point
        self.base_x, self.base_y = point

    def shape(self):
        self.x = self.base_x-random.randint(0,50)
        self.y = self.base_y-random.randint(0,20)
        self.radius = random.randint(5, 10)
        self.speed_y = -random.randint(2, 10)
        self.speed_x = (random.randint(1, 10) / 10) * math.sqrt(abs(self.speed_y))
        self.angle = random.randint(40, 80) / 100

    def update(self, speed_delta):
        if not point_in_polygon((self.x, self.y), SMALL_BUBBLES_AREA):
            self.angle = random.uniform(0, 2 * math.pi)

        self.x += self.speed_x * math.cos(self.angle)
        self.y += self.speed_y * math.sin(self.angle)

        self.radius += 0.1
        self.angle += 0.001


        # If the circle goes above the screen, reset it
        if self.radius > 20:
            self.radius = 0


        if self.x < TEAPOT_MIN_X + 50 or self.x > TEAPOT_MAX_X - 50 or self.y > TEAPOT_MAX_Y - 50 or self.radius < 0.5 or self.y < TEAPOT_MIN_Y:
            self.shape()
        else:
            self.radius += self.radius * 1.01

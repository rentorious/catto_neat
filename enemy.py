import pygame
from pygame.locals import *

from assets import MUMMY_SPRITE
from constants import (
    GROUND,
    WIN_HEIGHT,
    WIN_WIDTH
)


class Enemy:
    def __init__(self, speed):
        self.img = MUMMY_SPRITE
        self.y = GROUND
        self.x = WIN_WIDTH
        self.speed = speed

    def move(self):
        self.x -= self.speed

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def update(self):
        self.move()

    def collide(self, neko):
        neko_mask = pygame.mask.from_surface(neko.img)
        self_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - neko.x), round(self.y - neko.y))

        return neko_mask.overlap(self_mask, offset)

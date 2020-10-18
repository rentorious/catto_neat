import pygame
from assets import NEKO_TILESET
from constants import *


class Neko:
    NEKO_W = 64
    NEKO_H = 64

    SPRITE_LEN = 5
    ANIMATION_LEN = 5 * SPRITE_LEN

    def __init__(self):
        self.x = 100
        self.y = GROUND

        self.jumping = False
        self.jump_time = 0
        self.jump_vel = 0

        self.animation_time = 0

        self.NEKOS = [
            NEKO_TILESET.subsurface((i * self.NEKO_W, 64), (self.NEKO_W, self.NEKO_H)) for i in range(3)]
        self.img = self.NEKOS[0]

    def jump(self):
        if self.jumping:
            return

        self.jumping = True
        self.jump_time = 0
        self.jump_vel = -10.5

    def update(self):
        self.move()
        self.animate()

    def move(self):
        self.jump_time += 1

        # displacement
        d = self.jump_vel*self.jump_time + 1.32*self.jump_time**2

        # clamp
        if d >= 16:
            d = 16
        if d < 0:
            d -= 2

        # move dino
        self.y += d

        # stop jumping if has hit the ground
        if self.y > GROUND:
            self.jumping = False
            self.y = GROUND

    def animate(self):
        if self.animation_time < self.SPRITE_LEN:
            self.img = self.NEKOS[0]
        elif self.animation_time < 2 * self.SPRITE_LEN:
            self.img = self.NEKOS[1]
        elif self.animation_time < 3 * self.SPRITE_LEN:
            self.img = self.NEKOS[2]
        elif self.animation_time < 4 * self.SPRITE_LEN:
            self.img = self.NEKOS[1]
        elif self.animation_time < 5 * self.SPRITE_LEN:
            self.animation_time = 0
            self.img = self.NEKOS[0]

        self.animation_time += 1

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

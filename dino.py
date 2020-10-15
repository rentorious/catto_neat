import pygame
import os
from pygame.locals import *

WIN_HEIGHT = 450
WIN_WIDTH = 750

GROUND = 350

MAX_HEIGHT = 100

BG = [220, 220, 220]


NEKO_TILESET = pygame.image.load(os.path.join("imgs", "neko.png"))
GRASS_TILESET = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "grass.png")))
GRASS_TILE = GRASS_TILESET.subsurface((96, 0), (64, 64))

class Neko:
    NEKO_W = 32
    NEKO_H = 32

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
        pygame.transform.scale2x(NEKO_TILESET.subsurface((i * self.NEKO_W, 64), (self.NEKO_W, self.NEKO_H))) for i in range(3)]
        self.img = self.NEKOS[0]

    def jump(self):
        if self.jumping:
            return
        
        self.jumping = True
        self.jump_time = 0
        self.jump_vel = -9.8

    def update(self):
        self.move()
        self.animate()
        
    def move(self):
        self.jump_time += 1

        #displacement
        d = self.jump_vel*self.jump_time + 1.5*self.jump_time**2

        #clamp
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

        self.animation_time += 1

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))



class Ground:
    SPEED = 4
    
    def __init__(self):
        self.img = GRASS_TILE
        self.tile_num = int(WIN_WIDTH / self.img.get_width()) + 5
        print(self.tile_num)
        self.x = 0
        self.y = GROUND + self.img.get_height()
    def move(self):
        self.x -= self.SPEED

    def update(self):
        self.move()

    def draw(self, win):
        if self.x + self.img.get_width() < 0:
            self.x += self.img.get_width()

        for i in range(self.tile_num):
            #print(self.x + i * self.img.get_width())
            win.blit(self.img, (self.x + self.img.get_width() * i, self.y))
        
        

def draw_window(win, dino, ground):
    win.fill(BG)
    dino.draw(win)
    ground.draw(win)
    
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
     
    run = True

    dino = Neko()
    ground = Ground()

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                dino.jump()
                
        dino.update()
        ground.update()

        draw_window(win, dino, ground)

    pygame.quit()
    quit()

main()

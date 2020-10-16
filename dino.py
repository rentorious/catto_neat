import pygame
import os
from pygame.locals import *

from ground import Ground
from neko import Neko
from constants import *


def draw_window(win, dino, ground):
    win.fill(BG)
    ground.draw(win)
    dino.draw(win)
    
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
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                run = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                dino.jump()
                
        dino.update()
        ground.update()

        draw_window(win, dino, ground)

    pygame.quit()
    quit()

main()

import pygame
import os
from pygame.locals import *

cact = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "cactus.png")), (50, 50))
rect = cact.get_rect()

tiles = []
for i in range(4):
    tiles.append(Rect((i * cact.get_width(), 0), (cact.get_width(), cact.get_height())))
    print(tiles[-1])

def draw(win, sprite, tiles):
    win.fill([222,222,222])

    for tile in tiles:
        win.blit(cact, tile)

    pygame.display.update()

clock = pygame.time.Clock()
win = pygame.display.set_mode((1200, 600))
run = True
move = (2, 0)
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False
    
    for i in range(len(tiles)):
        tiles[i].move_ip(move)

        if tiles[i].x >= 300:
            #tmp = tiles.pop(-1)
            print("{}: {}".format(i ,tiles[i].x))
            tiles[i].move_ip(-len(tiles)*cact.get_width(), 0)
            
    draw(win, cact, tiles)

pygame.quit()
quit()

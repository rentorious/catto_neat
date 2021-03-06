import pygame
from constants import *
from assets import GRASS_TILE

class Ground:
    SPEED = 4
    SPRITE = GRASS_TILE
    S_WIDTH = GRASS_TILE.get_width()
    S_HEIGHT = GRASS_TILE.get_height()
    
    def __init__(self):
        self.x = 0
        self.y = GROUND + self.S_HEIGHT - 9
        
        self.tile_num = int(WIN_WIDTH / self.S_WIDTH) + 4
        self.tiles = [pygame.Rect((i * self.S_WIDTH, self.y), (self.S_WIDTH, self.S_HEIGHT)) for i in range(self.tile_num)]
        
    def move(self):
        for tile in self.tiles:
            tile.move_ip(-self.SPEED, 0)

    def update(self):
        self.move()

    def draw(self, win):
        for i in range(len(self.tiles)):
            if self.tiles[i].x + self.S_WIDTH < 0:
                self.tiles[i].move_ip(len(self.tiles) * self.S_WIDTH, 0)
            
        
        for tile in self.tiles:
            win.blit(self.SPRITE, tile)

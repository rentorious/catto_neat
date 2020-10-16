import pygame
import os

# Grass tileset
GRASS_TILESET = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "grass.png")))
GRASS_TILE = GRASS_TILESET.subsurface((96, 0), (64, 64))

# NEKO Tileset
NEKO_TILESET = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "neko.png")))
NEKO_TILESET = pygame.transform.flip(NEKO_TILESET, True, False)

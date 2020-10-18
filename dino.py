import pygame
import os
from pygame.locals import *

from ground import Ground
from neko import Neko
from enemy import Enemy
from enemy_manager import EnemyManager
from constants import *

import random


def draw_window(win, dino, enemies, ground):
    win.fill(BG)
    ground.draw(win)
    dino.draw(win)
    enemies.draw(win)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    run = True

    spawnRate = 0.01
    spawn_off_timer = 0
    difficulty_timer = 0
    current_enemy_speed = ENEMY_SPEED

    dino = Neko()
    ground = Ground()
    enemies = EnemyManager([Enemy(current_enemy_speed)])

    print("TRUE")

    while run:
        clock.tick(30)

        if random.random() < spawnRate and spawn_off_timer >= SPAWN_OFF_TIME:
            enemies.add(Enemy(current_enemy_speed))
            spawn_off_timer = 0
        spawn_off_timer += 1
        difficulty_timer += 1

        if difficulty_timer >= DIFICULTY_LEVEL_LENGTH:
            current_enemy_speed += ENEMY_SPEED_STEP
            difficulty_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                run = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                dino.jump()

        dino.update()
        ground.update()
        enemies.update()

        if enemies.check_collisions(dino):
            print("Game Over!")

        draw_window(win, dino, enemies, ground)

    pygame.quit()
    quit()


main()

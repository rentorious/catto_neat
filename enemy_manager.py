import pygame


class EnemyManager:
    def __init__(self, enemies):
        self.enemies = enemies

    def move(self):
        remove = []
        for enemy in self.enemies:
            if enemy.x + enemy.img.get_width() < 0:
                remove.append(enemy)

        for r in remove:
            del r

        for enemy in self.enemies:
            enemy.move()

    def draw(self, win):
        for enemy in self.enemies:
            enemy.draw(win)

    def check_collisions(self, neko):
        for enemy in self.enemies:
            if enemy.collide(neko):
                return True

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def add(self, enemy):
        self.enemies.append(enemy)

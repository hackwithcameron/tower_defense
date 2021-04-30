import pygame
import os

from enemy import Enemy


class EasyEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/1/" "1_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/1/" "1_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/1/" "1_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/1/" "1_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.health = health
        self.health = speed
        self.walk = True
        self.path_index = 0
        self.x, self.y = self.path[0]

        # self.mask = pygame.mask.from_surface()

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)




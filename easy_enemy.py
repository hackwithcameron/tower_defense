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

    def __init__(self, health):
        super().__init__(health)
        self.health = 100
        self.walk_img = self.WALK_IMG
        self.die_img = self.DIE_IMG

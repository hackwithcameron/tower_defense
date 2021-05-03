import pygame
import os

from Enemies.enemy import Enemy


class Boss(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/Boss/" "7_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/Boss/" "7_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/Boss/" "7_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/Boss/" "7_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.height = 110
        self.width = 110
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


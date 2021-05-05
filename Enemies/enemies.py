import pygame
import os

from Enemies.enemy import Enemy


class RedEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/RedEnemy/" "1_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/RedEnemy/" "1_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/RedEnemy/" "1_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/RedEnemy/" "1_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class LightGreenEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreenEnemy/" "2_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreenEnemy/" "2_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreenEnemy/" "2_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreenEnemy/" "2_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class LightGreyEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreyEnemy/" "8_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreyEnemy/" "8_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreyEnemy/" "8_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/LightGreyEnemy/" "8_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class PurpleEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/PurpleEnemy/" "5_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/PurpleEnemy/" "5_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/PurpleEnemy/" "5_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/PurpleEnemy/" "5_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class SilverEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/SilverEnemy/" "3_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/SilverEnemy/" "3_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/SilverEnemy/" "3_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/SilverEnemy/" "3_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class TanEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/TanEnemy/" "6_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/TanEnemy/" "6_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/TanEnemy/" "6_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/TanEnemy/" "6_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class DarkGreyEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreyEnemy/" "10_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreyEnemy/" "10_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreyEnemy/" "10_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreyEnemy/" "10_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class DarkGreenEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreenEnemy/" "9_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreenEnemy/" "9_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreenEnemy/" "9_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/DarkGreenEnemy/" "9_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


class BrownGreenEnemy(Enemy):
    WALK_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/BrownGreenEnemy/" "4_enemies_1_walk_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/BrownGreenEnemy/" "4_enemies_1_walk_0" + str(x) + ".png")) for x in range(0, 19)]
    DIE_IMG = [pygame.image.load(os.path.join(
        "assets/monster-enemy-sprites/PNG/BrownGreenEnemy/" "4_enemies_1_die_00" + str(x) + ".png") if x < 10 else os.path.join(
        "assets/monster-enemy-sprites/PNG/BrownGreenEnemy/" "4_enemies_1_die_0" + str(x) + ".png")) for x in range(0, 19)]

    def __init__(self, health=100, speed=1):
        super().__init__(health, speed)
        self.walk = True

    def walk_animation(self, window):
        self.draw(window, self.WALK_IMG)

    def die_animation(self, window):
        self.draw(window, self.DIE_IMG)


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
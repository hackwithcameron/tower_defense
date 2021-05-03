import pygame

import levels
from Enemies.red_enemy import RedEnemy
from Enemies.lightgreen_enemy import LightGreenEnemy
from Enemies.silver_enemy import SilverEnemy
from Enemies.browngreen_enemy import BrownGreenEnemy
from Enemies.purple_enemy import PurpleEnemy
from Enemies.tan_enemy import TanEnemy
from Enemies.boss import Boss
from Enemies.lightgrey_enemy import LightGreyEnemy
from Enemies.darkgreen_enemy import DarkGreenEnemy
from Enemies.darkgrey_enemy import DarkGreyEnemy


pygame.font.init()
pygame.display.set_caption("Tower Defense")


class Game:
    def __init__(self):
        self.WIN = pygame.display.set_mode((levels.WIDTH, levels.HEIGHT))

        self.play = True
        self.FPS = 60
        self.enemies = [
            RedEnemy(speed=1), LightGreenEnemy(speed=2), SilverEnemy(speed=1.75), BrownGreenEnemy(speed=1.2),
            PurpleEnemy(speed=0.75), TanEnemy(speed=2.25), Boss(speed=1.5), LightGreyEnemy(speed=1.35),
            DarkGreenEnemy(speed=2.15), DarkGreyEnemy(speed=3)
            ]

        self.clock = pygame.time.Clock()

    def update_window(self):
        self.WIN.blit(levels.LEVEL_BG, (0, 0))
        for enemy in self.enemies:
            if enemy.walk:
                enemy.walk_animation(self.WIN)

        pygame.display.update()

    def run(self):
        while self.play:
            self.clock.tick(self.FPS)
            self.update_window()

            for enemy in self.enemies:
                if enemy.walk and enemy.x - 20 < levels.WIDTH:
                    enemy.move()
                elif enemy.x > levels.WIDTH:
                    self.enemies.remove(enemy)

            # Checks for window close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass


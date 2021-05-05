import pygame

import levels

from Towers.towers import SpikeBallTower, FireTower, RockTower, BoulderTower
from Enemies.enemies import RedEnemy, LightGreenEnemy, SilverEnemy, BrownGreenEnemy, PurpleEnemy, TanEnemy, Boss, LightGreyEnemy, DarkGreenEnemy, DarkGreyEnemy


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
        self.towers = [SpikeBallTower(350, 350), FireTower(255, 255), RockTower(450, 350), BoulderTower(550, 350)]

        self.clock = pygame.time.Clock()

    def update_window(self):
        self.WIN.blit(levels.LEVEL_BG, (0, 0))
        """
        for enemy in self.enemies:
            if enemy.walk:
                enemy.walk_animation(self.WIN)
        """
        for tower in self.towers:
            tower.draw(self.WIN)

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

            for tower in self.towers:
                tower.shoot()

            # Checks for window close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass


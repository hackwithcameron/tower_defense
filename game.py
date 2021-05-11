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
            RedEnemy(speed=2), Boss(speed=1)
            ]
        self.towers = [SpikeBallTower(250, 250)]

        self.clock = pygame.time.Clock()

    def update_window(self):
        self.WIN.blit(levels.LEVEL_BG, (0, 0))

        for tower in self.towers:
            tower.enemy_in_range(self.enemies)
            tower.draw(self.WIN)

        for enemy in self.enemies:
            if enemy.walk:
                enemy.walk_animation(self.WIN)
            elif enemy.died:
                enemy.die_animation(self.WIN)
            else:
                self.enemies.remove(enemy)

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
                    # Test tower upgrades
                    for tower in self.towers:
                        tower.upgrade_tower()
                    # Test enemy health bar
                    for enemy in self.enemies:
                        enemy.health -= 12
                        if enemy.health < 0:
                            enemy.walk = False
                            enemy.died = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_u]:
                for tower in self.towers:
                    tower.upgrade_tower()
            if keys[pygame.K_d]:
                for tower in self.towers:
                    tower.downgrade_tower()



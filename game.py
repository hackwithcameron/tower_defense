import pygame

import levels
from easy_enemy import EasyEnemy

pygame.font.init()
pygame.display.set_caption("Tower Defense")


class Game:
    def __init__(self):
        self.WIN = pygame.display.set_mode((levels.WIDTH, levels.HEIGHT))

        self.play = True
        self.FPS = 60
        self.enemy = EasyEnemy(100)

        self.clock = pygame.time.Clock()

    def update_window(self):
        self.WIN.blit(levels.LEVEL_BG, (0, 0))
        self.enemy.walk(self.WIN)

        pygame.display.update()

    def run(self):
        while self.play:
            self.clock.tick(self.FPS)
            self.update_window()

            # Checks for window close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

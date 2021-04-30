import pygame
import os

WIDTH, HEIGHT = 1050, 700
LEVEL_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BG.png")), (WIDTH, HEIGHT))

LEVEL_PATH = [(-150, 384), (9, 384), (170, 384), (170, 181), (386, 181), (386, 455), (664, 452), (669, 323), (1037, 315)]

import pygame
import os

WIDTH, HEIGHT = 1050, 700
LEVEL_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BG.png")), (WIDTH, HEIGHT))

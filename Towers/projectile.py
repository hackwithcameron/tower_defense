import pygame
import os


class Projectile:
    def __init__(self, x, y, img):
        self.projectile_img = img
        self.width = 25
        self.height = 25
        self.projectile_x = (x - self.width // 2) - 3
        self.projectile_y = (y - self.height // 2) - 13
        self.fired = False

    def draw_projectile(self, window, projectile):
        window.blit(pygame.transform.scale(projectile.projectile_img, (self.width, self.height)), (self.projectile_x, self.projectile_y))





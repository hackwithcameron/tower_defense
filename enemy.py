import pygame
import os
from levels import LEVEL_PATH


class Enemy:
    def __init__(self, health=100, speed=1):
        self.x, self.y = (350, 350)
        self.width, self.height = 75, 75
        self.health = health
        self.enemy_img = None
        self.animation_count = 0
        self.path = LEVEL_PATH
        self.speed = speed
        self.path_index = 0

    def draw(self, window, imgs):
        window.blit(pygame.transform.scale(imgs[self.animation_count], (self.width, self.height)), (self.x - self.width//2, self.y - self.height//2))
        self.animation_count += 1
        if self.animation_count >= len(imgs):
            self.animation_count = 0

    def move(self):
        if self.path_index <= len(self.path):
            x2, y2 = self.path[self.path_index]
            x_diff, y_diff = ((x2 - self.x), (y2 - self.y))
            # Checks to see if enemy is within range of pos on path
            if self.speed >= x_diff >= -self.speed and self.speed >= y_diff >= -self.speed:
                self.path_index += 1
            if abs(x_diff) > abs(y_diff):
                if x_diff != 0 and x_diff > 0:
                    self.x += self.speed
                elif x_diff != 0 and x_diff < 0:
                    self.x -= self.speed
            elif abs(y_diff) > abs(x_diff):
                if y_diff != 0 and y_diff > 0:
                    self.y += self.speed
                elif y_diff != 0 and y_diff < 0:
                    self.y -= self.speed

            # Temp For Debugging
            # print(f"x diff: {x_diff}, y diff: {y_diff}")



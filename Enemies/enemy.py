import pygame
import os

from levels import LEVEL_PATH


class Enemy:
    def __init__(self, health=100, speed=1):
        self.width, self.height = 75, 75
        self.max_health = health
        self.health = health
        self.animation_count = 0
        self.path = LEVEL_PATH
        self.x, self.y = self.path[0]
        self.speed = speed
        self.path_index = 0
        self.health_bar_length = 75
        self.health_bar_height = 10
        self.walk = True
        self.died = False
        # self.mask = pygame.mask.from_surface()

    def draw(self, window, motion):
        window.blit(pygame.transform.scale(motion[self.animation_count], (self.width, self.height)), (self.x - self.width//2.4, self.y - self.height//1.4))
        self.draw_health_bar(window)  # Draws enemy health bar
        self.animation_count += 1
        if self.animation_count >= len(motion):
            self.animation_count = 0

    def move(self):
        if self.path_index <= len(self.path):
            x2, y2 = self.path[self.path_index]
            x_diff, y_diff = ((x2 - self.x), (y2 - self.y))
            # Checks to see if enemy is within range of pos on path
            if self.speed >= x_diff >= -self.speed and self.speed >= y_diff >= -self.speed:
                self.path_index += 1
            # Checks to see which direction the enemy needs to move only moves right angles
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

    def draw_health_bar(self, window):
        green_health_bar_length = (self.health / self.max_health) * self.health_bar_length
        green_bar = pygame.image.load(os.path.join("assets/monster-enemy-sprites/health_bar/", "health_bar-06.png"))
        red_bar = pygame.image.load(os.path.join("assets/monster-enemy-sprites/health_bar/", "health_bar-07.png"))

        window.blit(pygame.transform.scale(red_bar, (self.health_bar_length, self.health_bar_height)), (self.x - self.width / 2, self.y - (self.height / 2 + 15)))
        if green_health_bar_length > 0:
            window.blit(pygame.transform.scale(green_bar, (round(green_health_bar_length), self.health_bar_height)), (self.x - self.width / 2, self.y - (self.height / 2 + 15)))

    def die(self, DIE_IMG_LST):
        """
        Allows the die animation to be completed before enemy is removed
        :param DIE_IMG_LST: List of all anaimation images
        :return: None
        """
        if self.animation_count >= len(DIE_IMG_LST) - 1:
            self.died = False

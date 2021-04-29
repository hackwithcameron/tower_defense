import pygame
import os


class Enemy:
    def __init__(self, health):
        self.x, self.y = (350, 350)
        self.health = health
        self.enemy_img = None
        self.walk_img = []
        self.die_img = []
        self.animation_count = 0

    def walk(self, window):
        window.blit(self.walk_img[self.animation_count], (self.x, self.y))
        self.animation_count += 1
        if self.animation_count >= len(self.walk_img):
            self.animation_count = 0

    def die(self, window):
        window.blit(self.die_img[self.animation_count], (self.x, self.y))
        self.animation_count += 1
        if self.animation_count >= len(self.die_img):
            self.animation_count = 0
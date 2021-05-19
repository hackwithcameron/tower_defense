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
        self.projectile_vel = 0.020
        self.t = 0
        self.last_location_x = None
        self.last_location_y = None

    def draw_projectile(self, window, projectile):
        window.blit(pygame.transform.scale(projectile.projectile_img, (self.width, self.height)), (self.projectile_x, self.projectile_y))

    def projectile_move(self, enemies, tower_x, tower_y):
        """
        Shoots projectile at enemy. If len of enemy is 0 shot will continue to last know enemy location
        :param enemies: List of Enemies
        :param tower_x: Tower X Location
        :param tower_y: Tower Y Location
        :return: None
        """
        if self.fired:
            if len(enemies) > 0:
                mid_point_x = ((enemies[0].x + tower_x) / 2)
                mid_point_y = ((enemies[0].y + tower_y) / 2) - 250

                P0_x = pow((1 - self.t), 2) * ((tower_x - self.width / 2) - 2)
                P0_y = pow((1 - self.t), 2) * ((tower_y - self.height / 2) - 15)

                P1_x = 2 * (1 - self.t) * self.t * mid_point_x
                P1_y = 2 * (1 - self.t) * self.t * mid_point_y

                P2_x = self.t ** 2 * enemies[0].x
                P2_y = self.t ** 2 * enemies[0].y

                curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)
                self.last_location_x = enemies[0].x
                self.last_location_y = enemies[0].y

                self.projectile_x, self.projectile_y = curve
            else:
                mid_point_x = ((self.last_location_x + tower_x) / 2)
                mid_point_y = ((self.last_location_y + tower_y) / 2) - 250

                P0_x = pow((1 - self.t), 2) * ((tower_x - self.width / 2) - 2)
                P0_y = pow((1 - self.t), 2) * ((tower_y - self.height / 2) - 15)

                P1_x = 2 * (1 - self.t) * self.t * mid_point_x
                P1_y = 2 * (1 - self.t) * self.t * mid_point_y

                P2_x = self.t ** 2 * self.last_location_x
                P2_y = self.t ** 2 * self.last_location_y

                curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)

                self.projectile_x, self.projectile_y = curve
            if self.t >= 1:
                self.t = 0

            self.t += self.projectile_vel



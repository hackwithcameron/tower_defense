import pygame
import math

from .projectile import Projectile


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_width, self.base_height = 75, 75
        self.shooter_width, self.shooter_height = 65, 15
        self.selected = False
        self.range = [150, 250, 300]
        self.level = 0
        self.base_img = None
        self.back_img = None
        self.front_img = None
        self.projectile_img = None
        self.projectiles = []
        # Shooter adjustments for drawing START
        self.shooter_spacing = 2
        self.shooter_x_offset = -3
        self.shooter_y_offset = -5
        self.shooter_bottom = 5
        self.shooter_top = -20
        self.shooter_back_speed = 1
        self.shooter_forward_speed = 5
        # Shooter adjustments END
        self.shoot_projectile = False
        self.target_in_range = False
        self.in_range_enemies = []
        self.animation_count = 0
        self.cool_down = 0

    def draw(self, window):
        # Draws back shooter
        window.blit(pygame.transform.scale(self.back_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width // 2 + self.shooter_x_offset, (self.y - self.shooter_height // 2) - self.shooter_height + self.shooter_y_offset + self.shooter_spacing))
        # Draws base
        window.blit(pygame.transform.scale(self.base_img, (self.base_width, self.base_height)), (self.x - self.base_width//2, self.y - self.base_height//2))
        # Draws front shooter
        window.blit(pygame.transform.scale(self.front_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width // 2 + self.shooter_x_offset, self.y - self.shooter_height // 2 + self.shooter_y_offset))
        # Draw tower range circle if selected
        if self.selected:
            self.draw_range_circle(window)
        # Draw the projectiles for each tower
        for projectile in self.projectiles:
            projectile.draw_projectile(window, projectile)
            projectile.projectile_move(self.in_range_enemies, self.x, self.y + self.shooter_top)
            if projectile.t > 1:  # Checks if projectile is at end of arc and removes projectile from list
                self.projectiles.remove(projectile)

    def shoot(self):
        # load projectile
        if not self.shoot_projectile:
            self.shooter_y_offset += self.shooter_back_speed
            # Checks if shooter is at full power
            if self.shooter_y_offset >= self.shooter_bottom:
                self.load_projectile()
                self.shoot_projectile = True
        # shoot projectile
        elif self.shoot_projectile and self.target_in_range:
            self.shooter_y_offset -= self.shooter_forward_speed
            self.fire_projectile()
            # Checks if shooter has hit end of shot
            if self.shooter_y_offset <= self.shooter_top:
                self.shoot_projectile = False
                self.fire_projectile()

    def enemy_in_range(self, enemies):
        self.target_in_range = False
        self.in_range_enemies = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            # Gets distance to target enemy
            dis_to_target = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dis_to_target < self.range[self.level]:
                self.target_in_range = True
                self.in_range_enemies.append(enemy)

    def upgrade(self, BASE_IMG, BACK_IMG, FRONT_IMG):
        if self.level == 0:
            self.level = 1
            self.get_imgs(BASE_IMG, BACK_IMG, FRONT_IMG)
        elif self.level == 1:
            self.level = 2
            self.get_imgs(BASE_IMG, BACK_IMG, FRONT_IMG)
        else:
            pass

    def downgrade(self, BASE_IMG, BACK_IMG, FRONT_IMG):
        if self.level == 2:
            self.level = 1
            self.get_imgs(BASE_IMG, BACK_IMG, FRONT_IMG)
        elif self.level == 1:
            self.level = 0
            self.get_imgs(BASE_IMG, BACK_IMG, FRONT_IMG)
        else:
            pass

    def get_imgs(self, BASE_IMG, THROWER_BACK_IMG, THROWER_FRONT_IMG):
        if self.level == 0:
            self.base_img = BASE_IMG["LVL_1"]
            self.front_img = THROWER_FRONT_IMG["LVL_1"]
            self.back_img = THROWER_BACK_IMG["LVL_1"]
        elif self.level == 1:
            self.base_img = BASE_IMG["LVL_2"]
            if len(THROWER_BACK_IMG) > 2:
                self.front_img = THROWER_FRONT_IMG["LVL_2"]
                self.back_img = THROWER_BACK_IMG["LVL_2"]
            else:
                self.front_img = THROWER_FRONT_IMG["LVL_1"]
                self.back_img = THROWER_BACK_IMG["LVL_1"]
        elif self.level == 2:
            self.base_img = BASE_IMG["LVL_3"]
            self.front_img = THROWER_FRONT_IMG["LVL_3"]
            self.back_img = THROWER_BACK_IMG["LVL_3"]

    def draw_range_circle(self, window):
        # Draw tower range circle
        if self.selected:
            surface = pygame.Surface((self.range[self.level]*2, self.range[self.level]*2), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (0, 0, 0, 75), (self.range[self.level], self.range[self.level]), self.range[self.level], self.range[self.level])
            window.blit(surface, (self.x - self.range[self.level], self.y - self.range[self.level]))

    def load_projectile(self):
        projectile = Projectile(self.x, self.y, self.projectile_img)
        self.projectiles.append(projectile)

    def fire_projectile(self):
        for projectile in self.projectiles:
            if not projectile.fired and self.shoot_projectile:
                projectile.projectile_y -= self.shooter_forward_speed
            if not self.shoot_projectile:
                projectile.fired = True

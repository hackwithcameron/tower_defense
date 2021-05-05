import pygame


class Tower:
    def __init__(self, x, y, health=1000):
        self.x = x
        self.y = y
        self.base_width, self.base_height = 75, 75
        self.shooter_width, self.shooter_height = 65, 15
        self.selected = False
        self.health = health
        self.base_img = None
        self.back_img = None
        self.front_img = None
        self.shooter_spacing = 2
        self.shooter_x_offset = -3
        self.shooter_y_offset = -5
        self.shooter_bottom = 5
        self.shooter_top = -20
        self.shooter_back_speed = 1
        self.shooter_forward_speed = 3
        self.shoot_projectile = False
        self.animation_count = 0
        self.cool_down = 1

    def draw(self, window):
        # Draws back shooter
        window.blit(pygame.transform.scale(self.back_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width // 2 + self.shooter_x_offset, (self.y - self.shooter_height // 2) - self.shooter_height + self.shooter_y_offset + self.shooter_spacing))
        # Draws base
        window.blit(pygame.transform.scale(self.base_img, (self.base_width, self.base_height)), (self.x - self.base_width//2, self.y - self.base_height//2))
        # Draws front shooter
        window.blit(pygame.transform.scale(self.front_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width // 2 + self.shooter_x_offset, self.y - self.shooter_height // 2 + self.shooter_y_offset))

    def shoot(self):
        # load projectile
        if not self.shoot_projectile:
            self.shooter_y_offset += self.shooter_back_speed
            # Checks if shooter is at full power
            if self.shooter_y_offset >= self.shooter_bottom:
                self.shoot_projectile = True
        # shoot projectile
        elif self.shoot_projectile:
            self.shooter_y_offset -= self.shooter_forward_speed
            # Checks if shooter has hit end of shot
            if self.shooter_y_offset <= self.shooter_top:
                self.shoot_projectile = False

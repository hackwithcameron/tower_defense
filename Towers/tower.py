import pygame


class Tower:
    def __init__(self, x, y, health=1000):
        self.base_width, self.base_height = 75, 75
        self.shooter_width, self.shooter_height = 65, 15
        self.selected = False
        self.health = health
        self.base_img = None
        self.back_img = None
        self.front_img = None
        self.x = x
        self.y = y
        self.shooter_xoffset = -3
        self.shooter_yoffset = -5
        self.shooter_back_speed = 1
        self.shooter_forward_speed = 3
        self.shoot_rock = False
        self.animation_count = 0
        self.cool_down = 1

    def draw(self, window):
        # Draws back shooter
        window.blit(pygame.transform.scale(self.back_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width//2 + self.shooter_xoffset, (self.y - self.shooter_height//2) - self.shooter_height + self.shooter_yoffset + 2))
        # Draws base
        window.blit(pygame.transform.scale(self.base_img, (self.base_width, self.base_height)), (self.x - self.base_width//2, self.y - self.base_height//2))
        # Draws front shooter
        window.blit(pygame.transform.scale(self.front_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width//2 + self.shooter_xoffset, self.y - self.shooter_height//2 + self.shooter_yoffset))

    def shoot(self):
        # load rock
        if not self.shoot_rock:
            self.shooter_yoffset += self.shooter_back_speed
            # Checks if shooter is at full power
            if self.shooter_yoffset >= 5:
                self.shoot_rock = True
        # shoot rock
        elif self.shoot_rock:
            self.shooter_yoffset -= self.shooter_forward_speed
            # Checks if shooter has hit end of shot
            if self.shooter_yoffset <= -20:
                self.shoot_rock = False

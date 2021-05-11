import pygame
import os

from Towers.tower import Tower


class SpikeBallTower(Tower):
    BASE_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "3.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "6.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "7.png"))
    }

    THROWER_BACK_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "1.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "4.png"))
    }

    THROWER_FRONT_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "2.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "5.png"))
    }

    def __init__(self, x, y):
        super().__init__(x, y, health=1000)
        self.base_img = self.BASE_IMG["LVL_1"]
        self.front_img = self.THROWER_FRONT_IMG["LVL_1"]
        self.back_img = self.THROWER_BACK_IMG["LVL_1"]

    def upgrade_tower(self):
        super().upgrade(self.BASE_IMG, self.THROWER_BACK_IMG, self.THROWER_FRONT_IMG)

    def downgrade_tower(self):
        super().downgrade(self.BASE_IMG, self.THROWER_BACK_IMG, self.THROWER_FRONT_IMG)


class FireTower(Tower):
    BASE_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "12.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "13.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "14.png"))
    }

    THROWER_BACK_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "8.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "10.png"))
    }

    THROWER_FRONT_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "9.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "11.png"))
    }

    def __init__(self, x, y):
        super().__init__(x, y, health=1000)
        self.base_img = self.BASE_IMG["LVL_1"]
        self.front_img = self.THROWER_FRONT_IMG["LVL_1"]
        self.back_img = self.THROWER_BACK_IMG["LVL_1"]
        self.shooter_spacing = 9

    def upgrade_tower(self):
        super().upgrade(self.BASE_IMG, self.THROWER_BACK_IMG, self.THROWER_FRONT_IMG)

    def downgrade_tower(self):
        super().downgrade(self.BASE_IMG, self.THROWER_BACK_IMG, self.THROWER_FRONT_IMG)


class RockTower(Tower):
    BASE_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "15.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "16.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "17.png"))
    }

    THROWER_BACK_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "20.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "22.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "18.png"))
    }

    THROWER_FRONT_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "21.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "23.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "19.png"))
    }

    def __init__(self, x, y):
        super().__init__(x, y, health=1000)
        self.base_img = self.BASE_IMG["LVL_1"]
        self.front_img = self.THROWER_FRONT_IMG["LVL_1"]
        self.back_img = self.THROWER_BACK_IMG["LVL_1"]

    def upgrade_tower(self):
        super().upgrade(self.BASE_IMG, self.THROWER_BACK_IMG, self.THROWER_FRONT_IMG)

    def downgrade_tower(self):
        super().downgrade(self.BASE_IMG, self.THROWER_BACK_IMG, self.THROWER_FRONT_IMG)


class BoulderTower(Tower):
    BASE_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "24.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "25.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "26.png"))
    }

    THROWER_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "28.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "27.png")),
    }

    def __init__(self, x, y):
        super().__init__(x, y, health=1000)
        self.base_img = self.BASE_IMG["LVL_1"]
        self.front_img = self.THROWER_IMG["LVL_1"]
        self.back_img = self.THROWER_IMG["LVL_1"]
        self.x_spacing = 17
        self.shooter_y_offset = -45
        self.shooter_x_offset = -3
        self.shooter_bottom = -26
        self.shooter_top = -50
        self.shooter_width, self.shooter_height = 35, 50

    def draw(self, window):
        window.blit(pygame.transform.scale(self.front_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width // 2 + self.shooter_x_offset - self.x_spacing, self.y - self.shooter_height // 2 + self.shooter_y_offset))
        window.blit(pygame.transform.scale(self.front_img, (self.shooter_width, self.shooter_height)), (self.x - self.shooter_width // 2 + self.shooter_x_offset + self.x_spacing, self.y - self.shooter_height // 2 + self.shooter_y_offset))
        window.blit(pygame.transform.scale(self.base_img, (self.base_width, self.base_height)), (self.x - self.base_width//2, self.y - self.base_height//2))
        if self.selected:
            self.draw_range_circle(window)

    def upgrade_tower(self):
        super().upgrade(self.BASE_IMG, self.THROWER_IMG, self.THROWER_IMG)
        if self.level != 0:
            self.shooter_x_offset = -5
            self.x_spacing = 18

    def downgrade_tower(self):
        super().downgrade(self.BASE_IMG, self.THROWER_IMG, self.THROWER_IMG)
        if self.level == 0:
            self.shooter_x_offset = -3
            self.x_spacing = 17


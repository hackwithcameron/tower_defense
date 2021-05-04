import pygame
import os

from Towers.tower import Tower


class BasicTower(Tower):
    BASE_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "3.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "6.png")),
        "LVL_3": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "7.png"))
    }

    THROWER_BACK_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "1.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "4.png"))
    }

    THROWER_FRONT_IMG = {
        "LVL_1": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "2.png")),
        "LVL_2": pygame.image.load(os.path.join("assets/stone-tower-game-assets/PNG/" "5.png"))
    }

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=100)
        self.base_img = self.BASE_IMG["LVL_1"]
        self.front_img = self.THROWER_FRONT_IMG["LVL_1"]
        self.back_img = self.THROWER_BACK_IMG["LVL_1"]

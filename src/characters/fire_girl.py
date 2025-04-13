import pygame
from utils.constants import FIRE_GIRL_IMAGE_PATH

class FireGirl(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(FIRE_GIRL_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass

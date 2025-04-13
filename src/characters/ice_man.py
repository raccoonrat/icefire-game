import pygame
from utils.constants import ICE_MAN_IMAGE_PATH

class IceMan(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(ICE_MAN_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass

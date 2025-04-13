import pygame
from utils.constants import LEVEL_01_BACKGROUND_PATH

class Level01:
    def __init__(self, game):
        self.background_image = pygame.image.load(LEVEL_01_BACKGROUND_PATH).convert()
        self.game = game

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

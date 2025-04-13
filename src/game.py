import pygame
from characters.ice_man import IceMan
from characters.fire_girl import FireGirl
from assets.levels.level_01 import Level01

class Game:
    def __init__(self):
        pygame.display.set_caption("冰火人冒险")
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.ice_man = IceMan(x=100, y=500)
        self.fire_girl = FireGirl(x=200, y=500)
        self.all_sprites.add(self.ice_man, self.fire_girl)
        self.level = Level01(self)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill screen with black
        self.level.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

import os
import pygame
from game import Game

# 设置 SDL_AUDIODRIVER 为 dummy 以禁用音频输出
os.environ['SDL_AUDIODRIVER'] = 'dummy'

def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()

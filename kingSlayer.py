import pygame
from settingsGame import *
pygame.init()

# Window game size
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(NAME_GAME)
pygame.display.set_icon(pygame.image.load("img/game/logo.bmp"))

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

import pygame
from settingsGame import *
pygame.init()

# Window game size
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(NAME_GAME)
pygame.display.set_icon(pygame.image.load("img/Game/logo.bmp"))

clock = pygame.time.Clock()

player = pygame.image.load("img/Characters/mainHero.png")
x = 50
y = 50
speed = 5

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    controlKeys = pygame.key.get_pressed()

    if controlKeys[pygame.K_LEFT]:
        x -= speed
    elif controlKeys[pygame.K_RIGHT]:
        x += speed
    elif controlKeys[pygame.K_UP]:
        y -= speed
    elif controlKeys[pygame.K_DOWN]:
        y += speed

    window.blit(player, (x, y))
    pygame.display.update()

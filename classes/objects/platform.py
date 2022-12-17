import pygame

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Platform builder
        super().__init__()
        # Installation of a photo platform
        self.image = pygame.image.load('img//Game//platform.png')

        # Set link to rectangle image
        self.rect = self.image.get_rect()
        
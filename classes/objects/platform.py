import pygame

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, isRotate = False, angle = 0):
        # Platform builder
        super().__init__()
        # Installation of a photo platform
        self.image = pygame.image.load('img//Game//platform.png')
        self.image = pygame.transform.scale(self.image, (width, height))

        # Set link to rectangle image
        self.rect = self.image.get_rect()

        if isRotate:
            self.image = pygame.transform.rotate(self.image, angle)

        
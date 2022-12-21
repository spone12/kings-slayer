import pygame
from kingSlayer import *
from settingsGame import *
#from classes.levels.levelOne import *

# Class for arranging platforms on the stage
class Level(object):
    def __init__(self, player, bg):
        # Create a group of sprites
        self.platform_list = pygame.sprite.Group()
        # Link to main player
        self.player = player
        self.bg = bg

    # In order for everything to be drawn, you need to update the screen
    # When this method is called, the update will occur
    def update(self):
        self.platform_list.update()

    # Method for drawing objects on scenesе
    def draw(self, screen):
        # Draw the background
        screen.blit(self.bg, (0, 0))

        # Draw all platforms from a group of sprites
        self.platform_list.draw(screen)


# # A class that describes where the collision objects will be located
class Level_01(Level):
    def __init__(self, player, bg):
        # Calling the parent constructor
        Level.__init__(self, player, bg)

        # Array with data about platforms. Data in this format:
        # width, height, x and y position
        level = [

            [SCREEN_WIDTH, 20, 0, SCREEN_HEIGHT - 5],
            [100, 20, 600, 500],
            [100, 20, 50,  500],
            [100, 20, 50,  300],
            [100, 20, 200, 400],
            [100, 20, 600, 300],
            [100, 20, 400, 400],
        ]

        # Loop through the array and add each platform to the sprite group - platform_list
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
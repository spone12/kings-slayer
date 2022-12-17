import pygame
from kingSlayer import *
from classes.levels.level import *

#A class that describes where the collision objects will be located
class Level_01(Level):
    def __init__(self, player):
        # Calling the parent constructor
        Level.__init__(self, player)

        # Array with data about platforms. Data in this format:
        # width, height, x and y position
        level = [
            [210, 32, 500, 500],
            [210, 32, 200, 400],
            [210, 32, 600, 300],
        ]

        # Loop through the array and add each platform to the sprite group - platform_list
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
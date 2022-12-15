import pygame

from settingsGame import *
from classes.entities.player import *
#from classes.levels.level import *

# Подключение фото для заднего фона
bg = pygame.image.load('img//Game//bg.png')

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Platform builder
        super().__init__()
        # Installation of a photo platform
        self.image = pygame.image.load('img//Game//platform.png')

        # Set link to rectangle image
        self.rect = self.image.get_rect()


# Class for arranging platforms on the stage
class Level(object):
    def __init__(self, player):
        # Create a group of sprites
        self.platform_list = pygame.sprite.Group()
        # Link to main player
        self.player = player

    # In order for everything to be drawn, you need to update the screen
    # When this method is called, the update will occur
    def update(self):
        self.platform_list.update()

    # Method for drawing objects on scenesе
    def draw(self, screen):
        # Draw the background
        screen.blit(bg, (0, 0))

        # Draw all platforms from a group of sprites
        self.platform_list.draw(screen)


# A class that describes where the collision objects will be located
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


def main():
    # Initialization
    pygame.init()

    # Setting the screen height and width
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Setting the name of the game
    pygame.display.set_caption(NAME_GAME)

    # Create a player
    player = Player()

    # Create all levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Is the game running
    isRunGame = False

    # Used to control the screen refresh rate
    clock = pygame.time.Clock()

    # Main program loop
    while not isRunGame:
        # Activity Tracking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunGame = True

            # player moving
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                elif event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                elif event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player
        active_sprite_list.update()

        # Update objects in the scene
        current_level.update()

        # Preventing the player from moving beyond the right side of the screen
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        # Preventing the player from moving beyond the left side of the screen
        if player.rect.left < 0:
            player.rect.left = 0

        # Draw objects on the window
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # set FPS in game
        clock.tick(FPS)

        # Update the screen after drawing objects
        pygame.display.flip()

    # closing of the program
    pygame.quit()

if __name__ == '__main__':
    main()
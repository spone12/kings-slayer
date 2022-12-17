import pygame
import sys
pygame.font.init()

from settingsGame import *
from classes.entities.player import *
from classes.levels.level import *
from classes.objects.platform import *
from classes.printText import *
#from classes.levels.levelOne import *

screen = ''
# Подключение фото для заднего фона
bg = pygame.image.load('img//Game//bg.png')

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

    #
    text = PrintText(screen)
    

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

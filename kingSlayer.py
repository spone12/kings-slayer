import pygame as pg
import sys

from settingsGame import *
from classes.entities.player import *
from classes.levels.level import *
from classes.objects.platform import *
from classes.printText import *

class kingSlayer:
    def __init__(self):
        # Initialization
        pg.init()
        pg.font.init()
        self.clock = pg.time.Clock()
        self.bg = pg.image.load('img//Game//bg.png')

        # Setting the screen height and width
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.textObj = PrintText(self.screen)
        # Setting the name of the game
        pg.display.set_caption(NAME_GAME)

        self.newGame()
        self.level()

    def newGame(self):
        self.player = Player(self.screen)
        self.player.rect.x = 340
        self.player.rect.y = SCREEN_HEIGHT - self.player.rect.height

    def update(self, isDebugFps):
        # Update the player
        self.active_sprite_list.update()

        # Update objects in the scene
        self.current_level.update()
        # Update the screen after drawing objects
        pg.display.flip()
        self.clock.tick(FPS)
        if isDebugFps:
            pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def level(self):
        # Create all levels
        self.level_list = []
        self.level_list.append(Level_01(self.player, self.bg))

        # Set the current level
        self.current_level_no = 0
        self.current_level = self.level_list[self.current_level_no]

        self.active_sprite_list = pg.sprite.Group()
        self.player.level = self.current_level

        self.active_sprite_list.add(self.player)

    def draw(self):
        # Draw objects on the window
        self.current_level.draw(self.screen)
        self.active_sprite_list.draw(self.screen)

        # show health
        self.player.showCharacterBars(self.textObj)

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            # player moving
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.go_left()
                elif event.key == pg.K_RIGHT:
                    self.player.go_right()
                elif event.key == pg.K_UP:
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and self.player.change_x < 0:
                    self.player.stop()
                elif event.key == pg.K_RIGHT and self.player.change_x > 0:
                    self.player.stop()

    def run(self):
        while True:
            self.checkEvents()
            self.update(False)
            self.draw()

if __name__ == '__main__':
    game = kingSlayer()
    game.run()

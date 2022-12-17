import pygame
from settingsGame import *

#Print message class
class PrintText():

    fontType = 'effects//fonts//PingPong.ttf'
    fontColor = GREEN
    fontSize = 30

    def __init__(self, screen):
       self.screen = screen

    def print(self, message, x = 50, y = 100, color = fontColor):

        fontTypeObj = pygame.font.Font(self.fontType, self.fontSize)
        text = fontTypeObj.render(message, True, color)
        self.screen.blit(text, (x, y))
        
        
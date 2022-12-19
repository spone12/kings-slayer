import pygame
from settingsGame import *

# A class that describes the behavior of the main player
class Player(pygame.sprite.Sprite):
    # is the player turned right
    right = True
    # player health
    hp = 100
    # player mana
    mana = 100
    # player level
    level = 1
    # experience
    exp = 0

    # Constructor
    def __init__(self, screen):
        # calling parent class constructor
        super().__init__()

        # screen
        self.screen = screen

        # Image of the main character
        self.image = pygame.image.load('img//Characters//mainHero.png')

        self.healthImg = pygame.image.load('img//Game//heart.png')
        self.healthImg = pygame.transform.scale(self.healthImg, (20, 20))

        self.manaImg = pygame.image.load('img//Game//mana.png')
        self.manaImg = pygame.transform.scale(self.manaImg, (20, 20))

        # Set link to rectangle image
        self.rect = self.image.get_rect()

        # Set the player's velocity vector
        self.change_x = 0
        self.change_y = 0

    def update(self):
        # In this function we move the player
        # First set its gravity
        self.calc_grav()

        # Move it to the right/left
        # change_x will change later when you press the keyboard arrows
        self.rect.x += self.change_x

        # Whether we are hitting some other object, platforms, for example
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        # Iterate over all possible objects that could collide
        for block in block_hit_list:
            # If we go right
            # sets our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise, if we move to the left, then we do the opposite
                self.rect.left = block.rect.right

        # Moving up/down
        self.rect.y += self.change_y

        # for up/down collide
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Set our position based on the top/bottom of the object we hit
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop vertical movement
            self.change_y = 0

    def calc_grav(self):
        # Here we calculate how fast the object will be
        # fall to the ground under the influence of gravity
        if self.change_y == 0:
            self.change_y = 2.5
        else:
            self.change_y += .95

        # If already on the ground, then set the Y position as 0
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    # Jump handling
    def jump(self):
        # We need to check here if we are in contact with anything
        # or in other words, are we in flight.
        # To do this, we go down by 10 units, check the contact and then go back up
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        # If everything is in order, jump up
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -16

    # Player movement in left
    def go_left(self):
        # The functions themselves will be called later from the main loop
        self.change_x = -9 # Move player on X coordinate

        # We check where he is looking and if anything, then turn him over
        if(self.right):
            self.flip()
            self.right = False

    # Player movement in right
    def go_right(self):
        self.change_x = 9
        if (not self.right):
            self.flip()
            self.right = True


    def stop(self):
        # call this method when no keys are pressed
        self.change_x = 0

    def flip(self):
        # player flip (mirroring)
        self.image = pygame.transform.flip(self.image, True, False)

    # show character bars
    def showCharacterBars(self, textObj):
        self.screen.blit(self.healthImg, (20, 20))
        self.screen.blit(self.manaImg, (50, 20))
        textObj.print(self.hp, 20, 40)
        textObj.print(self.mana, 50, 40)

    def statPlus(self, stat, value):
        
        match stat:

            case 'hp':
                self.hp += value
            case 'mana':
                self.mana += value

    def statMinus(self, stat, value):
        
        match stat:

            case 'hp':
                self.hp -= value
            case 'mana':
                self.mana -= value

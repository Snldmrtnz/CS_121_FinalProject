
##Imports
import pygame
from Settings import *

##To initialize the font module
pygame.font.init()

class Tile(pygame.sprite.Sprite):

    ##Constructor for parameter
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()
        if self.text != "empty":
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(self.text, True, BLACK)

            ##To make the background of the tiles White
            self.image.fill(WHITE) 
            self.font_size = self.font.size(self.text)

            ##To make the text numbers in middle of the tiles
            draw_x = (TILESIZE / 2) - self.font_size[0]/2 
            draw_y = (TILESIZE / 2) - self.font_size[1]/2

            ##To put numbers on the tiles
            self.image.blit(font_surface, (draw_x, draw_y)) 

    ##update function
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    ##To check if the tile selected is correct
    def click(self, mouse_x, mouse_y): #mouse_x and mouse_y are mouse coordinates
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.botton
        
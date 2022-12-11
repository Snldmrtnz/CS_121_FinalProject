
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
        self.text = text
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        if self.text != "empty":
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(self.text, True, BLACK)

            ##To make the background of the tiles White
            self.image.fill(GREEN) 
            self.font_size = self.font.size(self.text)

            ##To make the text numbers in middle of the tiles
            draw_x = (TILESIZE / 2) - self.font_size[0]/2 
            draw_y = (TILESIZE / 2) - self.font_size[1]/2

            ##To put numbers on the tiles
            self.image.blit(font_surface, (draw_x, draw_y)) 
        else:
            self.image.fill(BGCOLOUR)
    ##update function
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    ##To check if the tile selected is correct
    def click(self, mouse_x, mouse_y): #mouse_x and mouse_y are mouse coordinates
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x + TILESIZE < GAME_SIZE * TILESIZE

    def left(self):
        return self.rect.x - TILESIZE >= 0

    def up(self):
        return self.rect.y - TILESIZE >= 0

    def down(self):
        return self.rect.y + TILESIZE < GAME_SIZE * TILESIZE

class UIElement:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 50)
        text = font.render(self.text, True, GREEN)
        screen.blit(text, (self.x, self.y))

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.color = color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y, self.width, self.height))
        font = pygame.font.SysFont("Consolas", 30)
        text = font.render(self.text, True, self.text_color)
        self.font_size = font.size(self.text)     
        draw_x = self.x + (self.width / 2) - self.font_size[0]/2 
        draw_y = self.y + (self.height / 2) - self.font_size[1]/2
        screen.blit(text, (draw_x, draw_y))

    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height

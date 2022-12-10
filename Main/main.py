
##imports
import pygame
import random
import time

##from imports
from sprite import *
from Settings import *


class Game: 


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode ((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    ##To create the list which the game will look/be displayed
    ##This will look like:
      ##[1. 2. 3],
      ##[4, 5, 6],
      ##[7, 8, 0]

    def create_game(self):
        ##nested for loops
        grid = [[x + y * GAME_SIZE for x in range(1, GAME_SIZE + 1)] for y in range(GAME_SIZE)]
        grid[-1][-1] = 0
        return grid

    #To draw the tiles
    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                else:
                    self.tiles[row].append(Tile(self, col, row, "empty"))


    def new(self):
        self.all_sprites = pygame.sprite.Group() 
        self.tiles_grid = self.create_game() ##will be changing depending on clicks
        self.tiles_grid_completed = self.create_game()##comparison to know if the game is completed

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    ##Grid to hold the puzzle
    def draw_grid(self):
        for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (row, 0), (row, GAME_SIZE * TILESIZE))
        for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, col), (GAME_SIZE * TILESIZE, col))


    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.draw_tiles()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)





game =  Game()
while True:
    game.new()
    game.run()
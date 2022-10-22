"""
Collects all the constants needed for the board
"""

import pygame

# board dimensions
WIDTH = 400
HEIGHT = 400

# number of rows and cols on board
ROWS = 4
COLS = 4

# individual square size
SQUARE_SIZE = HEIGHT // ROWS

# colors
GREEN = (119, 149, 86)
WHITE = (235, 236, 208)
BROWN = (100, 46, 28)

# queen image
QUEEN = pygame.transform.scale(pygame.image.load('assets/queen.png'), (100,100))

"""
Collects all the constants needed for the board
"""

import pygame
pygame.init()

# board dimensions
WIDTH = 450
HEIGHT = 450

# number of rows and cols on board
ROWS = 4
COLS = 4

# individual square size
SQUARE_SIZE = HEIGHT // ROWS

# size of shelf
SHELF_SIZE = SQUARE_SIZE

# size of start menu
START_MENU_HEIGHT = SQUARE_SIZE

# colors
GREEN = (119, 149, 86)
WHITE = (235, 236, 208)
BROWN = (100, 46, 28)
BLACK = (0, 0, 0)
GGREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# queen image
QUEEN = pygame.transform.scale(pygame.image.load(
    'assets/queen.png'), (SQUARE_SIZE, SQUARE_SIZE))

# sound for when piece is set down
piece_sound = pygame.mixer.Sound("assets/clack.mp3")

# sound for when you are
boo_sound = pygame.mixer.Sound("assets/boo.mp3")

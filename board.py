"""
Draws the board and the "shelf" which is where the pieces will be placed initially
"""

import pygame
from constants import GREEN, ROWS, WHITE, SQUARE_SIZE, WIDTH, HEIGHT, BROWN

class Board:

    """
    create board
    """
    def __init__(self):
        self.board = []

    """
    draw squares on board
    """
    def draw_squares(self, win):
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    """
    draw shelf on board
    """
    def draw_shelf(self, win):
        pygame.draw.rect(win, BROWN, (0, HEIGHT, WIDTH, SQUARE_SIZE))

    def create_board(self):
        pass
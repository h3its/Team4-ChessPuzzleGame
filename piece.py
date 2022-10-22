"""
Represents a chess piece on the board

RIGHT NOW is hardcoded as a Queen
"""

import pygame
from constants import SQUARE_SIZE, ROWS, QUEEN

class Piece:
    def __init__(self, number):
        self.number = number
        self.col = number
        self.row = ROWS
        self.x = 0
        self.y = 0
        self.calc_pos()

    """
    calculates the top-left position of current square
    """
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col #+ SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row #+ SQUARE_SIZE // 2

    """
    draws the piece
    """
    def draw(self, win):
        #pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), SQUARE_SIZE//2-10)
        win.blit(QUEEN, (self.x, self.y))

    def drawwhilemoving(self, win):
        pos = pygame.mouse.get_pos()
        x, y = pos
        win.blit(QUEEN, (x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2))

    """
    moves the piece to the specified row and col
    """
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    """
    makes the piece print "Q" in any string representation
    """
    def __repr__(self):
        return "Q"


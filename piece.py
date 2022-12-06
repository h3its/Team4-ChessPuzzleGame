"""
Represents a chess piece on the board
"""

import pygame
from abc import abstractmethod


class Piece:
    def __init__(self,col, game_def):
        self.x = 0
        self.y = 0
        self.game_def = game_def
        self.number = self.game_def['COLS']
        self.col = col
        self.row = self.game_def['ROWS']
        self.calc_pos()

    """
    calculates the top-left position of current square
    """

    def calc_pos(self):
        self.x = self.game_def['SQUARE_SIZE'] * self.col  # + SQUARE_SIZE // 2
        self.y = self.game_def['SQUARE_SIZE'] * self.row  # + SQUARE_SIZE // 2

    """
    draws the piece
    """

    def _draw(self, win, image):
        win.blit(image, (self.x, self.y))

    def draw_while_moving(self, win, image):
        pos = pygame.mouse.get_pos()
        x, y = pos
        win.blit(image, (x - self.game_def['SQUARE_SIZE'] // 2, y - self.game_def['SQUARE_SIZE'] // 2))

    """
    moves the piece to the specified row and col
    """

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    """
    makes the piece print "X" in any string representation
    """

    def __repr__(self):
        return "X"

    @abstractmethod
    def check_attacks(self): pass

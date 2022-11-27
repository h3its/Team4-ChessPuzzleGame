"""
Represents a chess piece on the board
"""
import pygame
from abc import abstractmethod


class Piece:

    def __init__(self):
        row = -1
        col = -1

    def set_pos(self, row, col):
        self.row = row
        self.col = col

    """
    makes the piece print "X" in any string representation
    """
    def __repr__(self):
        return "X"

    @abstractmethod
    def check_attacks(self, board, row, col): pass

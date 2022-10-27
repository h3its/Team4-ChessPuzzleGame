"""
Handles game processes including updating the game and moving pieces
"""

import pygame
from board import Board

class Game:

    def __init__(self, win):
        self._init()
        self.selected = None
        self.win = win

    """
    updates board
    """
    def update(self):
        self.board.draw(self.win, self.selected)
        pygame.display.update()

    """
    sets up initial state of game
    """
    def _init(self):
        self.selected = None
        self.board = Board()

    """
    resets board to initial state
    """
    def reset(self):
        self._init()

    """
    selects a piece to be moved
    """
    def pickup(self, row, col):
        if self.board.get_piece(row, col) != 0:
            self.selected = self.board.get_piece(row, col)

    """
    moves the piece then unselects it
    """
    def drop(self, row, col):
        if self.board.get_piece(row, col) == 0:
            self._move(row, col)
        self.selected = None

    """
    moves piece to specified row and col if valid
    """
    def _move(self, row, col):
        moveto = self.board.get_piece(row, col)
        if self.selected and moveto == 0:
            self.board.move(self.selected, row, col)
        else:
            return False

        return True

    """
    Checks to see if pieces are correctly placed
    """
    def check_solution(self):
        result = False
        if self.board.is_shelf_empty():
            result = self.board.check()
        if result:
            self.board.is_correct()


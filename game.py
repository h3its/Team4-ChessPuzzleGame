"""
Handles game processes including updating the game and moving pieces
"""

import pygame
from board import Board
from constants import *


class Game:

    def __init__(self, win, game_definition):
        self.game_def = game_definition
        self.ROWS = game_definition['ROWS']
        self.COLS = game_definition['COLS']
       # win.
       # self.SQUARE_SIZE = HEIGHT // ROWS
        self._init()
        self.selected = None
        self.win = win

    """
    updates board
    """

    def update(self):
        self.board.draw(self.win, self.selected)
        pygame.display.update()
        if self.board.correct != True:
            self.board.timer()
    """
    sets up initial state of game
    """

    def _init(self):
        self.selected = None
        self.board = Board(self.game_def)
        boo_sound.stop()

    """
    resets board to initial state
    """

    def reset(self):
        self._init()

    """
    selects a piece to be moved
    """

    def pickup(self, row, col):
        if self.board.wrong:
            self.board.is_not_wrong()
        if self.board.get_piece(row, col) != 0:
            self.selected = self.board.get_piece(row, col)
            boo_sound.stop()
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
            piece_sound.play()
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
            correct_sound.play()
        else:
            self.board.is_wrong()
            boo_sound.play()

    """
    Returns True if pieces can be moved, False if not
    Pieces can be moved until level is completed. Once the solution is checked and "Correct!" is
    displayed, pieces are not movable.
    """

    def movable(self):
        return not self.board.correct

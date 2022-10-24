"""
Draws the board and the "shelf" which is where the pieces will be placed initially
"""

import pygame
from constants import *
from piece import Piece

class Board:

    """
    create board
    """
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.setup_board()

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


    """
    draw Start Menu on board
    """
    def draw_start_menu(self, win):
        pygame.draw.rect(win, BLACK, (0, HEIGHT + STARTMENUHEIGHT, WIDTH, SQUARE_SIZE))
        # pygame.draw.rect(win, BLACK, (0, HEIGHT + STARTMENUHEIGHT / 2, WIDTH, SQUARE_SIZE))
        # pygame.font.init()
        # FONT = pygame.font.SysFont('comicsans', 30)
        # LARGE_FONT = pygame.font.SysFont('comicsans', 40)
        # font = FONT.render("R - Reset | SPACE - Start Backtracking | N - Next Level", 1, WHITE)
        # pygame.font.init()
        # win.blit(font, 0, HEIGHT + STARTMENUHEIGHT / 2)
        # font2 = pygame.font.SysFont('comicsans', 30)
        pygame.font.init()
        font1 = pygame.font.SysFont('comicsans', 30)
        img1 = font1.render(' R - Reset | N - Next Level', True, WHITE)
        win.blit(img1,(0, HEIGHT + STARTMENUHEIGHT + 50))
        img2 = font1.render('SPACE - Start Backtracking', True, WHITE)
        win.blit(img2,(0, HEIGHT + STARTMENUHEIGHT))


    """
    sets up the initial state of the board
    """
    def setup_board(self):
        for row in range(ROWS+1):
            self.board.append([])

        for row in range(ROWS):
            for col in range(COLS):
                self.board[row].append(0)

        for col in range(COLS):
            self.board[ROWS].append(Piece(col))

    """
    prints a string representation of board state
    """
    def print_board(self):
        for row in range(ROWS+1):
            print(*self.board[row])

    """
    draw the board and pieces on the board
    """
    def draw(self, win, selectedpiece):
        self.draw_squares(win)
        self.draw_shelf(win)
        self.draw_start_menu(win)
        for row in range(ROWS+1):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece is not selectedpiece:
                    piece.draw(win)
                if piece is selectedpiece:
                    piece.drawwhilemoving(win)

    """
    returns piece in specified row and col
    """
    def get_piece(self, row, col):
        return self.board[row][col]

    """
    moves piece to specified row and col
    """
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

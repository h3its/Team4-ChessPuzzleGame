"""
Draws the board and the "shelf" which is where the pieces will be placed initially
"""

import pygame
from constants import *
from piece import Piece
from queen import Queen

class Board:

    """
    create board
    """
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.correct = False
        self.wrong = False
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
        pygame.draw.rect(win, BROWN, (0, HEIGHT, WIDTH, SHELF_SIZE))


    """
    draw Start Menu on board
    """
    def draw_start_menu(self, win):
        pygame.draw.rect(win, BLACK, (0, HEIGHT + SHELF_SIZE, WIDTH, START_MENU_HEIGHT))
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
        win.blit(img1,(0, HEIGHT + SHELF_SIZE + 50))
        img2 = font1.render('SPACE - Check', True, WHITE)
        win.blit(img2,(0, HEIGHT + SHELF_SIZE))

        # BUTTON_WIDTH = WIDTH // 3 - 10
        # BUTTON_PADDING = 7.5
        # pygame.draw.rect(win, BLACK, (0, HEIGHT + SQUARE_SIZE, WIDTH, START_MENU_HEIGHT))
        # pygame.draw.rect(win, GGREEN, (BUTTON_PADDING, HEIGHT + SQUARE_SIZE + BUTTON_PADDING, BUTTON_WIDTH, START_MENU_HEIGHT - 10))
        # pygame.draw.rect(win, RED, (2*BUTTON_PADDING + BUTTON_WIDTH, HEIGHT + SQUARE_SIZE + BUTTON_PADDING, BUTTON_WIDTH, START_MENU_HEIGHT - 10))
        # pygame.draw.rect(win, BLUE, (3*BUTTON_PADDING+ BUTTON_WIDTH*2, HEIGHT + SQUARE_SIZE + BUTTON_PADDING, BUTTON_WIDTH, START_MENU_HEIGHT - 10))



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
            self.board[ROWS].append(Queen(col))

    """
    prints a string representation of board state
    """
    def print_board(self):
        for row in range(ROWS+1):
            print(*self.board[row])

    """
    draw the board and pieces on the board
    """
    def draw(self, win, selected_piece):
        self.draw_squares(win)
        self.draw_shelf(win)
        self.draw_start_menu(win)
        for row in range(ROWS+1):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece is not selected_piece:
                    piece.draw(win)
                if piece is selected_piece:
                    piece.draw_while_moving(win)
        if self.correct:
            self.draw_correct(win)
        elif self.wrong:
            self.draw_wrong(win)

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

    """
    Returns true if the shelf is empy, false if not
    """
    def is_shelf_empty(self):
        for col in range(COLS):
            if self.board[ROWS][col] != 0:
                return False

        return True

    """
    Checks every piece on the board to see if it is attacking another piece
    """
    def check(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if piece != 0:
                    result = piece.check_attacks(self.board, row, col)
                    if not result:
                        return False
        return True

    """
    Sets correct to True
    """
    def is_correct(self):
        self.correct = True

    """
    Draws "CORRECT!" on screen
    """
    def draw_correct(self, win):
        pygame.font.init()
        font = pygame.font.SysFont('comicsansbold', SQUARE_SIZE)
        text = font.render('CORRECT!', True, GGREEN, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)

    """
    Sets wrong to True
    """
    def is_wrong(self):
        self.wrong = True

    """
    Sets wrong to False
    """
    def is_not_wrong(self):
        self.wrong = False

    """
    Draw "TRY AGAIN!" on screen
    """
    def draw_wrong(self, win):
        pygame.font.init()
        font = pygame.font.SysFont('comicsansbold', SQUARE_SIZE)
        text = font.render('TRY AGAIN!', True, RED, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)


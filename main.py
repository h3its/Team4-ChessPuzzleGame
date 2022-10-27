"""
Runs the game and handles user input
"""

import pygame
from constants import *
from game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT + SQUARE_SIZE + START_MENU_HEIGHT))
pygame.display.set_caption('Chess Puzzle Game')

"""
runs the main processes of the game such as drawing the board and shelf
"""
def main():
    run = True
    # normalize game run speed on all hardware
    clock = pygame.time.Clock()

    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if y <= HEIGHT + SHELF_SIZE:
                    row, col = get_row_col_from_mouse(pos)
                    game.pickup(row, col)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if y <= HEIGHT + SHELF_SIZE:
                    row, col = get_row_col_from_mouse(pos)
                    game.drop(row, col)

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_SPACE:
                game.check_solution()

            if event.key == pygame.K_r:
                game.reset()

            if event.key == pygame.K_n:
                pass

        game.update()

"""
gets the row and col from mouse position
"""
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


main()

"""
Controls when the board is displayed and handles user input
"""

import pygame
from constants import WIDTH, HEIGHT
from board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT+100))
pygame.display.set_caption('Chess Puzzle Game')

"""
runs the main processes of the game such as drawing the board and shelf
"""
def main():
    run = True
    # normalize game run speed on all hardware
    clock = pygame.time.Clock()

    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(WIN)
        board.draw_shelf(WIN)
        pygame.display.update()

main()
"""
Runs the game and handles user input
"""

import pygame
from constants import *
from game import Game
import json

FPS = 60


"""
runs the main processes of the game such as drawing the board and shelf
"""


def load_games_definitions(filename):
    with open(filename) as file:
        json_game_definitions = file.read()
        return json.loads(json_game_definitions)


def get_window_size():
    d = pygame.display.Info()
    display_height = d.current_h
    display_width = d.current_w
    size = min(display_height, display_width)
    size = size - size // 2
    return size, size


game_definition = dict()
width, height = get_window_size()


def initialize_game(game_num):
    global game_definition
    game_definitions = load_games_definitions('gameDefinitions.json')
    game_definition = game_definitions[game_num]
    game_definition['WIDTH'], game_definition['HEIGHT'] = width, height
    game_definition['SQUARE_SIZE'] = game_definition['HEIGHT'] // game_definition['ROWS']
    game_definition['START_MENU_HEIGHT'] = game_definition['SQUARE_SIZE']
    game_definition['SHELF_SIZE'] = game_definition['SQUARE_SIZE']
    ss = game_definition['SQUARE_SIZE']
    game_definition['QUEEN_PIC'] = pygame.transform.scale(pygame.image.load(
        'assets/queen.png'), (ss, ss))
    game_definition['ROOK_PIC'] = pygame.transform.scale(pygame.image.load(
        'assets/rook.png'), (ss, ss))
    game_definition['BISHOP_PIC'] = pygame.transform.scale(pygame.image.load(
        'assets/bishop.png'), (ss, ss))
    WIN = pygame.display.set_mode(
        (game_definition['WIDTH'],
         game_definition['HEIGHT'] + game_definition['SHELF_SIZE'] + game_definition['START_MENU_HEIGHT']))
    pygame.display.set_caption(game_definition['gameName'])
    return WIN


def main(service, email):
    # Create a Database instance (ChessDB)
    # Create a ChessService(db)
    # Pass the service to whoever needs it
    current_game = 0
    WIN = initialize_game(current_game)

    run = True
    # normalize game run speed on all hardware
    clock = pygame.time.Clock()

    # passing in first game definiton into game objectOD
    # TODO: pass chess esrvice into Game

    game = Game(WIN, game_definition, service, email, current_game+1)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if game.movable():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    if y <= game_definition['HEIGHT'] + game_definition['SHELF_SIZE']:
                        row, col = get_row_col_from_mouse(pos)
                        game.pickup(row, col)

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    if y <= game_definition['HEIGHT'] + game_definition['SHELF_SIZE']:
                        row, col = get_row_col_from_mouse(pos)
                        game.drop(row, col)

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_SPACE:
                if game.check_solution():
                    if email is not None:
                        service.save_score(email, game.board.get_time(), current_game + 1)

            if event.key == pygame.K_r:
                game.reset()

            if event.key == pygame.K_n:
                #if game.board.correct:
                current_game = current_game + 1
                try:
                    WIN = initialize_game(current_game)
                    game = Game(WIN, game_definition, service, email, current_game+1)
                except IndexError:
                    game.finish()

        game.update()


"""
gets the row and col from mouse position
"""


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // game_definition['SQUARE_SIZE']
    col = x // game_definition['SQUARE_SIZE']
    return row, col


# Jenny moved the "main()" call that was previously here into login

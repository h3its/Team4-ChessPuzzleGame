import pygame
from board import Tile
from piece import Piece
from game import Game

pygame.init()

###################################################################################
###################################Display Screen##################################
###################################################################################
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 704
display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Trial!")

FPS = 60
clock = pygame.time.Clock()


###################################################################################
################################CREATE SPRITE GROUPS###############################
###################################################################################
main_tile_group = pygame.sprite.Group()
green_tile_group = pygame.sprite.Group()
lime_tile_group = pygame.sprite.Group()

# Create the tile map: 0 --> empty, 1 --> lime green, 2 --> green
# 15 rows (WINDOW_WIDTH = 960//11 = 64 pixels),
# 11 columns (WINDOW_HEIGHT = 704//11 = 64 pixels)
tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 1, 2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Create individual tile objects from the tile map
# Loop through the nested lists
# One for-loop will loop through the rows
# One for-loop will loop through the columns
for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        """We are multiplying j by 64 since each tiles has a width of 64 pixels"""
        """We are multiplying i by 64 since each tile has a height of 64 pixel"""
        if tile_map[i][j] == 1:
            Tile(j*64, i*64, 1, main_tile_group, green_tile_group)
        elif tile_map[i][j] == 2:
            Tile(j*64, i*64, 2, main_tile_group, lime_tile_group)
##################################################################################


###################################################################################
###############################CREATE SPRITE GROUPS################################
###################################################################################
piece_group = pygame.sprite.Group()             # Sprite group for user pieces
# Sprite group for opponent pieces
op_group = pygame.sprite.Group()
queen_group = pygame.sprite.Group()
king_group = pygame.sprite.Group()
bishop_group = pygame.sprite.Group()
pawn_group = pygame.sprite.Group()
rook_group = pygame.sprite.Group()
knight_group = pygame.sprite.Group()
opawn_group = pygame.sprite.Group()
orook_group = pygame.sprite.Group()
oknight_group = pygame.sprite.Group()
obishop_group = pygame.sprite.Group()
oking_group = pygame.sprite.Group()
oqueen_group = pygame.sprite.Group()


tile_map = [
    [0, 0,  0,  0,  0,   0,  0, 0,   0, 0, 0, 0, 0, 0, 0],
    [0, 0,  0,  0,  0,   0,  0, 0,   0, 0, 0, 0, 0, 0, 0],
    [0, 12, 13, 14, 16, 15, 13, 12, 12, 0, 0, 0, 0, 0, 0],  # Edge of Board
    [0, 11, 11, 11, 11, 11, 11, 11, 11, 0, 0, 0, 0, 0, 0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 0],
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 0],
    [0, 5,  5,  5,  5,  5,  5,  5,  5,  0, 0, 0, 0, 0, 0],
    [0, 6,  9,  4,  8,  7,  4,  9,  6,  0, 0, 0, 0, 0, 0],  # Edge of Board
    [0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 0],
]

####################################################################################
################# Place Chess Pieces According to Tile Map Placement ###############
####################################################################################
for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        """We are multiplying j by 64 since each main tile has a height of 64 pixels"""
        """We are multiplying i by 64 since each main tile has a height of 64 pixel"""
        if tile_map[i][j] == 4:
            Piece(j*64, i*64, 4, piece_group, bishop_group)
        if tile_map[i][j] == 5:
            Piece(j*64, i*64, 5, piece_group, pawn_group)
        if tile_map[i][j] == 6:
            Piece(j*64, i*64, 6, piece_group, rook_group)
        if tile_map[i][j] == 7:
            Piece(j*64, i*64, 7, piece_group, queen_group)
        if tile_map[i][j] == 8:
            Piece(j*64, i*64, 8, piece_group, king_group)
        if tile_map[i][j] == 9:
            Piece(j*64, i*64, 9, piece_group, knight_group)
        if tile_map[i][j] == 11:
            Piece(j*64, i*64, 11, op_group, opawn_group)
        if tile_map[i][j] == 12:
            Piece(j*64, i*64, 12, op_group, orook_group)
        if tile_map[i][j] == 13:
            Piece(j*64, i*64, 13, op_group, oknight_group)
        if tile_map[i][j] == 14:
            Piece(j*64, i*64, 14, op_group, obishop_group)
        if tile_map[i][j] == 15:
            Piece(j*64, i*64, 15, op_group, oking_group)
        if tile_map[i][j] == 16:
            Piece(j*64, i*64, 16, op_group, oqueen_group)

##################################################################################
##################Create Game Object to Utilize in Game Loop######################
##################################################################################
chess_game = Game(main_tile_group, piece_group)


##################################################################################
##################################MAIN GAME LOOP##################################
##################################################################################
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """""""""""""""""""""""""""""""""Movement"""""""""""""""""""""""""""""""""
        if event.type == pygame.MOUSEBUTTONDOWN:    # If user clicks on something
            position = pygame.mouse.get_pos()
            x = position[0]
            y = position[1]
            if event.button == 1:                   # If the mouse click is due to left button click
                for mouse in piece_group:           # Checks for mouse clicks on user pieces
                    # If mouse click occurs on a user piece
                    if mouse.rect.collidepoint(position):
                        mouse.clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            for mouse in piece_group:
                mouse.clicked = False               # User is no longer draggin piece

                bop_sound = pygame.mixer.Sound("jump_sound.wav")
                bop_sound.play()

            """""Attempting to center the piece on a tile. Currently a flop"""
            # for placement in main_tile_group:
            #    placement.rect.x = position[0] - (placement.rect.width//2)
            #    placement.rect.y = position[1] - (placement.rect.height//2)

    """""""Defines what happens when boolean key.clicked is True"""""""""
    for mouse in piece_group:
        if mouse.clicked == True:
            position = pygame.mouse.get_pos()
            # Place the mouse in the center of the user piece when clicked
            mouse.rect.x = position[0]-(mouse.rect.width//2)
            mouse.rect.y = position[1]-(mouse.rect.height//2)

    # Fill the display
    display_screen.fill((0, 0, 0))
    # Draw the tiles onto the screen
    main_tile_group.draw(display_screen)
    piece_group.draw(display_screen)
    op_group.draw(display_screen)
    chess_game.draw()
    chess_game.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

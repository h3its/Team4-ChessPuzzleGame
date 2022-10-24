import pygame

pygame.init()


# Set display screen
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 704
display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Trial!")

clock = pygame.time.Clock()

###################################################################################


class Game():
    """Class to control gameplay"""

    def __init__(self, board, piece_group):
        """Initialize game object"""
        self.round_time = 0  # $

        self.board = board
        self.piece_group = piece_group

        # Set font
        self.font = pygame.font.SysFont('arial', 28)

    def draw(self):
        "Function to Draw the text onto the display_screen when called"
        # SET COLORS
        WHITE = (255, 255, 255)
        BLUE = (0, 255, 0)
        GREEN = (0, 0, 255)
        RED = (255, 0, 0)
        YELLOW = (243, 157, 20)
        PURPLE = (255, 255, 0)
        BLACK = (0, 0, 0)

        # Set text
        time_text = self.font.render(
            "Time: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (10, 70)

        # Blit the text on the display_screen
        display_screen.blit(time_text, time_rect)
###################################################################################

###################################################################################
###MAIN BOARD CLASS###
# Tile class creates individual tiles and places them on display_screen according
# to tile map


class Tile(pygame.sprite.Sprite):
    """This method takes in the parameters: x-coordinate, y-coordinate, tile integer,"""
    """the group , and the specific containing all groups, and the specific group that"""
    """tile belongs to"""

    def __init__(self, x, y, tile_int, main_group, spec_group):
        super().__init__()
        # Input correct image into correct group
        if tile_int == 1:
            self.image = pygame.image.load("lime_tile.png")
            spec_group.add(self)
        elif tile_int == 2:
            self.image = pygame.image.load("green_tile.png")
            spec_group.add(self)
        elif tile_int == 3:
            self.image = pygame.image.load("brown_tile.png")
            spec_group.add(self)

        # Add all tiles to the main group
        main_group.add(self)

        # Get rect of each image and position them
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


###CREATE SPRITE GROUPS###
main_tile_group = pygame.sprite.Group()
green_tile_group = pygame.sprite.Group()
lime_tile_group = pygame.sprite.Group()
brown_tile_group = pygame.sprite.Group()

# Create the tile map: 0 --> empty, 1 --> lime green, 2 --> green, 3 --> time
# 11 rows, 12 columns
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
# One for loop will loop through the rows
# One for loop will loop through the columns
for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        """We are multiplying j by 64 since each tiles has a height of 64 pixels"""
        """We are multiplying i by 64 since each tile has a height of 64 pixel"""
        if tile_map[i][j] == 1:
            Tile(j*64, i*64, 1, main_tile_group, green_tile_group)
        elif tile_map[i][j] == 2:
            Tile(j*64, i*64, 2, main_tile_group, lime_tile_group)
        elif tile_map[i][j] == 3:
            Tile(j*64, i*64, 3, main_tile_group, brown_tile_group)
##################################################################################


##################################################################################
###CHESS PIECE CLASS###
###################################################################################
class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_int, piece_group, spec_group):
        super().__init__()
        if tile_int == 4:
            self.image = pygame.image.load("bishop.png")
            spec_group.add(self)
        elif tile_int == 5:
            self.image = pygame.image.load("pawn.png")
            spec_group.add(self)
        elif tile_int == 6:
            self.image = pygame.image.load("rook.png")
            spec_group.add(self)
        elif tile_int == 7:
            self.image = pygame.image.load("queen.png")
            spec_group.add(self)
        elif tile_int == 8:
            self.image = pygame.image.load("king.png")
            spec_group.add(self)
        elif tile_int == 9:
            self.image = pygame.image.load("knight.png")
            spec_group.add(self)

        piece_group.add(self)

        # Get rect of each image and position them
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


###CREATE SPRITE GROUPS###
piece_group = pygame.sprite.Group()
queen_group = pygame.sprite.Group()
king_group = pygame.sprite.Group()
bishop_group = pygame.sprite.Group()
pawn_group = pygame.sprite.Group()
rook_group = pygame.sprite.Group()
knight_group = pygame.sprite.Group()

tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Edge of Board
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0],
    [0, 6, 9, 4, 8, 7, 4, 9, 6, 0, 0, 0, 0, 0, 0],  # Edge of Board
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# One for loop will loop through the columns
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
##################################################################################
chess_game = Game(main_tile_group, piece_group)

##################################################################################
###MAIN GAME LOOP###
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    # Fill the display
    display_screen.fill((0, 0, 0))
    # Draw the tiles onto the screen
    main_tile_group.draw(display_screen)
    piece_group.draw(display_screen)
    chess_game.draw()
    pygame.display.update()
    clock.tick()

pygame.quit()

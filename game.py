import pygame

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 704
display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Trial!")

FPS = 60
clock = pygame.time.Clock()

####################################################################################
##############################Class Controls Gameplay###############################
####################################################################################


class Game():

    def __init__(self, board, piece_group):
        """Initialize game object"""
        self.round_time = 0
        self.frame_count = 0

        self.board = board
        self.piece_group = piece_group

        # Set font
        self.lilFont = pygame.font.SysFont('arial', 28)
        self.bigFont = pygame.font.SysFont('arial', 48)

    def update(self):
        self.frame_count += 1
        if FPS == self.frame_count:
            self.round_time += 1
            self.frame_count = 0

    def draw(self):
        "Function to Draw the text onto the display_screen when called"
        # SET COLORS
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        LIME = (120, 252, 140)
        GREEN = (40, 180, 76)
        RED = (255, 0, 0)
        YELLOW = (243, 157, 20)
        PURPLE = (255, 255, 0)
        BLACK = (0, 0, 0)

        # Set text
        level_text = self.bigFont.render("Level 8", True, WHITE)
        level_rect = level_text.get_rect()
        level_rect.topright = (384, 50)
        time_text = self.lilFont.render(
            "Time: " + str(self.round_time) + " seconds", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 96, 70)
        customize_text = self.lilFont.render(
            "Customize Tile 1", True, BLACK, LIME)
        customize_rect = customize_text.get_rect()
        customize_rect.topright = (WINDOW_WIDTH - 96, 210)

        # Blit the text on the display_screen
        display_screen.blit(time_text, time_rect)
        display_screen.blit(level_text, level_rect)
        display_screen.blit(customize_text, customize_rect)

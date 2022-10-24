import pygame

pygame.init()


# Set display screen
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 704
display_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Trial!")

clock = pygame.time.Clock()

###################################################################################


###################################################################################
############################## MAIN BOARD CLASS ###################################
###################################################################################

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

        # Add all tiles to the main group
        main_group.add(self)

        # Get rect of each image and position them
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


###CREATE SPRITE GROUPS###
main_tile_group = pygame.sprite.Group()
green_tile_group = pygame.sprite.Group()
lime_tile_group = pygame.sprite.Group()

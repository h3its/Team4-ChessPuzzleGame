import pygame
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
        elif tile_int == 11:
            self.image = pygame.image.load("opawn.png")
            spec_group.add(self)
        elif tile_int == 12:
            self.image = pygame.image.load("orook.png")
            spec_group.add(self)
        elif tile_int == 13:
            self.image = pygame.image.load("oknight.png")
            spec_group.add(self)
        elif tile_int == 14:
            self.image = pygame.image.load("obishop.png")
            spec_group.add(self)
        elif tile_int == 15:
            self.image = pygame.image.load("oking.png")
            spec_group.add(self)
        elif tile_int == 16:
            self.image = pygame.image.load("oqueen.png")
            spec_group.add(self)

        piece_group.add(self)

        # Get rect of each image and position them
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.clicked = False                # Checks if user clicked on sprite
        self.rect.topleft = (x+16, y+16)

    def update(self):
        pass

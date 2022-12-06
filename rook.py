"""
Represents a chess Rook
"""

from piece import Piece

class Rook(Piece):

    def __init__(self, col, game_def):
        super().__init__(col, game_def)

    """
    Uses the Piece draw method and passes an image to use
    """
    def draw(self, win):
        super()._draw(win, self.game_def['ROOK_PIC'])

    def draw_while_moving(self, win):
        super().draw_while_moving(win, self.game_def['ROOK_PIC'])

    """
    Makes the Rook print "R" in any string representation
    """
    def __repr__(self):
        return "R"

    """
    Checks to see if this rook can attack any other pieces on the board
    """
    def check_attacks(self, board, row, col):
        # check to see if there is a piece in the same row
        for c in range(len(board[0])):
            if c != col and board[row][c] != 0:
                return False

        # check to see if there is a piece in the same col
        for r in range(len(board)):
            if r != row and board[r][col] != 0:
                return False

        return True







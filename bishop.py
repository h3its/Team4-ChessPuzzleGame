"""
Represents a chess Bishop
"""

from piece import Piece

class Bishop(Piece):

    def __init__(self, col, game_def):
        super().__init__(col, game_def)

    """
    Uses the Piece draw method and passes an image to use
    """
    def draw(self, win):
        super()._draw(win, self.game_def['BISHOP_PIC'])

    def draw_while_moving(self, win):
        super().draw_while_moving(win, self.game_def['BISHOP_PIC'])

    """
    Makes the Bishop print "B" in any string representation
    """
    def __repr__(self):
        return "B"

    """
    Checks to see if this queen can attack any other pieces on the board
    """
    def check_attacks(self, board, row, col):
        # check to see if there is a piece in the upper left diagonal
        for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[r][c] != 0:
                return False

        # check to see if there is a piece in the lower left diagonal
        for r, c in zip(range(row+1, len(board)), range(col-1, -1, -1)):
            if board[r][c] != 0:
                return False

        # check to see if there is a piece in the upper right diagonal
        for r, c in zip(range(row-1, -1, -1), range(col+1, len(board[0]))):
            if board[r][c] != 0:
                return False

        # check to see if there is a piece in the lower right diagonal
        for r, c in zip(range(row+1, len(board)), range(col+1, len(board[0]))):
            if board[r][c] != 0:
                return False

        return True







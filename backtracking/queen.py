"""
Represents a chess Queen
"""

from piece import Piece

class Queen(Piece):

    def __init__(self):
        super().__init__()

    """
    Makes the Queen print "Q" in any string representation
    """
    def __repr__(self):
        return "Q"

    """
    Checks to see if this queen can attack any other pieces on the board
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







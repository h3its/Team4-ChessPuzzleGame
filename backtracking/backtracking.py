from queen import Queen
from rook import Rook
from bishop import Bishop


# Currently, MUST ROWS == COLS
ROWS = 6
COLS = 6
NUM_PIECES = 6

board = []
pieces = []

# I believe this will work more reliably when pieces are in descendingly-movable order
# HOWEVER it is not currently guaranteed to work if pieces are not all of same type
def setup_pieces():
    pieces.append(Bishop())
    pieces.append(Bishop())
    pieces.append(Bishop())
    pieces.append(Rook())
    pieces.append(Rook())
    pieces.append(Rook())

def print_board():
    for row in range(ROWS):
        print(*board[row])

def solve_helper(board, col, piece_num):

    if piece_num >= NUM_PIECES:
        return True

    for row in range(ROWS):

        if pieces[piece_num].check_attacks(board, row, col):
            board[row][col] = pieces[piece_num]
            pieces[piece_num].set_pos(row, col)

            for i in range(piece_num):
                if not pieces[i].check_attacks(board, pieces[i].row, pieces[i].col):
                    return False

            if solve_helper(board, col + 1, piece_num + 1):
                return True

            board[row][col] = 0
            pieces[piece_num].set_pos(-1, -1)

    return False


def solve():

    setup_pieces()

    for row in range(ROWS):
        board.append([])

    for row in range(ROWS):
        for col in range(COLS):
            board[row].append(0)

    if not solve_helper(board, 0, 0):
        print("Solution does not exist")
        return False

    print_board()
    return True

solve()
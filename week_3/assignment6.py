import numpy as np
from itertools import chain

NONE = '.'
RED = 'R'
YELLOW = 'Y'
FOUR = 4

# when FOUR times Y/R in a row is found, use this to print team name
Y = "Yellow"
R = "Red"


def lstCheckEqual(lst):
    return lst.count(lst[0]) == len(lst)


class Game:
    def __init__ (self, cols = 7, rows = 6):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.board = [[NONE] * rows for _ in range(cols)]
        self.four_red = [RED] * FOUR
        self.four_yellow = [YELLOW] * FOUR

    def insert (self, column, color):
        """Insert the color in the given column."""
        c = self.board[column]
        if c[0] != NONE:
            raise ColumnFullException("Selected column was already filled")
        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = color
        self.__checkForWin()

    def print_board (self):
        """Print the board."""
        print(' '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print(' '.join(str(self.board[x][y]) for x in range(self.cols)))
            print()

    def __checkForWin(self):
        """Check the current board for a winner."""
        didSomeoneWin = self.__checkNInARow(FOUR)
        if didSomeoneWin:
            self.print_board()
            print(FOUR, "in a row!\n", didSomeoneWin, "won!")
            exit()

    def __getRowsToCheck(self, npBoard):
        posdiag = [
            list(np.diagonal(npBoard, i))
                for i in range((self.rows * -1)+1, self.cols)
        ]
        npBoard = np.fliplr(npBoard)
        negdiag = [
            list(np.diagonal(npBoard, i))
                for i in range((self.rows * -1)+1, self.cols)
        ]
        rows = npBoard.tolist()
        cols = npBoard.transpose().tolist()
        return (rows, cols, posdiag, negdiag)

    def __checkNInARow(self, nInARow):
        npBoard = np.array(self.board)
        rowsToCheck = self.__getRowsToCheck(npBoard)
        for lst in chain(*rowsToCheck):
            lst = [x for x in lst if x != NONE] # remove all NONE's from the list
            if not lst: # list is empty (leftovers from diagonal checks)
                continue
            # I did not understand this part, so I did the code my own way.
            # for i in range(len(lst)-n+1):
            #     print("i in len(lst)-n+1: ",i, len(lst)-n+1)
            if lst[0] != NONE and len(lst) == nInARow and lstCheckEqual(lst):
                return Y if lst[0] == YELLOW else R

class ColumnFullException(Exception):
    def __init__(self, message):
        self.message = message

if __name__ == '__main__':
    g = Game()
    turn = RED
    while True:
        error = False
        g.print_board()
        row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))

        try:
            g.insert(int(row), turn)
        except ColumnFullException as err:
            print(err.message)
            continue # skip the part where turns are switched.

        turn = YELLOW if turn == RED else RED

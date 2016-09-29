NONE = '.'
RED = 'R'
YELLOW = 'Y'
FOUR = 4

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
            raise Exception
        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = color

    def print_board (self):
        """Print the board."""
        print(' '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print(' '.join(str(self.board[x][y]) for x in range(self.cols)))
            print()

if __name__ == '__main__':
    g = Game()
    turn = RED
    while True:
        error = False
        g.print_board()
        row = input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
        g.insert(int(row), turn)
        turn = YELLOW if turn == RED else RED

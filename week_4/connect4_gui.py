from tkinter import Tk, Button, Frame, Canvas, font, Toplevel, Message
from itertools import chain
import numpy as np

""" Warning/Notice!
Bad code ahead, do not do this at home kids..
"""

# when FOUR times Y/R in a row is found, use this to print winners name
Y = "Yellow"
R = "Red"

# old variables
NONE = '.'
RED = 'R'
YELLOW = 'Y'
FOUR = 4

STARTING_PLAYER = RED

class Game:
    def __init__ (self, cols = 7, rows = 6):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.board = [[NONE] * rows for _ in range(cols)]
        self.four_red = [RED] * FOUR
        self.four_yellow = [YELLOW] * FOUR
        self.turn = RED
        self.gameWinner = None

    def lstCheckEqual(self, lst):
        return lst.count(lst[0]) == len(lst)

    def insert (self, column):
        """Insert the color in the given column."""
        c = self.board[column]
        if c[0] != NONE:
            raise ColumnFullException("Selected column was already filled")
        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = self.turn
        self.__checkForWin()
        self.updateTurn()

    def updateTurn(self):
        self.turn = YELLOW if self.turn == RED else RED

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
            #self.gameWinner = didSomeoneWin
            self.print_board()
            self.gameWinner = str(FOUR)+" in a row!\n"+didSomeoneWin+" won!"
            # exit()

    def __getRowsToCheck(self):
        npBoard = np.array(self.board)
        posdiag = [
            list(np.diagonal(npBoard, i))
                for i in range((self.rows * -1)+1, self.cols)
        ]
        npBoard = np.fliplr(npBoard)
        negdiag = [
            list(np.diagonal(npBoard, i))
                for i in range((self.rows * -1)+1, self.cols)
        ]
        npBoard = np.fliplr(npBoard)
        rows = npBoard.tolist()
        cols = npBoard.transpose().tolist()
        return (rows, cols, posdiag, negdiag)

    def __checkNInARow(self, nInARow):
        rowsToCheck = self.__getRowsToCheck()
        for lst in chain(*rowsToCheck):
            lst = [x for x in lst if x != NONE] # remove all NONE's from the list
            if not lst: # list is empty (leftovers from diagonal checks)
                continue
            tempWinner = None
            i = 0
            for item in lst:
                if item == YELLOW:
                    if tempWinner == R: i = 0; # Break streak because prev was Y
                    tempWinner = Y
                    i += 1
                elif item == RED:
                    if tempWinner == Y: i = 0; # Break streak because prev was R
                    tempWinner = R
                    i += 1
                if i >= FOUR:
                    return tempWinner

class ColumnFullException(Exception):
    def __init__(self, message):
        self.message = message

class GameGui:
    def __init__(self):
        self.game = Game() # depend on Game to do our logic
        self.guiRoot = Tk()
        self.guiRoot.title("Connect4")
        self.guiRoot.resizable(width=False, height=False)
        self.colButtons = {}
        self.frame = Frame(self.guiRoot, bd=1, relief="raised")
        self.tiles = {}
        self.drawColumnButtons()
        self.drawNewGameBtn()
        self.drawBoard()

    def newGame(self):
        pass # TODO: redraw gui and call new game on self.game..

    def drawNewGameBtn(self):
        self.newGameBtn = Button(self.guiRoot, command=lambda: self.newGameCallback(),\
            text='new game')
        self.newGameBtn.grid(row=2, column=0, columnspan=self.game.cols, sticky="WE")

    def insertCallback(self, column):
        self.game.insert(column)
        self.drawBoard()
        self.toggleColBtnStateDependingOnRows()
        self.checkForWinner()

    def checkForWinner(self):
        if self.game.gameWinner:
            self.disableAllColumnButtons()
            self.drawWinnerText()

    def drawWinnerText(self):
        top = Toplevel()
        top.config(bg="white")
        top.title(str(FOUR)+" in a row!")
        top.resizable(width=False, height=False)
        Message(top, bg="white", fg="black", text=self.game.gameWinner,
            width=200, padx=20, pady=20).pack()
        Button(top, text="Close", command=top.destroy).pack()

    def disableAllColumnButtons(self):
        for btn in self.colButtons:
            self.colButtons[btn]['state'] = 'disabled'

    def newGameCallback(self):
        self.game = Game() # simply recreate the Game object from scratch
        self.drawBoard()
        self.toggleColBtnStateDependingOnRows()

    def drawBoard(self):
        self.frame.grid(row=1, column=0, columnspan=self.game.cols)
        self.prepareTiles()
        for col in range(self.game.cols):
            for row in range(self.game.rows):
                value = self.game.board[col][row]
                self.drawTileByStringValue(col, row, value)

    def toggleColBtnStateDependingOnRows(self):
        """ disable or enable column button(s) depending on their rows being filled """
        for colIndex in range(self.game.cols):
            if self.game.board[colIndex][-self.game.rows] == NONE:
              self.colButtons[colIndex]['state'] = 'normal'
            else:
              self.colButtons[colIndex]['state'] = 'disabled'

    def drawTileByStringValue(self, tileCol, tileRow, strValue):
        if strValue == YELLOW:
            tileFillColor = "yellow"
        elif strValue == RED:
            tileFillColor = "red"
        else:
            tileFillColor = "gray"

        self.tiles[tileCol, tileRow].create_oval(10, 5, 50, 45,\
            fill=tileFillColor, width=1)

    def prepareTiles(self):
        for col in range(self.game.cols):
            for row in range(self.game.rows):
                tile = Canvas(self.frame, width=60, height=50, bg="SkyBlue1",\
                    highlightthickness=0)
                tile.grid(row=row, column=col)
                self.tiles[col, row] = tile

    def drawColumnButtons(self):
        for colIndex in range(self.game.cols):
            cmdHandler = lambda x=colIndex: self.insertCallback(x)
            btn = Button(self.guiRoot, command=cmdHandler, \
                font=font.Font(family="Helvetica", size=14), text=colIndex+1)
            btn.grid(row=0, column=colIndex, sticky="WE")
            self.colButtons[colIndex] = btn

    def mainloop(self):
        self.guiRoot.mainloop()

if __name__ == '__main__':
    GameGui().mainloop()

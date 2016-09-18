from random import randint

BOARD_SIZE = 4
NR_GUESSES = 4

def getUserInputCoords():
    while True:
        inputMax = str(BOARD_SIZE-1)
        userGuess = input("[0-"+inputMax+"].[0-"+inputMax+"]: ")
        inputCoords = userGuess.split('.')
        try:
            if len(inputCoords) > 2: raise ValueError
            inputCoords[0] = int(inputCoords[0])
            inputCoords[1] = int(inputCoords[1])
        except ValueError:
            print("Incorrect input: ", inputCoords, "\nPlease try again " \
                "with the format: row.column")
            continue
        break
    return inputCoords

def print_board(board):
    for row in board:
        print(" ".join(row))

#initializing board
board = []

for x in range(BOARD_SIZE):
    board.append(['O'] * BOARD_SIZE)

#start the game and printing the board
print("Let's play Battleship!")
print_board(board)
print("\n")

#define where the ship is
ship_row = randint(1, BOARD_SIZE-1)
ship_col = randint(1, BOARD_SIZE-1)

# initialize empty userGuesses list to remember previous guesses
oldGuesses = []
# simple boolean to check whether the game has been won
wonGame = False

while len(oldGuesses) != NR_GUESSES:
    #print("cheat.., um debugging: ", ship_row,'.', ship_col)

    # ask user for guess
    print("Please choose a coordinate to strike.")
    newGuess = getUserInputCoords()

    # check if the user was right
    if newGuess == [ship_row, ship_col]:
        print("It's a hit! You've sunk the enemies ship!")
        board[newGuess[0]][newGuess[1]] = 'H'
        wonGame = True
    elif max(newGuess) > BOARD_SIZE-1 or min(newGuess) < 0:
        print("Your strike is outside of the boundaries.")
    elif newGuess in oldGuesses:
        print("You've already striken this area.")
    else:
        print("The strike area was occupied by nothing but water!")
        board[newGuess[0]][newGuess[1]] = 'X'

    oldGuesses.append(newGuess)
    if wonGame: break
    print_board(board)
    print("You are on turn: ", len(oldGuesses) + 1)

print("\n")
wonGame = "won!" if wonGame else "lost!"
print("Game Over! You " + wonGame, "\n" \
    "Amount of turns used: ", len(oldGuesses), "\n" \
    "End of game board: ")
print_board(board)

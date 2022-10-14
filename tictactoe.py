# Build a Tic Tac Toe game in python
# - 2 Human players
# - One player selects a space. If the space is not taken then the space is assigned with X or O depending on the player
# - If the space is taken then the user is asked to choose a different space
# - Display the state of the board to the players after each move
# - You will likely want to check for a win condition after each turn instead of waiting until the end
# - Make sure that all win conditions are checked for (row, column, diagonal)
# - Display the winner to the users unless game is a tie, in which case just display that it was a tie.

# Bonus points:
# - Add ability to start over after game is finished without having to run the program again
# - Make the game have an Ai that can play a single human player


# game board displays as 3x3 grid
# store data for 9 positions of the game board
# gather user input that translates into a change in a position of the game board
# check for a win


DEFAULTSPACE = "[ ]"
XGAMEPIECE = " X "
OGAMEPIECE = " O "
WINMESSAGE = "\n        Victory!"
DRAWMESSAGE = "\n          Draw!"


gameBoard = []

for _ in range(9):
    gameBoard.append(DEFAULTSPACE)


def displayBoard():
    print("\n", gameBoard[0:3], "     ", [1, 2, 3],
          "\n", gameBoard[3:6], "     ", [4, 5, 6],
          "\n", gameBoard[6:10], "     ", [7, 8, 9],
          "\n")


def checkPlay(userMove, userGamePiece):
    userMove = int(userMove)
    gameBoard[userMove - 1] = userGamePiece


def checkWin(gameBoard):
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[0] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    if gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] != DEFAULTSPACE:
        print(WINMESSAGE)
        return True
    else:
        spaces = 0
        for space in gameBoard:
            if space != DEFAULTSPACE:
                spaces += 1
        if spaces == 9:
            print(DRAWMESSAGE)
            return True
        return False


def aiMove():
    if gameBoard[4] == DEFAULTSPACE:
        gameBoard[4] = OGAMEPIECE
    elif gameBoard[0] == DEFAULTSPACE:
        gameBoard[0] = OGAMEPIECE
    elif gameBoard[2] == DEFAULTSPACE:
        gameBoard[2] = OGAMEPIECE
    elif gameBoard[6] == DEFAULTSPACE:
        gameBoard[6] = OGAMEPIECE
    elif gameBoard[8] == DEFAULTSPACE:
        gameBoard[8] = OGAMEPIECE
    elif gameBoard[1] == DEFAULTSPACE:
        gameBoard[1] = OGAMEPIECE
    elif gameBoard[3] == DEFAULTSPACE:
        gameBoard[3] = OGAMEPIECE
    elif gameBoard[5] == DEFAULTSPACE:
        gameBoard[5] = OGAMEPIECE
    elif gameBoard[7] == DEFAULTSPACE:
        gameBoard[7] = OGAMEPIECE


def userXturn():
    userXvalid = False
    while userXvalid is not True:
        userX = input("User X. Enter position #: ")

        try:
            int(userX)
            userXvalid = True
        except ValueError:
            print("\nNOT A VALID CHOICE. Please try again.\n")

    checkPlay(userX, XGAMEPIECE)


def twoPlayer():
    playerWin = False
    while playerWin is False:
        userXturn()
        playerWin = checkWin(gameBoard)
        displayBoard()
        if playerWin is True:
            break

        userO = input("User O. Enter position #: ")

        try:
            int(userO)
        except ValueError:
            print("\nNOT A VALID CHOICE. Please try again.\n")
            continue

        checkPlay(userO, OGAMEPIECE)

        playerWin = checkWin(gameBoard)
        displayBoard()
        if playerWin is True:
            break


def onePlayer():
    playerWin = False
    while playerWin is False:
        userX = input("User X. Enter position #: ")

        checkPlay(userX, XGAMEPIECE)
        playerWin = checkWin(gameBoard)
        displayBoard()
        if playerWin is True:
            break

        aiMove()

        playerWin = checkWin(gameBoard)
        displayBoard()
        if playerWin is True:
            break


print("\n      Tic Tac Toe")
displayBoard()
gameType = input("(1) player or (2) player? Enter #: ")
if gameType == "2":
    twoPlayer()
else:
    onePlayer()

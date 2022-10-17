DEFAULTSPACE = "[ ]"
XGAMEPIECE = " X "
OGAMEPIECE = " O "
XWINMESSAGE = "\n     Victory for X!"
OWINMESSAGE = "\n     Victory for O!"
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


def checkWin(gameBoard, gamePiece, winMessage):
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[0] == gamePiece and gameBoard[0] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] == gamePiece and gameBoard[3] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] == gamePiece and gameBoard[6] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] == gamePiece and gameBoard[0] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] == gamePiece and gameBoard[1] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] == gamePiece and gameBoard[2] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] == gamePiece and gameBoard[0] != DEFAULTSPACE:
        print(winMessage)
        return True
    if gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] == gamePiece and gameBoard[2] != DEFAULTSPACE:
        print(winMessage)
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


def userTurn(gamePiece):
    userTurnValid = False
    while userTurnValid is not True:
        playerMove = input("User " + gamePiece + ". " "Enter position #: ")

        try:
            if int(playerMove) > 0 and int(playerMove) < 10:
                userTurnValid = True
            else:
                print("\nNOT A VALID CHOICE. Please try again.\n")

        except:
            print("\nNOT A VALID CHOICE. Please try again.\n")

    checkPlay(playerMove, gamePiece)


def twoPlayer():
    playerWin = False
    while playerWin is False:
        userTurn(XGAMEPIECE)
        playerWin = checkWin(gameBoard, XGAMEPIECE, XWINMESSAGE)
        displayBoard()
        if playerWin is True:
            break

        userTurn(OGAMEPIECE)
        playerWin = checkWin(gameBoard, OGAMEPIECE, OWINMESSAGE)
        displayBoard()
        if playerWin is True:
            break


def onePlayer():
    playerWin = False
    while playerWin is False:
        userTurn(XGAMEPIECE)
        playerWin = checkWin(gameBoard, XGAMEPIECE, XWINMESSAGE)
        displayBoard()
        if playerWin is True:
            break

        aiMove()

        playerWin = checkWin(gameBoard, OGAMEPIECE, OWINMESSAGE)
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

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
# check for a win after 5 user inputs and thereafter


# area1 = ("-")
# area2 = ("-")
# area3 = ("-")
# area4 = ("-")
# area5 = ("-")
# area6 = ("-")
# area7 = ("-")
# area8 = ("-")
# area9 = ("-")

# gameBoard = [area1, area2, area3, area4, area5, area6, area7, area8, area9]

# for x in gameBoard:
#     print(gameBoard)


# # print("\n", area1, area2, area3,
# #       "\n", area4, area5, area6,
# #       "\n", area7, area8, area9,)


# # userX = input("User X enter row and column: ")
# # if userX = "11":


gameBoard = []


for x in range(9):
    gameBoard.append("[ ]")


def displayBoard():
    print("\n", gameBoard[0:3], "     ", [1, 2, 3],
          "\n", gameBoard[3:6], "     ", [4, 5, 6],
          "\n", gameBoard[6:10], "     ", [7, 8, 9],
          "\n")


def checkPlay(userMove, userGamePiece):
    if userMove == ("1"):
        gameBoard[0] = userGamePiece
    if userMove == ("2"):
        gameBoard[1] = userGamePiece
    if userMove == ("3"):
        gameBoard[2] = userGamePiece
    if userMove == ("4"):
        gameBoard[3] = userGamePiece
    if userMove == ("5"):
        gameBoard[4] = userGamePiece
    if userMove == ("6"):
        gameBoard[5] = userGamePiece
    if userMove == ("7"):
        gameBoard[6] = userGamePiece
    if userMove == ("8"):
        gameBoard[7] = userGamePiece
    if userMove == ("9"):
        gameBoard[8] = userGamePiece


print("\n     TicTacToe")
displayBoard()

for x in range(5):
    userX = input("User X. Enter position number: ")

    checkPlay(userX, " X ")
    displayBoard()

    userO = input("User O. Enter position number: ")

    checkPlay(userO, " O ")
    displayBoard()

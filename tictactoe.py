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
    gameBoard.append("[]")

print("\n", gameBoard[0:3],
      "\n", gameBoard[3:6],
      "\n", gameBoard[6:10])

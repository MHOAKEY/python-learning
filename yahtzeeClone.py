# Build a Yahtzee game clone

# Game will roll 5 dice (generate 5 random numbers between 1-6)

# Game will then figure out best possible combination:

# Yahtzee
# Full House
# Large Straight
# Small Straight
# Four of a Kind
# Three of a Kind
# Two Pair
# One Pair

# and display to the user the best combination they have rolled.

import random


diceArray = []


for x in range(5):
    diceArray.append(random.randrange(1, 6))


def checkDice(diceArray):
    diceArray.sort()
    if diceArray[1] == diceArray[4]:
        return "Yahztee!"
    if diceArray[0] == diceArray[1] and diceArray[0] != diceArray[2] and diceArray[2] == diceArray[4] \
            or diceArray[0] == diceArray[2] and diceArray[0] != diceArray[3] and diceArray[3] == diceArray[4]:
        return "Full house"
    if diceArray[0] == 2 and diceArray[1] == 3 and diceArray[2] == 4 \
            and diceArray[3] == 5 and diceArray[4] == 6:
        return "Large straight"
    if diceArray[0] == 1 and diceArray[1] == 2 and diceArray[2] == 3 \
            and diceArray[3] == 4 and diceArray[4] == 5:
        return "Small straight"
    if diceArray[0] == diceArray[3] \
            or diceArray[1] == diceArray[4]:
        return "4 of a kind"
    if diceArray[0] == diceArray[2] \
        or diceArray[1] == diceArray[3] \
            or diceArray[2] == diceArray[4]:
        return "3 of a kind"
    if diceArray[0] == diceArray[1] and diceArray[2] == diceArray[3] \
        or diceArray[0] == diceArray[1] and diceArray[3] == diceArray[4] \
            or diceArray[1] == diceArray[2] and diceArray[3] == diceArray[4]:
        return "2 pairs"
    if diceArray[0] == diceArray[1] or diceArray[1] == diceArray[2] \
            or diceArray[2] == diceArray[3] or diceArray[3] == diceArray[4]:
        return "1 pair"
    else:
        return "Chance?"


print("Dice Rolled: ", diceArray)
print("")
print("Dice sorted: ", sorted(diceArray))
print("")
print("You have:     ", checkDice(diceArray))

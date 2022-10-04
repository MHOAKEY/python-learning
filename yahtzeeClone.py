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


def checkOnePair(diceArray):
    sorted(diceArray)
    if (diceArray[0] == diceArray[1]) or (diceArray[1] == diceArray[2]) or (diceArray[2] == diceArray[3]) or (diceArray[3] == diceArray[4]) or (diceArray[4] == diceArray[5]):
        return "You have 1 pair"
    else:
        return "No Pairs"


print(diceArray)
print("")
print(sorted(diceArray))
print("")
print(checkOnePair)

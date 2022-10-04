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

print(diceArray)
print("")
print(sorted(diceArray))

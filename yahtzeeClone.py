# Build a Yahtzee game clone

# Game will roll 6 dice (generate 6 random numbers between 1-6)
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

for x in range(6):
    print(random.randrange(1, 6))

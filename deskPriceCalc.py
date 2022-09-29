# Create a program that calculates the price for custom desks
# The program will take specifications from the user:
# length, width, wood type (mahogany, oak, pine), and how many drawers

# There is a minimum cost of $200 for any desk

# There is a large surface additional cost of $50 if the surface is over 750 square inches

# Mahogany has an additional cost of $150,
# Oak has an additional cost of $125,
# and Pine is free.
# Drawers cost $30 each

# the program should take all the inputs from the user and then display the price for the custom desk.


from operator import le


length = input("How many inches is the desired LENGTH of your desk?: ")

width = input("How many inches is the desired WIDTH of your desk?: ")

woodType = input("Mahogany, Oak or Pine?: ")

drawerCount = input("How many drawers would you lile?: ")

minimumCost = 200

drawers = 30

mahogany = 150

oak = 125

pine = 0

drawers = 30

largeSurface = length * width

cost =

print()

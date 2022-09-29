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

MAHOGANY = 150
OAK = 125
PINE = 0

length = float(input("How many inches is the desired LENGTH of your desk?: "))

width = float(input("\nAn additional cost of $50 will apply if your desk is greater than \n750 sqaure inches.\
    \nHow many inches is the desired WIDTH of your desk?: "))

woodType = input("Mahogany is an additional $150\
        \nOak is an additional $125\
        \nPine is included for $0\
        \nWhich wood type would you like?: ")

woodType = woodType.lower()

if woodType == "mahogany":
    woodType = MAHOGANY

elif woodType == "oak":
    woodType = OAK

elif woodType == "pine":
    woodType = PINE

drawerCount = int(input("How many drawers would you like?: "))

minimumCost = 200

drawerCost = drawerCount * 30

cost = minimumCost + drawerCost + woodType

if length * width >= 750:
    cost = minimumCost + drawerCost + woodType + 50

print("Your desk will cost", cost)

# Build a program that can take in imperial lengths and convert them to metric
# Program will take inputs from the user for:
# miles
# yards
# feet
# inches
# and convert them to:
# kilometers
# meters
# centimeters

# 1 Mile =
# 1.609344 KM
# 1609.344  M
# 160934 CM


miles = float(input("Enter value of Miles: "))

yards = float(input("Enter value of yards: "))

feet = float(input("Enter value of feet: "))

inches = float(input("Enter value of inches: "))

kilometers = miles * 1.609344

meters = yards * 0.9144

centimenters = inches * 2.54

print(kilometers, "Kilometers", meters, "Meters", centimenters, "Centimeters")

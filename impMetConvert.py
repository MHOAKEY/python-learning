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


miles = float(input("Enter value of Miles: "))

yards = float(input("Enter value of yards: "))

feet = float(input("Enter value of feet: "))

inches = float(input("Enter value of inches: "))

totalCM = (miles * 160934) + (yards * 91.44) + (feet * 30.48) + (inches * 2.54)

kilometer = totalCM / 100_000

meter = 1000 * (kilometer - int(kilometer))

centimenter = 100 * (meter - int(meter))

print(int(kilometer), "kilometers", int(meter),
      "Meters", int(centimenter), "Centimeters")

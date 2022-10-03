# Write a program that takes 5 numbers from a user.

# The program will then place these numbers into an array.

# The program will reverse the list and then print the numbers one at a time back to the user.

# The program will find  the average of all numbers in the array and display the average to the user

# The program will then find and print out all numbers greater than the average

import re


userNum1 = int(input("Enter number: "))

userNum2 = int(input("Enter number: "))

userNum3 = int(input("Enter number: "))

userNum4 = int(input("Enter number: "))

userNum5 = int(input("Enter number: "))

userNumArray = [userNum1, userNum2, userNum3, userNum4, userNum5]

# userNumArray.append(int(input("Enter number: ")))

reverseArray = userNumArray[::-1]

averageOfArray = sum(userNumArray) / len(userNumArray)

print(reverseArray)

print("the average of these numbers is: ", float(averageOfArray))

for x in userNumArray:
    if x > averageOfArray:
        print("Unit greater than average: ", x)

# if userNumArray[0] > averageOfArray:
#     print("Unit greater than average: ", userNumArray[0])

# if userNumArray[1] > averageOfArray:
#     print("Unit greater than average: ", userNumArray[1])

# if userNumArray[2] > averageOfArray:
#     print("Unit greater than average: ", userNumArray[2])

# if userNumArray[3] > averageOfArray:
#     print("Unit greater than average: ", userNumArray[3])

# if userNumArray[4] > averageOfArray:
#     print("Unit greater than average: ", userNumArray[4])

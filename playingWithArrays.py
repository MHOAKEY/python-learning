# Write a program that takes 5 numbers from a user.

# The program will then place these numbers into an array.

# The program will reverse the list and then print the numbers one at a time back to the user.

# The program will find  the average of all numbers in the array and display the average to the user

# The program will then find and print out all numbers greater than the average

userNum1 = int(input("Enter number: "))

userNum2 = int(input("Enter number: "))

userNum3 = int(input("Enter number: "))

userNum4 = int(input("Enter number: "))

userNum5 = int(input("Enter number: "))

userNumArray = [userNum1, userNum2, userNum3, userNum4, userNum5]

reverseArray = userNumArray[::-1]

averageOfArray = sum(userNumArray) / len(userNumArray)

print(reverseArray)

print("the average of these numbers is: ", averageOfArray)

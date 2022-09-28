# Create a program that reverses a string. The program ask the user for a string and display the reversed string

# example:
# string = "Good morning"
# answer = "gninrom dooG"

# sequence[start:stop:step]

userInput = input("Enter sentence to be reversed: ")

reverse = userInput[::-1]

print(reverse)

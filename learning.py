# Write a program that takes in a string and returns how many vowels and consonants are in that string.
# Function should return: X Vowels X Consonants

# print(*map(userWord.lower().count, "aeiou"))

from asyncio import constants


userWord = input("Enter word(s) to display sum of letter A: ")
aSearch = "a"
aCount = userWord.count(aSearch)
print("The letter A has been found: ", aCount)
# Write a program that takes in a string and returns how many vowels and consonants are in that string.
# Function should return: X Vowels X Consonants

# print(*map(userWord.lower().count, "aeiou"))

from asyncio import constants


userWord = input("Enter word(s) to display sum of letter A: ")

count = userWord.lower().count("a") + userWord.count("e") + userWord.count(
    "i") + userWord.count("o") + userWord.count("u")

print("Sum of vowels found: ", count)

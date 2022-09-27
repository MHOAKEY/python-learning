# Write a program that takes in a string and returns how many vowels and consonants are in that string.
# Function should return: X Vowels X Consonants

# print(*map(userWord.lower().count, "aeiou"))

userWord = input("Enter word(s) to display sum of vowels found: ")

count = userWord.lower().count("a") + userWord.count("e") + userWord.count(
    "i") + userWord.count("o") + userWord.count("u") + userWord.count("y")

count2 = userWord.lower().count("b") + userWord.lower().count("c") \
    + userWord.lower().count("d") + userWord.lower().count("f") \
    + userWord.lower().count("g") + userWord.lower().count("h") \
    + userWord.lower().count("j") + userWord.lower().count("k") \
    + userWord.lower().count("l") + userWord.lower().count("m") \
    + userWord.lower().count("n") + userWord.lower().count("p") \
    + userWord.lower().count("q") + userWord.lower().count("r") \
    + userWord.lower().count("s") + userWord.lower().count("t") \
    + userWord.lower().count("v") + userWord.lower().count("w") \
    + userWord.lower().count("x") + userWord.lower().count("z")

print(count, "Vowel(s)", count2, "Consonant(s)")

userWord = input(
    "Enter word(s) to display sum of vowels and consonants found: ")

remove = userWord.strip(" `1234567890-=~!@#$%^&*()_+,./;'[]\<>?:")

removeSpaces = userWord.count(" ")

vowel = remove.lower().count("a")\
    + remove.lower().count("e")\
    + remove.lower().count("i")\
    + remove.lower().count("o")\
    + remove.lower().count("u")\
    + remove.lower().count("y")\

consonants = len(remove) - removeSpaces - vowel

print(vowel, " Vowel(s)", consonants, " Consonant(s)")

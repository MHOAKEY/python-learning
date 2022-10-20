print("\n1:")
# 1. Create a function that reverses a string but does not use any built in Python string functions. The function will take a string and return the reversed string

# example:
# string = "Good morning"
print("string = Good morning")
# answer = "gninrom dooG"


string = "Good morning"
answer = string[::-1]

print("reverse string =", answer)


# OR!


def reverseString(string):
    reverseString = ""
    for eachLetter in string:
        reverseString = eachLetter + reverseString
    return reverseString


print("reverse string =", reverseString(string))


print("\n2:")
# 2. Given an unsorted array of numbers, find the largest and smallest numbers in the array.
# Special Rule: You cannot sort the array to accomplish this task.

# Example:
# array = [ 5, 8, 1, 19, 7, 4, 6 ]
print("array = [ 5, 8, 1, 19, 7, 4, 6 ]")
# answer = Largest: 19 Smallest: 1


array = [5, 8, 1, 19, 7, 4, 6]

largeNum = array[0]
for num in array[1:]:
    if num > largeNum:
        largeNum = num
# print(largeNum)

smallNum = array[0]
for num in array[1:]:
    if num < smallNum:
        smallNum = num
# print(smallNum)

print("from array; Largest #:", largeNum, "Smallest #:", smallNum)


# OR!


def findLargeNum(numbers):
    largeNum = numbers[0]
    for number in numbers[1:]:
        if number > largeNum:
            largeNum = number
    # print(largeNum)
    return largeNum


def findSmallNum(numbers):
    smallNum = numbers[0]
    for number in numbers[1:]:
        if number < smallNum:
            smallNum = number
    # print(smallNum)
    return smallNum


print("from array; Largest #:", findLargeNum(
    array), "Smallest #:", findSmallNum(array))


print("\n3:")
# 3. Given an array of int and a target int, find the index of the 2 values in the array that sum the target.

# example:
# intArray = [1,2,3,4,5]
# targetInt = 5
# answer = index 1 and 2 or index 0 and 3


intArray = [1, 2, 3, 4, 5]
print("intArray =", intArray)

targetInt = 5
print("targetInt =", targetInt)

index = 0
innerLength = len(intArray)
innerIndex = 1

answer = []


for firstNum in intArray:
    # print("\n\nouterloop")
    # print("int (1):", firstNum)
    # print("index:", index)
    for innerLoopIndex in range(innerIndex, innerLength):
        # print("\ninnerloop")
        # print("int (2):", intArray[innerLoopIndex])
        # print("index:", innerLoopIndex)
        # print("int (1) + int (2) =", firstNum + intArray[innerLoopIndex])
        if firstNum + intArray[innerLoopIndex] == targetInt:
            answer.append([index, innerLoopIndex])
    innerIndex += 1
    index += 1


print("indices that equal targetInt:", answer)


# 4. Write a function that takes in 2 strings and finds out if they are anagrams of eachother.

# Function must take 2 arguments. Each of them a string.
# Function must find out if they are anagrams
# Function must return true or false


print("\n4:")
# word1 = "dog"

# word2 = "god"

# count = 0

# for letterFromWord1 in word1:
#     print("word1:", letterFromWord1)
#     for letterFromWord2 in word2:
#         print(" word2:", letterFromWord2)
#         if letterFromWord1 == letterFromWord2:
#             print("               count:", count)
#             count += 1
# if count == len(word1):
#     print("     length of word1:", len(word1))
#     print("Are these words an anagram? \nTrue")
# else:
#     print("Are these words an anagram? \nFalse")

print("enter a word below:")
word1 = input()
print("enter a word below:")
word2 = input()

while len(word1) != len(word2):
    print("These words are NOT an anagram")
    break

import datetime
import time
# 1. Given a date (yyyy-mm-dd) write a function that tells you how many days it has been since that date. The function must be able to find out what the current date is.

# BONUS if the date is in the future, make the function tell you how many days
# away it is until that date.

# Example:
# input: 2022-06-22
# output: 1 day ago (this is based on the function finding that today's date is
# 2022-06-23 this will obviously vary based on what day it currently is)


# def timeBetweenNowAndThen(dateInput):
#     today = datetime.datetime.now()
#     todayUnix = time.mktime(today.timetuple()) * 1000
#     userYear = dateInput[:4]
#     userMonth = dateInput[5:7]
#     userDay = dateInput[8:11]
#     userYearMonthDay = datetime.date(
#         int(userYear), int(userMonth), int(userDay))
#     userUnixTime = (time.mktime(userYearMonthDay.timetuple()) * 1000)
#     unixBetweenDates = todayUnix - userUnixTime
#     unixYearsBetween = unixBetweenDates / 31_536_000_000
#     unixMonthsBetween = (unixBetweenDates -
#                          (int(unixYearsBetween) * 31_536_000_000)) / 2_629_800_000
#     unixDaysBetween = ((unixBetweenDates - (int(unixYearsBetween) * 31_536_000_000)
#                         ) - (int(unixMonthsBetween) * 2_629_800_000)) / 86_400_000

#     result = str(int(unixYearsBetween)) + " Year(s), " + str(int(
#         unixMonthsBetween)) + " Month(s), " + str(int(unixDaysBetween)) + " Day(s)"

#     if result.find("-") == -1:
#         return result + " ago."
#     return result.replace("-", "") + " until."


# print("\nEnter date in format YYYY-MM-DD:")
# userYYYY_MM_DD = input()
# print(timeBetweenNowAndThen(userYYYY_MM_DD))


# 2. Write a function that will find the length of a nested array
# Given an array with an array inside, example: [1, [1,2,3], 2, 3]
# Find out if the given array has a nested array
# If it does, find the length of that nested array
# In the case of the above example array the answer would be 3. The nested array has 3 values [1,2,3]

# Example
# input: ["dog", ["apple", "orange"], "frog", "cat"]
# output: nested array has 2 values


array = ["dog", ["apple", "orange"], "frog", "cat"]


def findNestCheckLength(array):
    for i in array:
        if isinstance(i, list):
            return len(i)


print(findNestCheckLength(array))

# 3. Write a function that will find any prime numbers in a given range.
# Example input 5,7. The range is from 5 to 7 inclusive in this case. So the function will need to check if 5, 6 or 7 are prime numbers.
# Store all the found prime numbers in an array and return them to the user

# Examples:
# Input: 6,9
# Output: [7]

# Input: 10,20
# Output: [11,13,17,19]

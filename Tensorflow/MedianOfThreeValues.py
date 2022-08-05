# Exercise 88: Median of Three Values

"""
Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median.

Hint: The median value is the middle of the three values when they are sorted
into ascending order. It can be found using if statements, or with a little bit of
mathematical creativity
"""


def findMeridian(num1, num2, num3):
    return sorted([num1, num2, num3])[1]


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(findMeridian(num1, num2, num3))

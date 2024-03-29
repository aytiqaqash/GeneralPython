# Exercise 98: Is a Number Prime?

"""
A prime number is an integer greater than one that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.
"""


def numIsPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                return False
    return True


if __name__ == "__main__":
    num = int(input())
    numIsPrime(num)

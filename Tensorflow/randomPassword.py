# Exercise 100: Random Password

""""
Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters. Each character should be randomly
selected from positions 33 to 126 in the ASCII table. Your function will not take
any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file
"""
import random


def randomPassword():
    pss = ''
    for i in range(random.randint(6, 10)):
        pss = pss + chr(random.randint(33, 126))
    return pss


if __name__ == "__main__":
    print(randomPassword())

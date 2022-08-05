# Exercise 87: Shipping Calculator
"""
An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item in an order, and $2.95 for each subsequent item in the same order.
Write a function that takes the number of items in the order as its only parameter.
Return the shipping charge for the order as the function’s result.
Include a main program that reads the number of items purchased from the user
and displays the shipping charge.
"""


class ShippingCalculator:
    def __init__(self, numberOfItems):
        self.numberOfItems = numberOfItems

    def calculate(self):
        return 10.95 + (self.numberOfItems - 1) * 2.95


if __name__ == "__main__":
    numberOfItems = int(input())
    shC = ShippingCalculator(numberOfItems)
    print(shC.calculate())

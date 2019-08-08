#!/usr/bin/python3
# enumeration.py

from enum import Enum

Month = Enum('Month', 'January February ... December')

class MyMonth:

    def __init__(self, month):
        self.month = month

    def printmonth(self):
        if self.month == Month.January:
            print("January")
        elif self.month == Month.February:
            print("February")
        # ...
        elif self.month == Month.December:
            print("December")
        else:
            print("Not a real month")

if __name__== "__main__":
    month = MyMonth(Month.March)
    month.printmonth()
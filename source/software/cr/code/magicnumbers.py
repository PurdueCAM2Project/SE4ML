#!/usr/bin/python3
# magicnumbers.py

class MyMonth:

    def __init__(self, month):
        self.month = month

    def printmonth(self):
        if self.month == 1:
            print("January")
        elif self.month == 2:
            print("February")
        # ...
        elif self.month == 12:
            print("December")
        else:
            print("Not a real month")

if __name__== "__main__":
    month = MyMonth(3)
    month.printmonth()
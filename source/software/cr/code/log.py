#!/usr/bin/python3
# log.py

from enum import Enum
import logging

logging.basicConfig(level=logging.DEBUG)

Month = Enum('Month', 'January February ... December')

class MyMonth:

    def __init__(self, month):
        self.month = month

    def printmonth(self):
        if self.month == Month.January:
            logging.info("January")
        elif self.month == Month.February:
            logging.info("February")
        # ...
        elif self.month == Month.December:
            logging.info("December")
        else:
            logging.error("Not a real month")

if __name__== "__main__":
    month = MyMonth(Month.March)
    month.printmonth()
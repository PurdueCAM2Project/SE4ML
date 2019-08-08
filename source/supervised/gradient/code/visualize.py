#! /usr/bin/python3
# visualize.py
# Visualize test cases for graident descent

import sys
import matplotlib.pyplot as pyplot

def visualize(infile):
    try:
        fin = open(infile, 'r')
    except:
        sys.exit('open fail')
    # fine the maximum and minimum values
    # up to the first three dimensions
    # initialize the minimum values 
    xval = []
    yval = []
    for oneline in fin:
        numbers = oneline.split()
        xval.append(float(numbers[0]))
        yval.append(float(numbers[1]))
    pyplot.scatter(xval, yval)
    pyplot.show()

if __name__ == "__main__":
    input = 'data.txt'
    visualize(input)

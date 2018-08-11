#! /usr/bin/python3
# Visualize test cases for k-mean clustering program
# up to the third dimension
#

import sys
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

def visualize(infile):
    try:
        fin = open(infile, 'r')
    except:
        sys.exit('open fail')
    # fine the maximum and minimum values
    # up to the first three dimensions
    # initialize the minimum values 
    minval = sys.maxsize
    maxval = - sys.maxsize
    xval = []
    yval = []
    zval = []
    for oneline in fin:
        numbers = oneline.split()
        # get the number of dimensions
        dim = len (numbers)
        print (dim)
        # consider up to the first three dimension
        for ind in range(0, min(3, dim)):
            if (ind == 0):
                xval.append(int(numbers[ind]))
            if (ind == 1):
                yval.append(int(numbers[ind]))
            if (ind == 2):
                zval.append(int(numbers[ind]))
            minval = min(int(numbers[ind]), minval)
            maxval = max(int(numbers[ind]), maxval)
    print (minval, maxval)
    print (xval)
    print (yval)
    print (zval)
    if (dim == 1):
        yval = [0] * len(xval)
    if (dim <= 2):
        pyplot.scatter(xval, yval)
    if (dim == 3):
        fig = pyplot.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xval, yval, zval)
    pyplot.show()

if __name__ == "__main__":
    input = 'data.txt'
    visualize(input)

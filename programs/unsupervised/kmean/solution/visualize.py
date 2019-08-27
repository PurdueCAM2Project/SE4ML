#! /usr/bin/python3
# visualize.py
# Visualize results of k-mean clustering program
# Handle only 2-dimensional data
# Each line of input must have the following format:
# [x, y] c
# x and y are the coordinates
# c is the cluster

import sys
import matplotlib.pyplot as pyplot

def visualize(infile):
    try:
        fin = open(infile, 'r')
    except:
        sys.exit('open fail')
    kval = 0
    xlist = []
    ylist = []
    for oneline in fin:
        oneline = oneline.replace('[', '')
        oneline = oneline.replace(',', '')
        oneline = oneline.replace(']', '')
        oneline = oneline.replace(')', '')
        oneline = oneline.replace('(', '')
        numbers = list(map(int, oneline.split()))
        # print (numbers)
        [x, y, c] = numbers
        xsize = len(xlist)
        if (c >= xsize):
            # a new cluster
            # add more empty rows
            for ind in range(xsize, c + 1):
                # print ('add row', xsize, c)
                xlist.append([])
                ylist.append([])
        xlist[c].append(x)
        ylist[c].append(y)
        '''
        print('-------------------')
        for ind in range(len(xlist)):
            print (ind, xlist[ind], ylist[ind])
        '''
    markerlist = ['x', 'D', '1', 's', '+', 'x', 'o', '^']
    marklen = len(markerlist)
    for ind in range(len(xlist)): # last row not used
        pyplot.scatter(xlist[ind], ylist[ind],
                       marker = markerlist[ind % marklen])
    pyplot.show()

if __name__ == "__main__":
    input = 'data.txt'
    if (len(sys.argv) > 1):
        input = sys.argv[1]
    visualize(input)

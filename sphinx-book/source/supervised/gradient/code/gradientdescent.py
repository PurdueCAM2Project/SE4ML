#!/usr/bin/python3
# gradientdescent.py

import math
import random
import sys
import argparse

def readfile(file):
    # print(file)
    data = []
    try:
        fhd = open(file) # file handler
    except:
        return data
    for oneline in fhd:
        data.append(float(oneline))
    return data

def readfiles(f1, f2):
    x = readfile(f1)
    y = readfile(f2)
    return [x, y]

def sums(x, y):
    n = len(x)
    if (n != len(y)):
        print ("ERROR")
    sumx = 0
    sumx2 = 0
    sumy = 0
    sumxy = 0
    for ind in range(n):
        sumx = sumx + x[ind]
        sumy = sumy + y[ind]
        sumx2 = sumx2 + x[ind] * x[ind]
        sumxy = sumxy + x[ind] * y[ind]
    return [n, sumx, sumy, sumx2, sumxy]

def gradient(a, b, n, sumx, sumy, sumx2, sumxy):
    pa = 2 * (a * sumx2 + b * sumx - sumxy)
    pb = 2 * (a * sumx + b * n - sumy)
    # conver to unit vector
    length = math.sqrt(pa * pa + pb * pb)
    ua = pa / length
    ub = pb / length
    return [ua, ub]

def findab(args):
    [x, y] = readfiles(args.file1, args.file2)
    '''
    print (x)
    print (y)
    '''
    [n, sumx, sumy, sumx2, sumxy] = sums(x, y)
    '''
    print (n)
    print (sumx)
    print (sumy)
    print (sumx2)
    print (sumxy)
    '''
    # initial values for a and b
    a = -5
    b = 2
    eta = 0.1
    count =  10000
    while (count > 0):
        [pa, pb] = gradient(a, b, n, sumx, sumy, sumx2, sumxy)
        # print (pa, pb)
        a = a - eta * pa
        b = b - eta * pb
        print (a, b)
        count = count - 1


def checkArgs(args = None):
  parser = argparse.ArgumentParser(description='parse arguments')
  parser.add_argument('-f1', '--file1', 
                      help = 'name of the first data file',
                      default = 'xval')
  parser.add_argument('-f2', '--file2', 
                      help = 'name of the second data file',
                      default = 'yval')
  pargs = parser.parse_args(args)
  return pargs


if __name__== "__main__":
  args = checkArgs(sys.argv[1:])
  findab(args)


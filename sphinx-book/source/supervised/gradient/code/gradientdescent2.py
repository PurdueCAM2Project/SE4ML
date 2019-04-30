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

def gradient(a, b, n, x, y):
    h = 0.01
    error0 = 0
    errora = 0
    errorb = 0
    for ind in range(n):
        diff0 = y[ind] - (a * x[ind] + b)
        diffa = y[ind] - ((a + h) * x[ind] + b)
        diffb = y[ind] - (a * x[ind] + (b + h))
        error0 = error0 + diff0 * diff0
        errora = errora + diffa * diffa
        errorb = errorb + diffb * diffb
    pa = (errora - error0) / h
    pb = (errorb - error0) / h
    # conver to unit vector
    length = math.sqrt(pa * pa + pb * pb)
    ua = pa / length
    ub = pb / length
    return [ua, ub]

def findab(args):
    [x, y] = readfiles(args.file1, args.file2)
    n = len(x)
    # initial values for a and b
    a = -15
    b = 20
    eta = 0.1
    count =  10000
    while (count > 0):
        [pa, pb] = gradient(a, b, n, x, y)
        print (pa, pb)
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


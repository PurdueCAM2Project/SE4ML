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

def gradient1(a, b, n, sumx, sumy, sumx2, sumxy):
    pa = 2 * (a * sumx2 + b * sumx - sumxy)
    pb = 2 * (a * sumx + b * n - sumy)
    # convert to unit vector
    length = math.sqrt(pa * pa + pb * pb)
    ua = pa / length
    ub = pb / length
    return [ua, ub]

def gradient2(a, b, n, x, y):
    # use the definition
    # the partial derivative of function f respect to variable a is
    # (f(a + h) - f(a)) / h for small h
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
    # convert to unit vector
    length = math.sqrt(pa * pa + pb * pb)
    ua = pa / length
    ub = pb / length
    return [ua, ub]

def findab(args):
    [x, y] = readfiles(args.file1, args.file2)
    '''
    method 1: know the formula for the gradient
    '''
    [n, sumx, sumy, sumx2, sumxy] = sums(x, y)
    # initial values for a and b
    a = -5
    b = 2
    eta = 0.1
    count =  1000
    while (count > 0):
        [pa, pb] = gradient1(a, b, n, sumx, sumy, sumx2, sumxy)
        a = a - eta * pa
        b = b - eta * pb
        count = count - 1
    print (a, b)
    '''
    method 2: do not know the formula
    '''
    a = -15
    b = 21
    count =  1000
    while (count > 0):
        [pa, pb] = gradient2(a, b, n, x, y)
        a = a - eta * pa
        b = b - eta * pb
        count = count - 1
    print (a, b)

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


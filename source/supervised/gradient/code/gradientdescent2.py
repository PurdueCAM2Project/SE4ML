#!/usr/bin/python3
# gradientdescent2.py

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

def quadraticvalue(a, b, c, x):
    val = a * x * x + b * x + c
    return val

def gradient(a, b, c, n, x, y):
    # use the definition
    # the partial derivative of function f respect to variable a is
    # (f(a + h) - f(a)) / h for small h
    # h = random.random() * 0.5 # make it small
    h = 0.01
    error0 = 0
    errora = 0
    errorb = 0
    errorc = 0
    for ind in range(n):
        diff0 = y[ind] - quadraticvalue(a, b, c, x[ind])
        diffa = y[ind] - quadraticvalue(a + h, b, c, x[ind])
        diffb = y[ind] - quadraticvalue(a, b + h, c, x[ind])
        diffc = y[ind] - quadraticvalue(a, b, c + h, x[ind])
        error0 = error0 + diff0 * diff0
        errora = errora + diffa * diffa
        errorb = errorb + diffb * diffb
        errorc = errorc + diffc * diffc
    pa = (errora - error0) / h
    pb = (errorb - error0) / h
    pc = (errorc - error0) / h
    # convert to unit vector
    length = math.sqrt(pa * pa + pb * pb + pc * pc)
    ua = pa / length
    ub = pb / length
    uc = pc / length
    return [ua, ub, uc]

def findabc(args):
    [x, y] = readfiles(args.file1, args.file2)
    '''
    do not know the formula
    '''
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    count =  10000
    n = len(x)
    eta = 0.1
    while (count > 0):
        [pa, pb, pc] = gradient(a, b, c, n, x, y)
        a = a - eta * pa
        b = b - eta * pb
        c = c - eta * pc
        count = count - 1
    print (a, b, c)

def checkArgs(args = None):
  parser = argparse.ArgumentParser(description='parse arguments')
  parser.add_argument('-f1', '--file1', 
                      help = 'name of the first data file',
                      default = 'xval2')
  parser.add_argument('-f2', '--file2', 
                      help = 'name of the second data file',
                      default = 'yval2')
  pargs = parser.parse_args(args)
  return pargs


if __name__== "__main__":
  args = checkArgs(sys.argv[1:])
  findabc(args)


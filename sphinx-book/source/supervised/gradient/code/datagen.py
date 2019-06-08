#!/usr/bin/python3
# datagen.py

'''
Generate data using a polynomial for testing gradient descent

The program has three arguments:
   degree: what is the degree of the polynomial
   number: number of data points
   error: range of error (0 to 100). 
          The actual value is between (y - error * y, y + error * y)
   The range of x is (-50, 50)
'''
import random
import sys
import argparse

def generator(args):
    # print args
    # set the coefficients
    coeff = []
    for deg in range(args.degree):
        sign = random.randint(0,2) - 1 # positive or negative
        coeff.append((random.randint(2, 5) + 1) * sign)
        # coeff.append(random.random() * 10 * sign)
    # print ('coeff = ', coeff)
    for num in range(args.number): # number of data points
        xval = random.randint(2, 10) + 0.0
        # xval = (random.random() - 0.5) * 100
        # print('xval = ', xval)
        xdeg = 1
        xseq = [] # sequence of 1, x, x * x, x * x * x, ...
        for deg in range(args.degree):
            xseq.append(xdeg)
            xdeg = xdeg * xval
        # print ('xseq = ', xseq)
        yval = 0
        for deg in range(args.degree):
            yval = yval + xseq[deg] * coeff[deg]
        sign = random.randint(0,2) - 1
        # print ('xval, yval = ', xval, yval)
        yval = yval * (1 + sign * args.error * random.random())
        # print ('xval, yval = ', xval, yval)
        valstr = str(xval) + ' ' + str(yval)
        print (valstr)
        # print (xval, yval)
        # print ('------------------')

def checkArgs(args = None):
  parser = argparse.ArgumentParser(description='parse arguments')
  parser.add_argument('-d', '--degree', type=int,
                      help = 'degree of polynomial')
  parser.add_argument('-n', '--number', type=int,
                      help = 'number of data points')
  parser.add_argument('-e', '--error', type=float,
                      help = 'range of error')
  pargs = parser.parse_args(args)
  return pargs
  
if __name__== "__main__":
  args = checkArgs(sys.argv[1:])
  generator(args)


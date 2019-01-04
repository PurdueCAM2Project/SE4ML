#!/usr/bin/python3
# intpart.py

import sys
import argparse

def printArray(arr, ind):
  for i in range(0, ind - 1):
    print (str(arr[i]) + ' + ', end='')
  print (str(arr[ind - 1]))

def partitionHelp(arr, ind, left, odd, even, order, notself):
  if (left == 0):
    printArray(arr, ind)
  '''
  There are four conditions when this i is used
  1. not odd and not even: 
  2. odd and i is odd
  3. even and i is even
  '''
  maxi = left + 1
  if (notself):
    maxi = left
  for i in range(1, maxi):
    if (order and (ind != 0) and (arr[ind - 1] > i)):
      # orders do not matter
      # the numbers must not be decreasing
      continue
    if ((not odd) and (not even)):
      arr[ind] = i 
    elif (odd and (i % 2)):
      arr[ind] = i
    elif (even and ((i % 2) == 0)):
      arr[ind] = i
    else:
      continue # do not use this value of i
    partitionHelp(arr, ind + 1, left - i, odd, even, order, notself)

def partition(args):
  # print (args)
  odd = args.odd
  even = args.even
  order = args.order
  val = args.value
  notself = args.notself
  if (odd and even):
    sys.exit('-e and -o cannot be both set')
  if (even and (val % 2)):
    sys.exit('-e cannot partition an odd number')
  print('== Partition ' + str(val) + ' ==')
  if (odd):
    print('== Using only odd numbers ==')
  if (even):
    print('== Using only even numbers ==')
  arr = [0] * val
  partitionHelp(arr, 0, val, odd, even, order, notself)

def checkArgs(args = None):
  parser = argparse.ArgumentParser(description='parse arguments')
  parser.add_argument('-o', '--odd', action='store_true',
                      help = 'odd numbers only', default = False)
  parser.add_argument('-e', '--even',action='store_true',
                      help = 'even numbers only', default = False)
  parser.add_argument('-r', '--order',action='store_true',
                      help = 'orders do not matter', default = False)
  parser.add_argument('-s', '--notself',action='store_true',
                      help = 'not to include itself', default = False)
  parser.add_argument('value', type = int,
                      help = 'number to parition')
  pargs = parser.parse_args(args)
  return pargs
  
if __name__== "__main__":
  args = checkArgs(sys.argv[1:])
  partition(args)


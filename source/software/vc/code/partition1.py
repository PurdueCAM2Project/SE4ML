#!/usr/bin/python3
# partition.py

import sys

def printArray(arr, ind):
  for i in range(0, ind - 1):
    print (str(arr[i]) + ' + ', end='')
  print (str(arr[ind - 1]))

def partitionHelp(arr, ind, left):
  if (left == 0):
    printArray(arr, ind)
  for i in range(1, left + 1):
    arr[ind] = i
    partitionHelp(arr, ind + 1, left - i)

def partition(val):
  print('== Partition ' + str(val) + ' ==')
  arr = [0] * val
  partitionHelp(arr, 0, val)
  
if __name__== "__main__":
  if (len(sys.argv) < 2):
    sys.exit('Need a positive integer')
  val = int(sys.argv[1])
  if (val <= 0):
    sys.exit('Need a positive integer')
  partition(val)


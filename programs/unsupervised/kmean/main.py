#! /usr/bin/python3
# main.py for kmean
import sys
import kmean
import datetime
import random

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        sys.exit('need file name and k value')
    kval = int(sys.argv[2])
    kmean.kmean(sys.argv[1], kval)

#! /usr/bin/python3
# main.py for kmean
import sys
import kmean
import argparse

def checkArgs(argv = None):
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('-k', '--kval', type = int)
    parser.add_argument('-f', '--filename', 
                        help = 'name of the data file', default = 'data.txt')
    parser.add_argument('-s', '--summary', type = bool,
                        help = 'summary of result', default = False)
    args = parser.parse_args(argv)
    return args

if __name__ == "__main__":
    args = checkArgs(sys.argv[1:])
    kmean.kmean(args)

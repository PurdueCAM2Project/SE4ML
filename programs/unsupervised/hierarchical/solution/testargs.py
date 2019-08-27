#! /usr/bin/python
import sys
import argparse

def checkArgs(argv = None):
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('flag', choices = ('a', 'b', 'c', 'd'))
    args = parser.parse_args(argv)
    return args

if __name__ == "__main__":
    args = checkArgs(sys.argv[1:])
    print (args.flag)
    

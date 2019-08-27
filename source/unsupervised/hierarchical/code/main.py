#! /usr/bin/python
# main.py for hierarchical clustering
import sys
import cluster
import argparse

def checkArgs(argv = None):
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('-f', '--filename', 
                        help = 'name of the data file', default = 'data.txt')
    parser.add_argument('-d', '--distance', 
                        help = 'distance definition',
                        choices = ('c', 's', 'a', 't'))
    # four methods to measure distances between clusters:
    # complete, single, average, centroid
    args = parser.parse_args(argv)
    return args

if __name__ == "__main__":
    args = checkArgs(sys.argv[1:])
    cluster.cluster(args)

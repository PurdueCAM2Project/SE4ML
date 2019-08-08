#! /usr/bin/python3
# iterate multiple time with different values of k between 2 and 10
# each k value run 5 times
import sys
import kmean

class Args:
    def __init__(self, fn):
        self.filename = fn
        self.kval = 1
        self.summary = True

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        sys.exit('need file name')
    args = Args(sys.argv[1])
    for kval in range(2, 20):
        args.kval = kval
        for cnt in range(5):
            kmean.kmean(args)

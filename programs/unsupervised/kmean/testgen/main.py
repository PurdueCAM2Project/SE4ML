#! /usr/bin/python3
# main.py for testgen.py
# Generate test cases for k-mean clustering program

import sys
import testgen

def printUsage():
    usage = """usage:
               -t: truly random. False means the clusters do not overlap
               -d v: dimension is v
               -m v: number of clusters is v
               -q v: each cluster has at least v data points
               -r v: each cluster has at most v data points
               -o v: output data file name is v
               -c v: output cluster file name is v"""
    print (usage)
    sys.exit()

def nextIntArgument(argv, index):
    (index, v) = nextStrArgument(argv, index)
    return (index, int(v))

def nextStrArgument(argv, index):
    # print ('nextStrArgument' , argv[index])
    index = index + 1
    if (index == len(argv)):
        printUsage()
    v = argv[index]
    index = index + 1
    # print (index, v)
    return (index, v)

if __name__ == "__main__":
    # set the default values
    t = False # truly random
    d = 2 # dimension
    m = 3 # number of clusters
    q = 4 # at least q points per cluster
    r = 5 # at most  r points per cluster
    output1 = 'data.txt' 
    output2 = 'cluster.txt'
    # get the arguments, if given
    index = 1
    while (index < len(sys.argv)):
        if (sys.argv[index] == '-t'):
            t = True
            index = index + 1
            continue
        if (sys.argv[index] == '-d'):
            (index, d) = nextIntArgument(sys.argv, index)
            continue
        if (sys.argv[index] == '-m'):
            (index, m) = nextIntArgument(sys.argv, index)
            continue
        if (sys.argv[index] == '-q'):
            (index, q) = nextIntArgument(sys.argv, index)
            continue
        if (sys.argv[index] == '-r'):
            (index, r) = nextIntArgument(sys.argv, index)
            continue
        if (sys.argv[index] == '-o'):
            (index, output1) = nextStrArgument(sys.argv, index)
            continue
        if (sys.argv[index] == '-c'):
            (index, output2) = nextStrArgument(sys.argv, index)
            continue
    # check whether the arguments are acceptable
    if ((d < 1) or (m < 2) or (q < 3) or (r < q)):
        sys.exit('invalid values for the arguments')
    s = 1000 * m # the value in each dimension is between (-s, s)
    # set the names of the output files
    testgen.testgen(t, d, m, q, r, s, output1, output2)


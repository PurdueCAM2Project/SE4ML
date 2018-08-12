#! /usr/bin/python
# main.py for testgen.py
# Generate test cases for k-mean clustering program
# This program take three required and one optional arguments:
#
# Number of dimension ($p$)
# Number of clusters ($m$)
# Minimum numbers of data points per cluster ($q$)
# Maximum numbers of data points per cluster ($r$)
# (Optional) Range of the values (called $s$ in this program).

import sys
import testgen

if __name__ == "__main__":
    # set the default values
    p = 2
    m = 3
    q = 3
    r = 5
    # get the arguments, if given
    if (len(sys.argv) > 1):
        p = int (sys.argv[1])
    if (len(sys.argv) > 2):
        m = int (sys.argv[2])
    if (len(sys.argv) > 3):        
        q = int (sys.argv[3])
    if (len(sys.argv) > 4):        
        r = int (sys.argv[4])
    # check whether the arguments are acceptable
    if (p < 1):
        sys.exit('# dimension must be 1 or greater')
    if (m < 2):
        sys.exit('# clusters must be 2 or greater')
    if (q < 3):
        sys.exit('# data point per cluster must be 3 or greater')
    if (r < q):
        sys.exit('Maximum # data point per cluster must be greater than r')
    s = 1000 * m
    testgen.generate(p, m, q, r, s)


# kmean.py
import sys
import random
from datapoint import DataPoint
'''
def findCentroid(data, cluster, kval):
    for ind in range(0, len(cluster)
    centroid = [[0] * len(data[0]) 
'''

def cluster(data, kval):
    cluster = [0]
    for ind in range(0, len(data)):
        cluster.append(random.randint(0, kval - 1))
    print cluster
    done = false
    while (done == false):
        centroid = findCentroid(data, cluster, kval)
'''

'''
def findRange(data):
    # find the minimum and maximum values in each dimension
    # return two lists: maxvalues and minvalues
    # initialize
    maxval = [0] * len(data[0])
    minval = [0] * len(data[0])
    for dim in range(0, len(data[0])):
        maxval[dim] = data[0][dim]
        minval[dim] = data[0][dim]

    # find the maximum and minimum in each dimension
    for row in range(1, len(data)):
        for dim in range(0, len(data[0])):
            maxval[dim] = max(maxval[dim], data[row][dim])
            minval[dim] = min(minval[dim], data[row][dim])
    print minval
    print maxval
    return minval, maxval

def initCentroid(minval, maxval, kval):
    
    centroid = [0] * len(minval)
'''

def readfile(fhd, kval):
    data = []
    for oneline in fhd:
        clu = random.randint(0, kval - 1)
        dp = DataPoint(map(int, oneline.split()), clu)
        data.append(dp)
        # IMPORTANT: map convert string to int
        # must use integers for calculation, not string
    # print data
    return data

def kmean(filename, kval):
    print "kmean", filename, kval
    try:
        fhd = open(filename)
    except:
        sys.exit('open fail')
    data = readfile(fhd, kval)
    centroid = cluster(data, kval)
    '''
    centroid = initCentroid(minval, maxval, kval)
    [] # two dimensional array
    # first dimension: data points
    # second dimension: list of numbers as one data point
    # a data point can be high dimensional
    # assume all data points have the same length
    for oneline in fhd:
        data.append(map(int, oneline.split()))
        # IMPORTANT: map convert string to int
        # must use integers, not string
    print data
    minval, maxval = findRange(data)
    centroid = initCentroid(minval, maxval, kval)
    '''
        

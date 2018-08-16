# testgen.py
'''This program randomly assigns the center of each cluster within
(-s, s) for each dimension. The clusters are distributed within (-sm,
sm). Then, the points of each cluster are within (-span, span) of the
center. If the points are truly random, span is as large 4s (allowing
the clusters to overlap). If overlaping is not allowed, span is only
s/3 (integer).

'''

import sys
import random
def testgen(t, d, m, q, r, s, output1, output2):
    # print (t, d, m, q, r, s, output1, output2)
    try:
        fout1 = open(output1, 'w')
        fout2 = open(output2, 'w')
    except:
        sys.exit('open fail')
    # initialize the center of the first cluster
    span = int(s / 3)
    # centers are two-dimensional (m rows and d columns) arrays for
    # the centers of clusters
    centers = []
    for cl in range (0, m):
        newcenter = list(range(-m, m)) 
        random.shuffle(newcenter)
        # pick the first d elements and 
        # multiple every element by s
        newcenter = [i * s * m for i in newcenter[0:d]] 
        centers.append(newcenter)
    if (t == True):
        span = 4 * s
    cl = 1
    for cl in range (0, m):
        n = random.randint(q, r)
        # how many point in this cluster
        for dp in range (0, n):
            # data point
            line = ''
            for dim in range (0, d):
                # dimension
                x = centers[cl][dim] + random.randint(-span, span)
                line = line + str(x) + ' '
            fout1.write(line + '\n')
            fout2.write(line + ' ' + str(cl) + '\n')
    fout1.close()
    fout2.close()


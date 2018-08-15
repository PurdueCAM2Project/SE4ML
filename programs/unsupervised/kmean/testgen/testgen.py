# testgen.py
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
    span = 500
    center = -s
    if (t == True):
        # span = 1000
        span = s
    cl = 1
    for cl in range (0, m):
        n = random.randint(q, r)
        # how many point in this cluster
        for dp in range (0, n):
            # data point
            line = ''
            for dim in range (0, d):
                # dimension
                x = center + random.randint(-span, span)
                line = line + str(x) + ' '
            fout1.write(line + '\n')
            fout2.write(line + ' ' + str(cl) + '\n')
        # center = center + 2000
    fout1.close()
    fout2.close()


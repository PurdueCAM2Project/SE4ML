import random
def generate(p, m, q, r, s):
    # set the names of the output files
    output1 = 'data.txt'
    output2 = 'cluster.txt'
    fout1 = open(output1, 'w')
    fout2 = open(output2, 'w')
    # initialize the center of the first cluster
    center = -s
    for clu in range (0, m):
        n = random.randint(q, r)
        # how many point in this cluster
        for dp in range (0, n):
            # data point
            line = ''
            for dim in range (0, p):
                # dimension
                x = center + random.randint(-200, 200)
                line = line + str(x) + ' '
            fout1.write(line + '\n')
            fout2.write(line + ' ' + str(clu) + '\n')
        center = center + 2000
        

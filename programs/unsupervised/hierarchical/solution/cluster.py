# cluster.py for hierarchical clustering
import sys
from hclist import HCList

def cluster(args):
    filename = args.filename
    distdef = args.distance
    try:
        fhd = open(filename) # file handler
    except:
        sys.exit('open fail')
    # create an empty hierarchical clustering list
    hcl = HCList(distdef)
    # read the data
    count = 0
    for oneline in fhd:
        data = map(int, oneline.split())
        count = count + 1
        # print "add to list", data
        hcl.add(data)
    # print "--- finish reading file ---"    
    hcl.printList()
    hcl.cluster()
    print "--- final cluster ---"    
    hcl.printList()

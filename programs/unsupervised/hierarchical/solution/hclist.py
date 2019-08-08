from hctree import TreeNode
import sys

class ListNode:
    def __init__(self, tn):
        # double linked list, with after and before
        # use after and before, not next and prev
        # because next is already defined in Python
        self.trnode = tn
        self.after = None
        self.before = None
    
class HCList:
    def __init__(self, distdef):
        # the list has a dummy node. It is both head and tail
        trnd = TreeNode(None)
        lsnd = ListNode(trnd)
        self.head = lsnd 
        self.tail = lsnd
        self.dist = distdef # definition of distance

    # add a cluster to the list
    # a new cluster is stored in a tree node
    # the tree node is added to the list
    def add(self, val):
        trnd = TreeNode(val)
        lsnd = ListNode(trnd)
        self.tail.after = lsnd
        lsnd.before = self.tail
        self.tail = lsnd
        return trnd

    def delete(self, lsnd):
        # cannot delete the first node (dummy)
        if (lsnd == self.head):
            print "ERROR, delete dummy head"
            return
        # delete the last node
        if (lsnd == self.tail): 
            self.tail = self.tail.before
            self.tail.after = None
            return
        # delete a node in the middle 
        before = lsnd.before
        after  = lsnd.after
        before.after = after
        after.before = before

    def printList(self):
        print "HCList::printList"
        lsnd = self.head.after
        while (lsnd != None):
            lsnd.trnode.printNode()
            lsnd = lsnd.after

    def distance(self, lsnd1, lsnd2):
        if ((self.dist == 'c') or (self.dist == 'C')):
            return lsnd1.distanceComplete(lsnd2)
        if ((self.dist == 's') or (self.dist == 'S')):
            return lsnd1.distanceSimple(lsnd2)
        if ((self.dist == 'a') or (self.dist == 'A')):
            return lsnd1.distanceAverage(lsnd2)
        if ((self.dist == 't') or (self.dist == 'T')):
            return lsnd1.distanceCentroid(lsnd2)
        print ('Unknown method for calcuating distance')
        return 0

    def merge(self, trnd1, trnd2):
        # value not used for non-leaf nodes
        val = [-1] * len(trnd1.value) 
        trnd = self.add (val)
        trnd.left = trnd1
        trnd.right = trnd2
        trnd.printNode()

    def cluster(self):
        # this implementation is not efficient but it should
        # be easy to understand
        # remember that head is the dummy node
        while (self.head.after != self.tail):
            # at least two list nodes, not done yet
            # distance of the first two list nodes as reference
            lsnd1 = self.head.after
            lsnd2 = lsnd1.after
            mindist = self.distance(lsnd1, lsnd2)

            # find the pair of the smallest distance
            flsnd = self.head.after # first list node
            while (flsnd != self.tail):
                slsnd = flsnd.after # second list node
                while (slsnd != None):
                    dist = self.distance(flsnd, slsnd)
                    if (dist < mindist): # notice, no =
                        dist = mindist
                        lsnd1 = flsnd
                        lsnd2 = slsnd
                    slsnd = slsnd.after
                flsnd = flsnd.after                        
            # remove the two nodes that have the smallest distance
            # from the list
            print "merge", lsnd1.trnode.value, lsnd2.trnode.value
            self.delete(lsnd1)
            self.delete(lsnd2)
            self.merge(lsnd1.trnode, lsnd2.trnode)
        return self.head.after.trnode
            

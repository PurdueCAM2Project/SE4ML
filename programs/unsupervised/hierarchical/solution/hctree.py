# hctree.py for hierarchical
class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def printNode(self):
        if (self == None):
            return

        if ((self.left == None) and
            (self.right == None)):
            print "Leaf: ", self.value
        else:
            print self.value

        if (self.left != None):
            self.left.printNode()
        if (self.right != None):           
            self.right.printNode()
        
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def distanceComplete(self, trnd):
        dist1 = self._distanceCompleteNode(trnd)
        dist2 = dist1
        dist3 = dist1
        if (self.left != None):
            dist2 = self._distanceCompleteNode(self.left, trnd)
        if (self.right != None):
            dist3 = self._distanceCompleteNode(self.right, trnd)
        return max(dist1, dist2, dist3)

    def distanceSingle(self, trnd):
        return 0

    def distanceAverage(self, trnd):
        return 0

    def distanceCentroid(self, trnd):
        return 0
    
    def _distance(self, sndnode):
        sum = 0
        for ind in range(len(self.value)):
            dist = self.value[ind] - sndnode.value[ind]
            sum = dist * dist
        return sum
    
    def _distanceCompleteNode(self, trnd):
        # find the maximum distance of one node with all nodes in trnd
        dist1 = self._distance(trnd)
        dist2 = dist1
        dist3 = dist1
        if (trnd.left != None):
            dist2 = self._distanceCompleteNode(self, trnd.left)
        if (trnd.right != None):
            dist3 = self._distanceCompleteNode(self, trnd.right)
        return max(dist1, dist2, dist3)
    

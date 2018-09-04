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
        return 0

    def distanceSingle(self, trnd):
        return 0

    def distanceAverage(self, trnd):
        return 0

    def distanceCentroid(self, trnd):
        return 0
    
    
    

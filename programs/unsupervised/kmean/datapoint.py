# datapoint.py
# each object has two attributes:
#     data (an array) and
#     which cluster it belongs to (an integer)

class DataPoint:
    def __init__(self, dat, clu):
        self._data = dat # assign only once, read only
        self.cluster = clu

    def changeCluster(self, newclu):
        self.cluster = newclu

    def getData(self):
        return self._data

    def getDimension(self):
        return len(self._data)

    def getCluster(self):
        return self.cluster

    def printData(self):
        print self._data, self.cluster

    

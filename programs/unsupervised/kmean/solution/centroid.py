# centroid.py

class Centroid:
    def __init__(self, dim, id):
        if (dim <= 0):
            print ('Invalid Number of Dimension')
            return
        self._dim = dim # assign once, read only
        self._ID = id # assign once, read only
        self.reset()

    def reset(self):
        self.size = 0 # number of data points in this cluster
        self.data = [0] * self._dim
        
    def addPoint(self, point):
        dim = len(self.data)
        if (dim != point.getDimension()):
            print ('Wrong Dimension')
            return
        for ind in range(0, dim):
            self.data[ind] = self.data[ind] + point._data[ind]
        self.size = self.size + 1

    def findCenter(self):
        if (self.size == 0):
            # print ('Centroid', self._ID, 'Without Data')
            return
        for ind in range(0, self._dim):
            self.data[ind] = self.data[ind] / self.size
        

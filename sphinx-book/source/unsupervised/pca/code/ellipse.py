#!/usr/bin/python3
# ellipse.py
# generate points along an ellipse and draw it
import random
import math
import matplotlib.pyplot as pyplot

class Ellipse:
    def __init__(self, rx, ry, cx, cy, theta):
        self.rx = rx # major radius
        self.ry = ry # minor radius
        self.cx = cx # center of x
        self.cy = cy # center of y
        self.theta = theta # rotation angle
    def getPoints(self, num, draw = False):
        # return a list of point on the ellipse
        points = [] 
        for ind in range(0, num):
            rv = random.random() * math.pi * 2 # random value
            xval = self.rx * math.cos(rv) * math.cos(self.theta)
            xval = xval - self.ry * math.sin(rv) * math.sin(self.theta)
            xval = xval + self.cx
            yval = self.rx * math.cos(rv) * math.sin(self.theta)
            yval = yval - self.ry * math.sin(rv) * math.cos(self.theta)
            yval = yval + self.cy
            points.append([xval, yval])
        if (draw):
            for ind in range(0, num):
                pyplot.scatter(points[ind][0], points[ind][1])
            pyplot.show()
        return points
    
if __name__ == "__main__":
   ep = Ellipse(10, 5, 10, -3, -1)
   points = ep.getPoints(100, True)

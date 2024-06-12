import copy
import numpy as np


class Hough(object):
    """
    Implementation of the Hough transform for straight lines
    """
    def __init__(self, datastore):
        chamber = datastore.get('chamber')
        self.max_d = (chamber.getWidth() ** 2 + chamber.getHight() ** 2) ** 0.5
        self.min_d = self.max_d * (-1)
        self.precision = 200
        self.HoughSpace = np.zeros((self.precision, self.precision))
        self.HoughParam = []
        datastore.put('Hough', self)

    def execute(self, datastore):
        chamber = datastore.get('chamber')
        particles = datastore.get('particles')
        for i in range(particles):
            self.Field = datastore.get('Field' + str(i))
            HoughSpace = copy.copy(self.HoughSpace)
            y = chamber.getHight()
            for j in self.Field:
                y -= 1
                for x in range(chamber.getWidth()):
                    if j[x] == "X":
                        for a in range(self.precision):
                            alpha = a * 3.1415926 / self.precision
                            d = x * np.cos(alpha) + y * np.sin(alpha)
                            d = (self.precision * (d + self.max_d)) / (2 * self.max_d)
                            HoughSpace[a][int(d)] += 1
            out_a, out_d = np.unravel_index(HoughSpace.argmax(), HoughSpace.shape)
            List = [[out_a * 3.1415926 / self.precision, 2 * self.max_d * out_d / self.precision - self.max_d]]
            datastore.put('Hough' + str(i), List)

    def getHoughParam(self):
        return self.HoughParam

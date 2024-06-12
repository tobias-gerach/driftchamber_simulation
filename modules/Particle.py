from random import uniform


class Particle:
    """
    Basic class to define a Particle and its path.

    :param xmin: lower boundary of randomly assigned X position
    :param xmax: upper boundary of randomly assigned X position
    :param ymin: lower boundary of randomly assigned Y position
    :param ymax: upper boundary of randomly assigned Y position
    :param pxmin: lower boundary of randomly assigned X impulse
    :param pxmax: upper boundary of randomly assigned X impulse
    :param pymin: lower boundary of randomly assigned Y impulse
    :param pymax: upper boundary of randomly assigned Y impulse
    """
    def __init__(self, xmin, xmax, ymin, ymax, pxmin, pxmax, pymin, pymax): 
        self.x = uniform(xmin, xmax)
        self.y = uniform(ymin, ymax)
        self.px = uniform(pxmin, pxmax)
        self.py = uniform(pymin, pymax)

    def execute(self):
        print(self.x, self.y, self.px, self.py)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def vx(self, px, py):
        return px

    def vy(self, px, py):
        return py

    def move(self, deltaT, BField=0):
        Pybuffer = self.py
        Pxbuffer = self.px
        self.py -= Pxbuffer * BField * deltaT
        self.px += Pybuffer * BField * deltaT
        self.x += self.px * deltaT
        self.y += self.py * deltaT


class ParticleGun:
    def __init__(self, datastore, ParticleTest, ParticleData):
        self.test = ParticleTest
        self.data = ParticleData
        print("Initialized ParticleGun")

    def execute(self, datastore):
        chamber = datastore.get('chamber')
        particles = datastore.get('particles')

        for i in range(particles):
            if self.test == 1:
                b = self.data[i]
                a = Particle(b[0], b[0], b[1], b[1], b[2], b[2], b[3], b[3])
                datastore.put('p' + str(i), a)
            else:
                a = Particle(0, chamber.getWidth(), 0, 0, -1, 1, 0, 1)
                datastore.put('p' + str(i), a)

    def __del__(self):
        print("Destroyed ParticleGun")

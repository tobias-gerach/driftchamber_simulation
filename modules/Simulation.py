import copy
from random import uniform


class Simulation:
    """
    Module to simulate the detection of particles in the drift chamber.
    
    :param sensitivity: threshold for particle detection (detection if sensitivity > rand([0,1]))
    """
    def __init__(self, sensitivity):
        self.sensitivity = sensitivity
        pass

    def execute(self, datastore):
        chamber = datastore.get('chamber')
        particles = datastore.get('particles')
        self.HField = copy.copy(chamber.getField())

        for i in range(particles):
            self.Field = copy.copy(chamber.getField())
            particle = datastore.get('p' + str(i))
            while particle.gety() < chamber.getHight():
                particle.move(0.5, datastore.get('BField')) 
                x = int(particle.getx())
                y = int(particle.gety())
                rndm = uniform(0, 1)
                if 0 <= x < chamber.getWidth() and 0 <= y < chamber.getHight():
                    if rndm < self.sensitivity:
                        self.Field[-(y + 1)] = self.Field[-(y + 1)][:x] + str("X") + self.Field[-(y + 1)][x + 1:]
                        self.HField[-(y + 1)] = self.HField[-(y + 1)][:x] + str("X") + self.HField[-(y + 1)][x + 1:]
                else:
                    break
            datastore.put('Field' + str(i), self.Field)
        datastore.put('HField', self.HField)

    def __del__(self):
        print("Simulation finished")

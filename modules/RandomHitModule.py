from random import random


class RandomHitModule:
    """
    This module implements background noise as random detections 
    in the drift chamber.

    :param prob: probability threshold that needs to be surpassed for random event to occur
    """
    def __init__(self, prob):
        self.probability = prob

    def execute(self, datastore):
        chamber = datastore.get('chamber')
        self.Field = chamber.getField()
        for i in range(len(self.Field)):
            for c in range(len(self.Field[i])):
                if self.probability > random():
                    self.Field[i] = self.Field[i][:c] + 'X' + self.Field[i][c + 1:]

    def __del__(self):
        print('Destroyed RandomHitModule')

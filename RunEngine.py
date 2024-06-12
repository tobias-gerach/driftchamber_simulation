import numpy as np
from modules import Particle, Chamber, Simulation, RandomHitModule, OutputModule, Hough
import datastore

chamberGeometry = np.loadtxt('data/Chamber.txt')

# Function to run all events in the RunEngine
def event(RunEngine, datastore):
    nEvent = 1
    for i in range(0, nEvent):
        for j in range(0, len(RunEngine)):
            RunEngine[j].execute(datastore)


# Initialize datastore
DS = datastore.DataStore()

# Use ParticleTest = 1 to load predefined particles from a textfile
ParticleTest = 0
if ParticleTest == 1:
    Particledaten = np.loadtxt('data/Particles.txt')

    N = len(Particledaten)
    DS.put('particles', N)
else:
    Particledaten = []
    N = 3
    DS.put('particles', N)


# Magnetic field strength. Disables Hough detection.
BField = 0.0
DS.put('BField', BField)

superlayerlist = []
breite = int(chamberGeometry[0])
for i in range(2, len(chamberGeometry)):
    superlayerlist.append(chamberGeometry[i])

# Run all moodules in a defined order
if BField == 0:
    RunEngine = [Chamber.Chamber(superlayerlist, breite, DS), Particle.ParticleGun(DS, ParticleTest, Particledaten), RandomHitModule.RandomHitModule(chamberGeometry[1]),
                 Simulation.Simulation(0.2), Hough.Hough(DS), OutputModule.OutputModule()]
else:
    RunEngine = [Chamber.Chamber(superlayerlist, breite, DS), Particle.ParticleGun(DS, ParticleTest, Particledaten), RandomHitModule.RandomHitModule(chamberGeometry[1]),
                 Simulation.Simulation(0.2), OutputModule.OutputModule()]

event(RunEngine, DS)

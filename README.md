# driftchamber_simulation

## Description

This is a small driftchamber simulation, that uses a simple Hough algorithm to detect randomly recorded particles in a straight line. 
It is possible to activate a magnetic field in the RunEngine.py file, but this deactivates the particle detection feature. 
For testing purposes, an option was implemented to use pre-defined particles in data/Particles.txt. 
The dimension of the chamber is set in data/Chamber.txt.
This project had no ambition to be a physically correct simulation and was part of a software design workshop in 2016.

## Usage

You can run the project via the command line by executing:

./RunEngine.py

## Unit Tests

To run all unit tests, execute:

./run_unittest.sh

or

./drift_tests.py


#!/usr/bin/python
import numpy as np
from pedestrianParameters.pedestrianSettings import *
from pedestrianParameters.pedestrianType import pedestrianType
from worldParameters.worldDimensions import *

import matplotlib.pyplot as plt

def spawnRandomPedestrians():
    pedestrian = [None] * nbPedestrians
    for i in range(nbPedestrians):
        position    = (np.random.rand(3) * 2. - 1.)
        position[0] = position[0] * worldLength
        position[1] = position[1] * worldLength
        velocity    = (np.random.rand(3) * 2. - 1.)
        target      = (np.random.rand(3) * 2. - 1.)
        target[0]   = target[0] * worldLength
        target[1]   = target[1] * worldLength
        pedestrian[i] = pedestrianType(pedestrian, position, velocity, target)
    return pedestrian

# pedestrian = spawnRandomPedestrians()


# fig = plt.figure()
# ax = fig.add_subplot(111)
# for i in range(nbPedestrians):
#     print pedestrian[1].position[0], pedestrian[1].position[1]
#     plt.plot([pedestrian[i].position[0]],[pedestrian[i].position[1]], 'bo')

# plt.xlim([-worldLength, worldLength])
# plt.ylim([-worldWidth, worldWidth])
# plt.show()

        
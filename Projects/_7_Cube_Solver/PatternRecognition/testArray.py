import numpy as np
from numpy.core.fromnumeric import shape
from CubeSide import CubeSide

list = []

cs = CubeSide()

print(cs.colors["white"])

side = np.zeros(shape=(3,3)) #emty array with 0
side.fill(-1) # fill with -1

print(side)
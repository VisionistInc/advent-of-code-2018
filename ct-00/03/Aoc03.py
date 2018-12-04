import re
import numpy as np

fp = open('input.txt')
fabric = np.ndarray(shape=(10000,10000), dtype=int, order='C')
fabric.fill(0)

for curLine in fp:
    parsedLine = list(filter(None, re.split("[# @,:x\n]+", curLine)))
    entry  = int(parsedLine[0])
    xstart = int(parsedLine[1]) 
    ystart = int(parsedLine[2])
    xlen   = int(parsedLine[3])
    ylen   = int(parsedLine[4])
    entryFabric = np.ndarray(shape=(ylen,xlen), dtype=int, order='C')
    entryFabric.fill(1)
    fabric[ystart:ystart+ylen, xstart:xstart+xlen] += entryFabric

answer = 0
for x in range(fabric.shape[0]):
    for y in range(fabric.shape[1]):
        if fabric[x,y] > 1:
            answer += 1
print(answer)
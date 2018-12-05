import re
import numpy as np

fp = open('input.txt')
fabric = np.ndarray(shape=(10000,10000), dtype=int, order='C')
fabric.fill(0)

entries = []
for curLine in fp:
    parsedLine = list(filter(None, re.split("[# @,:x\n]+", curLine)))
    entryNum  = int(parsedLine[0])
    xstart = int(parsedLine[1]) 
    ystart = int(parsedLine[2])
    xlen   = int(parsedLine[3])
    ylen   = int(parsedLine[4])
    entries.append([entryNum, xstart, ystart, xlen, ylen])

    entryFabric = np.ndarray(shape=(ylen,xlen), dtype=int, order='C')
    entryFabric.fill(1)

    fabric[ystart:ystart+ylen, xstart:xstart+xlen] += entryFabric

for entry in entries:
    entryNum, xstart, ystart, xlen, ylen = entry
    entryFabric = np.ndarray(shape=(ylen,xlen), dtype=int, order='C')
    entryFabric.fill(1)
    if np.array_equal(fabric[ystart:ystart+ylen, xstart:xstart+xlen], entryFabric):
        print(entryNum)
        break
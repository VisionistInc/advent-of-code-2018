import numpy as np

def calculatePowerLevel(x, y, serialNum):
    rackId = x + 10
    powerLevel = int(str((rackId * y + serialNum) * rackId)[-3:-2]) - 5
    return powerLevel

def findMax(array):
    max = 0
    maxX = -1
    maxY = -1
    maxLength = None

    for x in range(298):
        for y in range(298):
            power = np.sum(array[x:x+3,y:y+3])

            if power > max:
                max = power
                maxX = x
                maxY = y

    return maxX + 1, maxY + 1

array = np.ndarray(shape=(300, 300), dtype=int, order='C')

for x in range(300):
    for y in range(300):
        array[x][y] = calculatePowerLevel(x + 1, y + 1, 1308)

xMax, yMax = findMax(array)

print("%i,%i" % (xMax, yMax))
import numpy as np

def calculatePowerLevel(x, y, serialNum):
    rackId = x + 10
    powerLevel = int(str((rackId * y + serialNum) * rackId)[-3:-2]) - 5
    return powerLevel

def findMax(array, length):
    max = 0
    maxX = -1
    maxY = -1
    maxLength = None

    for x in range(300-length+1):
        for y in range(300-length+1):
            power = np.sum(array[x:x+length,y:y+length])

            if power > max:
                max = power
                maxX = x
                maxY = y

    return maxX + 1, maxY + 1, max

def findMaxVarLength(array):
    max = 0
    maxX = None
    maxY = None
    maxLength = None

    for length in range(1, 301, 1):
        x, y, power = findMax(array, length)

        if power > max:
            max = power
            maxX = x
            maxY = y
            maxLength = length

    return maxX, maxY, maxLength

array = np.ndarray(shape=(300, 300), dtype=int, order='C')

for x in range(300):
    for y in range(300):
        array[x][y] = calculatePowerLevel(x + 1, y + 1, 1308)

xMax, yMax, length = findMaxVarLength(array)

print("%i,%i,%i" % (xMax, yMax, length))

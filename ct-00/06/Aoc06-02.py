import re
fp = open('input.txt')

points = []
maxY = 0
maxX = 0

for curLine in fp:
    x = int(list(filter(None, re.split("[, ]+", curLine)))[0])
    y = int(list(filter(None, re.split("[, ]+", curLine)))[1])
    points.append([x,y])
    if y > maxY:
        maxY = y
    if x > maxX:
        maxX = x

safeSpaces = 0

for x in range(maxX + 1):
    for y in range(maxY + 1):
        totalDistance = 0
        for pointNum in range(len(points)):
            curDistance = abs(points[pointNum][0] - x) + abs(points[pointNum][1] - y)
            totalDistance += curDistance
        if totalDistance < 10000:
            safeSpaces += 1

print(safeSpaces)

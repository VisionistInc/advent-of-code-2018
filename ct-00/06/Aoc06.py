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

counts = [0] * len(points)

for x in range(maxX + 1):
    for y in range(maxY + 1):
        closestDistance = maxX + maxY + 2
        currentClosest = None

        for pointNum in range(len(points)):
            curDistance = abs(points[pointNum][0] - x) + abs(points[pointNum][1] - y)
            if curDistance < closestDistance:
                closestDistance = curDistance
                currentClosest = pointNum
                if closestDistance == 0:
                    break
            elif curDistance == closestDistance:
                currentClosest = None
        if currentClosest is not None:       
            if x == 0 or y == 0 or x == maxX or y == maxY:
                counts[currentClosest] = None
            elif counts[currentClosest] != None:
                counts[currentClosest] += 1

maxArea = 0
for pointNum in range(len(counts)):
    if counts[pointNum]:
        if counts[pointNum] > maxArea:
            maxArea = counts[pointNum]
            
print(maxArea)

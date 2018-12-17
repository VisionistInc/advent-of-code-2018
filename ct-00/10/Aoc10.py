from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import imageio

fp = open('input.txt')

points = []
X = 0
Y = 1
XVEL = 2
YVEL = 3

xmin = 0
xmax = 0
ymin = 0
ymax = 0


def increment():
    global points
    for point in points:
        point[X] += point[YVEL]
        point[Y] += point[XVEL]

def cull():
    global xmin
    global xmax
    global ymin
    global ymax
    global points
    
    points = [point for point in points if point[X] <= xmax and point[X] >= xmin and point[Y] <= ymax and point[Y] >= ymin]

            
def xextent(points):
    xmin = min(points, key=itemgetter(X))[X]
    xmax = max(points, key=itemgetter(X))[X]
    return xmax - xmin    

def yextent(points):
    ymin = min(points, key=itemgetter(Y))[Y]
    ymax = max(points, key=itemgetter(Y))[Y]
    return ymax - ymin

def printPoints(points):
    curxmin = min(points, key=itemgetter(X))[X]    
    curymin = min(points, key=itemgetter(Y))[Y]
    curImage = np.ndarray(shape=(yextent(points) + 1, xextent(points) + 1), dtype=int, order='C')
    curImage.fill(0)

    for point in points:
        curImage[point[Y] - curymin, point[X] - curxmin] = 1
    
    print(curImage)
    
for curLine in fp:
    x = int(curLine[10:16].lstrip())
    y = int(curLine[18:24].lstrip())
    yVel = int(curLine[36:38].lstrip())
    xVel = int(curLine[40:42].lstrip())
    
    points.append([x, y, xVel, yVel])

xmin = min(points, key=itemgetter(X))[X]
xmax = max(points, key=itemgetter(X))[X]
ymin = min(points, key=itemgetter(Y))[Y]
ymax = max(points, key=itemgetter(Y))[Y]

count = 0
np.set_printoptions(threshold=np.nan)

while len(points):
    increment()
    cull()
    if len(points) == 0:
        print("no points left!!")
        break
    count += 1

    curYExtent = max(points, key=itemgetter(Y))[Y] - min(points, key=itemgetter(Y))[Y]
    
    if curYExtent < 10:
        printPoints(points)
        print()
        print(count)
        break
    

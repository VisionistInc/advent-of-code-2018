from operator import itemgetter

LEFT_TURN = -1
CENTER_TURN = 0
RIGHT_TURN = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

carts = []
tracks = []
fp = open("input.txt")
curY = 0

for curLine in fp:
    for curX in range(len(curLine)):
        if curLine[curX] == '<':
            carts.append((curX,curY,LEFT,LEFT_TURN))
        elif curLine[curX] == '>':
            carts.append((curX,curY,RIGHT,LEFT_TURN))
        elif curLine[curX] == 'v':
            carts.append((curX,curY,DOWN,LEFT_TURN))
        elif curLine[curX] == '^':
            carts.append((curX,curY,UP,LEFT_TURN))

    newLine = curLine.replace('^', '|').replace('v', '|').replace('<', '-').replace('>', '-').strip('\n')
    tracks.append(newLine)
    curY += 1

def countCars():
    count = 0
    lastX = None
    lastY = None 
    for cart in carts:
        x, y, direction, nextTurn = cart
        if x != -1:
            count += 1
            lastX = x
            lastY = y
    return count, lastX, lastY

for i in range(20000):
    carts.sort(key=itemgetter(1, 0))
    
    for cartNum, cart in enumerate(carts):
        x, y, direction, nextTurn = cart
        if x == -1:
            continue
            
        if direction == UP:
            y -= 1
        elif direction == DOWN:
            y += 1
        elif direction == LEFT:
            x -= 1
        elif direction == RIGHT:
            x += 1

        if tracks[y][x] == '+':
            direction = (direction + nextTurn) % 4
            nextTurn = (nextTurn + 2) % 3 - 1

        elif tracks[y][x] == '\\':
            if direction == UP or direction == DOWN:
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4

        elif tracks[y][x] == '/':
            if direction == UP or direction == DOWN:
                direction += 1
            else:
                direction -= 1

        for checkCartNum, checkCart in enumerate(carts):
            checkX, checkY, checkDirection, checkNextTurn = checkCart
            if checkX == x and checkY == y:
                carts[checkCartNum] = (-1, 1, 0, 0)
                x, y, direction, nextTurn = (-1, 1, 0, 0)
                break

        carts[cartNum] = (x, y, direction, nextTurn)
    carCount, lastX, lastY = countCars()
    if carCount == 1:
        print("%i,%i" % (lastX, lastY))
        break
        

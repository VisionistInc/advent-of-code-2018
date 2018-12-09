testSet = [[9, 25], [10, 1618], [13, 7999], [17, 1104], [21, 6111], [30, 5807], [431, 70950], [431, 7095000]]

for players, marbles in testSet:
    circle = [0]
    curPlace = 0
    curPlayer = 0
    scores = [0] * players

    for marble in range(1, marbles + 1):
        if marble % 23 == 0:
            scores[curPlayer] += marble
            if curPlace >= 7:
                curPlace -= 7
            else:
                curPlace = len(circle) + curPlace - 7 
            scores[curPlayer] += circle.pop(curPlace)
        else:
            if curPlace + 2 == len(circle) + 1:
                curPlace = 1
            else:
                curPlace += 2
            circle.insert(curPlace, marble)

        curPlayer += 1
        if curPlayer >= players:
            curPlayer = 0
        
    print(max(scores))


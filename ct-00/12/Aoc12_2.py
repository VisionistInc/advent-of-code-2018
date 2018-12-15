fp = open('input.txt')

pots = fp.readline()[15:-1]
startPot = 0

fp.readline()

def calculateMagicNum(pots):
    answer = 0
    for charNum in range(len(pots)):
        if pots[charNum] == "#":
            answer += charNum + startPot
    return answer

growths = []
for curLine in fp:
    combo = curLine[0:5]
    result = curLine[-2:-1]

    growths.append((combo, result))

prevMagicNum = calculateMagicNum(pots)

for i in range(200):
    prevMagicNum = calculateMagicNum(pots)
    
    nextPots = ""
    for charNum in range(-2, len(pots) + 2, 1):
        if charNum < 2:
            curCombo = "." * (2-charNum) + pots[:3+charNum]
        elif charNum > len(pots) - 3:
            curCombo = pots[charNum-2:] + "." * (charNum-len(pots)+3)
        else:
            curCombo = pots[charNum-2:charNum+3]

        curResult = None
        for growth in growths:
            combo, result = growth
            if curCombo == combo:
                curResult = result
                break

        if charNum < 0 and nextPots == "" and curResult == "#":
            startPot = startPot + charNum
            nextPots += curResult
        elif charNum >= 0:
            nextPots += curResult

    pots = nextPots.rstrip(".")
    if len(pots) == 0:
        break

print((calculateMagicNum(pots) - prevMagicNum) * (50000000000-200) + calculateMagicNum(pots))

fp = open('input.txt')
input = list(map(int, fp.readline().split()))

def nodeGetValue(node):
    childrenCount = node[0]
    metaDataLen = node[1]

    nodeValue = 0
    curIndex = 2

    if childrenCount > 0:
        childValues = [0] * childrenCount

        for i in range(childrenCount):
            curChildLen, curChildValue = nodeGetValue(node[curIndex:])
            curIndex += curChildLen
            childValues[i] = curChildValue

        for metaDataElement in node[curIndex:curIndex+metaDataLen]:
            if metaDataElement <= childrenCount:
                nodeValue += childValues[metaDataElement - 1]
    else:
        nodeValue = sum(node[curIndex:curIndex+metaDataLen])

    curIndex += metaDataLen

    return curIndex, nodeValue

length, nodeValue = nodeGetValue(input)

print(nodeValue)

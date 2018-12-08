fp = open('input.txt')
input = list(map(int, fp.readline().split()))

metaDataSum = 0

def nodeSumMetaData(node):
    global metaDataSum

    childrenCount = node[0]
    metaDataLen = node[1]
    curIndex = 2

    for i in range(childrenCount):
        curIndex += nodeSumMetaData(node[curIndex:])

    metaDataSum += sum(node[curIndex:curIndex+metaDataLen])
    curIndex += metaDataLen

    return curIndex

length = nodeSumMetaData(input)

print(metaDataSum)

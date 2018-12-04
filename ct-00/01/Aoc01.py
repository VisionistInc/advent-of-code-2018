fp = open('input.txt')
sum = 0
for curLine in fp:
    sum += float(curLine)

print(sum)
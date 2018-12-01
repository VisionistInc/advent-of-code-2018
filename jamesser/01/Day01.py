sum = 0

with open('input.txt') as f:
    for line in f:
        strNumber = line[1:].strip()
        realNumber = int(strNumber)
        if line[0] == '-':
            sum = sum - realNumber
        else:
            sum = sum + realNumber      

print(sum)
sum = 0
freqs = {
    '0': True
}

loop = True

while(loop):
    with open('input.txt') as f:
        for line in f:
            strNumber = line[1:].strip()
            realNumber = int(strNumber)
            if line[0] == '-':
                sum = sum - realNumber
            else:
                sum = sum + realNumber

            if(str(sum) in freqs):
                loop = False
                break

            freqs[str(sum)] = True

print(sum)

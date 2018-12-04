fp = open('input.txt')
lines = []
common = ""

for curLine in fp:
    for line in lines:
        common = ""
        for i in range(len(line)):
            if curLine[i] == line[i]:
                common += curLine[i]
                
        if len(common) == len(curLine) - 1:
            print(common)
            exit()   
    lines.append(curLine)
    

fp = open('input.txt')
sum = 0
seenBefore = {0}
while 1:
    line = fp.readline()
    
    if not line:
        fp.seek(0)
        continue
        
    sum += float(line)
    
    if sum in seenBefore:
        break

    seenBefore.add(sum) 

print(sum)
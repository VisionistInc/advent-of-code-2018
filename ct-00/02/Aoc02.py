fp = open('input.txt')
containsTwo = 0
containsThree = 0

for line in fp:
    charCounts = dict()
    for char in line:
        try:
            charCounts[char] = charCounts[char] + 1
        except:
            charCounts[char] = 1

    for count in charCounts.values():
        if count == 2:
            containsTwo += 1
            break
    
    for count in charCounts.values():
        if count == 3:
            containsThree += 1
            break
    
print(containsTwo * containsThree)
fp = open('input.txt')

polymer = fp.readline()

changesMade = True

while changesMade:
    changesMade = False
    i = 0
    while i < len(polymer) - 1:
        if polymer[i] != polymer[i+1] and polymer[i].upper() == polymer[i+1].upper():
            polymer = polymer[:i] + polymer[i+2:]
   
            changesMade = True
        i += 1
        
print(len(polymer))
        
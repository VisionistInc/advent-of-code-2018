fp = open('input.txt')

polymer = fp.readline()

entries = set()

for entry in polymer:
    entries.add(entry.upper())

def shrunkPolymerLen(polymer):
    changesMade = True
    while changesMade:
        changesMade = False
        i = 0
        while i < len(polymer) - 1:
            if polymer[i] != polymer[i+1] and polymer[i].upper() == polymer[i+1].upper():
                polymer = polymer[:i] + polymer[i+2:]               
                changesMade = True
            i += 1
    return len(polymer)    

def removeEntryShrinkPolymer(polymer, entry):
    i = 0
    while i < len(polymer):
        if polymer[i].upper() == entry.upper():
            polymer = polymer[:i] + polymer[i+1:]
        else:
            i += 1
    return shrunkPolymerLen(polymer)


minLength = shrunkPolymerLen(polymer)

for entry in entries:
    newLen = removeEntryShrinkPolymer(polymer, entry)
   
    if newLen < minLength:
        minLength = newLen
        
print(minLength)
    
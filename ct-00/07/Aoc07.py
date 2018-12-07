NEXT = 0
PREV = 1


steps = dict()

fp = open('input.txt')

#fill entries
for curLine in fp:
    first = curLine.split()[1]
    second = curLine.split()[7]

    if not first in steps:
        steps[first] = [[second], []]
    else:
        steps[first][NEXT].append(second)
        
    if not second in steps:
        steps[second] = [[], [first]]
    else:
        steps[second][PREV].append(first)
    
#sort entries
sortedSteps = dict()
ready = []
for stepName, links in steps.items(): 
    sortedSteps[stepName] = [sorted(links[NEXT]), sorted(links[PREV])]
    if len(links[PREV]) == 0:
        ready.append(stepName)

done = ""
       
while len(ready):
    ready = sorted(ready)
    newStep = ready.pop(0)
    done += newStep
    
    for stepNextToCheck in sortedSteps[newStep][NEXT]:
        newStepReady = True
        for stepPrevToCheck in sortedSteps[stepNextToCheck][PREV]:
            if stepPrevToCheck not in done:
                newStepReady = False
                break
        if newStepReady == True:
            if stepNextToCheck not in done:
                ready.append(stepNextToCheck)
    

print(done)


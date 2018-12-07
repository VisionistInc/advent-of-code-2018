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
inProgress = []

def getNextStep():
    global ready
    ready = sorted(ready)
    try:
        newStep = ready.pop(0)
    except:
        return None
    inProgress.append(newStep)
    return newStep

def completeStep(completedStep):
    global done
    if completedStep is None or completedStep == '' :
        return
    inProgress.remove(completedStep)
    done += completedStep 
    for stepNextToCheck in sortedSteps[completedStep][NEXT]:
        newStepReady = True
        for stepPrevToCheck in sortedSteps[stepNextToCheck][PREV]:
            if stepPrevToCheck not in done:
                newStepReady = False
                break
        if newStepReady == True:
            if stepNextToCheck not in done and stepNextToCheck not in inProgress:
                ready.append(stepNextToCheck)

workers = [[0, ''], [0, ''], [0, ''], [0, '']]
time = 0        
       

while len(ready) or len(inProgress):
    #complete steps
    for i in range(len(workers)):
        if workers[i][0] == 0:
            completeStep(workers[i][1])
            workers[i][1] = ''
    
    #get new steps
    for i in range(len(workers)):
        if workers[i][1] == '':
            workers[i][1] = getNextStep()
            if workers[i][1] is not None:
                workers[i][0] = ord(workers[i][1]) - ord('A') + 60
        else:
            workers[i][0] -= 1

    time += 1    

print(time-1)  #there was an extra increment in loop after it was done


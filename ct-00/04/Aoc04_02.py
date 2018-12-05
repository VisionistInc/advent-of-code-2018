import re
import numpy as np
import datetime
from operator import itemgetter
from enum import Enum

class GuardState(Enum):
    SLEEPING = 1
    AWAKE = 2
    UNK = 3
    

fp = open('input.txt')

events = []
for curLine in fp:
    parsedLine = list(filter(None, re.split("[- :#\n]+", curLine)))
    eventTime = datetime.datetime( int(parsedLine[0][1:]), int(parsedLine[1]), int(parsedLine[2]), int(parsedLine[3]), int(parsedLine[4][:-1]))
    state = GuardState(GuardState.UNK)
    guard = None
    if parsedLine[5] == "Guard":
        guard = int(parsedLine[6])
        state = GuardState.AWAKE
    elif parsedLine[5] == "falls":
        state = GuardState.SLEEPING
    else:
        state = GuardState.AWAKE 
    events.append([eventTime, guard, state])

events = sorted(events, key=itemgetter(0))

curGuardNum = None
curState = None
startSleep = None
guardLog = dict()

def addAwake(entryTime):
    if not curGuardNum in guardLog:
        existingEntry = np.zeros(60, dtype=int, order='C')
    else:
        existingEntry = guardLog[curGuardNum]
    newEntry = np.ones(entryTime - startSleep, dtype=int, order='C')        
    existingEntry[startSleep:entryTime] += newEntry        
    guardLog[curGuardNum] = existingEntry

for event in events:
    if event[1]:
        if curGuardNum and curState == GuardState.SLEEPING:
            addAwake(60)
        curGuardNum = event[1]  
        curState = GuardState.AWAKE
    elif event[2] == GuardState.SLEEPING:
        startSleep = event[0].minute
        curState = GuardState.SLEEPING
    else:
        addAwake(event[0].minute)
        curState = GuardState.AWAKE

sleepiestGuard = None
maxSleep = 0
maxSleepMinute = None
for guard, log in guardLog.items():
    if np.amax(log) > maxSleep:
        maxSleepMinute = np.argmax(log)
        maxSleep = np.amax(log)
        sleepiestGuard = guard

print(sleepiestGuard * maxSleepMinute)

#if you are going for leaderboards, i'd sort the input in Excel
text = {}
dates = []

with open('./input.txt') as file:
    for line in file:
        split = line.split(']')
        fullDate = split[0][1:]
        date = fullDate.split()

        text[fullDate] = split[1].strip()

        dates.append(fullDate)

def sortDates(dates):
    split = dates.split('-')
    return split[0], split[1], split[2]

dates.sort(key=sortDates)

#now that the dates are sorted, need to determine guard schedule
minTracker = {}
currGuard = -1
startSleep = -1

for date in dates:
    split = text[date].split()

    if (split[0] == 'Guard'):
        currGuard = split[1]
    elif (split[0] == 'falls'):
        startSleep = int(date.split()[1].split(':')[1])
    else: #else should be 'wakes up'
        endSleep = int(date.split()[1].split(':')[1])
        #insert each minute fallen asleep for the guard
        for currMinute in range(startSleep, endSleep):
            if (currMinute in minTracker):
                minTracker[currMinute].append(currGuard)
            else:
                minTracker[currMinute] = [currGuard]

topTimesSlept = 0
topGuard = '#-1'
topMinute = -1

for minute, guards in minTracker.items():
    #check which guard fell asleep most on this minute
    maxGuard = {}
    for guard in guards:
        if (guard in maxGuard):
            maxGuard[guard] += 1
        else:
            maxGuard[guard] = 1
    sleepiestGuard = max(maxGuard, key=maxGuard.get)
    if (maxGuard[sleepiestGuard] > topTimesSlept):
        topTimesSlept = maxGuard[sleepiestGuard]
        topGuard = sleepiestGuard
        topMinute = minute

print(int(topGuard[1:]) * topMinute)
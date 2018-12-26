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
schedule = {}
minSlept = {}
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
            if (currGuard in schedule):
                schedule[currGuard].append(currMinute)
            else:
                schedule[currGuard] = [currMinute]

        #track the guard's minutes slept
        slept = endSleep - startSleep
        if (currGuard in minSlept):
            minSlept[currGuard] = minSlept[currGuard] + slept
        else:
            minSlept[currGuard] = slept

#find guard with max minSlept
sleepiestGuard = max(minSlept, key=minSlept.get)

minTrack = {}
#find the minute most fallen asleep
for sleptMin in schedule[sleepiestGuard]:
    if (sleptMin in minTrack):
        minTrack[sleptMin] += 1
    else:
        minTrack[sleptMin] = 1

sleepiestMin = max(minTrack, key=minTrack.get)

hash = int(sleepiestGuard[1:]) * sleepiestMin

print(hash)

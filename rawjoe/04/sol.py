with open('input', 'r') as file:
    input = file.read()

lines = sorted(input.split('\n'))

guards = {}

current_guard = -1
asleep = 0

for line in lines:
    # new guard
    if '#' in line:
        parts = line.split()
        # strip off '#'
        current_guard = int(parts[3][1:])
        if current_guard not in guards:
            # make new guard with list of 60 minutes
            guards[current_guard] = [0] * 60
    elif 'asleep' in line:
        parts = line.split(':')
        # first two digits are minute
        asleep = int(parts[1][:2])
    else:
        parts = line.split(':')
        # first two digits are minute
        awake = int(parts[1][:2])
        for i in range(asleep, awake):
            guards[current_guard][i] += 1

max_minutes = 0
sleepy_guard = -1
for key, value in guards.items():
    if sum(value) > max_minutes:
        max_minutes = sum(value)
        sleepy_guard = key

# find the minute the guard sleeps the most
minute = guards[sleepy_guard].index(max(guards[sleepy_guard]))
print('Part 1: %d' % (sleepy_guard * minute))

max_minutes = 0
sleepy_guard = -1
for key, value in guards.items():
    if max(value) > max_minutes:
        max_minutes = max(value)
        sleepy_guard = key

# find the minute the guard sleeps the most
minute = guards[sleepy_guard].index(max(guards[sleepy_guard]))
print('Part 2: %d' % (sleepy_guard * minute))
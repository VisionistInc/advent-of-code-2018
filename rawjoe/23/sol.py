import re

with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

X = 0
Y = 1
Z = 2
R = 3

bots = []
for line in lines:
    nums = re.findall(r'-?\d+', line)
    nums = [ int(x) for x in nums ]
    bots.append(list(nums))

bots = sorted(bots, key=lambda x: x[R])
big_bot = list(bots[-1])

num_in_range = 0
for bot in bots:
    d = abs(big_bot[X] - bot[X]) + abs(big_bot[Y] - bot[Y]) + abs(big_bot[Z] - bot[Z])
    if d <= big_bot[R]:
        num_in_range += 1

print ("Part 1: ", num_in_range)

print ("Part 2:  No solution yet.  I tried someone elses code and it worked, but I don't fully get it yet.")
with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

class Step:
    # Constructor method
    def __init__(self, letter):
        self.pre = []
        self.post = []
        # 'A' is 65 ascii
        # ascii value - 64 + 60
        self.time = ord(letter) - 4
        self.worker_assigned = False

def print_dict(d):
    for k,v in d.items():
        print(k,v.pre,v.post)
        print('')

steps = dict()

for line in lines:
    parts = line.split()
    before = parts[1]
    after = parts[7]
    if before in steps:
        steps[before].post.append(after)
        steps[before].post.sort()
    else:
        steps[before] = Step(before)
        steps[before].post.append(after)
    if after in steps:
        steps[after].pre.append(before)
        steps[after].pre.sort()
    else:
        steps[after] = Step(after)
        steps[after].pre.append(before)

import copy
saved_steps = copy.deepcopy(steps)

order = ''

while len(steps) > 0:
    # find next step
    # Z is the last step we'll do
    next_step = 'Z'
    for k,v in steps.items():
        if len(v.pre) == 0:
            if k < next_step:
                next_step = k
    # add next step to list
    order += next_step

    # now remove step as a blocker
    for c in steps[next_step].post:
        steps[c].pre.remove(next_step)

    # now remove step from dictionary
    del steps[next_step]

print("Part 1: ", order)

steps = saved_steps

time = 0

free_workers = 5

while len(steps) > 0:
    time += 1

    # find any step ready
    next_steps = []
    for k,v in steps.items():
        if len(v.pre) == 0:
            next_steps.append(k)
    
    # put in order any available steps
    next_steps.sort()

    # assign any possible workers and do work
    for c in next_steps:
        if steps[c].worker_assigned:
            steps[c].time -= 1
        elif free_workers > 0:
            steps[c].worker_assigned = True
            free_workers -= 1
            steps[c].time -= 1

    # now remove any done steps as a blocker
    for c in next_steps:
        if steps[c].time == 0:
            free_workers += 1
            for n in steps[c].post:
                steps[n].pre.remove(c)
            del steps[c]

print("Part 2: ", time)
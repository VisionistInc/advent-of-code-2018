with open('input', 'r') as file:
    input = file.read()

init,transitions = input.split('\n\n')

words,pots = init.split(': ')

# tracks the first pot we know about
first_pot = 0

# at this point I think i have to assume that five empty
# pots will never generate a new plant, otherwise we'd have
# plants growing for infinity

# determine the logic that generates a new pot
new_growth = []
transitions = transitions.split('\n')
for i in range(len(transitions)):
    parts = transitions[i].split(' => ')

    # if it results in an empty pot, we don't care
    if parts[1] == '.':
        continue
    # save off the conditions that fill a pot
    new_growth.append(parts[0])

def trim_pots():
    '''
    Trims the list of pots down to no more
    than 5 empty ones on either end
    '''
    global pots
    global first_pot
    # find first filled pot
    for i in range(len(pots)):
        if pots[i] == '#':
            break
    pots = pots[i:len(pots)]
    pots = '.....' + pots
    first_pot += i
    first_pot -= 5

    # find last filled pot
    for i in range(len(pots)-1, -1, -1):
        if pots[i] == '#':
            break
    pots = pots[:i+1] + '.....'

# solve part 1
for i in range(20):
    # make sure five empty pots on either end
    trim_pots()
    next_pots = '..'
    for j in range(2, len(pots) - 2):
        if pots[j-2:j+3] in new_growth:
            next_pots += '#'
        else:
            next_pots += '.'
    
    pots = next_pots

total = 0
for i in range(len(pots)):
    if pots[i] == '#':
        total += (i + first_pot)

print("Part 1: ", total)

def repeating(p1, p2):
    p1_first = p1.find('#')
    p1_last  = p1.rfind('#')
    p2_first = p2.find('#')
    p2_last  = p2.rfind('#')

    if p1[p1_first:p1_last+1] == p2[p2_first:p2_last+1]:
        return True, p2_first - p1_first
    return False, None

# don't worry, we wont run to 50 billion
for i in range(20, 50000000000):
    # make sure five empty pots on either end
    trim_pots()
    next_pots = '..'
    for j in range(2, len(pots) - 2):
        if pots[j-2:j+3] in new_growth:
            next_pots += '#'
        else:
            next_pots += '.'
    next_pots += '..'

    # i noticed by observation that the pot pattern entered a steady
    # state at around 100-some loops, it just shifts.  So I am
    # looking for that here.  Once a pot pattern repeats, it will
    # always repeat, we just need to determine the offset

    repeats, offset = repeating(pots, next_pots)
    pots = next_pots

    if repeats:
        break

# figure out the total for the current iteration
# also count how many full pots there are
total = 0
full_pots = 0
for j in range(len(pots)):
    if pots[j] == '#':
        full_pots += 1
        total += (j + first_pot)

# how many more iterations to 50 billion
loops_left = 50000000000 - i - 1

# each pot will shift by offset for each reamining iteration
shifts_left = loops_left * offset

# multiply by total number of full pots
total += (shifts_left * full_pots)

print("Part 2: ", total)
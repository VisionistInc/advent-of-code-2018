with open('input', 'r') as file:
    input = file.read()

# standardize input
input = input.replace('^', '(')
input = input.replace('$', ')')

paths = dict()
index = 1 # jump in past first paren
x = 0
y = 0
total_dis = 0

def xy_str():
    return '%d,%d' % (x,y)

def advance_xy(dir):
    global x
    global y
    if dir == 'N':
        y += 1
    if dir == 'S':
        y -= 1
    if dir == 'W':
        x -= 1
    if dir == 'E':
        x += 1

def fill_out():
    global x
    global y
    global index
    global total_dis
    # save off in case we cross any | that will reset
    saved_dis = total_dis
    saved_x,saved_y = x,y

    # keep going till we find the end of this paren group
    while input[index] != ')':
        c = input[index]
        index += 1

        if c == '|':
            # we need to reset our counters and position
            total_dis = saved_dis
            x,y = saved_x,saved_y
        elif c == '(':
            # we are entering a new sub group
            fill_out()
        else:
            # move to new xy
            advance_xy(c)
            total_dis += 1
            if xy_str() in paths:
                if paths[xy_str()] > total_dis:
                    paths[xy_str()] = total_dis
            else:
                paths[xy_str()] = total_dis
    # scoot past the )
    index += 1


fill_out()

longest = 0
rooms = 0
for key,val in paths.items():
    longest = max(longest, val)
    if val >= 1000:
        rooms += 1

print('Part 1: ', longest)
print('Part 2: ', rooms)



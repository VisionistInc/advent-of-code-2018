with open('input', 'r') as file:
    input = file.read()

X = 0
Y = 1

ROCKY  = 0
WET    = 1
NARROW = 2

# these line up nicely with the terrain above
# can't be neither if terrain rocky
# can't be torch if wet
# can't be climbing if narrow
NEITHER = 0
TORCH = 1
CLIMBING = 2

class state:
    def __init__(self, equip, pos, time):
        self.equip = equip
        self.pos = list(pos)
        self.time = time

lines = input.split('\n')

depth = int(lines[0].split()[1])
target = lines[1].split()[1].split(',')
target = [int(i) for i in target]

# these will be used to bound our growth in the cave
bound_x = 0
bound_y = 0

# solve part 1
cave = []
risk = 0
for y in range(target[Y]+1):
    row = list()
    for x in range(target[X] + 1):
        if x == 0 and y == 0:
            index = 0
        elif x == target[X] and y == target[Y]:
            index = 0
        elif y == 0:
            index = x * 16807
        elif x == 0:
            index = y * 48271
        else:
            index = row[-1] * cave[y-1][x]
        
        erosion = (index + depth) % 20183

        risk += (erosion % 3)

        row.append(erosion)
    cave.append(list(row))

print("Part 1: ", risk)

# helper function fol calulating the manhattan distance
def distance_to_target(pos):
    return abs(target[X] - pos[X]) + abs(target[Y] - pos[Y])

# times will track best time to each location/equip combo
times = dict()

# moves will hold all of our current moves
moves = []

# make terrain map
for y in range(target[Y]+1):
    for x in range(target[X]+1):
        cave[y][x] = cave[y][x] % 3

def add_if_not_already(move,new_x,new_y):
    '''
    This func will add a new move to the move list
    at the new x,y, with all equips possible at the
    new x,y
    '''
    global moves
    global times
    # can't go  negative
    if new_y < 0 or new_x < 0:
        return
    # don't go past where we are bounding the map
    if new_y > bound_y or new_x > bound_x:
        return
    # if the current equip wont work in the new section
    # then we can't move there
    if move.equip == cave[new_y][new_x]:
        return

    # for all the equips
    equips = [NEITHER,TORCH,CLIMBING]
    for e in equips:
        # if the new terrain won't allow the equip
        # skip over it
        if e == cave[new_y][new_x]:
            continue
        move_str = '%d,%d,%d' % (new_x,new_y,e)
        new_move = state(e,[new_x,new_y],move.time+1)
        # if we changed equips to get here
        if e != move.equip:
            new_move.time += 7

        # see if the move already exists
        # if so, if this move was quicker, update
        if move_str in times:
            if times[move_str] > new_move.time:
                times[move_str] = new_move.time
                moves.append(new_move)
        else:
            times[move_str] = new_move.time
            moves.append(new_move)

# our best time (theoretical) is the manhattan distance with a
# gear change each time (including the extra one at the end)
best_time = (target[X] + target[Y]) * 8

# our new cave will extend beyond the target half of the best time
# probably way more extension than necessary
max_x = target[X] + best_time//2
max_y = target[Y] + best_time//2
cave = []
for y in range(max_y+1):
    row = list()
    for x in range(max_x + 1):
        if x == 0 and y == 0:
            index = 0
        elif x == target[X] and y == target[Y]:
            index = 0
        elif y == 0:
            index = x * 16807
        elif x == 0:
            index = y * 48271
        else:
            index = row[-1] * cave[y-1][x]
        
        erosion = (index + depth) % 20183

        row.append(erosion)
    cave.append(list(row))

# make terrain map
for y in range(max_y + 1):
    for x in range(max_x + 1):
        cave[y][x] = cave[y][x] % 3

# add our initial states at 0,0
# if we switch to climbing, add 7 minutes
moves.append(state(TORCH,[0,0],0))
moves.append(state(CLIMBING,[0,0],7))

# while there are viable moves
while len(moves) > 0:
    # update our bounds
    if bound_x < target[X] or bound_y < target[Y]:
        # this first ensures we consider everything
        # that doesn't extend past the target first
        # without this, our options grow unnecessarly large
        bound_x = min(bound_x+1, target[X])
        bound_y = min(bound_y+1, target[Y])
    else:
        bound_x = min(bound_x+1, max_x)
        bound_y = min(bound_y+1, max_y)
    
    # while there are viable moves for this bound
    while len(moves) > 0:
        move = moves.pop(0)
        # if this move is too far away to be viable, skip it
        if move.time + distance_to_target(move.pos) > best_time:
            continue
        # if this move matches the end criteria
        if move.pos[X] == target[X] and move.pos[Y] == target[Y] and move.equip == TORCH:
            # assign any new best_time
            best_time = min(move.time, best_time)
        else:
            # try moving to all adjacent spots
            add_if_not_already(move,move.pos[X]-1,move.pos[Y])
            add_if_not_already(move,move.pos[X]+1,move.pos[Y])
            add_if_not_already(move,move.pos[X],move.pos[Y]-1)
            add_if_not_already(move,move.pos[X],move.pos[Y]+1)
    
    # there are no more viable moves for that bound
    # so lets search the best times for the edges
    # and add them to the viable moves
    for key,value in times.items():
        keys = key.split(',')
        x = int(keys[0])
        y = int(keys[1])
        if x == bound_x or y == bound_y:
            equip = int(keys[2])
            moves.append(state(equip,[x,y],value))

print("Part 2: ", best_time)

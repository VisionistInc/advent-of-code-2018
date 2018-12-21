from copy import deepcopy
import operator

with open('input', 'r') as file:
    input = file.read()

NUM_ELVES = input.count('E')

lines = input.split('\n')

cave = []
for line in lines:
    row = []
    for c in line:
        if c == 'G':
            row.append(' G200')
        elif c == 'E':
            row.append(' E200')
        else:
            row.append(c)
    cave.append(row)

CAVE_ORIG = deepcopy(cave)
CAVE_HEIGHT = len(cave)
CAVE_WIDTH  = len(cave[0])

def has_move(cave,r,c):
    '''
    Determines if this unit should move
    It could be this unit is already adjacent to an enemy
    '''
    for rr in [r-1, r+1]:
        if cave[rr][c] > -1:
            return True
    for cc in [c-1, c+1]:
        if cave[r][cc] > -1:
            return True
    
    return False

def measure_dis(cave,r,c,space):
    cave_copy = deepcopy(cave)
    cave_copy[space[0]][space[1]] = 1
    # here we measure the distance to each foe
    # by starting at the foes and growing outward
    # till all spreading is done
    growth = 1
    growing = True
    while growing and (has_move(cave,r,c) == False):
        growing = False
        for y in range(CAVE_HEIGHT):
            for x in range(CAVE_WIDTH):
                # look for foe distances that match our growth
                if cave_copy[y][x] == growth:
                    for xx in [x-1, x+1]:
                        if cave_copy[y][xx] == -1:
                            cave_copy[y][xx] = growth + 1
                            growing = True
                    for yy in [y-1, y+1]:
                        if cave_copy[yy][x] == -1:
                            cave_copy[yy][x] = growth + 1
                            growing = True
        growth += 1

    # now we can check to see if there is a spot next to our
    # current piece we can move to, in the reading order specified
    answer = [r,c]
    dis = 9999

    if cave_copy[r-1][c] > -1:
        if cave_copy[r-1][c] < dis:
            answer = [r-1, c]
            dis = cave_copy[r-1][c]
    if cave_copy[r][c-1] > -1:
        if cave_copy[r][c-1] < dis:
            answer = [r, c-1]
            dis = cave_copy[r][c-1]
    if cave_copy[r][c+1] > -1:
        if cave_copy[r][c+1] < dis:
            answer = [r, c+1]
            dis = cave_copy[r][c+1]
    if cave_copy[r+1][c] > -1:
        if cave_copy[r+1][c] < dis:
            answer = [r+1, c]
            dis = cave_copy[r+1][c]

    return dis, answer

def make_move(cave, r, c, foe):
    cave_copy = deepcopy(cave)

    # see if any foes remain and
    # gather list of spaces adjacent foes
    adj_foe = []
    for y in range(CAVE_HEIGHT):
        for x in range(CAVE_WIDTH):
            if foe in cave_copy[y][x]:
                cave_copy[y][x] = -2
                for xx in [x-1, x+1]:
                    adj_foe.append([y,xx])
                for yy in [y-1, y+1]:
                    adj_foe.append([yy,x])
            elif cave_copy[y][x] == '.':
                cave_copy[y][x] = -1
            else:
                # if a wall or another friend
                cave_copy[y][x] = -2
    
    # didn't find any foes, we are done
    if len(adj_foe) == 0:
        return False, False, r, c
    
    # now determine how many of those spaces adjacent to foes are vacant
    in_range = []
    for xy in adj_foe:
        if cave_copy[xy[0]][xy[1]] == -1:
            in_range.append(xy)

    # now sort by y value, then x value
    in_range = sorted(in_range, key = operator.itemgetter(0, 1))

    # now, for each space, see how long it is to the piece
    # we are moving this round
    best_dis, new_space = 9999,[r,c]
    for space in in_range:
        dis, go = measure_dis(cave_copy,r,c,space)
        if dis < best_dis:
            best_dis, new_space = dis, go

    if new_space[0] == r and new_space[1] == c:
        return True, False, r, c
    
    return True, True, new_space[0], new_space[1]


def move_piece(cave,r,c,elf_power):

    if cave[r][c] == '#':
        # can't move wall
        return False
    if cave[r][c] == '.':
        # can't move open space
        return False
    if '*' in cave[r][c]:
        # already moved this piece
        return False
    if 'E' in cave[r][c]:
        foe = 'G'
        power = elf_power
    else:
        foe = 'E'
        power = 3

    next_to_enemy = False
    for rr in [r-1, r+1]:
        next_to_enemy |= foe in cave[rr][c]
    for cc in [c-1, c+1]:
        next_to_enemy |= foe in cave[r][cc]

    can_move = False
    if not next_to_enemy:
        foes_alive, can_move, new_r, new_c = make_move(cave,r,c,foe)
        if not foes_alive:
            return True
    
    # mark the piece as already taking their turn
    cave[r][c] = cave[r][c].replace(' ', '*')

    if can_move:
        cave[new_r][new_c] = cave[r][c]
        cave[r][c] = '.'
        r = new_r
        c = new_c
    
    # now, we are all done moving, let's fight

    target = None
    low_hp = 201
    if foe in cave[r-1][c]:
        hp = int(cave[r-1][c][2:])
        if hp < low_hp:
            low_hp = hp
            target = [r-1,c]
    if foe in cave[r][c-1]:
        hp = int(cave[r][c-1][2:])
        if hp < low_hp:
            low_hp = hp
            target = [r,c-1]
    if foe in cave[r][c+1]:
        hp = int(cave[r][c+1][2:])
        if hp < low_hp:
            low_hp = hp
            target = [r,c+1]
    if foe in cave[r+1][c]:
        hp = int(cave[r+1][c][2:])
        if hp < low_hp:
            low_hp = hp
            target = [r+1,c]
    
    if target != None:
        low_hp -= power
        if low_hp < 1:
            cave[target[0]][target[1]] = '.'
        else:
            cave[target[0]][target[1]] = cave[target[0]][target[1]][:2] + str(low_hp)
    
    return False


elves_die = True
elf_power = 3
while elves_die:
    cave = deepcopy(CAVE_ORIG)
    done = False
    rounds = 0
    while not done:
        # make any moves
        for row in range(CAVE_HEIGHT):
            for col in range(CAVE_WIDTH):
                done |= move_piece(cave,row,col,elf_power)
        # remove any moved indicators
        incomplete_round = False
        for row in range(CAVE_HEIGHT):
            for col in range(CAVE_WIDTH):
                if ('E' in cave[row][col]) or ('G' in cave[row][col]):
                    if ' ' in cave[row][col]:
                        incomplete_round = True
                    else:
                        cave[row][col] = cave[row][col].replace('*', ' ')
        if not incomplete_round:
            rounds += 1
    
    # no more moves made
    total = 0
    for row in cave:
        for col in row:
            if len(col) > 1:
                total += int(col[2:])
    if elf_power == 3:
        print("Part 1: ", total*rounds)

    elf_count = 0
    for row in cave:
        for col in row:
            if 'E' in col:
                elf_count += 1
    print('Elf Power %d: %d/%d elves lived' % (elf_power, elf_count, NUM_ELVES))

    if elf_count == NUM_ELVES:
        elves_die = False
        print("Part 2: ", total*rounds)

    elf_power += 1
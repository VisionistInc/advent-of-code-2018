with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

# turn input into coordinates
coords = []
for line in lines:
    x,y = line.split(', ')
    x = int(x)
    y = int(y)
    coords.append([x,y])

def man_dis(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

# initialize max values, used to bound my map
max_x = coords[0][0]
max_y = coords[0][1]
min_x = coords[0][0]
min_y = coords[0][1]
for xy in coords:
    max_x = max(max_x, xy[0])
    max_y = max(max_y, xy[1])
    min_x = min(min_x, xy[0])
    min_y = min(min_y, xy[1])

# list of area for each coordinate
areas = [0] * len(lines)

# find coordinates with infinite areas
for i in range(len(areas)):
    x = coords[i][0]
    y = coords[i][1]

    # 4 cardinal directions to extend, all infinite for now
    infinite = [True] * 4

    # compare to every other coordinate
    for xy in coords:
        if xy == coords[i]:
            continue

        _x = xy[0]
        _y = xy[1]
        
        # to extend left forever (past a further left coordinate)
        # make sure it is far enough away on the y axis
        if x > _x:
            if (abs(y-_y)) <= x - _x:
                infinite[0] = False
        # to extend right forever (past a further right coordinate)
        # make sure it is far enough away on the y axis
        if x < _x:
            if (abs(y-_y)) <= _x - x:
                infinite[1] = False
        # to extend north forever (past a further north coordinate)
        # make sure it is far enough away on the x axis
        if y > _y:
            if (abs(x-_x)) <= y - _y:
                infinite[2] = False
        # to extend south forever (past a further south coordinate)
        # make sure it is far enough away on the x axis
        if y < _y:
            if (abs(x-_x)) <= _y - y:
                infinite[3] = False
    
    # if, after iterating through all the coordinates, one of the
    # directions remains True, it is an infinite coordinate
    if True in infinite:
        # flag it
        areas[i] = -1

# determine the biggest x and y diff between coordinates
# cut in half, because that is where there manhattans will meet
h = (max_y - min_y) // 2 + 1
w = (max_x - min_x) // 2 + 1

# we add the y range to the min/max x values because there is no
# chance of one consuming the other after that
# same for the x range to the min/max y values
# gives us a decent bound
# but there is probably a better way to determine when infinity starts
for x in range(min_x-h, max_x+h):
    for y in range(min_y-w, max_y+w):
        # init crazy high distance
        min_dis = 999999999999
        targets = []
        # iterate over all the coordinates to determine their distance
        for i in range(len(areas)):
            dis = man_dis(coords[i], [x,y])
            # save off new shorter coordinate
            if dis < min_dis:
                targets = [i]
                min_dis = dis
            # else if the same, append to the list of shortest
            elif dis == min_dis:
                targets.append(i)
        # as long as we have one winner, and they weren't flagged
        # as an infinite coordinate, we can increase their area score
        if len(targets) == 1 and areas[targets[0]] != -1:
            areas[targets[0]] += 1

print("Part 1: ", max(areas))

# our answer
area = 0

# from the problem
MAX_DIS=10000
# we can't extend MAX_DIS past a point, we know the sum wont add up
# so we have to limit how far we extend by splitting up MAX_DIS evenly
MAX_LEG=(MAX_DIS//len(coords)) + 1

# now we can figure out some bounded ranges
min_x -= MAX_LEG
min_y -= MAX_LEG
max_x += MAX_LEG
max_y += MAX_LEG

# iterate over all the xy, determine if they qualify
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        dis = 0
        for xy in coords:
            dis += man_dis(xy, [x,y])
            if dis >= MAX_DIS:
                break
        if dis < MAX_DIS:
            area += 1
print("Part 2: ", area)
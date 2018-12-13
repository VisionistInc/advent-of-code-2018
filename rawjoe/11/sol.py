with open('input', 'r') as file:
    input = file.read()

SERIAL = int(input)

GRID_SIZE = 300

grid = [[0] * GRID_SIZE for i in range(GRID_SIZE)]

# figure out power for each fuel cell
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        rack_id = (x + 1) + 10
        val = ((rack_id * (y+1)) + SERIAL) * rack_id
        val = (val % 1000) // 100
        val -= 5
        grid[x][y] = val

# for every 3x3 square, see if the combined power is the largest
max_power = None
for x in range(GRID_SIZE-2):
    for y in range(GRID_SIZE-2):
        power =  sum(grid[x][y:y+3])
        power += sum(grid[x+1][y:y+3])
        power += sum(grid[x+2][y:y+3])
        if max_power == None or power > max_power:
            max_power = power
            x_sol = x+1
            y_sol = y+1

print("Part 1: ", x_sol, y_sol)

# for every x/y
max_power = None
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        # we need to find the largest side a square can be
        max_d = min(GRID_SIZE-x, GRID_SIZE-y)
        power = 0
        # start with a 1x1 square, grow to 2x2, up till max d
        for d in range(max_d):
            col = 0
            # add the new column to the current square total power
            for xx in range(x, x+d+1):
                col += grid[xx][y+d]
            # add the new row to the current square total power
            power += sum(grid[x+d][y:y+d+1])
            power += col
            # when we add the whole column and row, we actually add
            # the bottom right-most square twice, so we subtract it
            power -= grid[x+d][y+d]
            if max_power == None or power > max_power:
                max_power = power
                x_sol = x+1
                y_sol = y+1
                d_sol = d+1

print("Part 2: ", x_sol, y_sol, d_sol)
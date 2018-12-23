import re

with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

CLAY = '#'
SAND = ' '
WATER = '~'

max_x = 0
min_x = 9999999999
min_y = 9999999999
max_y = 0

# determine min/max values
for line in lines:
    nums = re.findall(r'-?\d+', line)
    nums = [ int(x) for x in nums ]
    if line[0] == 'x':
        max_x = max(nums[0], max_x)
        min_x = min(nums[0], min_x)
        min_y = min(nums[1], min_y)
        max_y = max(nums[2], max_y)
    else:
        min_y = min(nums[0], min_y)
        max_y = max(nums[0], max_y)
        min_x = min(nums[1], min_x)
        max_x = max(nums[2], max_x)

# fill out land with SAND
land = []
rows = [SAND] * (max_x + 2)
for y in range(max_y+1):
    land.append(list(rows))

def print_land():
    print('-------------------------------')
    for row in land:
        print(''.join(row[min_x-1:]))

# now add in CLAY from input
for line in lines:
    nums = re.findall(r'-?\d+', line)
    nums = [ int(x) for x in nums ]
    if line[0] == 'x':
        for y in range(nums[1], nums[2]+1):
            land[y][nums[0]] = CLAY
    else:
        for x in range(nums[1], nums[2]+1):
            land[nums[0]][x] = CLAY

# a drip point is the first sand point under water
land[0][500] = WATER
drip_points = [[1,500]]

# fill out land with water from a drip point
def fill_out(y,x):
    global land

    # already has water, done
    if land[y][x] == WATER:
        return

    y_start = y
    x_start = x
    
    # drip down to first clay (or bottom)
    while (y <= max_y) and (land[y][x] != CLAY) :
        #print(y,x)
        land[y][x] = WATER
        y += 1

    # dripped to bottom, done, not spreading out at all
    if y > max_y:
        return
    
    # y is clay, so go back a row
    y -= 1

    new_drip_point = False

    # now lets raise the water level
    while new_drip_point == False:
        x = x_start
        land[y][x] = WATER
        # flood left
        while land[y][x] != CLAY:
            x -= 1
            if (land[y+1][x] == WATER) and (land[y+1][x+1] == CLAY) and (land[y][x-1] == SAND):
                new_drip_point = True
                break
            if land[y][x] != CLAY:
                land[y][x] = WATER
                if land[y+1][x] == SAND:
                    new_drip_point = True
                    drip_points.append([y+1,x])
                    break
        # flood right
        x = x_start
        while land[y][x] != CLAY:
            x += 1
            #print(y,x)
            if (land[y+1][x] == WATER) and (land[y+1][x-1] == CLAY) and (land[y][x+1] == SAND):
                new_drip_point = True
                break
            if land[y][x] != CLAY:
                land[y][x] = WATER
                if land[y+1][x] == SAND:
                    new_drip_point = True
                    drip_points.append([y+1,x])
                    break
        y -= 1

# keep filling out water for each drip point we identify
while len(drip_points) > 0:
    point = drip_points.pop()
    fill_out(point[0],point[1])
    
water_count = 0
for y in range(min_y, max_y+1):
    water_count += ''.join(land[y]).count(WATER)
#print_land()
print(water_count)

# remove all water at very bottom
for x in range(min_x-1, max_x+2):
    if land[max_y][x] == WATER:
        land[max_y][x] = SAND

removing = True
while removing:
    removing = False
    for y in range(max_y):
        for x in range(min_x-1, max_x+2):
            if land[y][x] == WATER:
                # if sand below, or to left or right
                if land[y+1][x] == SAND or land[y][x-1] == SAND or land[y][x+1] == SAND:
                    land[y][x] = SAND
                    removing = True

water_count = 0
for y in range(min_y, max_y+1):
    water_count += ''.join(land[y]).count(WATER)
#print_land()
print(water_count)
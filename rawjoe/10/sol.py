import re

with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

class Spot:
    def __init__(self, l):
        nums = re.findall(r'-?\d+', l)
        self.x = int(nums[0])
        self.y = int(nums[1])
        self.x_vel = int(nums[2])
        self.y_vel = int(nums[3])
    
    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
    
    def is_next(self, spot):
        # two spots are neighbors if they are at most 1 x or 1 y away
        x_dis = abs(self.x - spot.x)
        y_dis = abs(self.y - spot.y)
        if (x_dis + y_dis) == 1:
            return True
        return False

# init the spots
spots = []
for line in lines:
    spots.append(Spot(line))

time = 0
while True:
    time += 1

    # grab out the min and max x/y for use later
    min_x = spots[0].x
    min_y = spots[0].y
    max_x = spots[0].x
    max_y = spots[0].y
    for spot in spots:
        spot.update()
        min_x = min(spot.x, min_x)
        min_y = min(spot.y, min_y)
        max_x = max(spot.x, max_x)
        max_y = max(spot.y, max_y)
    
    # look and see how far away the furthest spots are
    # we can make a reasonable assumption they have to be somewhat close
    # to spell out a word in the sky
    # and this prevents us from doing costly calculations below
    if ((max_x - min_x) + (max_y - min_y)) > 2 * len(spots):
      continue
    
    # ok, all the spots are starting to come together
    # we want to see how many are actually next to another one
    # we assume the majority will be next to another spot
    # in order to spell words in the sky
    neighbors = 0
    for i in range(len(spots)):
        for j in range(len(spots)):
            if spots[i].is_next(spots[j]):
                neighbors += 1
                break
    
    # if more than 3/4 spots touch, we assume we have our answer
    if neighbors >= 3*len(spots)/4:
        print("Part 1:")

        # for each x/y, see if it matches a spot
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                found = False
                for s in spots:
                    if x == s.x and y == s.y:
                        found = True
                        break
                if found:
                    print('#', end='')
                else:
                    print('_', end='')
            print('')

        print("Part 2: ", time)
        break
with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

def parse(line):
    num, at, base, size = line.split(' ')
    start_x, start_y = base.split(',')
    width, height = size.split('x')
    start_x = int(start_x)
    start_y = int(start_y[:-1])
    width = int(width)
    height = int(height)
    
    return start_x, start_y, width, height

used = set()
overlap = set()

for line in lines:
   start_x, start_y, width, height = parse(line)
   for x in range(start_x, start_x+width):
       for y in range(start_y, start_y+height):
           coord = "%d-%d" % (x,y)
           if coord in used:
               # since it's a set,
               # no dup entries will get added
               overlap.add(coord)
           else:
               used.add(coord)

print("Part 1: %s" % len(overlap))

def do_overlap(start_1, len_1, start_2, len_2):
    if (start_1 < start_2) and (start_1 + len_1 > start_2):
        return True
    if start_1 == start_2:
        return True
    if (start_2 < start_1) and (start_2 + len_2 > start_1):
        return True
    return False

for first in range(len(lines)):
    collide = False
    for second in range(len(lines)):
        if second == first:
            continue
        f_x, f_y, f_w, f_h = parse(lines[first])
        s_x, s_y, s_w, s_h = parse(lines[second])
        if do_overlap(f_x, f_w, s_x, s_w):
            if do_overlap(f_y, f_h, s_y, s_h):
                # if the x values overlap and
                # the y values overlap
                # we collide
                collide = True
                break
    if collide == False:
        # if collide was never set, we found ours
        print("Part 2: %d" % (first+1))

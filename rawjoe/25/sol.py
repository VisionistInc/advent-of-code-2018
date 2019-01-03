with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

points = []

for line in lines:
    line = line.split(',')
    point = [int(x) for x in line]
    points.append(list(point))

def in_range(p1, p2):
    dis = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2]) + abs(p1[3]-p2[3])
    return dis < 4

num_const = 0

while len(points) > 0:
    num_const += 1
    const = []
    const.append(points.pop())
    for p1 in const:
        for p2 in points:
            if in_range(p1,p2):
                const.append(p2)
                points.remove(p2)

print("Part 1: ", num_const)

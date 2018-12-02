with open('input', 'r') as file:
    input = file.read()

lines = input.split()

two_cnt = 0
three_cnt = 0

for line in lines:
    two = False
    three = False
    for c in line:
        if line.count(c) == 2:
            two = True
        if line.count(c) == 3:
            three = True
    
    if two:
        two_cnt += 1
    if three:
        three_cnt += 1

print ("Part 1: %d" % (two_cnt * three_cnt))

line_len = len(lines[0])
num_lines = len(lines)

for i in range(num_lines):
    for j in range(i+1, num_lines):
        differ = 0
        for k in range(line_len):
            if lines[i][k] != lines[j][k]:
                differ += 1
            if differ > 1:
                break
        if differ == 1:
            print("Part 2: ", end='')
            for k in range(line_len):
                if lines[i][k] == lines[j][k]:
                    print(lines[i][k], end='')
            exit()
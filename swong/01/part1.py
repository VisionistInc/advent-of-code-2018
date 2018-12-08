x = 0

with open('./input.txt', 'r') as file:
    for line in file:
        x += int(line)

print('sum = ', x)
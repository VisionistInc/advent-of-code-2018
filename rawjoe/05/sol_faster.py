with open('input', 'r') as file:
    input = file.read()

def reduce_string(s):
    while True:
        length = len(s)
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            remove = '%s%s' % (c, c.lower())
            s = s.replace(remove, '')
            remove = '%s%s' % (c.lower(),c)
            s = s.replace(remove, '')
        if len(s) == length:
            break
    return len(s)

print("Part 1: ", reduce_string(input))

minimum = 99999999999
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    test = input.replace(c, '')
    test = test.replace(c.lower(), '')
    length = reduce_string(test)
    if length < minimum:
        minimum = length

print("Part 2: ", minimum)
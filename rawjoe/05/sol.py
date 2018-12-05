with open('input', 'r') as file:
    input = file.read()

def reduce_list(l):
    while True:
        found = False
        for i in range(len(l)-1):
            if i + 1 >= len(l):
                break
            if l[i].lower() == l[i+1].lower():
                if l[i] != l[i+1]:
                    l.pop(i)
                    l.pop(i)
                    found = True
        if found == False:
            break
    return len(l)

print("Part 1: ", reduce_list(list(input)))

minimum = 99999999999
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    test = input.replace(c, '')
    test = test.replace(c.lower(), '')
    length = reduce_list(list(test))
    if length < minimum:
        minimum = length

print("Part 2: ", minimum)
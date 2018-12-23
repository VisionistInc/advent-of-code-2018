# this python was created by the analysis in README
# the values of r4 will probably bary based on your input

def solve(r4):
    r0 = 0
    r5 = 1
    while r5 <= r4:
        if r4 % r5 == 0:
            r0 += r5
        r5 += 1
    
    return r0


print('Part 1: ', solve(906))

print('Part 2: ', solve(10551306))
with open('input', 'r') as file:
    input = file.read()

nums = input.split()

i = 0

for num in nums:
    i += int(num)

print("Part 1: %d" % i)

i = 0

# if i had used a set first instead of a list
# i would have finished much faster
freqs = {0}

while True:

    for num in nums:
        i += int(num)
        if i in freqs:
            print("Part 2: %d" % i)
            exit()
        freqs.add(i)
#!/usr/bin/env python3

with open('input') as infile:
    lines = [x.strip() for x in infile.readlines()]

    # part 1
    twos = 0
    threes = 0
    for line in lines:
        # sort the characters in a line, convert to a set, then get the count of each (unique) caracter in the original string
        charcounts = list(map(lambda x: line.count(x), set(sorted(line))))
        if 2 in charcounts:
            twos += 1
        if 3 in charcounts:
            threes += 1
    print(twos * threes)

    # part 2 (lazy coding ftw)
    for line in lines:
        for otherline in lines:
            if line != otherline:
                differences = 0
                matchingchars = []
                # compare chars, if they match, add to list for submission, otherwise indicate difference
                for i in range(len(line)):
                    if line[i] == otherline[i]:
                        matchingchars.append(line[i])
                    else:
                        differences += 1
                # looking for exactly 1 difference
                if differences == 1:
                    # better output for copy/paste
                    print(''.join(matchingchars))
                    exit(0)
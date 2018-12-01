#!/usr/bin/env python3

with open('input') as infile:
    lines = [int(x.strip()) for x in infile.readlines()]

    # part1
    print(sum(lines))

    # part2
    sum = 0
    values = {0}
    while True:
        for line in lines:
            sum += line
            if sum in values:
                print('found sum!')
                print(sum)
                exit(0)
            values.add(sum)

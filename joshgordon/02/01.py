#!/usr/bin/env python3

from itertools import groupby

with open("input.txt", "r") as f:
    data = f.read().strip()
    array = data.split("\n")

    count_2x = 0
    count_3x = 0

    for element in array:
        has_2 = False
        has_3 = False
        element = list(element)
        element.sort()
        for key, group in groupby(element):
            length = len(list(group))
            if length == 2:
                has_2 = True
            if length == 3:
                has_3 = True

        if has_2:
            count_2x += 1
        if has_3:
            count_3x += 1

    print(f"2x: {count_2x}, 3x: {count_3x}, sum = {count_2x * count_3x}")

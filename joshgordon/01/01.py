#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    data = f.read().strip()
    array = [int(x) for x in data.split("\n")]
    result = sum(array)
    print(result)

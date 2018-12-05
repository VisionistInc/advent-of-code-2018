#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    data = f.read().strip()
    seen = set()
    array = [int(x) for x in data.split("\n")]
    current = 0
    iters = 0
    while True:
        num = array[iters % len(array)]
        iters += 1
        current += num
        if current in seen:
            print(f"answer: {current} found in {iters} iterations.")
            break
        seen.add(current)

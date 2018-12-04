#!/usr/bin/env python3


class InventoryId:
    """
    Yup, I know this whole thing is overkill, but I've never _actually_ done
    operator overloading in python, so now is as good a time as any to learn.
    """

    string = ""

    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __sub__(self, other):
        result = ""
        for idx, char in enumerate(self.string):
            if other.string[idx] == char:
                result += char
        return result

    def __eq__(self, other):
        return self.string == other.string

    def __repr__(self):
        return self.string


with open("input.txt", "r") as f:
    data = f.read().strip()
    array = data.split("\n")

array = [InventoryId(string) for string in array]
length = len(array[0])
target_length = length - 1

for idx, string in enumerate(array):
    for string2 in array[idx + 1 :]:
        diff = string2 - string
        if len(diff) == target_length:
            print(diff)

import re
from boilerplate import AdventOfCode


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Claim:
    _claim_re = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    def __init__(self, claim):
        match = self._claim_re.match(claim)
        self.id = int(match[1])
        self.left = int(match[2])
        self.top = int(match[3])
        self.width = int(match[4])
        self.height = int(match[5])

    def __hash__(self):
        return hash((self.id, self.left, self.top, self.width, self.height))

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.left == other.left
            and self.top == other.top
            and self.width == other.width
            and self.height == other.height
        )

    def __repr__(self):
        return f"#{self.id} @ {self.left},{self.top}: {self.width}x{self.height}"

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top + self.height

    def __sub__(self, other):
        # check the case when there's no overlap at all
        if (
            other.left > self.right
            or other.right < self.left
            or other.top > self.bottom
            or other.bottom < self.top
        ):
            return []

        overlap = []
        # figure out what the overlap is.
        for x in range(self.left, self.right):
            for y in range(self.top, self.bottom):
                sq = Square(x, y)
                if sq in other:
                    overlap.append(sq)
        return overlap

    def __contains__(self, value):
        return (
            value.x >= self.left
            and value.x < self.right
            and value.y >= self.top
            and value.y < self.bottom
        )


with AdventOfCode() as aoc:
    array = [Claim(e) for e in aoc]

all_claims = set(array)

for idx, claim in enumerate(array):
    for remainder in array[idx + 1 :]:
        overlap = claim - remainder
        if len(overlap) > 0:
            all_claims.discard(claim)
            all_claims.discard(remainder)

print(all_claims)

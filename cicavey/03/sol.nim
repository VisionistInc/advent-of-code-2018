import parseutils
import re
import tables
import strformat

type Claim = tuple[id: int, x: int, y: int, w: int, h: int]

var claims: seq[Claim]

for line in "input".lines:
    var m: array[5, string]
    if match(line, re"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", m):
        # This is awful
        var c : Claim
        discard parseInt(m[0], c[0])
        discard parseInt(m[1], c[1])
        discard parseInt(m[2], c[2])
        discard parseInt(m[3], c[3])
        discard parseInt(m[4], c[4])
        claims.add(c)

type Point = tuple[x: int, y: int]

var grid = newTable[Point, int]()

for c in claims:
    var has_overlap = false
    var ex = c.x + c.w
    var ey = c.y + c.h
    for x in c.x..<ex:
        for y in c.y..<ey:
            var p:Point = (x,y)
            grid.mgetOrPut(p, 0) += 1

var safe_claim:Claim

for c in claims:
    var has_overlap = false
    var ex = c.x + c.w
    var ey = c.y + c.h
    block outer:
        for x in c.x..<ex:
            for y in c.y..<ey:
                var p:Point = (x,y)
                if grid[p] > 1:
                    has_overlap = true
                    break outer
    if not has_overlap:
        safe_claim = c
                
echo fmt"Non-overlapping claim id: {safe_claim.id}"

var over:int = 0
for p,v in grid:
    if v > 1:
        over += 1
echo fmt"Num overlapping squares: {over}"

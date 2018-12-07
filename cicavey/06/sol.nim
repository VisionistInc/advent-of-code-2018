import strutils
import strformat
import tables
import algorithm

type Point = tuple[x: int, y: int]

proc manDist(a:Point, b:Point) : int =
  return abs(a.x - b.x) + abs(a.y - b.y)

proc add(a:var Point, v:int) =
  a.x += v
  a.y += v

proc cadd(a: Point, v:int): Point =
  return (a.x + v, a.y + v)

var min:Point = (high(int), high(int))
var max:Point = (low(int), low(int))

var targets: seq[Point]

for line in "input".lines:
  let s = line.split(", ")
  let p:Point = (parseInt(s[0]), parseInt(s[1]))
  targets.add(p)

  if p.x < min.x: min.x = p.x
  if p.y < min.y: min.y = p.y
  if p.x > max.x: max.x = p.x
  if p.y > max.y: max.y = p.y

let max_delta = max(max.x - min.x, max.y-min.y)

min.add(-1)
max.add(1)

proc magic(min : Point, max : Point) : TableRef[int, int] =

  var grid = newTable[Point, int]()
  for y in min.y..max.y:
    for x in min.x..max.x:
      let p:Point = (x, y)

      var mind = high(int)
      var idx = -1
      for i in 0..<targets.len:
        let d = p.manDist(targets[i])
        if d < mind:
          mind = d
          idx = i

      var matches = 0
      for i in 0..<targets.len:
        let d = p.manDist(targets[i])
        if d == mind:
          matches += 1
      
      if matches > 1:
        grid[p] = -1
      else:
        grid[p] = idx

  var hist = newTable[int, int]()

  for p, v in grid:
    if v != -1:
      hist.mgetOrPut(v, 0) += 1

  return hist

let base = magic(min, max)
let ext = magic(min.cadd(-max_delta*2), max.cadd(max_delta*2))

var finite: seq[(int, int)]

for k, v in base:
  if v == ext[k]:
    finite.add((k, v))

finite.sort(proc(a, b : (int, int)): int = 
    cmp(a[1], b[1])
)

echo finite[^1]

# Calculate distance to all targets for all points
var grid = newTable[Point, int]()
for y in min.y..max.y:
  for x in min.x..max.x:
    let p:Point = (x, y)
    for i in 0..<targets.len:
      let d = p.manDist(targets[i])
      grid.mgetOrPut(p, 0) += d

var c = 0
for p, v in grid:
  if v < 10000:
    c += 1
echo c
import strutils
import re
import tables
import strformat

type Body = tuple[id: int, x: int, y: int, vx: int, vy: int]

proc step(b : var Body) = 
  b.x += b.vx
  b.y += b.vy

proc bounds(bodies: var seq[Body]): seq[int] = 

  var minX = high(int)
  var maxX = low(int)
  var minY = high(int)
  var maxY = low(int)

  for b in bodies.mitems:
    minX = min(minX, b.x)
    maxX = max(maxX, b.x)
    minY = min(minY, b.y)
    maxY = max(maxY, b.y)

  return @[minX, minY, maxX, maxY]

var bodies : seq[Body]

var i = 0
for line in "input".lines:
    var m: array[4, string]
    if match(line, re"position=<(.*?),(.*?)> velocity=<(.*?),(.*?)>", m):
        var b : Body
        b.id = i
        b[1] = parseInt(m[0].strip())
        b[2] = parseInt(m[1].strip())
        b[3] = parseInt(m[2].strip())
        b[4] = parseInt(m[3].strip())
        i += 1
        bodies.add(b)

for s in 1..10000000:
  for b in bodies.mitems:
    b.step()
  let bb = bodies.bounds()
  if abs(bb[3] - bb[1]) < 19:
    echo s, bb, abs(bb[3] - bb[1])
    break
  if s mod 100000 == 0:
    echo s, bb, abs(bb[3] - bb[1])

let bb = bodies.bounds()
for y in bb[1]..bb[3]:
  for x in bb[0]..bb[2]:
    var f = false
    for b in bodies:
      if b.x == x and b.y == y:
        system.stdout.write "#"
        f = true
        break
    if not f:
      system.stdout.write "."
  echo ""
        
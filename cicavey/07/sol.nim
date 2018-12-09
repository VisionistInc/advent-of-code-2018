import strutils
import strformat
import tables
import algorithm
import sets
import sequtils

let cost_base = 60;

type Node = tuple[key:char, deps:HashSet[char], time:int]

proc empty(n:Node): bool =
  n.deps.len == 0


# Mostly for lookup, use a sorted list of Nodes instead
var nodes = newOrderedTable[char, Node]()

for line in "input".lines:
  let s = line.split(" ")
  let child = s[1][0]
  let parent = s[7][0]

  if not nodes.hasKey(child):
    nodes[child] = (child, initSet[char](), cost_base + (int(child) - 64))

  if not nodes.hasKey(parent):
    nodes[parent] = (parent, initSet[char](), cost_base + (int(parent) - 64))

  nodes[parent].deps.incl(child)

# resort table by key
nodes.sort(proc(a,b:(char, Node)): int = 
  cmp(a[0], b[0])
)

type Worker = tuple[key:char, time:int]

var free = newSeq[Worker](1 + 4)
var work = newSeq[Worker]()

var o = newSeq[char]()

proc join(s : seq[char]): string = 
  var oStr: string
  for n in s:
    oStr &= n
  return oStr

var t = 0

while nodes.len > 0 or work.len > 0:
  for k, node in nodes:
    let os = toSet(o)
    if node.empty:
      if free.len > 0:
        var w = free.pop()
        w.key = k
        w.time = node.time
        work.add(w)
        nodes.del(k)

    elif node.deps <= os:

      if free.len > 0:
        var w = free.pop()
        w.key = k
        w.time = node.time
        work.add(w)
        nodes.del(k)

    if free.len == 0:
      break
  

  var l:string  = fmt"{t}:"
  for w in work:
    l &= fmt" {w.key} "
  l &= " | " & o.join()

#  echo t, " :: ", work.len, " % ", free.len, " | ", o.join()
  echo l
  for i, w in work.mpairs:
    w.time -= 1
    if w.time == 0:
      free.add(w)
      o.add(w.key)

  work.keepIf(proc(w: Worker): bool = w.time > 0)

  t += 1

echo t

import strutils
import re
import tables
import sets
import strformat
import times
import algorithm

type Action = enum Start, Wake, Sleep
type Event = tuple[id: int, action: Action, stamp: DateTime]

var events: seq[Event]

var g: array[7, string]
for line in "input".lines:
    if match(line, re"\[(.*?)\] (falls|wakes|Guard #(\d+))", g):
        var e:Event = (-1, Start, parse(g[0], "yyyy-MM-dd HH:mm"))
        case g[1]:
          of "falls":
            e.action = Sleep
          of "wakes":
            e.action = Wake
          else:
            e.id = parseInt(g[2])
        events.add(e)

# time order
events.sort(proc(x, y: Event): int = 
  cmp(x.stamp, y.stamp)
)

var guards= initSet[int]() # unique guards

# Fix up ids
var last:int
for i in 0..<events.len: # for-each are immutable? ugh
  var e = events[i]
  if e.action == Start:
    last = e.id
  e.id = last
  events[i] = e # probably should have stored references or something
  guards.incl(e.id)

# track sleep (guard id, cummulative minutes)
var s = newTable[int, int64]() # guardId -> totalSleep
var sHist = newTable[(int, int), int]() # (guardId, minute) -> freq
for i in 1..<events.len:
  let prev = events[i-1]
  let cur = events[i]

  if cur.action == Wake and prev.action == Sleep:
    # Track total sleep
    s.mgetOrPut(cur.id, 0) += minutes(cur.stamp - prev.stamp)
    # Also build histogram for guard
    for m in prev.stamp.minute..<cur.stamp.minute:
      sHist.mgetOrPut((cur.id, m), 0) += 1

var maxid: int
var maxsleep: int64

# which guard slept the most
for id, sleep in s:
  if sleep > maxsleep:
    maxsleep = sleep
    maxid = id

# helper to figure out max minute for given guard
proc max_minute(gid: int): int = 
  var maxf: int
  var maxm: int
  for m in 0..59:
    let f = sHist.getOrDefault((gid, m))
    if f > maxf:
      maxf = f
      maxm = m
  return maxm

echo max_minute(maxid) * maxid


# which guard sleep the most on which minute
var maxg: int
var maxm: int
var maxf: int
for g in guards:
  let mm = max_minute(g)
  let f = sHist.getOrDefault((g,mm))
  if f > maxf:
    maxf = f
    maxg = g
    maxm = mm
echo maxg * maxm

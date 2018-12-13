import strutils

var l = newSeq[string]()
for a in "input".lines:
  if a.isNilOrWhitespace():
    continue
  l.add(a)

type Pattern = tuple[p: string, v: string]

var state = "....." & l[0][15..^1] & "....................................................................................................................................................................................................................................................................................................................................................."
var s2 = newString(state.len)

var pats = newSeq[Pattern]()
for pat in l[1..^1]:
  var p : Pattern = (pat[0..4], pat[9..9])
  pats.add(p)

proc potcount(state: var string): int = 
  var pCount = 0
  for i in 0..<state.len:
    let pn = i - 5
    if state[i] == '#':
      pCount += pn
  return pCount


var prev = 0
var delta = 0

for g in 0..<1000:
  #echo state
  for i in 0..<state.len:
    var n : string
    if i == 0:
      n = ".." & state[0..2]
    elif i == 1:
      n = "." & state[0..3]
    elif i == state.len-2:
      n = state[i-3..i] & "."
    elif i == state.len-1:
      n = state[i-2..i] & ".."
    else:
      n = state[i-2..i+2]

    var found = false
    for p in pats:
      if n == p.p:
        found = true
        s2[i] = p.v[0]
        break;
    if not found:
      s2[i] = '.'
  state = s2

  state &= "."
  s2 &= "."

  let cur = potcount(state)
  
  if g == 19:
    echo cur

  # echo g, " : " , cur - prev, " ", cur, " ", prev

  if delta == cur-prev:
    let base = prev - delta
    #echo base, " ", g-2
    echo base + ((50_000_000_000 - (g-1)) * delta)

    break

  delta = cur - prev
  prev = cur
  

#echo state

# var pCount = 0
# for i in 0..<state.len:
#   let pn = i - 5
#   if state[i] == '#':
#     pCount += pn
# echo pCount

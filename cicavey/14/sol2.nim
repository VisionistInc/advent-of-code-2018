import lists
import strutils
import sequtils

var b = initDoublyLinkedRing[int]()
b.append(3)
b.append(7)

var e1 = b.head
var e2 = e1.next

let targ = 409551
#let targ = 59414
let targS = $targ
let SVL = ($targ).len
let SV = ($targ)[0]

proc ns(start : DoublyLinkedNode[int], s: int) : string = 
  var cur = start
  var r = ""
  for i in 0..<s:
    r = r & $cur.value
    cur = cur.next
  return r

var pNode = b.head
var pTotal = 0

var total = 2

type PMatch = tuple[node : DoublyLinkedNode[int], total: int, fail: bool]
var potential = newSeq[PMatch]()
var found = false
while total < 100000000 and not found: #total < (targ + 10):
  let v = e1.value + e2.value
  for c in $v:
    var newNode = newDoublyLinkedNode(parseInt($c))
    b.append(newNode)
    total += 1

    # potential match if we just added a value equal to the first digit of input
    if c == SV:
      potential.add((newNode, total-1, false))

  for i in 0..<e1.value+1:
    e1 = e1.next
  for i in 0..<e2.value+1:
    e2 = e2.next

  #echo "! ", potential.len
  for pm in potential.mitems:
    if total - pm.total > SVL:
      #echo " test ", pm.node.value, " ", pm.total, " ", pm.fail
      if pm.node.ns(SVL) == targS:
        found = true
        echo pm.total
      else:
        pm.fail = true
  potential.keepIf(proc(pm : PMatch): bool = not pm.fail)
#echo total
#[
var res = ""
var cur = b.head
for i in 0..total:
  if i >= targ and i < targ + 10:
    res = res & $cur.value
  cur = cur.next
echo res
]#

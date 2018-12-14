import lists
import strutils

var b = initDoublyLinkedRing[int]()
b.append(3)
b.append(7)

var e1 = b.head
var e2 = e1.next

let targ = 409551
var total = 2

while total < (targ + 10):
  let v = e1.value + e2.value
  for c in $v:
    b.append(parseInt($c))
    total += 1
  for i in 0..<e1.value+1:
    e1 = e1.next
  for i in 0..<e2.value+1:
    e2 = e2.next

echo total

var res = ""
var cur = b.head
for i in 0..total:
  if i >= targ and i < targ + 10:
    res = res & $cur.value
  cur = cur.next
echo res

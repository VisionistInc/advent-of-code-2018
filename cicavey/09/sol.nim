#import sequtils
import lists

proc simulate(n:int, np:int): int =
  var ps = newSeq[int](np)

  var c = initDoublyLinkedRing[int]()
  c.append(0)
  var cm = c.head

  var p = 0 # current player
  for mv in 1..n: # marble value
    # p's turn to play marble with value mv

    if mv mod 23 == 0:
      for i in 0..<7:
        cm = cm.prev
      ps[p] += mv + cm.value
      cm.prev.next = cm.next
      cm.next.prev = cm.prev
      cm = cm.next

    else:
      cm = cm.next

      var node = newDoublyLinkedNode(mv)

      node.next = cm.next
      node.prev = cm
      cm.next.prev = node
      cm.next = node
      cm = node


    p = (p + 1) mod np
  
  max(ps)

echo simulate(25, 9)
echo simulate(1618, 10)
echo simulate(7999, 13)
echo simulate(1104, 17)
echo simulate(6111, 21)
echo simulate(5807, 30)
echo simulate(71082, 413)
echo simulate(7108200, 413)
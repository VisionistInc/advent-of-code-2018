import lists
import strutils

proc react(data: var DoublyLinkedList[char], len: int): int =
  var ogl = len
  var i = data.head
  while i != nil and i.next != nil:
    let a = i.value
    let b = i.next.value
    if abs(int(a) - int(b)) != 32:
      i = i.next
    else:
      let prev = i.prev
      data.remove i.next
      data.remove i
      i = prev
      ogl -= 2
  return ogl


var input = readFile("input")
#var input = "dabAcCaCBAcCcaDA"

for ex in 'a'..'z':
  
  let uex = int(ex) - 32
  let lex = int(ex)

  var data = initDoublyLinkedList[char]()
  var ogLen = input.len
  for c in input:
    if int(c) == uex or int(c) == lex:
      ogLen -= 1
      continue
    data.append(c)
  echo react(data, ogLen), ex
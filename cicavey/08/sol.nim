import strutils
import sequtils
import strformat

proc sumMeta(data : var seq[int], offset: int): (int, int) =

  let num_kids = data[offset + 0]
  let num_meta = data[offset + 1]

  var o = offset + 2
  var v = 0

  for k in 0..<num_kids:
    let r = sumMeta(data, o)
    o = r[0]
    v += r[1]
      
  for j in 0..<num_meta:
    v += data[o + j]

  return (o + num_meta, v)

proc indexMeta(data : var seq[int], offset: int): (int, int) =

  let num_kids = data[offset + 0]
  let num_meta = data[offset + 1]

  var o = offset + 2
  var v = 0

  var csum = newSeq[int]()

  for k in 0..<num_kids:
    let r = indexMeta(data, o)
    o = r[0]
    csum.add(r[1])
    v += r[1]

  if num_kids == 0:
    for j in 0..<num_meta:
      v += data[o + j]
  else:
    # meta is indexes into csum?
    var iv = 0
    for j in 0..<num_meta:
      let cidx = data[o + j]
      if cidx <= csum.len:
        iv += csum[cidx-1]
    v = iv

  return (o + num_meta, v)

var data = readFile("input").split(" ").mapIt(parseInt(it))

echo sumMeta(data, 0)[1]
echo indexMeta(data, 0)[1]


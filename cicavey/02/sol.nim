import parseutils
import strutils
import sets
import tables

# Load all freq changes into a seq
var codes = newSeq[string](0)
for line in "input".lines:
    codes.add(line)


var twoCnt: int = 0
var thrCnt: int = 0

for code in codes:
    var hist = newTable[char, int]()
    for c in code:    
        hist.mgetOrPut(c, 0) += 1

    for k, v in hist:
        if v == 2:
            twoCnt += 1
            break
    for k, v in hist:        
        if v == 3:
            thrCnt += 1
            break

echo twoCnt * thrCnt

for i in 0..codes.len-1:
    for j in i+1..codes.len-1:
        let codeA = codes[i]
        let codeB = codes[j]

        if editDistance(codeA, codeB) == 1:
            # print only the same
            for k in 0..codeA.len-1:
                if codeA[k] == codeB[k]:
                    stdout.write codeA[k]
            stdout.flushFile()
            echo ""
            break
import parseutils
import sets

# Load all freq changes into a seq
var changes = newSeq[int](0)
for line in "input".lines:
    var value = 0
    discard parseInt(line, value)
    changes.add(value)


var freq = 0
for v in changes:
    freq += v

echo freq

var knownFreq = initSet[int]()

freq = 0
knownFreq.incl(freq)

block outer:
    while true:
        for v in changes:
            freq += v
            if knownFreq.containsOrIncl(freq):
                echo freq
                break outer
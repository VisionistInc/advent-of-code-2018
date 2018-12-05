function solve(inputString) {
  const boxIds = inputString.split('\n')

  // count when letter appears twice
  let twiceCounter = 0
  // count when letter appears thrice
  let thriceCounter = 0

  const charCounts = boxIds.map(id => 
    id.split('').reduce((acc, char) => {
      if (acc[char] == null) {
        acc[char] = 0
      }
      
      acc[char]++

      return acc
    }, {})
  )

  charCounts.forEach(counts => {
    let twice = false, thrice = false

    Object.keys(counts).forEach(char => {
      if (counts[char] === 2) {
        twice = true
      } else if (counts[char] === 3) {
        thrice = true
      }
    })

    if (twice) twiceCounter++
    if (thrice) thriceCounter++
  })

  console.log(twiceCounter * thriceCounter)
}

const testInput = `abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab`

solve(testInput)

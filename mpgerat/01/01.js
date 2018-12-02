const input = `put
your
input
here`.split("\n").map(x => parseInt(x))

const partOne = input.reduce((current, next) => current + next, 0)
console.log(partOne)

const seenSet = new Set()

let iterations = 1
let index = 0
let frequency = 0
while(!seenSet.has(frequency)) {
  seenSet.add(frequency)
  
  if (index === input.length) {
    iterations++
    index = 0
  }

  frequency = frequency + input[index++]
}

console.log(`
Part two:
\tRepeated frequency: ${frequency}
\t# iterations: ${iterations}
`)

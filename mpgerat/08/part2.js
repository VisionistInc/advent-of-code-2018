// this is ... not pretty
const input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

function processNode(arr, i) {
  const childCt = arr[i]
  const metaCt = arr[i+1]

  let childValues = []
  i = i + 2
  for (let ci = 0; ci < childCt; ci++) {
    const childResult = processNode(arr, i)

    i = childResult.i
    childValues.push(childResult.value)
  }

  let value = 0
  for (let mi = 0; mi < metaCt; mi++) {
    const meta = arr[i++]

    if (childCt === 0) {
      value += meta
    } else if (meta !== 0) {
      if (meta <= childValues.length) {
        value += childValues[meta-1]
      }
    }
  }

  console.log(i, value)

  return { i, value }
}

function solve(stringInput) {
  const arrayInput = stringInput.split(' ').map(x => parseInt(x))

  const result = processNode(arrayInput, 0)

  console.log(result.value)
}

solve(input)

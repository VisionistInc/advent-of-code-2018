const input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

function processNode(arr, i) {
  const childCt = arr[i]
  const metaCt = arr[i+1]

  let metaSum = 0
  i = i + 2
  for (let ci = 0; ci < childCt; ci++) {
    const childResult = processNode(arr, i)

    i = childResult.i
    metaSum += childResult.metaSum
  }

  for (let mi = 0; mi < metaCt; mi++) {
    metaSum += arr[i++]
  }

  return { i, metaSum }
}

function solve(stringInput) {
  const arrayInput = stringInput.split(' ').map(x => parseInt(x))

  const result = processNode(arrayInput, 0)

  console.log(result.metaSum)
}

solve(input)

const testInput = `dabAcCaCBAcCcaDA`

function solve(inputString) {
  let index = 0;

  while(index < inputString.length-1) {
    const a = inputString.charCodeAt(index)
    const b = inputString.charCodeAt(index+1)

    if (Math.abs(a-b) === 32) {
      inputString = inputString.substring(0, index) + inputString.substring(index + 2, inputString.length)

      index = 0
    } else {
      index++
    }
  }

  console.log(inputString.length)
}

solve(testInput)

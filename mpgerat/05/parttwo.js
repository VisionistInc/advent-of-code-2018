const testInput = `dabAcCaCBAcCcaDA`

function solve(ogStringDontTouch) {
  let shortest = Number.MAX_SAFE_INTEGER

  for(let i = 0; i < 25; i++) {
    const removeChar = String.fromCharCode(65+i)

    let inputString = ogStringDontTouch.replace(new RegExp(removeChar, 'ig'), '')

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

    shortest = Math.min(shortest, inputString.length)
  }
  
  console.log(shortest)
}

solve(testInput)

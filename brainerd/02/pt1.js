// count number that have an ID containing exactly two of any letter
// count number that have three of any letter
// multiply counts for answer

const input = require('./input');

let i = 0;
let results = []
do {
  let count = {};
  for (let j = 0; j < input[i].length; j++) {
    console.log(count[input[i][j]])
    count[input[i][j]] = count[input[i][j]] !== undefined ? ++count[input[i][j]] : 1;
  }
  results.push(count);
  ++i;
} while (i < input.length)

let twosCount = 0;
let threesCount = 0;

results.forEach(result => {
  if (Object.values(result).find(a => a === 2)) twosCount++;
  if (Object.values(result).find(a => a === 3)) threesCount++;
})

console.error(`result is ${twosCount * threesCount}`);
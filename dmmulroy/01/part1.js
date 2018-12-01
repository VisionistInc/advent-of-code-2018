const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt'), 'utf8');

const output = input
  .split('\n')
  .map(Number)
  .reduce((prev, curr) => prev + curr, 0);

console.log(`output: ${output}`);

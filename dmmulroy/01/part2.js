const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt'), 'utf8');

const sanitizedInput = input.split('\n').map(Number);

const frequencies = new Set([0]);
let repeatedFrequency;
let sum = 0;
let iter = 0;

while (!repeatedFrequency) {
  sum += sanitizedInput[iter++ % sanitizedInput.length];

  if (frequencies.has(sum)) {
    repeatedFrequency = sum;
  }

  frequencies.add(sum);
}

console.log(`output: ${repeatedFrequency}`);

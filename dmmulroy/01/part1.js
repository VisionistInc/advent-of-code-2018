const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.join(__dirname, 'input.txt'), 'utf8');

const output = input.split('\n').reduce((prev, curr) => prev + Number(curr), 0);

console.log(`output: ${output}`);

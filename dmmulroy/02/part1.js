const fs = require('fs');
const path = require('path');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .split('\n');

const output = input.reduce(
  (prev, curr, idx, arr) => {
    const { two, three } = countTwosAndThrees(countLetters(curr));

    if (two > 0) prev.two++;

    if (three > 0) prev.three++;

    if (idx === arr.length - 1) return prev.two * prev.three;

    return prev;
  },
  { two: 0, three: 0 }
);

console.log(`output: ${output}`);

function countLetters(str) {
  return [...str].reduce((lookup, letter) => {
    if (lookup[letter]) {
      lookup[letter]++;
    } else {
      lookup[letter] = 1;
    }

    return lookup;
  }, {});
}

function countTwosAndThrees(letterLookup) {
  return Object.values(letterLookup).reduce(
    (prev, curr) => {
      if (curr === 2) {
        prev.two++;
      } else if (curr === 3) {
        prev.three++;
      }

      return prev;
    },
    { two: 0, three: 0 }
  );
}

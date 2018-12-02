const fs = require('fs');
const path = require('path');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .split('\n');

let output = '';

for (let id of input) {
  let match = null;
  let deltaIdx = null;

  for (let comparedId of input) {
    let delta = 0;

    for (let idx = 0; idx < id.length; idx++) {
      if (id[idx] !== comparedId[idx]) {
        delta++;
        deltaIdx = idx;
      }

      if (delta > 1) break;
    }

    if (delta > 1) continue;

    if (delta === 1) {
      match = comparedId;
      break;
    }
  }

  if (match) {
    output = [
      ...id.slice(0, deltaIdx),
      ...id.slice(deltaIdx + 1, id.length)
    ].join('');
    break;
  }
}

console.log(`output: ${output}`);

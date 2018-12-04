const fs = require('fs');
const path = require('path');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .split('\n');

const extractDimensions = claim => {
  const [, , leftTop, widthHeight] = claim.replace(':', '').split(' ');

  let [left, top] = leftTop.split(',');
  let [width, height] = widthHeight.split('x');

  [left, top, width, height] = [left, top, width, height].map(Number);

  return { left, top, width, height };
};

const createCoordinatesFromDimensions = ({ left, top, width, height }) => {
  const coordinates = [];

  for (let row = 0; row < height; row++) {
    for (let column = 0; column < width; column++) {
      coordinates.push(`${top + row},${left + column}`);
    }
  }

  return coordinates;
};

const output = input.reduce(
  (acc, claim, idx, arr) => {
    const claimCoordinates = createCoordinatesFromDimensions(
      extractDimensions(claim)
    );

    claimCoordinates.forEach(coordinates => {
      if (acc.seenCoordinates.has(coordinates)) {
        acc.seenOverlaps.add(coordinates);
      } else {
        acc.seenCoordinates.add(coordinates);
      }
    });

    if (idx === arr.length - 1) return acc.seenOverlaps.size;

    return acc;
  },
  { seenCoordinates: new Set(), seenOverlaps: new Set() }
);

console.log(`output: ${output}`);

const fs = require('fs');
const path = require('path');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .split('\n');

const extractIdAndDimensions = claim => {
  const [id, , leftTop, widthHeight] = claim.replace(/(#|:)/gm, '').split(' ');

  let [left, top] = leftTop.split(',');
  let [width, height] = widthHeight.split('x');

  [left, top, width, height] = [left, top, width, height].map(Number);

  return { id, left, top, width, height };
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
    const { id, ...dimensions } = extractIdAndDimensions(claim);
    const claimCoordinates = createCoordinatesFromDimensions(dimensions);

    acc.ids.add(id);

    claimCoordinates.forEach(coordinates => {
      if (acc.seenCoordinates.has(coordinates)) {
        acc.seenOverlaps.add(coordinates);

        const overlappedIds = acc.coordinatesToIds[coordinates] || [];

        [id, ...overlappedIds].map(id => acc.overlappedIds.add(id));
      } else {
        acc.seenCoordinates.add(coordinates);
      }

      if (acc.coordinatesToIds[coordinates]) {
        acc.coordinatesToIds[coordinates].push(id);
      } else {
        acc.coordinatesToIds[coordinates] = [id];
      }
    });

    if (idx === arr.length - 1)
      return [...acc.ids].filter(id => !acc.overlappedIds.has(id))[0];

    return acc;
  },
  {
    seenCoordinates: new Set(),
    seenOverlaps: new Set(),
    ids: new Set(),
    overlappedIds: new Set(),
    coordinatesToIds: {}
  }
);

console.log(`output: ${output}`);

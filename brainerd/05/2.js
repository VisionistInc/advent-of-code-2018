let input = require('./input');
const gimmetheanswer = require('./1');

const alphabet = 'abcdefghijklmnopqrstuvwxzy';

let hits = {}

alphabet.split('').forEach(letter => {
  console.log('starting letter', letter);
  let regex1 = new RegExp('(' + letter + letter.toUpperCase() +  "|" + letter.toUpperCase() + letter + ")", "g");
  console.log(regex1);
  const newInput = input.replace(regex1, '');
  console.log(`length after initial trimming for letter ${letter}: newInput.length`);
  try {
    gimmetheanswer(newInput);
  } catch(e) {
    hits[letter] = {
      count: newInput.length,
      answer: e.message
    }
    console.log('done with letter', letter);
  }
});
console.log("|||hits", hits);
// var maxHits = Math.min(...Object.values(hits));
// var maxHitsIdx = Object.values(hits).indexOf(maxHits);
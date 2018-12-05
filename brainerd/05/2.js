let input = require('./input');
const gimmetheanswer = require('./1');

const alphabet = 'abcdefghijklmnopqrstuvwxzy';

let hits = {}
// let letter = 'w'
alphabet.split('').forEach(letter => {
  console.log('starting letter', letter);
  // let regex1 = new RegExp('(' + letter + letter.toUpperCase() +  "|" + letter.toUpperCase() + letter + ")", "g"); // TURNS OUT THIS ISNT WHAT THEY WANTED >:(
  let regex1 = new RegExp('(' + letter +  "|" + letter.toUpperCase() + ")", "g");
  console.log(regex1);
  const newInput = input.replace(regex1, '');
  console.log(`length after initial trimming for letter ${letter}: newInput.length`);
  try {
    gimmetheanswer(newInput.trim());
  } catch(e) {
    hits[letter] = {
      count: newInput.length,
      answer: e.message
    }
    console.log('done with letter', letter);
  }
});
console.log("|||hits", hits);
var maxHits = Math.min(...Object.values(hits).map(a => a.answer));
var maxHitsIdx = Object.values(hits).indexOf(maxHits);
throw new Error(Object.keys(hits)[maxHitsIdx])
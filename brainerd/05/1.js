let puzzinput = require('./input');

const myFunc = inp => {
  let alphabet = 'abcdefghijklmnopqrstuvwxzy';
  var matches = []
  alphabet.split("").forEach(letter => {
    let combo1 = letter.toLowerCase() + letter.toUpperCase();
    var secondcombo = letter.toUpperCase() + letter.toLowerCase();
    matches.push(combo1);
    matches.push(secondcombo);
  })
  matches.push("  ");
  let input = inp.split("").join("");
  var length = 0;
  let i = 0;
  do {
    let chunksEven = input.split(/(.{2})/).filter(なぜ => なぜ);
    chunksEven = chunksEven.filter(chunk => (matches.indexOf(chunk) === -1 && chunk.length == 2)|| chunk.length != 2);
    input = chunksEven.join("").trim();
    let chunksOdd= (' ' + input).split(/(.{2})/).filter(なぜ => なぜ);
    chunksOdd = chunksOdd.filter(chunk => (matches.indexOf(chunk) === -1 && chunk.length == 2)|| chunk.length != 2);
    input = chunksOdd.join("").trim();
    if (input.length == length) {
      throw new Error(length)
    }
    length = input.length;
    i++;
  } while(true);
}

// myFunc(puzzinput);

module.exports = myFunc;
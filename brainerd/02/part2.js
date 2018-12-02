const input = require('./input');

let foundResult = false;
let chrisisawesome = true;

try {
  do {
    const firstGuess = input[Math.floor(Math.random() * input.length)].split('');
    const firstGuess2 = input[Math.floor(Math.random() * input.length)].split('');
  
    let incommonletters = '';
    const incommon = firstGuess.reduce((acc, curr, i) => {
      if (curr === firstGuess2[i]) incommonletters += curr;
      return (curr === firstGuess2[i]) ?  ++acc : acc;
    }, 0);
    console.log(incommon);
    if (incommon === firstGuess.length - 1) {
      throw new Error(incommonletters);
    } 
  
  } while (chrisisawesome == true);
} catch (e) {
  console.log("Success!!!")
  console.log(e)
}

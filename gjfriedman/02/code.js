const fs = require("fs");

const inputs = fs.readFileSync("input.txt", 'utf8').split("\n");

// Part A
let hasTwo = new Set();
let hasThree = new Set();

for (input of inputs) {
    const letters = {};
    for (letter of input) {
        if (!letters[letter]) {
            letters[letter] = 1;
        } else {
            letters[letter]++;
        }
    }

    for (letter in letters) {
        if (letters[letter] === 2) {
            hasTwo.add(input);
        } else if (letters[letter] === 3) {
            hasThree.add(input);
        }
    }
}

console.log(hasTwo.size * hasThree.size);

// Part B
for (let i = 0; i < inputs.length; i++) {
    for (let j = i; j < inputs.length; j++) {
        const x = inputs[i];
        const y = inputs[j];
        let same = "";
        let diff = 0;
        
        for (let k = 0; k < x.length; k++) {
            if (x[k] === y[k]) {
                same += x[k];
            } else {
                if (diff > 1) {
                    break;
                }
                diff++;
            }
        }
        if (diff === 1) {
            console.log(same);
        }
    }
}

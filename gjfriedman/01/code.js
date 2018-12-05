const fs = require("fs");

const frequencies = fs.readFileSync("input.txt", 'utf8').split("\n");
const frequencySums = {};
let frequencyStart = 0;
while(true) {
    frequencyStart = frequencies.reduce((sum, frequency) => {
        sum += parseInt(frequency);
        if (frequencySums[sum]) {
            throw `Frequency Found: ${sum}`;
        }
        frequencySums[sum] = true;
        return sum;
    }, frequencyStart);
}

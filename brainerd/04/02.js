const allTheMinutes = require('./input.js');
  // const guards = Array.from(new Set(allTheMinutes.map(minute => minute.guard_status.id)));
// let secretAnswerFromPartOne = 29;

// const asleepMinutes = allTheMinutes.filter(min => min.guard_status.awake == false);
// const allThe29s = asleepMinutes.filter(min => +min.date.toString().substr(19,2) == secretAnswerFromPartOne);
// let guardMap = {}
// guards.forEach(guard => {guardMap[guard] = 0})
// allThe29s.forEach(fiftynine => {
//   guardMap[fiftynine.guard_status.id]++;
// });

// const findThe29est29 = function(guardMap) {
//   let max29idx = Object.values(guardMap).indexOf(Math.max(...Object.values(guardMap)));
//   let guardDude = Object.keys(guardMap)[max29idx];
//   throw new Error(+guardDude * secretAnswerFromPartOne);
// }
// findThe29est29(guardMap);
// lolololol that's not the question


let mapThing = {}
let sleepMinutes = allTheMinutes.filter(min => min.guard_status.awake == false);
sleepMinutes.forEach(min => {
  let minuteStr = '' + +min.date.toString().substr(19,2);
  let weirdStr = '' + min.guard_status.id + "|" + minuteStr;
  if (Object.keys(mapThing).indexOf(weirdStr) == -1) mapThing[weirdStr] = 0;
  mapThing[weirdStr] = ++mapThing[weirdStr];
})

let max = Object.keys(mapThing).reduce((acc, curr) => {
  let count = mapThing[curr];
  if (count > acc.count) {
    return {
      thing: curr,
      count: count
    }
  }
  return acc;
}, {thing: '', count: 0});
let result = max.thing.split("|")[0] * max.thing.split("|")[1]
throw new Error(result);
const allTheMinutes = require('./input.js');

const guards = Array.from(new Set(allTheMinutes.map(minute => minute.guard_status.id)));
let guardMap = {};
guards.forEach(guard => {
  asleepMinutes = allTheMinutes.filter(a => a.guard_status.awake == false && a.guard_status.id == guard).length;
  guardMap[guard] = asleepMinutes;
})
try {
  let maxSleep = Math.max(...Object.values(guardMap));
  for (i=0;i<Object.keys(guardMap).length;i++) {
    if (guardMap[Object.keys(guardMap)[i]] == maxSleep) {
      throw new Error(Object.keys(guardMap)[i]);
    }
  }
} catch(e) {
  let guardWhoShouldBeFiredsId = +e.message;
  let guardmins = allTheMinutes.filter(min => min.guard_status.id == guardWhoShouldBeFiredsId && min.guard_status.awake == false)
  let minMap = {}
  for (i=0;i<60;i++){
    minMap[i] = 0;
  }
  for (min of guardmins) {
    minMap['' + +min.date.toString().substr(19,2)]++
  }
  let maxMinIdx = Object.values(minMap).indexOf(Math.max(...Object.values(minMap).map(i => +i)));
  let maxMin = Object.keys(minMap)[maxMinIdx]
  throw new Error(maxMin * guardWhoShouldBeFiredsId)
}
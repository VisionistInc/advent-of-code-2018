import java.io.File;

var execOrder = String()
var timeMap = mutableMapOf<String, Int>()
var clock = 0
var inProgress = mutableMapOf<String, Int>()

fun main(args: Array<String>) {
  var steps = File(args.first()).readLines()
  var stepsToDependencies = parseSteps(steps)

  // Answer to part 1
  // var executableMap = recurse(stepsToDependencies)
  // while (executableMap.isNotEmpty()) {
  //  executableMap = recurse(executableMap)
  // }
  // println(execOrder)

  // Answer to part 2
  var executableMap = timedRecurse(stepsToDependencies)
  while (inProgress.size != 0) {
    executableMap = tick(executableMap)
    executableMap = timedRecurse(executableMap)
  }

  println(clock)
  return
}

private fun timedRecurse(stepsToDependencies: MutableMap<String, MutableList<String>>):  MutableMap<String, MutableList<String>> {
	var depsLength = stepsToDependencies.values.minBy {it.size}?.size
  var candidates = stepsToDependencies.filter {it.value.size == depsLength} as MutableMap<String, MutableList<String>>

  while (inProgress.size < 6 && candidates.isNotEmpty()) {
  	var c = candidates.keys.minBy {it}
    if (!inProgress.contains(c.toString())) {
      inProgress.put(c.toString(), clock)
    }
    candidates.remove(c)
  }

  return stepsToDependencies
}

private fun tick(stepsToDependencies: MutableMap<String, MutableList<String>>): MutableMap<String, MutableList<String>> {
  var toBeRemoved = mutableListOf<String>()
  for ((step, startTime) in inProgress) {
    if ((clock - startTime) == timeMap.get(step)!!.toInt() - 1) {
      toBeRemoved.add(step)
    }
  }

  toBeRemoved.forEach {
    inProgress.remove(it)
    execOrder += it
    stepsToDependencies.remove(it)
    for ((_, v) in stepsToDependencies) {
      if (v.contains(it)) {
        v.remove(it)
      }
    }
  }

  clock++
  return stepsToDependencies
}

private fun recurse(stepsToDependencies: MutableMap<String, MutableList<String>>):  MutableMap<String, MutableList<String>> {
  var depsLength = stepsToDependencies.values.minBy {it.size}?.size
  var candidates = stepsToDependencies.filter {it.value.size == depsLength}
  var c = candidates.keys.minBy {it}
  var execStep = String()
  var cDeps = stepsToDependencies.get(c) as MutableList<String>

  if (cDeps.isEmpty()) {
    execStep = c.toString()
  }

  if (execStep != "") {
    stepsToDependencies.remove(execStep)
    for ((_, v) in stepsToDependencies) {
      if (v.contains(execStep)) {
          v.remove(execStep)
      }
    }

    execOrder += execStep
  }
  return stepsToDependencies
}

private fun parseSteps(steps: List<String>): MutableMap<String, MutableList<String>> {
  var stepsToDependencies = mutableMapOf<String, MutableList<String>>()
  steps.forEach {
    var step = it.substringAfter("e step ").substringBefore(" c")
    var depeendency = it.substringAfter("Step ").substringBefore(" m")
    if (stepsToDependencies.contains(step)) {
      var dependsList = stepsToDependencies.get(step) as MutableList<String>
      dependsList.add(depeendency)
    } else {
      stepsToDependencies.put(step, mutableListOf(depeendency))
    }
  }

  // insert steps that don't have any dependencies as just step=[]
  var c = 'A'
  var time = 61
  while (c <= 'Z') {
    if (!stepsToDependencies.contains(c.toString())) {
      stepsToDependencies.put(c.toString(), mutableListOf<String>())
    }
    timeMap.put(c.toString(), time)
    time++
    c++
  }

  return stepsToDependencies
}

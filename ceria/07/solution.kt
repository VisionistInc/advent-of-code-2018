import java.io.File;

var execOrder = String()

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
  while (c <= 'Z') {
    if (!stepsToDependencies.contains(c.toString())) {
      stepsToDependencies.put(c.toString(), mutableListOf<String>())
    }
    c++
  }

  // sort the lists of depdencies for ease later
  //for ((_, v) in stepsToDependencies) { v.sortBy{ it } }

  return stepsToDependencies
}

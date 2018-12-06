import java.io.File;

var keepGoing = true

fun main(args : Array<String>) {

  var origPolymer = File(args.first()).readLines().first().toCharArray()

  // Answer to part 1 -- tried to use true recursion, but kept getting stackoverflow...
  // var newPolymer = reactPolymer(origPolymer)
  // while (keepGoing) {
  //   newPolymer = reactPolymer(newPolymer)
  // }
  // println(newPolymer.size)

  var c = 'a'
  var shortestPolymerLength = origPolymer.size
  while (c <= 'z') {
      var candidate = origPolymer.filter { !it.equals(c, ignoreCase = true) }.toCharArray()
      while (keepGoing) {
         candidate = reactPolymer(candidate)
       }
       keepGoing = true

      if (candidate.size < shortestPolymerLength) {
         shortestPolymerLength = candidate.size
      }
      ++c
  }

  println(shortestPolymerLength)
  return
}

private fun reactPolymer(polymer: CharArray) :CharArray {
     var newPolymer = CharArray(polymer.size)
     var index = 0

     while (keepGoing) {
       if (index+1 < polymer.size) {
          if (polymer.get(index).equals(polymer.get(index+1), ignoreCase = true)) {
            if ((polymer.get(index).isUpperCase() && polymer.get(index+1).isLowerCase()) || (polymer.get(index).isLowerCase() && polymer.get(index+1).isUpperCase())) {
                newPolymer = polymer.copyOfRange(0,index) + polymer.copyOfRange(index+2, polymer.size)
                break
            }
          }
          index++
      } else {
        keepGoing = false
      }
     }
     return newPolymer
}

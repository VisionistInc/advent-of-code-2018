import java.io.File;

fun main(args : Array<String>) {

  var polymer = File(args.first()).readLines()
 
  // Answer to part 1
  println(reactPolymer(polymer.first()))
}

private fun reactPolymer(polymer: String) :String {    
     var newPolymer = polymer 
     for ((index, candidate) in polymer.withIndex()) {
         if (index+1 < polymer.length) {
          if (candidate.equals(polymer[index+1], ignoreCase = true)) {
            if ((candidate.isUpperCase() && polymer[index+1].isLowerCase()) || (candidate.isLowerCase() && polymer[index+1].isUpperCase())) {
               //  return reactPolymer(polymer.removeRange(index, index+2))  <- stack overflows
                newPolymer = reactPolymer(polymer.removeRange(index, index+2))
                break
            }
          }
        }
     }

    if (newPolymer != polymer) {
        reactPolymer(newPolymer)
    }

     return newPolymer

//    var newPolymer = polymer.toMutableList()
//     //var polymerChars = polymer.toCharArray()
//      for ((index, candidate) in newPolymer.withIndex()) {
//          if (index+1 < newPolymer.size) {
//           if (candidate.equals(polymer[index+1], ignoreCase = true)) {
//             if ((candidate.isUpperCase() && polymer[index+1].isLowerCase()) || (candidate.isLowerCase() && polymer[index+1].isUpperCase())) {
//                 //return reactPolymer(polymer.removeRange(index, index+2))
//                 newPolymer.removeAt(index)
//                 newPolymer.removeAt(index+1)
//                 reactPolymer(newPolymer)
//             }
//           }
//         }
//      }

//    return String(newPolymer.toCharArray())

}

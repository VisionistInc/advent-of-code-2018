import java.io.File;

fun main(args : Array<String>) {
  // Answer to part 1
  // var twoSum = 0
  // var threeSum = 0
  // File(args.first()).forEachLine {
  //  val charsMap = mutableMapOf<Char, Int>()
  //  it.forEach {
  //    charsMap[it] = charsMap.getOrDefault(it, 0) + 1
  //  }
  //  if (!charsMap.filterValues { it == 2}.isEmpty()) {
  //    twoSum++
  //  }
  //  if (!charsMap.filterValues { it == 3}.isEmpty()) {
  //    threeSum++
  //  }
  // }
  // println(twoSum * threeSum)


  // Answer to part 2
  var boxIDs = File(args.first()).readLines()
  var boxIDsIterator = boxIDs.iterator()
  for ((index, candidate) in boxIDsIterator.withIndex()) {
    var remainingIDsIterator = boxIDs.listIterator(index + 1)
    remainingIDsIterator.forEach {
      if (candidate != it) {
        print(candidate)
        print(" -- ")
        println(it)
      }


    }
  }

  println(boxIDs)
}

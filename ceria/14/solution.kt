import java.io.File;

fun main(args: Array<String>) {
  var elf1Index = 0
  var elf2Index = 1

  var recipieScores = "37".chunked(1).toMutableList() // 37 is used as a seed for all input
  val startLength = File(args.first()).readLines().first()
  val endLength = startLength.toInt() + 10

  while (recipieScores.size < endLength) {
    var newScore = recipieScores[elf1Index].toInt() + recipieScores[elf2Index].toInt()
    recipieScores.addAll(newScore.toString().chunked(1))
    elf1Index = calculateElfIndexes(elf1Index, recipieScores)
    elf2Index = calculateElfIndexes(elf2Index, recipieScores)
  }

  // Answer to part 1
  println(recipieScores.takeLast(10).joinToString(""))

  // Answer to part 2
  while (recipieScores.joinToString("").indexOf(startLength) == -1) {
    var count = 0
    while (count != 100) {
      var newScore = recipieScores[elf1Index].toInt() + recipieScores[elf2Index].toInt()
      recipieScores.addAll(newScore.toString().chunked(1))
      elf1Index = calculateElfIndexes(elf1Index, recipieScores)
      elf2Index = calculateElfIndexes(elf2Index, recipieScores)
      count++
    }
  }
  println(recipieScores.joinToString("").indexOf(startLength))

}

private fun calculateElfIndexes(elfIndex: Int, recipieScores: List<String>) :Int {
  var newElfIndex = (recipieScores[elfIndex].toInt() + 1)  + elfIndex
  while (newElfIndex >= recipieScores.size) {
    newElfIndex = newElfIndex - recipieScores.size
  }

  return newElfIndex
}

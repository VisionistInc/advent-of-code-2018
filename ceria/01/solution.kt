import java.io.File;
import java.io.InputStream;

var frequency = 0
var seenFreqs = mutableSetOf(0)  // Seed the seen frequencies with the start frequency

fun main(args : Array<String>) {
  // Answer to part 1
  // File(args.first()).forEachLine { frequency += it.toInt() }
  // println(frequency)

  // Answer to part 2
  while (true) {
    val input: InputStream = File(args.first()).inputStream()
    input.bufferedReader().useLines {
      lines -> for (it in lines) {
        frequency += it.toInt()
        if (seenFreqs.contains(frequency)) {
          println(frequency) // this is our duplicate frequency
          return
        } else {
            seenFreqs.add(frequency)
        }
      }
    }
  }

}

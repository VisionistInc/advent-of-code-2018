import java.io.File;

fun main(args: Array<String>) {
  var input = File(args.first()).readLines().first()
  var players = input.substringBefore(" ").toInt()
  var marbles = input.substringAfter("worth ").substringBefore(" points").toInt()

  var marble = 2
  var player = 2
  var index = 1
  var circle = mutableListOf<Int>()
  circle.add(0)
  circle.add(1)
  var playerScores = mutableMapOf<Int, Int>()
  while (marble != marbles + 1) {
    if (marble % 23 == 0) {
      if (index > 6) {
        index -= 7
      } else {
        var diff = 7 - index
        index = circle.size - diff
      }

      var score = playerScores.getOrDefault(player, 0) + marble + circle.get(index)
      playerScores.put(player, score)

      var circleCopy = mutableListOf<Int>().apply { addAll(circle.subList(0, index)) }
      circleCopy.apply { addAll(circle.subList(index+1, circle.size)) }
      circle = circleCopy

      marble++
    } else {
      var m1 = index + 1
      if (m1 == circle.size) {
        m1 = 0
      }
      var m2 = m1 + 1
      if (m2 == circle.size) {
        m2 = 0
      }
      if (m2 < m1) {
        index = m1 + 1
      } else {
        index = m2
      }
      var circleCopy = mutableListOf<Int>().apply { addAll(circle.subList(0, index)) }
      circleCopy.add(marble++)
      circleCopy.apply { addAll(circle.subList(index, circle.size)) }
      circle = circleCopy
    }

    if (player == players) {
      player = 1
    } else {
      player++
    }
  }

  println(playerScores.maxBy{ it.value }!!.value)
}

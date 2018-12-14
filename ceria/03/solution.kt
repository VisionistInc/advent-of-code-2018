import java.io.File;

var maxXCoord = 0
var maxYCoord = 0

fun main(args : Array<String>) {
  var claims = File(args.first()).readLines()
  var claimsMap = parseClaims(claims)

  var fieldOfXCoords = (0..maxXCoord).toList()
  var fieldOfYCoords = (0..maxYCoord).toList()
  var seen = mutableListOf<Pair<Int, Int>>()
  var overlap = mutableMapOf<Int, Pair<Int, Int>>()

  // Answer to part 1
  // for (x in fieldOfXCoords) {
  //  for (y in fieldOfYCoords) {
  //    var fieldPoint = Pair(x,y)
  //    for ((key, value) in claimsMap) {
  //      if (value.contains(fieldPoint)) {
  //        if (seen.contains(fieldPoint)) {
  //          overlap.add(fieldPoint)
  //        } else {
  //          seen.add(fieldPoint)
  //        }
  //      }
  //    }
  //  }
  // }

  //  println(overlap.size)

  // Answer to part 2
  for ((claimID, coords) in claimsMap) {
    var foundInAnotherClaim = false
    for (p in coords) {
      for ((key, points) in claimsMap) {
        if (key != claimID) {
          if (p in points) {
            foundInAnotherClaim = true
            break
          }
        }
      }

      if (foundInAnotherClaim) {
        break
      }
    }

    if (!foundInAnotherClaim) {
      println(claimID)
      return
    }
  }

}

private fun parseClaims(claims: List<String>): MutableMap<Int, MutableList<Pair<Int, Int>>> {
  var claimMap = mutableMapOf<Int, MutableList<Pair<Int, Int>>>()
  claims.forEach {
    var pointsList = mutableListOf<Pair<Int, Int>>()
  	var claimID = it.substringAfter("#").substringBefore(" @").toInt()
    var initialPair = Pair(it.substringAfter("@ ").substringBefore(",").toInt(),  it.substringAfter(",").substringBefore(":").toInt())
    var mX = initialPair.first + (it.substringAfter(": ").substringBefore("x").toInt())
    var mY = initialPair.second + (it.substringAfter("x").toInt())
    var xList = (initialPair.first..mX -1).toList()
    var yList = (initialPair.second..mY -1).toList()

    for (x in xList) {
        for (y in yList) {
            pointsList.add(Pair(x,y))
        }
    }

    if (maxXCoord < mX) {
        maxXCoord = mX
    }
    if (maxYCoord < mY) {
        maxYCoord = mY
    }
    claimMap.put(claimID, pointsList)
  }

  return claimMap
}

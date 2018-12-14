import java.math.*;


var serialNum = 9424

fun main(args: Array<String>) {
    var xCoords = (1..300).toMutableList()
    var yCoords = (1..300).toMutableList()
    var coordPower = mutableMapOf<Pair<Int, Int>, Int>()
    for (x in xCoords) {
        for (y in yCoords) {
            coordPower[Pair(x, y)] = calculatePower(x, y)
        }
    }
   
    var totalPower = mutableMapOf<Pair<Int, Int>, Int>()
    
    // Answer to part 1
    // for ((cell, power) in coordPower) {
    //    var sum = power.toInt()
    //    if (cell.first + 2 <= 300 && cell.second + 2 <= 300) {
    //        var x = cell.first.toInt()
    //        var y = cell.second.toInt()
    //        // 2 to the right
    //        sum += coordPower[Pair(x+1, y)]!!.toInt() + coordPower[Pair(x+2, y)]!!.toInt()
    //        // 3 1 row below
    //        sum += coordPower[Pair(x, y+1)]!!.toInt() + coordPower[Pair(x+1, y+1)]!!.toInt() + coordPower[Pair(x+2, y+1)]!!.toInt()
    //        // 3 2 rows below 
    //        sum += coordPower[Pair(x, y+2)]!!.toInt() + coordPower[Pair(x+1, y+2)]!!.toInt() + coordPower[Pair(x+2, y+2)]!!.toInt()
        
    //        totalPower[cell] = sum
    //    }
    // }
    
   // println(totalPower.maxBy{ it.value })

 	 for ((cell, power) in coordPower) {
        var sum = power.toInt()
        var previousSum = -0
        var index = 1
        while (sum > previousSum) {
            previousSum = sum
            sum = 0
        	if (cell.first + index <= 300 && cell.second + index <= 300) {
           		var rowIndex = 0
                while (rowIndex != index) {
                    sum += sumRow(Pair(cell.first + rowIndex, cell.second), index)
                    rowIndex++
                }
        		
        	}
            index++
        }
     	totalPower[cell] = previousSum

    }
    println(totalPower.maxBy{ it.value })
     
}

private fun sumRow(start: Pair<Int, Int>, to: Int): Int {
    var x = start.first.toInt()
    var y = start.second.toInt()
    var index = 0
    var sum = 0
    while (index <= to) {
        sum += coordPower[Pair(x, y+index)]!!.toInt()
        index++
    }
    return sum
}

}

private fun calculatePower(x: Int, y: Int): Int {
    var rackID = x + 10
    var powerLevel = ((y * rackID) + serialNum) * rackID
 
    var powerLength = powerLevel.length()
    if (powerLength >= 3 ) {
        return powerLevel.toString().map { it.toString().toInt() }[powerLength - 3 ] -5
    }

    return -4
}

fun Int.length() = when(this) {
    0 -> 1
    else -> Math.log10(Math.abs(toDouble())).toInt() + 1
}

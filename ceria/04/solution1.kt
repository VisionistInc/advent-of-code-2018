import java.io.File;

import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun main(args: Array<String>) {
   val dateTimeStrToLocalDateTime: (String) -> LocalDateTime = {
     LocalDateTime.parse(it.substringAfter('[').substringBefore(']'), DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"))
   }
   var sortedGuardSchedule = File(args.first()).readLines().sortedBy(dateTimeStrToLocalDateTime)

   sortedGuardSchedule.forEach {
     println(it)
   }

   // Between one index val to the next index - 1 val is one guard's duty period.
   val guardDutyIndexes: List<Int> = sortedGuardSchedule.withIndex().filter { it.value.contains("Guard") }.map { it.index }

   val guardMap = mutableMapOf<Int, List<Int>>()
   var index = 0

   while (index < guardDutyIndexes.size) {
      //val nextGuardDutyIndex = sortedGuardSchedule.size
      var nextGuardDutyIndex = sortedGuardSchedule.size
      if (index+1 < guardDutyIndexes.size) {
        nextGuardDutyIndex = guardDutyIndexes[index+1]
       }
      val guardID = sortedGuardSchedule[guardDutyIndexes[index]].substringAfter('#').substringBefore(' ').toInt()
      val dutyPeriod = sortedGuardSchedule.subList(guardDutyIndexes[index] +1, nextGuardDutyIndex)

      var sleepMinutes = mutableListOf<Int>()
      dutyPeriod.forEach {
        sleepMinutes.add(it.substringAfter(':').substringBefore(']').toInt() )
      }

      var guardDutyMinutesList = guardMap.get(guardID)
      if (guardDutyMinutesList == null) {
        guardDutyMinutesList = mutableListOf<Int>()
      }
      guardDutyMinutesList.forEach {
        sleepMinutes.add(it)
      }
      var t = sleepMinutes.size
      println("$guardID to $t")
      guardMap.put(guardID, sleepMinutes)
      index++
   }
   println("guardMap size is $guardMap")

   var totalTimeSleeping = 0
   var sleepiestGuardID = 0
   for ((guard, sleepTimeList) in guardMap) {
     var time = 0
     var idx = 0
     while (idx < sleepTimeList.size) {
         time = time + ((sleepTimeList[idx + 1] - sleepTimeList[idx]))
         idx += 2
     }

     if (time > totalTimeSleeping) {
       totalTimeSleeping = time
       sleepiestGuardID = guard
     }
   }

   println("guard id $sleepiestGuardID")
   println("totalTimeSleeping $totalTimeSleeping")
    val minutesCountMap = mutableMapOf<Int, Int>()

var i = 0
    guardMap[sleepiestGuardID]?.forEach {
      if (i % 2 == 0) {
        minutesCountMap[it] = minutesCountMap.getOrDefault(it, 0) + 1
      }
      i++
    }

    println(minutesCountMap)

    var highestCount = 0
    var sleepiestMinute = 0
    var sleepMinute = 0
    while (sleepMinute < minutesCountMap.size) {
      var minute = guardMap.get(sleepiestGuardID)?.get(sleepMinute)
      var count = minutesCountMap.get(minute)
      sleepMinute++
      if (count != null && count > highestCount) {
       highestCount = count
       sleepiestMinute = minute!!
      }
      //println(minute)
      //println(count)
    }

    println("highestCount was $highestCount")
    println("sleepiestMinute was $sleepiestMinute")
    println(sleepiestGuardID * sleepiestMinute)
}

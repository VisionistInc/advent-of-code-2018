import java.io.File;

import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun main(args: Array<String>) {
   val dateTimeStrToLocalDateTime: (String) -> LocalDateTime = {
     LocalDateTime.parse(it.substringAfter('[').substringBefore(']'), DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"))
   }
   var sortedGuardSchedule = File(args.first()).readLines().sortedBy(dateTimeStrToLocalDateTime)

   // Between one index val to the next index - 1 val is one guard's duty period.
   val guardDutyIndexes: List<Int> = sortedGuardSchedule.withIndex().filter { it.value.contains("Guard") }.map { it.index }

   val guardMap = mutableMapOf<Int, MutableList<MutableList<Int>>>()
   var index = 0

   while (index < guardDutyIndexes.size) {
      var nextGuardDutyIndex = sortedGuardSchedule.size
      if (index+1 < guardDutyIndexes.size) {
        nextGuardDutyIndex = guardDutyIndexes[index+1]
       }

      val guardID = sortedGuardSchedule[guardDutyIndexes[index]].substringAfter('#').substringBefore(' ').toInt()
      val dutyPeriod = sortedGuardSchedule.subList(guardDutyIndexes[index] +1, nextGuardDutyIndex)
      var guardDutyMinutesList = guardMap.get(guardID)
      if (guardDutyMinutesList == null) {
        guardDutyMinutesList = mutableListOf<MutableList<Int>>()
      }

      var sleepIndex = 0
      var wakeIndex = 1
      while (sleepIndex != dutyPeriod.size) {
        var sleep = dutyPeriod.get(sleepIndex).substringAfter(':').substringBefore(']').toInt()
        var wake = dutyPeriod.get(wakeIndex).substringAfter(':').substringBefore(']').toInt() - 1

        guardDutyMinutesList.add((sleep..wake).toMutableList())
        sleepIndex += 2
        wakeIndex += 2
      }

      guardMap.put(guardID, guardDutyMinutesList)
      index++
   }

  // Answer to part 1
  // var totalTimeAsleep = 0
  // var sleepiestGuardID = 0
  // for ((guardID, sleepLists) in guardMap) {
  //  var totalSleepTime = 0
  //  for (sleepList in sleepLists) {
  //      totalSleepTime += sleepList.last() - sleepList.first()
  //  }

  //  if (totalSleepTime > totalTimeAsleep) {
  //    totalTimeAsleep = totalSleepTime
  //    sleepiestGuardID = guardID
  //  }
  //}

  // var minutesCountMap = mutableMapOf<Int, Int>()
  // var sleepListsOfSleepiestGuard = guardMap[sleepiestGuardID]
  // sleepListsOfSleepiestGuard?.let{
  //  for (sleepList in sleepListsOfSleepiestGuard) {
  //    sleepList.forEach {
  //      minutesCountMap[it] = minutesCountMap.getOrDefault(it, 0) + 1
  //    }
  //  }
  // }

  // var sleepiestMinute = minutesCountMap.maxBy{ it.value }!!.key
  // println(sleepiestGuardID * sleepiestMinute)

  // Answer to part 2
  var guardAsleepAtMinuteMap = mutableMapOf<Int, Map.Entry<Int, Int>?>()
  for ((guardID, sleepLists) in guardMap) {
    var minutesCountMap = mutableMapOf<Int, Int>()
    if (sleepLists.isNotEmpty()) {
      for (sleepList in sleepLists) {
        sleepList.forEach {
          minutesCountMap[it] = minutesCountMap.getOrDefault(it, 0) + 1
        }
      }
      guardAsleepAtMinuteMap.put(guardID, minutesCountMap.maxBy{ it.value })
    }
  }

  var mostAsleepMinuteFrequency = 0
  var mostAsleepMinute = 0
  var guardIDOfMostAsleepMinute = 0
  for ((guard, sleepFrequencyMapEntry) in guardAsleepAtMinuteMap) {
    if (sleepFrequencyMapEntry!!.value > mostAsleepMinuteFrequency) {
      mostAsleepMinuteFrequency = sleepFrequencyMapEntry.value
      mostAsleepMinute = sleepFrequencyMapEntry.key
      guardIDOfMostAsleepMinute = guard
    }
  }

  println(guardIDOfMostAsleepMinute * mostAsleepMinute)
}

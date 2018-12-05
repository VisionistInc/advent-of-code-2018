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

   var guardMap = mutableMapOf<Int, List<Int>>()
   var index = 0
   while (index < guardDutyIndexes.size) {
     val guardID = sortedGuardSchedule[guardDutyIndexes[index]].substringAfter('#').substringBefore(' ').toInt()
     val dutyPeriod = sortedGuardSchedule.subList(guardDutyIndexes[index] + 1, if (index+1 < guardDutyIndexes.size) guardDutyIndexes[index+1] else sortedGuardSchedule.size)

      var sleepMinutes = mutableListOf<Int>()
      dutyPeriod.forEach {
        sleepMinutes.add(it.substringAfter(':').substringBefore(']').toInt() )  
      }
      guardMap[guardID] = guardMap.getOrDefault(guardID, mutableListOf<Int>()).addAll(sleepMinutes)
      //guardMap.put(sortedGuardSchedule[c[index]].substringAfter('#').substringBefore(' ').toInt(), sleepMinutes)
      index++
      println(guardMap)
   }

}

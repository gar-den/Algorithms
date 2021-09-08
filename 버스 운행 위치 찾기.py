"""
버스 운행 위치 찾기
"""

from datetime import datetime

timetable = [  # using as global variable
  {
    "number": "1-1",
    "timetable": {
      "weekday": [
        { "name": "정류장 A", "arrive": "09:00" },
        { "name": "정류장 b", "arrive": "09:20" },
        { "name": "정류장 D", "arrive": "09:45" },
        { "name": "정류장 e", "arrive": "10:00" },
        { "name": "정류장 F", "arrive": "10:20" }
      ],
      "weekend": []
    }
  },
  {
    "number": "50",
    "timetable": {
      "weekday": [
        { "name": "정류장 a", "arrive": "09:10" },
        { "name": "정류장 B", "arrive": "09:35" },
        { "name": "정류장 E", "arrive": "09:50" },
        { "name": "정류장 f", "arrive": "10:20" },
        { "name": "정류장 G", "arrive": "10:30" },
        { "name": "정류장 H", "arrive": "15:30" },
        { "name": "정류장 I", "arrive": "18:30" },
        { "name": "정류장 J", "arrive": "19:30" }
      ],
      "weekend": []
    }
  }
]

def whereisbus(bus):
    busNum = 0
    while busNum < len(existBuses):
        if bus == existBuses[busNum]:
            busNum = busNum
            
            break

        busNum += 1

    if busNum == len(existBuses):
        return "존재하지 않습니다."

    busStops = len(timetable[busNum]["timetable"][isWeekend])
    if busStops == 0:
        return "운행하지 않습니다."

    busTable = timetable[busNum]["timetable"][isWeekend]
    for i in range(busStops - 1):
        if busTable[i]["arrive"] < now < busTable[i + 1]["arrive"]:
            return "'" + busTable[i + 1]["name"] +"'를 향해 운행하고 있습니다."

    return "운행이 종료되었습니다."


buses = input()
buses = buses.split()

now = datetime.now()
day = now.strftime("%A")
now = now.strftime("%H:%M")  # using as global variable
isWeekend = "weekday"  # using as global variable

existBuses = []
for i in range(len(timetable)):
    existBuses.append(timetable[i]["number"])

if day == "Saturday" or day == "Sunday":
    isWeekend == "weekend"

for i in range(len(buses)):
    print("'"+ str(buses[i]) + "'번 버스는 " + whereisbus(buses[i]))

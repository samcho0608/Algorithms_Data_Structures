# if no exit record => assume exited at 23:59
# calculate in total
# default is less than min time
# unit fee * unit time over min time + default fee
# round up if not divisible by unit time

# fee = [min time in min, default fee, unit time in min, unit fee]
# records = "HH:MM PLATE_NUM IN/OUT"
#   IN : 2
#   OUT : 3

from math import ceil


def calcFee(timeSpan, minTime, defaultFee, unitTime, unitFee) :
    if timeSpan <= minTime :
        return defaultFee

    extraFee = int(ceil((timeSpan - minTime) / unitTime )) * unitFee
    return extraFee + defaultFee

def calcTimeSpan(entry : str, exit : str) :
    ihr, imin = entry.split(":")
    thr, tmin = exit.split(":")
    return (int(thr) * 60 + int(tmin)) - (int(ihr) * 60 + int(imin))



def solution(fees : list, records : list) :
    minTime, defaultFee, unitTime, unitFee = fees
    carEntry = dict()
    carTime = dict()

    for r in records :
        ts, plate, t = r.split(" ")
        isIn = t == "IN"

        if isIn :
            carEntry[plate] = ts
        else :
            timeSpan = calcTimeSpan(carEntry[plate], ts)
            if plate not in carTime.keys() :
                carTime[plate] = timeSpan
            else :
                carTime[plate] += timeSpan
            carEntry.pop(plate)

    for plate, ts in carEntry.items():
        timeSpan = calcTimeSpan(carEntry[plate], "23:59")

        if plate not in carTime.keys() :
            carTime[plate] = timeSpan
        else :
            carTime[plate] += timeSpan

    carFee = dict()
    for plate, timeSpan in carTime.items():
        carFee[plate] = calcFee(timeSpan, minTime, defaultFee, unitTime, unitFee)


    answer = []
    plate = sorted([p for p in carFee.keys()])
    print(plate)

    for p in plate :
        answer.append(carFee[p])
    
    return answer

    
# actual = solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
# assert actual==[14600, 34400, 5000]
# assert solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])==[0, 591]
# assert solution([1, 461, 1, 10], ["00:00 1234 IN"])==[14841]
ans = solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:34 5961 OUT", "07:34 5961 IN", "08:34 5961 OUT", "09:34 5961 IN", "10:34 5961 OUT", "11:34 5961 IN", "12:34 5961 OUT"]
  )

print(ans)
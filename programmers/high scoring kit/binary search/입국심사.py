
# my original solution
# def solution(n, times):

#     totalTimes = [ 0 for i in range(len(times))]

#     for i in range(n) :
#         minTime = totalTimes[0] + times[0]
#         minIndex = 0

#         for j in range(1, len(totalTimes)) :
#             expectedFinTime = totalTimes[j] + times[j]

#             if minTime > expectedFinTime :
#                 minTime = expectedFinTime
#                 minIndex = j
#             elif minTime == expectedFinTime :
#                 if times[j] < times[minIndex] :
#                     minIndex = j
#                     minTime = expectedFinTime
        
#         totalTimes[minIndex] = minTime
    
#     return max(totalTimes)

def solution(n, times) :
    times.sort()
    answer = 0
    minT = times[0]
    maxT = times[0] * n # if everyone was dealt with by quickest staff

    while True :
        count = 0
        mid = (minT + maxT) // 2 # time spent dealing with half the people by quickest staff

        for t in times :         # count = total number of people each of other staff can deal with in the meantime
            count += (mid // t)
        
        if count >= n :     # overachieved
            maxT = mid
        elif count < n :    # underachieved
            minT = mid

        if minT == maxT - 1 :
            answer = maxT
            break
    
    return answer


        

assert solution(6, [7, 10])	== 28


# for each person
#   find a person who will finish the earliest
#       * earliest : start time + process time

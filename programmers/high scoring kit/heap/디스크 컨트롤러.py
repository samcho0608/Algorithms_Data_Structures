
# 전반적으로 짧으면 됨
# avg(fin - start)

# list[[requested, length]]
from heapq import heapify, heappop, heappush

def solution(jobs): # job = [requestTime, length]
    heapify(jobs)

    timeTook = []

    currTime = 0

    while jobs :
        options = []
        heapify(options)
        while jobs and jobs[0][0] <= currTime :
            job = heappop(jobs)
            heappush(options, [job[1], job[0]]) # option = [length, requestTime]
        
        if not options :
            currTime += 1
            continue
        
        currJob = heappop(options)
        
        while options :
            job = heappop(options)
            heappush(jobs, [job[1], job[0]])
        

        timeTook.append(currJob[0] + currTime - currJob[1])
        currTime += currJob[0]

    return sum(timeTook) // len(timeTook)
        
    
    
    

# solution([[0, 3], [1, 9], [2, 6]])
assert solution([[0, 3], [1, 9], [2, 6]]) == 9
assert solution([[0, 10], [4, 10], [15, 2], [5, 11]]) == 15
assert solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]) == 72
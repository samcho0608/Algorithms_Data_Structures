from math import ceil


def solution(progresses, speeds):
    deployments = []

    subDaysToFinish = 0
    subDeployment = 0

    for i in range(len(progresses)) :
        speed = speeds[i]
        progress = progresses[i]
        daysToFinish = ceil((100 - progress) / speed)

        if subDaysToFinish < daysToFinish :
            if subDeployment != 0 :
                deployments.append(subDeployment) 
            subDaysToFinish = daysToFinish
            subDeployment = 1
        else :
            subDeployment += 1

    deployments.append(subDeployment)
            
    return deployments

assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
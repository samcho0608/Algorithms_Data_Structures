
def solution(answers):
    tester1 = [1,2,3,4,5]
    tester2 = [2,1,2,3,2,4,2,5]
    tester3 = [3,3, 1,1, 2,2, 4,4, 5,5]

    score1, score2, score3 = 0, 0, 0

    for i, a in enumerate(answers):
        if a == tester1[i % len(tester1)] :
            score1 += 1
        if a == tester2[i % len(tester2)] :
            score2 += 1
        if a == tester3[i % len(tester3)] :
            score3 += 1

    scores = [score1, score2, score3]
    maxScore = max(scores)
    return [i+1 for i, score in enumerate(scores) if score == maxScore]

assert solution([1,2,3,4,5]) == [1]
assert solution([1,3,2,4,2]) == [1,2,3]
def solution(array, commands):
    answers = []

    for c in commands :
        i,j,k = c
        answers.append(sorted(array[i-1:j])[k - 1])
    return answers

assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]

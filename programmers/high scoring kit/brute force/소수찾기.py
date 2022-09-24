from itertools import permutations
from math import ceil, sqrt


def solution(numbers):
    count = 0
    checked = set()
    for i in range(1, len(numbers) + 1) :
        for j in permutations(list(numbers), i) :
            if j[0] == '0':
                continue

            comb = int(''.join(j))
            if comb == 1 or comb in checked:
                continue
            if isPrime(comb) :
                count += 1
                checked.add(comb)
    return count

def isPrime(number) :
    if number == 2 :
        return True

    for i in range(2, ceil(sqrt(number)) + 1) :
        if number % i == 0 :
            return False
    return True

assert solution("17") == 3
assert solution("011") == 2
assert solution("11") == 1
assert solution("1231") == 18
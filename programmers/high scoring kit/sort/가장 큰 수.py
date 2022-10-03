# len(numbers) in range(1,100001)
# n in numbers in range(0,1001)

def solution(numbers: list[int]) -> str :
    numbers.sort(key= lambda x : (str(x) * 4)[:4], reverse= True)
    if numbers[0] == 0 :
        return '0'
    return ''.join([str(n) for n in numbers])


assert solution([6,10,2]) == "6210"
assert solution([1000, 100]) == "1001000"
assert solution([0,1,2]) == "210"
assert solution([0, 0]) == "0"
# len(numbers) in range(1,100001)
# n in numbers in range(0,1001)

def solution(numbers: list[int]) -> str :
    numbers.sort(key= lambda x : (str(x) * 4)[:4], reverse= True)
    # 1000이 가장 큼으로 4자리 수로 만들어 비교하면 편함
    # 예 : 1, 10 중 1을 먼저 두는 것이 좋음. 이는 1 다음자리에 1과 같거나 큰 수가 올것이기 때문
    #   1111 > 1010으로 비교하여 비교 가능
    # 1000과 100에서는 100이 먼저와야함. 동일한 논리로 1001 > 1000이므로 edge case도 처리됨
    
    if numbers[0] == 0 : # 0으로만 채워졌을 경우를 대비
        return '0'
    return ''.join([str(n) for n in numbers])


assert solution([6,10,2]) == "6210"
assert solution([1000, 100]) == "1001000"
assert solution([0,1,2]) == "210"
assert solution([0, 0]) == "0"
# 한 다리, 여러 트럭. 모든 트럭 건너는 min time
# bridge_length : 다리에 올라갈 수 있는 최대 트럭 수
# weight : 다리가 견딜 수 있는 최대 무게

# condition :
# * bridge_length in range(1, 10001)
# * weight in range(1, 10001)
# * len(truck_weights) in range(1, 10001)
# * weight of each truckt in range(1, weight)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    next_truck_index = 0 # 다리 위에 올라갈 다음 트럭의 index
    on_bridge = deque() # 현재 다리 위에 올라간 트럭 Queue
    current_weight_on_bridge = 0 # 현재 다리 위 무게

    time = 1 # 이해하기 쉽게 예제처럼 1초에 첫 트럭이 움직이게끔 함
    while next_truck_index < len(truck_weights) or len(on_bridge) > 0: # 남은 트럭이 있거나 다리 위에 아직 트럭이 있을때
        if len(on_bridge) > 0 :
            first_t, first_w = on_bridge.popleft()          # 맨 앞 트럭
            if time - first_t < bridge_length :             # 다리를 다 지나지 않았다면
                on_bridge.appendleft((first_t, first_w))
            else :                                          # 다 지났다면
                current_weight_on_bridge -= first_w
        
        if next_truck_index < len(truck_weights) :          # 올라갈 트럭이 있다면
            curr = truck_weights[next_truck_index]
            
            if len(on_bridge) + 1 <= bridge_length and current_weight_on_bridge + curr <= weight:   # 다리 길이나 무게가 여유가 있다면
                on_bridge.append((time, curr))
                current_weight_on_bridge += curr
                next_truck_index += 1
            
        time += 1
    return time - 1
    

assert solution(2, 10, [7,4,5,6]) == 8
assert solution(100,100,[10]) == 101
assert solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110
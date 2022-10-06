# rotate a list by k elements

# k elements to the right

# test cases : 
#   k < 0
#   k > len(input_list)

# # technically this is copying the list?
# def solution(input_list: list[int], k : int) -> list[int] :
#     cursor = calculate_initial_index(k, len(input_list))
#     answer = []

#     while len(answer) != len(input_list) :
#         answer.append(input_list[cursor])
#         cursor += 1
#         if cursor >= len(input_list) :
#             cursor = 0
    
#     return answer

# def calculate_initial_index(k, length) :
#     initial_index = abs(k) % length
#     if k < 0 :
#         initial_index = length - initial_index
#     return initial_index

# example_input = [1,2,3,4,5,6]
# assert solution(example_input, 2) == [3,4,5,6,1,2]
# assert solution(example_input, -1) == [6,1,2,3,4,5]

def solution(input_list: list[int], k : int) -> int :
    to_move_elements_count = count_elements_to_move(k, len(input_list))

    count = 0
    if to_move_elements_count > len(input_list) // 2 :
        count = _swap_elements_left_to_the_end(input_list, to_move_elements_count)
    else :
        count = _swap_elements_right_to_the_end(input_list, to_move_elements_count)

    return count

def count_elements_to_move(k, length) :
    to_move_elements_count = abs(k) % length
    if k < 0 :
        to_move_elements_count = length - to_move_elements_count
    return to_move_elements_count

def _swap_elements_left_to_the_end(input_list : list[int], to_move_size : int) :
    start, end = (to_move_size, len(input_list))
    swap_count = 0
    while True :
        for i in range(start, end) :
            swapping_index = i - to_move_size
            input_list[i], input_list[swapping_index] = input_list[swapping_index], input_list[i]
            swap_count += 1
        start -= len(input_list) - to_move_size
        end -= len(input_list) - to_move_size
        if start == 0 :
            break

    return swap_count

def _swap_elements_right_to_the_end(input_list : list[int], to_move_size : int) :
    start, end = 0, to_move_size
    swap_count = 0
    while True :
        for i in range(start, end) :
            swapping_index = i + to_move_size
            input_list[i], input_list[swapping_index] = input_list[swapping_index], input_list[i]
            swap_count += 1
        start += to_move_size
        end += to_move_size
        if end == len(input_list) :
            break

    return swap_count
        



example_input = [1,2,3,4,5,6]
assert solution(example_input, 1) == 5
assert example_input == [2,3,4,5,6,1]

example_input = [1,2,3,4,5,6]
assert solution(example_input, 2) == 4
assert example_input == [3,4,5,6,1,2]

example_input = [1,2,3,4,5,6]
assert solution(example_input, 3) == 3
assert example_input == [4,5,6,1,2,3]

example_input = [1,2,3,4,5,6]
assert solution(example_input, -1) == 5
assert example_input == [6,1,2,3,4,5]

def rotate(lst, k):
    reverse(lst, 0, k - 1)
    reverse(lst, k, len(lst) - 1)
    reverse(lst, 0, len(lst) - 1)


def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

example_input = [1,2,3,4,5,6]
rotate(example_input, 1)
assert example_input == [2,3,4,5,6,1]

example_input = [1,2,3,4,5,6]
rotate(example_input, 2)
assert example_input == [3,4,5,6,1,2]

example_input = [1,2,3,4,5,6]
rotate(example_input, 3)
assert example_input == [4,5,6,1,2,3]

example_input = [1,2,3,4,5,6]
rotate(example_input, -1)
assert example_input == [6,1,2,3,4,5]
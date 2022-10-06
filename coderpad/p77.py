# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

# my answer
def solution(intervals) :
    sortedIntervals = sorted(intervals, key=lambda x : x[0])

    mergedIntervals = []

    for i, interval in enumerate(sortedIntervals) :
        if i == 0 :
            mergedIntervals.append(interval)
            continue

        s, e = interval
        ls, le = mergedIntervals.pop()

        if s <= le :
            mergedIntervals.append((ls, le if le > e else e))
        else :
            mergedIntervals.append((ls, le))
            mergedIntervals.append((s,e))

    return mergedIntervals

## solution
# def merge(intervals):
#     sorted_intervals = sorted(intervals, key=lambda i: i[0])
#     merged_intervals = []
#     for interval in sorted_intervals:
#         if merged_intervals and interval[0] <= merged_intervals[-1][1]:
#             merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
#         else:
#             merged_intervals.append(interval)

#     return 

    
assert solution([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]

def test_p77_solution():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert solution(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert solution(intervals) == [(1, 3), (4, 10), (20, 27)]

test_p77_solution()
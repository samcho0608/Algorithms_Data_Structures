def solution(sizes):
    sizesToCompare = [
        sorted(s)
        for s in sizes
    ]

    maxH, maxW = 0, 0
    for s in sizesToCompare :
        h,w = s
        if h > maxH :
            maxH = h
        if w > maxW :
            maxW = w
    return maxH * maxW

assert solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000
assert solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120
assert solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133
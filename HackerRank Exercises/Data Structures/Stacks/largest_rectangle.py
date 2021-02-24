def largestRectangle(h):
    stack = [] # indices where the height increases
    area = 0
    i = 0
    while i < len(h):
        height = h[i]
        if not stack or h[stack[-1]] < height:
            stack.append(i)
            i += 1
        elif h[stack[-1]] == height:
            i += 1
        elif h[stack[-1]] > height:
            begin = stack.pop()
            area = max(area, h[begin] * (i - begin))
    # there are consective heights in increasing order left
    while stack:
        begin = stack.pop()
        area = max(area, h[begin] * (len(h) - begin))
        
    
    return area

print(largestRectangle([11,11,10,10,10]))
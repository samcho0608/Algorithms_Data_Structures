def largestRectangle(h):
    # max_area = max_h = h.pop()
    # used = [max_h]
    # consec = 1
    # max_index = 0
    # checked = []
    # while h:
    #     new_h = h.pop()
    #     used.append(new_h)
        
    #     if new_h >= max_h and len(used) - 1 == max_index + 1:
    #         consec += 1
    #         max_area = consec * max_h
    #         max_index += 1
        
        
    #     count = 0
        
    #     while used:
    #         prev = used.pop()
    #         checked.append(prev)
            
    #         if prev < new_h:
    #             break
    #         count += 1

    #     while checked:
    #         used.append(checked.pop())
        
    #     if max_area < new_h * count:
    #         max_area = new_h * count
    #         max_h = new_h
    #         max_index = len(used) - 1
    #         consec = count
            
    # return max_area


    max_h = h.pop()
    used = [max_h]
    consec = 1
    inc = 1
    while h:
        new_h = h.pop()
        used.append(new_h)
        if new_h >= max_h:
            consec += inc
        else:
            inc = 0

        checked = []
        while used:
            prev = used.pop()
            if prev < new_h:
                break
            checked.append(prev)

        new_consec = len(checked)

        while checked:
            used.append(checked.pop())

        if new_consec * new_h > max_h * consec:
            max_h = new_h
            consec = new_consec
            inc = 1
    return max_h * consec

print(largestRectangle([11,11,10,10,10]))
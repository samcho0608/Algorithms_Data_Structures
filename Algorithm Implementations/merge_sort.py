# I think this is my own implementation so let's check the actual implementation just in case

def merge_sort(l):
    if len(l) == 1:
        return l

    first = merge_sort(l[:len(l)//2])
    second = merge_sort(l[len(l)//2:])
    to_return = []
    while first and second:
        if first[0] < second[0]:
            to_return.append(first[0])
            first = first[1:]
        else:
            to_return.append(second[0])
            second = second[1:]

    to_return.extend(first if first else second)
    return to_return
def romanToInt(s):
    translator = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }
    prev = s[0]
    partialTotal = translator[s[0]]
    total = 0
    for curr in s[1:]:
        if(prev != curr) :
            if((prev == 'I' or prev == 'X' or prev == 'C') and translator[prev] < translator[curr]) :
                total +=  translator[curr] - translator[prev]
                prev = curr
                partialTotal = 0
                continue
            total += partialTotal
            prev = curr
            partialTotal = translator[curr]
        else :
          partialTotal += translator[curr]
    total += partialTotal
    return total
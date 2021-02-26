s = input()

result = []
summ = -1
for i in range(len(s)):
    if s[i].isalpha():
        result.append(s[i])
    else:
        summ += int(s[i])
result = ''.join(sorted(result))
if summ > -1:
    result += str(summ + 1)
print(result)
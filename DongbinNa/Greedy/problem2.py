# string with only digits
# checking from left to right, one character at a time
# find the biggest number you can make with only + and x

s = input()
num = int(s[0])
for i in range(1,len(s)):
    operand = int(s[i])
    if num < 2 or operand < 2:
        num += operand
    else:
        num *= operand

print(num)
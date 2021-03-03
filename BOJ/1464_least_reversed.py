# Given a string, one iterates through it.
# For each character, one may decide to flip the string from beginnging till that number.
# Find the lexically least possible string one can find using this.
#
# e.g.
# Input:
# BCDAF
#
# Output:
# ABCDF
#
# Explanation:
# 1. BCDAF
# 2. BCDAF
# 3. DCBAF
# 4. ABCDF

s = input()

if len(s) == 1:
    print(s)
else:
    increasing = s[0] < s[1]
    for i in range(1,len(s)):
        if increasing and s[0] >= s[i] or not increasing and s[i-1] < s[i]:
            s = s[:i][::-1] + s[i:]
            increasing = not increasing

    if not increasing:
        s = s[::-1]

    print(s)


# Better way
# Make a new string with first character
#
# if next character is more, add it to the end
# if next character is equal or less, add it to the front
#
#
# This works bc we need to compare the least lexical value we have found so far


s = input()

p = s[0]
for i in range(1,len(s)):
    if s[i] > p:
        p += s[i]
    else:
        p = s[i] + p
print(p)


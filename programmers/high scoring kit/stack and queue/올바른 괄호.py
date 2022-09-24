def solution(s):
    if len(s) % 2 != 0 :
        return False

    paranStack = []

    for i in range(len(s)):
        if s[i] == "(" :
            paranStack.append("(")
        else :
            if not paranStack :
                return False
            paranStack.pop()


    return len(paranStack) == 0

assert solution("()()") == True
assert solution("(())()") == True
assert solution(")()(") == False
assert solution("(()(") == False
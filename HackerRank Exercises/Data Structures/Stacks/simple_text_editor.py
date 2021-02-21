# Enter your code here. Read input from STDIN. Print output to STDOUT
s = ''
stack = []
for i in range(int(input())):
    query = input()
    if len(query) != 1:
        operator, operand = tuple(query.split())
        if operator == '1':
            stack.append(s)
            s = s + operand
        elif operator == '2':
            operand = int(operand)
            stack.append(s)
            s = s[:-operand]
        else:
            print(s[int(operand) - 1])
    else:
        s = stack.pop()
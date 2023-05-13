# 모든 괄호들은 올바른 짝이 있다.

while True:
    sen = input()
    stack = []
    if sen == '.':
        break
    for s in sen:
        if s == '(' or s =='[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(': 
                stack.pop()
            else:
                stack.append(s)
                break
        
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
    


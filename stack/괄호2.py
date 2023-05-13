n = int(input())

lst = [list(input()) for _ in range(n)]

for i in range(n):
    stack = []
    for j in range(len(lst[i])):
        if lst[i][j] == '(':
            stack.append(lst[i][j])
        
        elif lst[i][j] == ')': 
            if stack: # stack이 비어있지 않은 상태에서 ')'가 들어올경우
                stack.pop()
            else: # stack이 비어있는 상태에서 ')'가 들어오면 정상적인 괄호가 아님
                stack.append(lst[i][j])
                break
    
    if stack: # stack이 비어있지 않으면 
        print("NO")
    else:
        print('YES')
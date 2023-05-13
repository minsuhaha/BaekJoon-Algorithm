import sys
input = sys.stdin.readline
n = int(input())
stack = []
lst = [list(input().split()) for _ in range(n)]
    
for i in range(n):
    if lst[i][0] == 'push':
        stack.append(lst[i][1])
    elif lst[i][0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif lst[i][0] == 'size':
        print(len(stack))
    elif lst[i][0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif lst[i][0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

next = 1 # stack에 들어 갈 다음 값
stack = [] 
answer = [] 

for s in seq:
    while s >= next:
        answer.append('+')
        stack.append(next)
        next += 1
    
    if s == stack[-1]:
        answer.append('-')
        stack.pop()
    elif s < stack[-1]:
        break
    
if stack:
    print('NO')
else:
    print(*answer)

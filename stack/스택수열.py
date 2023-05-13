# 1부터 n까지에 수에 대해 차례로 
# [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 
# 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

# pop 기준으로 수열 정렬된다고 생각하면 될듯.

# '+' -> push / '-' -> pop
import sys
input = sys.stdin.readline
n = int(input())
stack = [int(input()) for _ in range(n)]

prior = 1
result = []
answer = []

for i in range(n):
    while prior <= stack[i]:
        result.append(prior) # result = [1, 2, 3, 4]
        answer.append('+')   # answer = [+, +, +, +]
        prior += 1
    
    if stack[i] == result[-1]:
        result.pop()
        answer.append('-')

if result:
    print("NO")
else:
    print(*answer)


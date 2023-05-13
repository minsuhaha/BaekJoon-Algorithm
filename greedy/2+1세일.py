import sys
input = sys.stdin.readline

n = int(input())
# 내림차순 정렬
cost = sorted([int(input()) for _ in range(n)], reverse=True)

total = 0
for i in range(n):
    if (i+1) % 3 != 0: # 세번째 수가 아닐때만 +
        total+=cost[i]
print(total)
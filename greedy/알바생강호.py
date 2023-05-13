import sys
input = sys.stdin.readline

n = int(input())
tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)
total = 0
for i in range(n):
    if (tip[i] - (i+1-1)) > 0:
        total += tip[i] - (i+1-1)
print(total)
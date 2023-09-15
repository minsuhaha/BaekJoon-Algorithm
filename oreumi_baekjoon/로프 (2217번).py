import sys
input=sys.stdin.readline
n = int(input())

weight = [int(input().rstrip()) for _ in range(n)]
weight.sort(reverse=True)

result = []
cnt = 1
for w in weight:
    result.append(w*cnt)
    cnt += 1

print(max(result))
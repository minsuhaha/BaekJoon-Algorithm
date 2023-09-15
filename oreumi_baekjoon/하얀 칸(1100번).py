import sys
input = sys.stdin.readline
lst = [list(input()) for _ in range(8)]
res = 0
cnt = 0
for i in range(8):
    for j in range(8):
        if cnt % 2 == 0:
            if lst[i][j] == 'F':
                res += 1
        cnt += 1
    cnt += 1

print(res)
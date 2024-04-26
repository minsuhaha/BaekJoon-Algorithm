# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, m = map(int, input().split())
# exclude = [set(map(int, input().rstrip().split())) for _ in range(m)]
# result = []

# for comb in combinations(range(1,n+1), 3):
#     skip = False
#     for ex in exclude:
#         if ex.issubset(comb):
#             skip = True
#             break
    
#     if not skip:
#         result.append(comb)    

# print(len(result))

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
mixed = [[True]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    mixed[a][b] = False
    mixed[b][a] = False

cnt = 0
for comb in combinations(range(1, n+1), 3):
    if not mixed[comb[0]][comb[1]] or not mixed[comb[0]][comb[2]] or not mixed[comb[1]][comb[2]]:
        continue
    cnt += 1

print(cnt)

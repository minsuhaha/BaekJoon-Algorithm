import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
prior = [list(map(int, input().split())) for _ in range(n)]

total = 0
for a, b, c in combinations(range(m), 3):
    max_prior = 0
    for i in range(n):
        max_prior += max(prior[i][a], prior[i][b], prior[i][c])
    total = max(total, max_prior)

print(total)

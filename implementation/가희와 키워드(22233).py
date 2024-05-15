import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = set(input().rstrip() for _ in range(n))
kward = [list(input().rstrip().split(',')) for _ in range(m)]

for i in range(m):
    for ward in kward[i]:
        if ward in memo:
            memo.remove(ward)
    print(len(memo))

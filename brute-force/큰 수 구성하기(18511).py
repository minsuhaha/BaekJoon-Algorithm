import sys
from itertools import product
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

res = 1
for i in range(len(str(n)), len(str(n))-2, -1):
    for num in product(nums, repeat=i):
        num = int(''.join(map(str, num)))
        if num <= n:
            if num > res:
                res = num
print(res)

import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())
k = int(input())
nums = [input().rstrip() for _ in range(n)]

result = set((''.join(num) for num in permutations(nums, k)))
print(len(result))

# 1
# 2
# 12
# 1

# 12, 112, 11, 21, 212, 121, 122

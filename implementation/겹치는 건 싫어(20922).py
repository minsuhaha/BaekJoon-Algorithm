import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(input().split())

nums_cnt = defaultdict(int)
start, end = 0, 0
res = 1

while end < n:
    if nums_cnt[nums[end]] < k:
        nums_cnt[nums[end]] += 1
        end += 1
        res = max(res, end - start)
    else:
        nums_cnt[nums[start]] -= 1
        start += 1

print(res)

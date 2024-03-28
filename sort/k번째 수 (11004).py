import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = sorted(map(int, input().split()))
print(nums[k-1])

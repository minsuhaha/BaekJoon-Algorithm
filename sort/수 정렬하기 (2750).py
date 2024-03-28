import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(*nums)

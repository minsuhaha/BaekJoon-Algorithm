import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = sorted(map(int, input().split()))

start = 0
end = n-1
cnt = 0
sum = nums[start]+nums[end]

while start < end:
    if sum == m:
        cnt += 1
        start += 1
        end -= 1
    elif sum < m:
        start += 1
    elif sum > m:
        end -= 1
    sum = nums[start] + nums[end]

print(cnt)

        

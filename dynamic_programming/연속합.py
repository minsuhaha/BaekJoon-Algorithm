import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

# dp 인덱스를 한칸씩 땡김!
dp = [0]*n
dp[0] = nums[0]

# dp[현재값의인덱스] = max(이전dp + 현재값, 현재값)
for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])

print(max(dp))


    #       # 이전값 + 현재값      /   현재값
    # dp[2] = dp[1] + nums[1]  /  nums[1]  -> dp[2] = 6
    # dp[3] = dp[2] + nums[2]  /  nums[2]  -> dp[3] = 9
    # dp[4] = dp[3] + nums[3]  /  nums[3]  -> dp[4] = 10
    # dp[5] = dp[4] + nums[4]  /  nums[4]  -> dp[5] = 15
    # dp[6] = dp[5] + nums[5]  /  nums[5]  -> dp[6] = 21
    # dp[7] = dp[6] + nums[6]  /  nums[6]  -> dp[7] = -14
    # dp[8] = dp[7] + nums[7]  /  nums[7]  -> dp[8] = 12
    # dp[9] = dp[8] + nums[8]  /  nums[8]  -> dp[9] = 33
    # dp[10]= dp[9] + nums[9]  /  nums[9]  -> dp[10] = 32

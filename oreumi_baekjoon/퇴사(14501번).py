n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = lst[0][1]

# 현재의 일차를 따져줘야 함! (뒤부터 top-down 방식으로 : 왜냐면 일수 또한 따져줘야 하기 때문에)
for i in range(n-1, -1, -1):
    time, profit = lst[i][0], lst[i][1] # [0] : 시간, [1]: 이익

    # 현재 일차에서 해당 일차에 있는 상담시간을 합한 값이 n보다 클 경우 
    if time + i > n:
        dp[i] = dp[i+1]
    
    else:
        dp[i] = max(dp[i+1], dp[i+time]+profit)
print(max(dp))

# 거꾸로
# dp[7] = 0
# dp[6] = 0 = dp[7]
# dp[5] = dp[6] or dp[7] + 15 = 15
# dp[4] = dp[5] or dp[5] + 20 = 35
# dp[3] = dp[4] or dp[4] + 10 = 45
# dp[2] = dp[3] or dp[7] + 20 = 45
# dp[1] = dp[2] or dp[4] + 10 = 45

import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(n+1)
data = [list(map(int, input().split())) for _ in range(n)]

# top-bottom 방식으로 구현
for i in range(n-1, -1, -1):
    time = data[i][0] # 상담시 걸리는 기간
    money = data[i][1] # 상담 시 받는 돈
    
    if time + i > n:  # 기간이 넘는다면
        dp[i] = dp[i+1] # 기존위에 있는 dp값 그대로 가져오기
    else:
        dp[i] = max(dp[i+time] + money, dp[i+1]) # 
        # dp[i+time] -> 누적으로 값 구해주기 위해서 사용 이후 money를 더해준 값과 바로 위 dp[i+1] 비교해서 max값을 뽑기
print(dp[0])


#dp[6] = dp[7] = 0
#dp[5] = dp[6] = 0
#dp[4] = max(dp[6] + 15, dp[5]) = 15
#dp[3] = max(dp[4] + 20, dp[4]) = 35
#dp[2] = max(dp[3] + 10, dp[3]) = 45
#dp[1] = max(dp[6] + 20, dp[2]) = 45
#dp[0] = max(dp[3] + 10, dp[1] ) = 45


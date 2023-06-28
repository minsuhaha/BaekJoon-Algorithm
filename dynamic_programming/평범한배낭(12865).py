import sys
input = sys.stdin.readline
n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < bag[i-1][0]: # 이 경우 어차피 dp값이 0이 되므로
            dp[i][j] = dp[i-1][j] # dp는 결국 i기준 위에서 계속 누적으로 큰 값을 넣고 있기 때문에 위에 dp가 더 크지 작지는 않을거란 생각
        else:
            dp[i][j] = max(dp[i-1][j],  dp[i-1][j-bag[i-1][0]]+bag[i-1][1])
print(max(dp[n]))
# 어차피 누적 값 dp라 결국 맨 마지막 줄의 리스트에 가장 큰 값이 있음 -> 중요!
#  Fn = Fn-1 + Fn-2 (n ≥ 2)
import sys
input = sys.stdin.readline

n = int(input())

# dp 초기화
dp = [0] * (n+1)
dp[0] = 0 # 0번째 피보나치 수
dp[1] = 1 # 1번째 피보나치 수

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])


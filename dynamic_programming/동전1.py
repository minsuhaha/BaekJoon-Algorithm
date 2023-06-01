
# 누적한다고 생각 / 동전이 한개씩 추가될때 해당 동전으로 수를 만들 수 있는지 파악하고 만들 수 있으면 + 하기

#         0   1    2    3    4     5    6   7   8   9   ....
# 1       1   1    1    1    1     1    1   1   1   1   ....
# 1,2     1   1    2    2    3     3    4   4   5   5   .....
# 1,2,5   1   1    2    2    3     4    5   6   7   8   .....

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

dp[0] = 1 # 처음 coin 나올 시 값을 넣어주기 위해

for coin in coins:
    # coin부터 도는게 맞음 -> coin 전에는 어차피 추가될수가 없기에
    for i in range(coin, k+1):
        # 기존 dp[i] + 추가된 코인으로 인해 만들어질수있는 경우의 수 추가
        # 예를들어 coin = 5일때 dp[6] = dp[6] + dp[6-coin]
        # dp[6-coins] -> 사용이유는 : dp[1] 만드는거에 + coin(5) 해주면 경우의 수가 똑같이 늘어나는거이기에 그렇게 누적 합 구하기!
        dp[i] += dp[i-coin]

print(dp[k])
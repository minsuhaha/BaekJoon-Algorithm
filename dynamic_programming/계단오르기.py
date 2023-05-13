# import sys
# n = int(sys.stdin.readline())
# score = []
# for i in range(n):
#     score.append(int(sys.stdin.readline()))

# 계단은 1계단, 2계단 가능.
# 연속되게 3계단을 밟을수없음.
# 마지막 계단 꼭 밟아야함.

# '''
# 마지막 계단 기준으로 생각해보자
# dp[k]는 현재 가장 최대의 값일때 구하기
# k가 마지막 계단임
# dp[1] = 10(1)
# dp[2] = 10+(1) 20(2) = 30
# dp[3] = 20(2)+15(3) = 35 -> dp[2], dp[1]+15, dp[0] + 20 + 15
# dp[4] = 10(1)+20(2)+25(4) = 55 -> dp[2] + 25 = dp[1] + 15 + 25
# dp[5] = 10(1)+20(2)+25(4)+10(5) = 65 -> dp[4] + 10 = dp[2] + 25 + 10 > dp[3] + 10, 
# dp[6] = dp[4] + 20 = 75 -> dp[4] + 20(k) >  dp[3] + 10(k-1)일때 값 + 20(k) 일때 값3

# 결국 자기 값까지 밟아야 최대값이 나오네?
# '''

import sys
n = int(sys.stdin.readline())
score = []
for i in range(n):
    score.append(int(sys.stdin.readline()))

dp = [0] * (n+1)

if n == 1:
    print(score[0])
elif n == 2:
    print(score[0]+score[1])
else:
    dp[1] = score[0]
    dp[2] = score[0] + score[1] 
    for i in range(2, n+1):
        dp[i] = max(dp[i-2] + score[i-1], dp[i-3] + score[i-2] + score[i-1])
    print(dp[-1])
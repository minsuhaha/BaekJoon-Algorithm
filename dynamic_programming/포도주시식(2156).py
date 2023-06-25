# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

# 예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 
# 첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

import sys
input = sys.stdin.readline

n = int(input())
grapes = [int(input()) for _ in range(n)]

dp = [0]*(n+1)

# n <= 2 때는 for문을 돌 필요가 없기 때문에! 또한 n이 1일 경우 오류가 발생하기에! if문 설정
if n <= 2:
    print(sum(grapes))
else:
    dp[1] = grapes[0]
    dp[2] = grapes[0] + grapes[1]
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+grapes[i-1], dp[i-3]+grapes[i-2]+grapes[i-1])
    print(max(dp))


#  전 dp에서 가장 큰 값은 그대로 남음   - 경우의 수를 다 따져봤음
# dp[1] = 6 = 6                                            
# dp[2] = 6+10 = 16                                        
# dp[3] = 6+10 or 6+13 or 10+13 = 23                       
# dp[4] = 6+10+9 or 6+13+9 or 10+13 = 28                    
# dp[5] = 6+10+9+8 or 6+13+9 or 10+13+8 = 33
# dp[6] = 6+10+9+8 or 6+13+9+1 or 10+13+8+1 = 33 


# dp[1] = grapes[0]
# dp[2] = dp[1] + grapes[1]

# dp[3] = dp[2] or dp[1] + grapes[2] or dp[0] + grapes[1] + grapes[2]
# dp[4] = dp[3] or dp[2] + grapes[3] or dp[1] + grapes[2] + grapes[3]
# dp[5] = dp[4] or dp[3] + grapes[4] or dp[2] + grapes[3] + grapes[4]

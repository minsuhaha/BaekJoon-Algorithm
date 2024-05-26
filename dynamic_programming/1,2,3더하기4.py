'''
        1   2   3   4   5   6   7
1       1   1   1   1   1   1   1
1,2     1   2   2   3   3   3   4
1,2,3   1   2   3   4   5   6   8
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    
    dp = [1]*(n+1)
    
    for i in range(2, 4):
        for j in range(i, n+1):
            dp[j] += dp[j-i]
    
    print(dp[n])

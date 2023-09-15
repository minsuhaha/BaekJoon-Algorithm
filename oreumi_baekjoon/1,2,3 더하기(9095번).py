T = int(input())

def answer(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

for i in range(T):
    n = int(input())
    result = answer(n)
    print(result)




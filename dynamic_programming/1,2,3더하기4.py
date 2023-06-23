# n = int(input())
# nums = [int(input()) for _ in range(n)]

# for num in nums:
#     dp = [0] * (max(nums)+1)
#     dp[0] = 1
#     for i in range(1,4): # 1, 2, 3 의 숫자로 경우의 수를 만드는 것이니깐
#         for j in range(i, num+1):
#             dp[j] += dp[j-i]
#     print(dp[num])


num = int(input())
lst = [int(input()) for i in range(num)]
d = [1]*10001
d[1] = 1
d[2] = 2
d[3] = 3

for i in range(4,10001):
    d[i] += d[i-2]

for j in range(5, 10001):
    d[i] += d[i-3]

for i in lst:
    print(d[i])
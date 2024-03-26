import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
sum_nums = [[0]*(n+1) for _ in range(n+1)]

# 누적합 구하기
for i in range(1, n+1):
    row_sum = 0
    for j in range(1, n+1):
        row_sum += nums[i-1][j-1]
        sum_nums[i][j] = sum_nums[i-1][j] + row_sum

# 구간 합 구하기
        
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum_nums[x2][y2] - sum_nums[x1-1][y2] - sum_nums[x2][y1-1] + sum_nums[x1-1][y1-1]
    print(ans)

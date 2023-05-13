import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 방향 : 왼쪽아래, 바로아래, 오른쪽아래 이렇게 3가지 -> 하나의 값 당 방향 3개
dp = [[[0]*3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for k in range(3): # 방향이 3개이기 때문에
        dp[0][i][k] = lst[0][i] # dp 초기값 설정 -> lst 첫번째 열 값 그대로 집어넣기
        
# i:열, m:행, k:방향 으로 생각하고 풀자
# 아 ㅅㅂ 같은 방향으로 연속으로 움직이면 안된대
for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if j == 0 and k == 0:
                dp[i][j][k] = 100000 # 아무 큰 값 넣어주기 결과에 영향 없는 값
            elif j == M-1 and k == 2: 
                dp[i][j][k] = 100000 # 아무 큰 값 넣어주기
            else:
                if k == 0: # 왼쪽 방향에서
                    dp[i][j][k] = min(dp[i-1][j-1][k+1], dp[i-1][j-1][k+2]) + lst[i][j]
                elif k == 1:
                    dp[i][j][k] = min(dp[i-1][j][k-1], dp[i-1][j][k+1]) + lst[i][j]
                elif k == 2:
                    dp[i][j][k] = min(dp[i-1][j+1][k-1], dp[i-1][j+1][k-2]) + lst[i][j]
min_move = []
for i in range(M):
    min_move.append(min(dp[N-1][i]))

print(min(min_move))


# 5,5,5     8,8,8      5,5,5     1,1,1
# I,8,11  10,13,10    16,13,9    9,5,I
# I,17,19 85,87,86    75,74,70   14,10,I
# I,19,87 18,86,71    90,75,15   72,12,I


# 5 8 5 1
# 3 5 8 4
# 9 77 65 5
# 2 1 5 2
# 5 98 1 5
# 4 95 67 58
# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다
# 안전 거리가 가장 큰 칸을 구해보자
from collections import deque
# 입력
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 여러칸의 아기상어가 있기에 미리 queue에 아기상어가 있는 칸 담아놓기
queue = deque()
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            queue.append((i,j))

# 8개 방향 설정
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

# 최대 안전거리값을 담을 res 변수 선언
res = 0 

while queue:
    x, y = queue.popleft()

    # 8개의 방향 반영
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if lst[nx][ny] != 0:
            continue

        else:
            lst[nx][ny] = lst[x][y] + 1
            queue.append((nx,ny))
            res = max(lst[nx][ny], res)

print(res - 1)














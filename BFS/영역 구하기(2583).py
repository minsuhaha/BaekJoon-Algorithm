import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0]*n for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 직사각형 입력받기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1 # 방문처리

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1 # 방문처리
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                continue
            if not graph[nx][ny]:
                cnt += 1
                queue.append((nx, ny))
                graph[nx][ny] = 1 # 방문처리
    return cnt

result = []
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            cnt = bfs(i, j)
            result.append(cnt)

print(len(result))
print(*sorted(result))

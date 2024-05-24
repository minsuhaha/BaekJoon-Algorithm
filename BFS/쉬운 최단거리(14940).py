'''
0 : 갈 수 없는 땅, 1 : 갈 수 있는 땅, 2 : 목표지점
가로 세로만 움직일 수 있다 -> 상하좌우 4방향
n : 세로(행의 수), m : 가로(열의 수)
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0 # 목표지점 0으로 초기화
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] += graph[x][y]
                visited[nx][ny] = True
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and not visited[i][j]:
            bfs(i, j)
            break

# graph에서는 1 값인데 방문을 하지 않은 지점 -1 처리
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])

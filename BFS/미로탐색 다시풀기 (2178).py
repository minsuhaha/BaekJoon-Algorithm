import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상하좌우 4개의 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                graph[nx][ny] += graph[x][y]
                visited[nx][ny] = True

    return graph[n-1][m-1]

print(bfs(0,0))

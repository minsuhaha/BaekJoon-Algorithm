import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                continue
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                cnt += 1
                queue.append((nx, ny))
                visited[ny][nx] = True
    return cnt

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            width = bfs(j, i)
            result.append(width)

if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)

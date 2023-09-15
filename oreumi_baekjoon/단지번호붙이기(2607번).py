from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

# 연결 -> 상하좌우

graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt


res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            res.append(bfs(i,j))
            
res.sort()
print(len(res))
for r in res:
    print(r)
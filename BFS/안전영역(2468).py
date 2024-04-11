import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

max_num = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > max_num:
            max_num = graph[i][j]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j, k):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if graph[nx][ny] > k and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

result = 0
for k in range(max_num+1): # 비가 아예 안오는 케이스도 포함해줘야 함!
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                bfs(i, j, k)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)

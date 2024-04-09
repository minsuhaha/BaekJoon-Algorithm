import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
total_cnt = 0 # 총 단지 수
result = [] # 단지 내 집의 수 담을 리스트

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    cnt = 1 # 해당 단지 내 집의 수

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            result.append(cnt)
            total_cnt += 1

print(total_cnt)
for res in sorted(result):
    print(res)

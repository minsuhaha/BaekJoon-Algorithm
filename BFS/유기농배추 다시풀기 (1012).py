import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    def bfs(y, x):
        queue = deque([(y, x)])
        graph[y][x] = 0 # 배추 방문처리

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                    continue
                
                if graph[ny][nx] == 1:
                    queue.append((ny, nx))
                    graph[ny][nx] = 0 # 배추 방문처리

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)

import sys
from collections import deque
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

# 나이트가 한 번에 이동 할 수 있는 x,y 좌표
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > l-1 or ny < 0 or ny > l-1:
                continue
            if not chess[nx][ny] and not visited[nx][ny]:
                chess[nx][ny] = chess[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return chess

for _ in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    chess = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    res = bfs(start_x, start_y)
    print(res[end_x][end_y])
    
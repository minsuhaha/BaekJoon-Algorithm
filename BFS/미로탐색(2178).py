from collections import deque
N, M = map(int,input().split())
mirror = [list(map(int, input())) for _ in range(N)]

def bfs(x, y):
    queue = deque([(x,y)])
    
    # 인접하게 이동 할 수 있는 (상하좌우) x, y 좌표 초기 설정 
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        # (x, y) 좌표에서 이동 할 수 있는 상하좌우 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # x, y 좌표 범위 제한        
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # mirror[nx][ny] 값이 0 이면 이동이 불가 한 곳이기 때문
            elif mirror[nx][ny] == 0:
                continue
            
            # mirror[nx][ny] 값이 1 이면 현재 이동 할 수 있는 공간임!
            elif mirror[nx][ny] == 1:
                mirror[nx][ny] = mirror[x][y] + 1
                queue.append((nx,ny))

    return mirror[N-1][M-1]

print(bfs(0,0))
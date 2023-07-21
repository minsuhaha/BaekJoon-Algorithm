from collections import deque
import sys

T = int(input())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[[0] for _ in range(N)] for _ in range(M)] # 밭 리스트
    
    # 상하좌우 x축 y축 초기설정
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # 배추흰지렁이 값
    cnt = 0 

    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        # 배추 있는 좌표 표시
        field[x][y] = 1

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        # 배추 방문처리
        field[x][y] = 0
        
        while queue:
            x, y = queue.popleft()
            # 인접위치의 배추무리 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # x, y 범위 확인
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                else:
                    # 배추가 있는 위치라면
                    if field[nx][ny] == 1:
                        field[nx][ny] = 0
                        queue.append((nx,ny))

    # 밭 공간 하나씩 탐색
    for i in range(M):
        for j in range(N):
            # 배추가 심어져 있는 좌표라면
            if field[i][j] == 1:
                # 인접 배추 무리 찾기
                bfs(i, j)
                # 한 무리가 끝난 뒤 실행
                cnt += 1
    print(cnt)
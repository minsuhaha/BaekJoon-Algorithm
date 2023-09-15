#  일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
#  물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 최대값 0 ~ (최대값-1) 까지 돌리기위해 -> 경우의 수
high = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > high:
            high = graph[i][j]

# 상하좌우 인접 4개방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
def bfs(i, j, high):
    queue.append((i,j))
    visited[i][j] = 1 # 방문처리

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[nx][ny] > high and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1


# high 값은 모든 지역이 잠기므로 빼고 for 돌리기
result = 0
for k in range(high):
    cnt = 0
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 높이가 high보다 크면 안전영역이고, 아직 방문을 하지않았다면
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k)
                cnt += 1
    
    # 각 k 마다의 cnt 개수를 파악 후 result에 담아주기
    if result < cnt:
        result = cnt
        
print(result)
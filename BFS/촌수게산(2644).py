from collections import deque
N = int(input()) # 전체 사람의 수 N
a, b = map(int, input().split()) # 계산해야 되는 두 사람의 촌수 a, b 로 둠

graph = [[] for _ in range(N+1)]
m = int(input())
for _ in range(m):
    # 양뱡으로 입력 받아야 한다
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# ---------- 입력부분 -----------

visited = [0]*(N+1) # 방문처리를 해주기 위해
result = [0]*(N+1) # a 기준으로 떨어진 거리 계산을 해주기 위해

# 그래프 탐색 시작 지점인 a, 끝나는 지점인 b를 매개변수로 담아주기
def bfs(a,b):
    queue = deque([a])
    visited[a] = 1 # 방문처리 해주기
    
    while queue:
        q = queue.popleft()

        if q == b:
            return result[q]

        for i in graph[q]:
            if visited[i] != 1:
                visited[i] = 1
                queue.append(i)
                result[i] = result[q] + 1

    # while 문을 다 돌았는데 return 값이 없었다면
    return -1

answer = bfs(a, b)
print(answer)


 








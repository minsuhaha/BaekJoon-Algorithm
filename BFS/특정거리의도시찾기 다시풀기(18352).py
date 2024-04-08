import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node != x and not visited[node]: # 출발지점은 제외
                queue.append(node)
                visited[node] = visited[v] + 1
    return visited

answer = bfs(x)

for num, cnt in enumerate(answer):
    if cnt == k:
        result.append(num)

if result:
    for res in result:
        print(res)
else:
    print(-1)
    
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                cnt += 1
    return cnt

print(bfs(1))

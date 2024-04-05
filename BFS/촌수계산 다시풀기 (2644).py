import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, b):
    queue = deque([a])
    visited[a] = True

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                distance[node] = distance[v] + 1
                visited[node] = True
    
    if not distance[b]:
        return -1
    return distance[b]

print(bfs(a,b))


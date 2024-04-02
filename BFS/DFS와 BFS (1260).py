import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(i):
    print(i, end=' ')
    visited1[i] = True
    for node in sorted(graph[i]):
        if not visited1[node]:
            DFS(node)
        
def BFS(i):
    queue = deque([i])
    visited2[i] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for node in sorted(graph[v]):
            if not visited2[node]:
                queue.append(node)
                visited2[node] = True

DFS(v)
print()
BFS(v)

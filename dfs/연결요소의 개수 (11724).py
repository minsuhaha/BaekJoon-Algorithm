import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

# 노드 별 연결리스트
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
def dfs(graph, i, visited):
    visited[i] = True # 방문처리
    for node in graph[i]:
        if not visited[node]:
            dfs(graph, node, visited)
    
visited = [False] * (n+1)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(graph, i, visited)
        
print(cnt)

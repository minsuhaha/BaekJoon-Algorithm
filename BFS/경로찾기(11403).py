import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque([x])
    visited = [False] * n

    while queue:
        v = queue.popleft()

        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                answer[x][i] = 1
                visited[i] = True

for i in range(n):
    bfs(i)

for ans in answer:
    print(*ans)

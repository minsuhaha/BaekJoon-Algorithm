import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [0] * 100001 # 나올 수 있는 최대거리

def bfs(i):
    queue = deque([i])

    while queue:
        x = queue.popleft()
        
        if x == k:
            print(dist[x])
            break
        
        for nx in (x-1, x+1, x*2): # 3가지 경우 (-1, 1 *2)
            if 0 <= nx <= 100000 and not dist[nx]:
                queue.append(nx)
                dist[nx] = dist[x] + 1

bfs(n)

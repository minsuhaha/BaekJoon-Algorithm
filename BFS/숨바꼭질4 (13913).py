import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    queue = deque([x])

    while queue:
        x = queue.popleft()

        if x == K:
            res.appendleft(K)
            m = K
            while m != N: 
                m = move[m]
                res.appendleft(m)

            return point[x], res
            

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and point[nx] == 0:
                point[nx] = point[x] + 1
                queue.append(nx)
                move[nx] = x # 부모 노드 담기


N, K = map(int, input().split())
point = [0] * 100001
move = [0] * 100001
res = deque([])
d, d_lst = bfs(N)
print(d)
print(*d_lst)

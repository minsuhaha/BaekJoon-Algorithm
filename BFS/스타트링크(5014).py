import sys
from collections import deque
input = sys.stdin.readline

'''
F : 모든 층 
G : 스타트링크 층
S : 강호가 있는 층
U : 위로 U층 가는 버튼
D : 아래로 D층 가는 버튼
강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.
(만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
'''

F, S, G, U, D = map(int, input().split())

graph = [0 for _ in range(F+1)]

def bfs(v):
    queue = deque([v])
    graph[v] = 1 # S층이 중복으로 계산되는것을 방지하기 위해 / 처음부터 방문처리

    while queue:
        v = queue.popleft()
        
        if v == G:
            return graph[v]-1

        for x in (v+U, v-D):
            if (0 < x <= F) and not graph[x]:
                graph[x] = graph[v] + 1
                queue.append(x)

    return 'use the stairs'

print(bfs(S))

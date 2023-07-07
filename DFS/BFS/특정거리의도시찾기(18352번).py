import sys
from collections import deque
n, m , k, x = map(int, sys.stdin.readline().split())
graphs = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향이 아닌 단방향이기 때문에 a -> b
    graphs[a].append(b)

# -1로 초기화 해줘야지 안 그러면 x 출발지점이 양방향 처리될때 최단경로로 들어올수있음! -> 문제 조건에서 출발지점은 최단경로가 0이라고 명시해놓음
connects = [-1] * (n+1)
# 출발지점을 제외한 나머지 값들의 최단경로 합을 위해 출발지점 connect 부분만은 0으로 초기화 -> 이따 합할때 골치아파지는것을 방지
connects[x] = 0

queue = deque()
queue.append(x)
while queue:
    # queue 선입선출
    num = queue.popleft()
    for graph in graphs[num]:
        if connects[graph] == -1:
            connects[graph] = connects[num] + 1
            queue.append(graph)


res = False
for idx, connect in enumerate(connects):
    if connect == k:
        print(idx)
        res = True

if not res:
    print(-1)


# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input())
# queue = deque()

# for i in range(1, n+1):
#     queue.appendleft(i)

# while len(queue) >= 2:
#     queue.pop()
#     queue.appendleft(queue.pop()) 

# print(queue.pop())
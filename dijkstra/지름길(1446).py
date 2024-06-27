import sys
import heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            cost = distance[node] + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (distance[next_node], next_node))


N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

# 일반길
for i in range(D):
    graph[i].append((i+1, 1))

# 지름길
for _ in range(N):
    start, end, short = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, short))

dijkstra(0)
print(distance[D])

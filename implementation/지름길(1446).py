import sys
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dist = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        dist[i] = min(dist[i], dist[i-1]+1)

    for start, end, short in graph:
        if i == start and end <= D and short < end-start:
            dist[end] = min(dist[i]+short, dist[end])

print(dist[D])

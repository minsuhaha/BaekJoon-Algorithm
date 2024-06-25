import sys
input = sys.stdin.readline

n = int(input())
graph = []

max_l = 1
for _ in range(n):
    l, h = map(int, input().split())
    graph.append((l, h))
graph.sort(key=lambda x:x[0])

max_h, max_idx = 1, 1
for i in range(n):
    if graph[i][1] > max_h:
        max_idx = i
        max_h = graph[i][1]

res = 0
# 왼 -> 최대값까지
left_h = 1
for i in range(max_idx):
    if graph[i][1] > left_h:
        left_h = graph[i][1]
    res += left_h*(graph[i+1][0] - graph[i][0])

# 오 -> 최대값까지
right_h = 1
for i in range(n-1, max_idx, -1):
    if graph[i][1] > right_h:
        right_h = graph[i][1]
    res += right_h*(graph[i][0] - graph[i-1][0])

res += graph[max_idx][1]
print(res)

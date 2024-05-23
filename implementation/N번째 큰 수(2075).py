import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for i in range(n):
        if len(heap) < n:
            heapq.heappush(heap, nums[i])
        else:
            if heap[0] < nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])

print(heapq.heappop(heap))

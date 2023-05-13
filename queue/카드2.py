from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()

for i in range(1, n+1):
    queue.appendleft(i)

while len(queue) >= 2:
    result = queue.pop()
    queue.appendleft(queue.pop()) 

print(queue.pop())


# 4 3 2 1
# 2 4 3
# 4 2
# 4 출력


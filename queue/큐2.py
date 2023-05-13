from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

queue = deque()

for i in range(n):
    data = input().split()
    if data[0] == 'push':
        queue.appendleft(data[1]) # 왼쪽으로 입력받음
    elif data[0] == 'pop':
        if queue:
            print(queue.pop()) # queue는 선입선출이기 때문에 맨 앞 인덱스값 pop
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(queue))
    elif data[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif data[0] == 'back':
        if queue:
            print(queue[0])
        else:
            print(-1)

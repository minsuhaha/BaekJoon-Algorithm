from collections import deque
import sys
input = sys.stdin.readline
# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

n, m = map(int, input().split()) # n : 큐의 크기, m : 뽑아내려는 수
data = list(map(int, input().split()))
queue = deque(i for i in range(1,n+1))

total_count = 0

for d in data:
    while True:
        if queue[0] == d: # 1번에 해당하는 경우 -> 2,3번 경우에 해당 x -> total_count = 0
            queue.popleft()
            break
# 10 3  [2, 3, 4, 5, 6, 7, 8, 9, 10, 1] 1
# 2 9 5
        else: # 2,3번에 해당하는 경우
            # temp = queue[0] # temp 초기화
            if queue.index(d) <= len(queue) // 2: # 2번에 해당하는 경우
                while queue[0] != d:
                    queue.append(queue.popleft()) # 2번에 해당하기에 오른쪽 끝으로 보내주기
                    total_count +=1
                
            else:
                while queue[0] != d:
                    queue.appendleft(queue.pop())
                    total_count +=1
            
print(total_count)
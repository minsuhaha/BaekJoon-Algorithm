from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
queue = deque(i for i in range(1,n+1)) 
result = []
# queue = [1 2 3 4 5 6 7]
idx = 0
while queue:
    idx += 1 
    temp = queue.popleft() 
    if idx % k == 0: 
        result.append(temp) 
    else:
        queue.append(temp) 
print(str(result).replace('[','<').replace(']','>'))
    


# # 원형 큐 문제 예시
# 1 2 3 4 5 6 7 
# 1 2 [3] 4 5 6 7
# 1 2 [3] 4 5 [6] 7
# 1 [2] [3] 4 5 [6] 7
# 1 [2] [3] 4 5 [6] [7]
# 1 [2] [3] 4 [5] [6] [7]
# [1] [2] [3] 4 [5] [6] [7]
# [1] [2] [3] [4] [5] [6] [7]

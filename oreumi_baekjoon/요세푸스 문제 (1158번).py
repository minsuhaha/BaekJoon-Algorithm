from collections import deque
# n : 총사람 / k : k번째 사람 제거
n, k = map(int, input().split())
queue = deque()
result = []

# 총 숫자 넣어주기
for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        q = queue.popleft()
        queue.append(q)
    result.append(queue.popleft())    

res = str(result).replace('[','<').replace(']','>')
print(res)



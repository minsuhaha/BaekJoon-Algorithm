import sys
input = sys.stdin.readline
n = int(input())

data = list(map(int, input().split()))
# data = [2, 1, 1, 0]
result = [x for x in range(1, n+1)]
# result = [1, 2, 3, 4]

# 4 1 2 3

# KeyPoint : 예제에서 준 값들중 뒤에서 부터 보고 숫자 자리 위치 바꿔주기
for i in range(n-1, -1, -1): # 맨 마지막 부분은 항상 0이기에 빼주기
    idx = data[i]
    if idx == 0:
        continue
    elif idx == 1:
        result[i], result[i+1] = result[i+1], result[i]
    else: # idx >=2 일때
        for j in range(idx):
            result[i+j], result[i+j+1] = result[i+j+1], result[i+j]    

print(*result)
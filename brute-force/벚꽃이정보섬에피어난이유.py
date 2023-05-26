def multiply(x):
    max = 1
    for i in range(len(x)):
        max *= x[i]
    return max

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

result = []

# 3개의 가림막 만들어주기
for i in range(1, n-2): # 뒤에 2개 그룹 추가 생성 필요
    for j in range(i+1,n-1): # 뒤에 1개 그룹 추가 생성 필요
        for k in range(j+1,n): # 뒤에 그룹 필요 x
            total = 0
            # 4개 그룹
            total += multiply(lst[0:i])
            total += multiply(lst[i:j])
            total += multiply(lst[j:k])
            total += multiply(lst[k:])
            result.append(total)
print(max(result))
      



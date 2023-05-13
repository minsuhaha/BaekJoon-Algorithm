import sys
input = sys.stdin.readline

A, B = input().split()

count = 0
result = []

for i in range(len(B)-len(A)+1): # 순서의 경우의 수도 고려해주기 위해서 -> 끼워맞춰보는 활동
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count+=1
    result.append(count)
print(min(result))
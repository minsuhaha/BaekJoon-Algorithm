import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # A배열을 오름차순으로 정렬
B.sort(reverse=True) # B배열은 내림차순으로 정렬

total = 0

for i in range(n):
    total += A[i]*B[i]

print(total)


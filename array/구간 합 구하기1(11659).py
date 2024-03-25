import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum_numbers = [0] 
total = 0

# 구간 합 배열
for num in numbers:
    total += num
    sum_numbers.append(total) 

# 구간 합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_numbers[j] - sum_numbers[i-1])

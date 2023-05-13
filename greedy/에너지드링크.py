import sys
input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))
total = data[-1] # data에서 가장 큰값 넣기

for i in range(n-1):
    total += data[i]/2

print(total)
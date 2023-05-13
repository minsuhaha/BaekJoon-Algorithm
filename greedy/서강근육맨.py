import sys
input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))
n_data = []


if n % 2 != 0: # 운동기구가 홀수개라면
    for i in range(n//2):
        total = data[i] + data[n-i-2]
        n_data.append(total)
    n_data.append(data[-1])

else: # 운동기구가 짝수개라면
    for i in range(n//2):
        total = data[i] + data[n-i-1]
        n_data.append(total)

print(max(n_data))
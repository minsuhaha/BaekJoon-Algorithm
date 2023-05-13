n = int(input())
time = list(map(int,input().split()))
time.sort()
total = 0
result = 0
for i in range(n): 
    total += time[i]
    result += total
print(result)
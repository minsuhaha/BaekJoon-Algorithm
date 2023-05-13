n = int(input())
times = list(map(int,input().split()))
times.sort() # 오름차순으로 정렬!

total = 0 # 각 사람들 입장에서의 기다리는 시간을 담은 total (개인)
result = 0 # 각각 사람들의 기다리는 시간의 총합을 담는 result (총합)

for i in range(n):
    total += times[i]  # 1/3/6/9/13
    result += total # 1/4/10/19/32
    
print(result)
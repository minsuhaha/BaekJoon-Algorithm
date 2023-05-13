n = int(input())

# 첫번째 곳에서 두번째 곳까지 가는 거리는 첫번째 도시에서 주유를 무조건 해야됨!
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
oil = oil[:-1] # 맨 마지막 도시는 도착지점이기에 oil가격이 필요가없음

# total 초기화 -> 무조건
total = road[0]*oil[0]

# 비교해서 작은 oil 값 담기
min_oil = oil[0] 

for i in range(1, n-1):
    if min_oil > oil[i]: # 옆 도시값과 비교
        total += road[i]*oil[i]
        min_oil = oil[i]
    else:
        total += road[i]*min_oil
print(total)



# for i in range(2,n):
#     if oil[i] < oil[i-1]: # 이전 도시의 oil보다 현재 도시의 oil 가격이 더 싸다면
#         total += oil[i]*road[1:]



# 대근이는 터널의 입구에, 영식이는 터널의 출구에 각각 잠복
n = int(input()) # 차량대수

start = {}

for i in range(n):
    start[input()] = i

end = [input() for _ in range(n)]

cnt = 0 # 추월 차량 대수
for i in range(n-1):
    for j in range(i, n):
        # start 지점에서 뒷차량이였던 차량이 앞차량을 추월을 했을 경우
        if start[end[i]] > start[end[j]]:
            cnt += 1          
            break
# cnt의 최대값은 n-1개
print(cnt)

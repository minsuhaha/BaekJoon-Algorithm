p = int(input())
data = [list(map(int, input().split())) for _ in range(p)]

for i in range(p):
    count = 0
    for j in range(1, len(data[i])-1): # 앞에 이미 있는 값
        for k in range(j+1, len(data[i])): # 앞에 값과 비교할, 지금 들어오는 값이라고 생각!
            if data[i][j] > data[i][k]:
                data[i][j], data[i][k] = data[i][k], data[i][j] # swap해서 자리 바꿔주기
                count += 1
    print(f"{data[i][0]} {count}")
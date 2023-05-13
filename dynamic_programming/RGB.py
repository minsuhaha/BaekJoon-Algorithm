n = int(input())
color = []
for i in range(n):
    color.append(list(map(int,input().split())))

# [][0] - 빨, [][1] - 초, [][2] - 파

for i in range(1, n):
    color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0] # 빨간색 기준
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1] # 초록색 기준
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2] # 파란색 기준

print(min(color[n-1][0], color[n-1][1], color[n-1][2]))


    
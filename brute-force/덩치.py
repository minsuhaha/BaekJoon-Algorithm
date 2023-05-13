# keypoint : N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다.
import sys
input = sys.stdin.readline
n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]
result = []

for i in range(n):
    rank = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 비교해서 뒤에가 더 덩치가 커버리면
            rank+=1
    result.append(rank)
print(*result)



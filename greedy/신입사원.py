# 서류등수 면접등수 
# 서류등수가 3일 경우 3 위의 서류등수 1, 2위를 보고 면접등수가 서류 3일 경우의 면접등수보다 높은지 확인해야됨
# 확인 결과 서류1,2의 면접등수가 서류3의 면접등수보다 낮을 때는 선발 그렇지 않을때(서류,면접등수 모두 낮음) -> 선발 x

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    # 서류등수를 기준으로 먼저 오름차순으로 정렬해주기
    data = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
    prior = data[0][1] # 가장 서류등수가 높은 사람의 면접등수 (이 사람은 이미 선발되었다고 간주)
    minus = 0 # 선발되지 않는 사람을 제하기 위해

    for i in range(1, n):
        if data[i][1] > prior:
            minus += 1
        else: # 서류등수는 낮지만 면접점수는 더 높을경우
            prior = data[i][1]
    print(n - minus)

                

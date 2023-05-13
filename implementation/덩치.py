n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

# 덩치는 몸무게와 키로 판단! -> 우선순위 없음.
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다

result = ''
for i in range(n):
    rank = 1 # rank는 1위 부터 있기에 자신보다 덩치가 큰 사람이면 0명기준 rank=1    
    for j in range(n):
        # 몸무게 키 둘다 클 경우
        if (lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]):
            rank+=1

    result+=f'{rank} '
print(result[:-1])
        
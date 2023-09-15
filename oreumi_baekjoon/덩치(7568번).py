# A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 
# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다
n = int(input())
person = [list(map(int, input().split())) for _ in range(n)]
rank = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            cnt += 1
    rank.append(cnt)
print(*rank)
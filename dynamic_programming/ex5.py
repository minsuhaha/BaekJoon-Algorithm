n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

# 만들 수 없는 값 초기화
d = [100001] * (m+1)
d[0] = 0 
# coin값을 돌리기 위해
for i in range(n):
    # coin의 제일 작은 값부터 해당 m까지 돌리기
    for j in range(coin[i], m+1):   
        d[j] = min(d[j], d[j - coin[i]] + 1)
print(d[m])
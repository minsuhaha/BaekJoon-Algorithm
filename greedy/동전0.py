# n : 동전의 종류, k : 동전을 적절히 활용하여 만들 동전가치의 합 
n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
count = 0
# 큰 단위가 작은 단위의 배수이므로 그리디 알고리즘 사용가능!
# coin의 개수만큼 돌려서 비교하면 k값이 나오므로 len(coin)만큼 돌기!
coin.sort(reverse=True) # 내림차순으로 정렬
for i in range(len(coin)):
    count+=k//coin[i]
    k = k%coin[i]
print(count) 

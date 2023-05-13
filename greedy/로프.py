# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. 
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
# 2
# 10 - 하나의 로프가 들 수 있는 중량
# 15 - 하나의 로프가 들 수 있는 중량
import sys
input = sys.stdin.readline
n = int(input())

weight = [int(input()) for _ in range(n)]
weight.sort(reverse=True) # 내림차순으로 바꿔주기

total = []
for i in range(1, n+1):
    total.append(weight[i-1]*i)

print(max(total))
# 5
# 5
# 4
# 2
# 2
# 2

# 10
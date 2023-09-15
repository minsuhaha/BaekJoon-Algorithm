from math import comb # 조합의 경우의 수를 구해주는 것이 아니라 조합의 개수를 구해준다!
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M,N))
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
J = int(input())

L, R = 1, M
size = R-L
count = 0
for _ in range(J):
    pos = int(input()) # 사과가 떨어지는 위치
    if L <= pos <= R: # 사과가 떨어지는 위치가 바구니 안에 있을 때
        continue
    elif pos < L: # 바구니 왼쪽 끝이 사과가 떨어지는 위치보다 오른쪽에 있을 때
        count += L-pos
        L = pos
        R = L + size
    elif pos > R:
        count += pos - R
        R = pos
        L = R - size
print(count)
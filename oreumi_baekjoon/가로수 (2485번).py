import sys
input = sys.stdin.readline
n = int(input().rstrip())

# lst안에 들어있는 수들 간의 차이값들의 최대공약수를 구해주고 그 값을 간격 기준점으로 잡아줘야할듯! -> 정확했음
lst = [int(input().rstrip()) for _ in range(n)]

# 최대공약수 구해주는 함수 (gcd)
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# lst 간격 값을 담을 interval 
interval = []
for i in range(n-1):
    interval.append(lst[i+1] - lst[i])

# 간격 값들의 최대공약수
gcd_num = interval[0]
for i in range(1, len(interval)):
    gcd_num = gcd(interval[i], gcd_num)

# 추가되어야하는 가로수 수
cnt = ((lst[-1]- lst[0]) // gcd_num) - n + 1
print(cnt)





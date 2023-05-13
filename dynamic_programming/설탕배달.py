n = int(input())

# 봉지 3kg, 5kg 1
bucket = 0

while n >= 0:
    # 0은 어떠한 수와 나눠도 0이라는 것을 기억!
    if n % 5 == 0:
        bucket += n//5
        print(bucket)
        break
    n = n - 3 # 3kg 봉지는 있기 때문에 하지만 최소한의 봉지개수를 위해서는 -3 해줌으로써 얼른 5의 배수를 만들어줘야함!
    bucket += 1
    if n < 0:
        print(-1)
    
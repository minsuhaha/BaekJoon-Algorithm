m, n = map(int, input().split())

numbers = [True for _ in range(n+1)]

for i in range(2, int(n**0.5)+1):
    if numbers[i]: # 소수이면
        j = 2
        while i * j <= n:
            numbers[i*j] = False    
            j += 1

for i in range(m, n+1):
    if i > 1:
        if numbers[i]:
            print(i)
    
import sys
input = sys.stdin.readline

# 설탕봉지는 3kg 짜리, 5kg 짜리가 있음

n = int(input()) # 18kg

count = 0

while n > 0:
    if n % 5 == 0: # 가장 최상의 경우 -> 봉지가 가장 적게 사용됨
        count += n // 5
        break
    else: 
        if n >= 3:
            n -= 3 # 우리의 목표는 5kg 봉지를 많이 사용하는것이기에 일단 3kg 봉지 하나만 사용하고 남은 설탕을 5kg 봉지들로만 가능한지 비교하기
            count += 1 # 3kg 봉지 하나가 사용됨
        else:
            count = -1
            break
print(count)

# 2. 실전문제 위에서 아래로

n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

result = sorted(num, reverse=True) # 내림차순

for i in range(len(result)):
    print(result[i], end=' ') # 띄어쓰기 없이 한칸만 띄우고 다시 진행



# 백준 별찍기 - 8
'''
n = int(input())

for i in range(1, n*2):
    if i <= n:
        print('*'*i + ' '*(n*2-i*2) + '*'*i)
    else:
        print('*'*(n*2-i) + ' '*(n*2-(n*2-i)*2) + '*'*(n*2-i))
'''

# 나는 요리사다 - 2953번
'''
scores = [list(map(int,input().split())) for i in range(5)]

max = 0
idx = 0
for i, score in enumerate(scores):
    if sum(score) > max:
        max = sum(score)
        idx = i+1
print(idx, max)
'''

# 손익분기점 - 1712번
'''
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    # 고정비용은 고정되어있기에 변동 x / 가변비용과 수익비용만 변동 o
    print(a // (c-b) + 1)
'''

# 소가 길을 건너간 이유 1 - 14467번
'''
n = int(input())

arr = {}
cnt = 0

for _ in range(n):
    num, loc = map(int, input().split())
    
    if num not in arr.keys():
        arr[num] = loc
    
    else:
        if arr[num] != loc:
            cnt += 1
            arr[num] = loc
print(cnt)
'''

# 과제 안 내신 분? - 5597번
'''
student = [int(input()) for _ in range(28)]
students = list(range(1,31))

for s in students:
    if s not in student:
        print(s)
'''

# 비밀편지 - 5426번
# from math import sqrt
# n = int(input())

# for _ in range(n):
#     result = ''
#     letter = input()

#     for i in range(int(sqrt(len(letter)))-1, -1, -1):
#         for j in range(i, len(letter), int(sqrt(len(letter)))):
#             result += letter[j]
#     print(result)
        
# 처음 파일 읽기
with open ('../example.txt', 'r') as file:
    content = file.read()
    print(content)

# 문구 추가하기
with open ('../example.txt', 'a') as file:
    file.write("추가된 문구")

# 추가된 문구 포함한 텍스트파일 읽기
with open ('../example.txt', 'r') as file:
    content = file.read()
    print(content)
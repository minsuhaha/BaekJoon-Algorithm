# 4. 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a에서 가장 작은 값과 b에서 가장 큰값과 스와프 하는 원리를 이용
a.sort() # 오름차순으로 정렬해줌으로써 가장 작은 값이 맨앞에 나오도록 설정!
b.sort(reverse=True) # 내림차순으로 정렬해줌으로써 가장 큰 값이 맨앞에 나오도록 설정!
 
for i in range(k): # k번만큼 스와프 실행
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # a배열의 가장 작은값과 b배열의 가장 큰 값과 스와프
    else:
        break # a의 배열이 더 이상 b배열보다 작은 값이 존재하지 않을때 break로 미리 빠져나와주기

print(sum(a))
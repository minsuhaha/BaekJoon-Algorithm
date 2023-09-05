# 스위치의 개수
import sys
input = sys.stdin.readline
n = int(input())
switch =  [0] + list(map(int, input().split()))
m = int(input())

for _ in range(m):
    gender, k = map(int, input().split())
    # 남자 일 경우
    if gender == 1:
        idx = k
        while idx <= n:
            switch[idx] = 1 if switch[idx] == 0 else 0
            idx += k # k의 배수
    
    # 여자 일 경우
    elif gender == 2:
        # switch[k]는 무조건 체인지됨
        switch[k] = 1 if switch[k] == 0 else 0
        i, j = k-1, k+1
        while i >= 1 and j <= n:
            if switch[i] == switch[j]:
                switch[i] = 1 if switch[i] == 0 else 0
                switch[j] = 1 if switch[j] == 0 else 0
            else:
                break
            i -= 1
            j += 1

for i in range(1, n+1):
    print(switch[i], end=' ')
    
    # 즉 i가 20의 배수일때
    if i % 20 == 0:
        print()
                    

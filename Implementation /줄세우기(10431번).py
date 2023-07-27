# T = int(input())
# for _ in range(T):
#     students = list(map(int, input().split()))
#     students = students[1:]
#     cnt = 0
#     # bubble 솔트문제네!
#     for i in range(len(students)-1, 0, -1):
#         for j in range(i):
#             if students[j] >  students[j+1]:
#                 students[j], students[j+1] = students[j+1], students[j] # swap
#                 cnt += 1
#     print(cnt)

import sys
T = int(input())

for _ in range(T):
    students = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(1, len(students)):
        # i 기준 앞에 있는 친구들만 신경
        for j in range(1, i):
            if students[i] < students[j]:
                cnt += 1
    print(f'{students[0]} {cnt}')
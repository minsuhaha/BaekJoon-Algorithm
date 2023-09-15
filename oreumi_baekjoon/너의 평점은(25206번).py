# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
import sys
input = sys.stdin.readline

grades = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total = 0
credit = 0
for i in range(20):
    name, grade, rank = input().split()

    if rank != 'P':
        total += float(grade)*grades[rank]
        credit += float(grade)

print(total/credit)
# 3. 성적이 낮은 순서로 학생 출력하기

n = int(input())
student = []

for _ in range(n):
    student_data = input().split() # 띄어쓰기를 기준으로 데이터 리스트 만들어주기
    student.append((student_data[0], int(student_data[1]))) # 점수 정수형으로 만들어주고 튜플로 감싸주기

result = sorted(student, key=lambda x:x[1]) # (이름,점수) 튜플에서 점수만으로 오름차순

for res in result:
    print(res[0], end =' ')
